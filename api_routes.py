"""
routes/api_routes.py
مسارات API — تستخدم كلاسات Favorite, WatchProgress, Content, Admin
"""

from flask import Blueprint, jsonify, request, session
from models import Favorite, WatchProgress, Content, User, DatabaseConnection

api_bp = Blueprint('api', __name__)


@api_bp.route('/api/favorites')
def get_favorites():
    if 'user_id' not in session:
        return jsonify({'favorites': []})
    # استخدام كلاس Favorite
    ids = Favorite.get_user_favorite_ids(session['user_id'])
    return jsonify({'favorites': ids})


@api_bp.route('/api/favorite', methods=['POST'])
def toggle_favorite():
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    data       = request.get_json()
    content_id = data.get('content_id')
    # استخدام كلاس Favorite للتبديل
    is_fav = Favorite.toggle(session['user_id'], content_id)
    msg = 'Favorilere eklendi' if is_fav else 'Favorilerden çıkarıldı'
    return jsonify({'message': msg, 'is_favorite': is_fav})


@api_bp.route('/api/progress/<int:content_id>')
def get_progress(content_id):
    if 'user_id' not in session:
        return jsonify({'progress': 0})
    # استخدام كلاس WatchProgress
    progress = WatchProgress.get(session['user_id'], content_id)
    return jsonify({'progress': progress})


@api_bp.route('/api/progress', methods=['POST'])
def save_progress_api():
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    data       = request.get_json()
    content_id = data.get('content_id')
    progress   = data.get('progress', 0)
    # استخدام كلاس WatchProgress للحفظ
    WatchProgress.save(session['user_id'], content_id, progress)
    return jsonify({'success': True})


@api_bp.route('/api/delete/<int:content_id>', methods=['POST'])
def delete_content(content_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    if session.get('user_type') != 'admin':
        return jsonify({'error': 'Admin access required'}), 403

    content = Content.find_by_id(content_id)
    if not content:
        return jsonify({'success': False, 'message': 'İçerik bulunamadı'}), 404

    title = content.title
    # استخدام كلاس Admin للحذف عبر كلاس Content
    content.delete()
    return jsonify({'success': True, 'message': f'"{title}" silindi'})


# ============================================
# API التقييم
# ============================================

@api_bp.route('/api/rate', methods=['POST'])
def rate_content():
    """تقييم محتوى من 1 إلى 5 نجوم"""
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401

    data       = request.get_json()
    content_id = data.get('content_id')
    rating     = int(data.get('rating', 0))

    if not (1 <= rating <= 5):
        return jsonify({'error': 'Invalid rating'}), 400

    user_id = session['user_id']

    # حفظ تقييم المستخدم
    existing = DatabaseConnection.execute(
        "SELECT id FROM user_ratings WHERE user_id=%s AND content_id=%s",
        (user_id, content_id), fetchone=True
    )
    if existing:
        DatabaseConnection.execute(
            "UPDATE user_ratings SET rating=%s WHERE user_id=%s AND content_id=%s",
            (rating, user_id, content_id)
        )
    else:
        DatabaseConnection.execute(
            "INSERT INTO user_ratings (user_id, content_id, rating) VALUES (%s,%s,%s)",
            (user_id, content_id, rating)
        )

    # حساب متوسط وتحديث جدول content
    avg = DatabaseConnection.execute(
        "SELECT ROUND(AVG(rating), 1) as avg_rating FROM user_ratings WHERE content_id=%s",
        (content_id,), fetchone=True
    )
    new_rating = float(avg['avg_rating']) if avg and avg['avg_rating'] else float(rating)

    DatabaseConnection.execute(
        "UPDATE content SET rating=%s WHERE id=%s",
        (new_rating, content_id)
    )

    return jsonify({
        'success':    True,
        'new_rating': new_rating,
        'message':    f'Puanınız kaydedildi! Ortalama: {new_rating}'
    })


@api_bp.route('/api/my_ratings')
def get_my_ratings():
    """جلب تقييمات المستخدم الحالي"""
    if 'user_id' not in session:
        return jsonify({'ratings': {}})

    rows = DatabaseConnection.execute(
        "SELECT content_id, rating FROM user_ratings WHERE user_id=%s",
        (session['user_id'],), fetch=True
    )
    ratings = {str(r['content_id']): r['rating'] for r in rows}
    return jsonify({'ratings': ratings})
