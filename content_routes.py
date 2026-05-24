"""
routes/content_routes.py
مسارات المحتوى — تستخدم كلاسات Content, User, Favorite, WatchHistory
"""

from flask import Blueprint, render_template_string, request, redirect, session
from models import Content, User, Favorite, WatchHistory
from main_templates  import INDEX_TEMPLATE, WATCH_TEMPLATE, PROFILE_TEMPLATE
from admin_templates import ADD_CONTENT_TEMPLATE, EDIT_CONTENT_TEMPLATE

content_bp = Blueprint('content', __name__)


# ============================================
# الصفحة الرئيسية
# ============================================

@content_bp.route('/')
@content_bp.route('/index')
def index():
    if 'user_id' not in session:
        return redirect('/login')
    # استخدام كلاس Content لجلب البيانات
    content_list = [c.to_dict() for c in Content.get_all()]
    return render_template_string(INDEX_TEMPLATE, content=content_list, session=session)


# ============================================
# مشاهدة المحتوى
# ============================================

@content_bp.route('/watch/<int:content_id>')
def watch(content_id):
    if 'user_id' not in session:
        return redirect('/')

    content = Content.find_by_id(content_id)
    if not content:
        return "Content not found", 404

    # تسجيل في سجل المشاهدة عبر كلاس WatchHistory
    WatchHistory.add(session['user_id'], content_id)

    return render_template_string(WATCH_TEMPLATE, content=content.to_dict())


# ============================================
# صفحات التصفية
# ============================================

@content_bp.route('/movies')
def movies():
    if 'user_id' not in session:
        return redirect('/')
    content_list = [c.to_dict() for c in Content.get_by_type('film')]
    return render_template_string(INDEX_TEMPLATE, content=content_list, session=session)


@content_bp.route('/series')
def series():
    if 'user_id' not in session:
        return redirect('/')
    content_list = [c.to_dict() for c in Content.get_by_type('dizi')]
    return render_template_string(INDEX_TEMPLATE, content=content_list, session=session)


@content_bp.route('/favorites')
def favorites():
    if 'user_id' not in session:
        return redirect('/')
    # استخدام كلاس Favorite لجلب المحتوى المفضل
    content_list = [c.to_dict() for c in Favorite.get_user_content(session['user_id'])]
    return render_template_string(INDEX_TEMPLATE, content=content_list, session=session)


@content_bp.route('/history')
def history():
    if 'user_id' not in session:
        return redirect('/')
    # استخدام كلاس WatchHistory لجلب سجل المشاهدة
    content_list = [c.to_dict() for c in WatchHistory.get_user_content(session['user_id'])]
    return render_template_string(INDEX_TEMPLATE, content=content_list, session=session)


# ============================================
# الملف الشخصي
# ============================================

@content_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect('/')

    success_msg = None
    error_msg   = None

    if request.method == 'POST':
        new_name         = request.form.get('name', '').strip()
        new_password     = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        if not new_name:
            error_msg = "İsim boş olamaz!"
        elif new_password and new_password != confirm_password:
            error_msg = "Şifreler eşleşmiyor!"
        else:
            # استخدام كلاس User لتحديث البيانات
            user = User.find_by_id(session['user_id'])
            if user:
                user.name = new_name
                if new_password:
                    user.password = new_password
                user.save()
                session['user_name'] = new_name
                success_msg = "Profil başarıyla güncellendi!"

    return render_template_string(PROFILE_TEMPLATE, session=session,
                                  success=success_msg, error=error_msg)


# ============================================
# إدارة المحتوى (للمشرف فقط)
# ============================================

@content_bp.route('/add', methods=['GET', 'POST'])
def add_content():
    if 'user_id' not in session or session.get('user_type') != 'admin':
        return redirect('/')

    error = None

    if request.method == 'POST':
        title        = request.form.get('title', '').strip()
        description  = request.form.get('description', '').strip()
        year         = int(request.form.get('year', 2024))
        content_type = request.form.get('content_type', 'film')
        category     = request.form.get('category', '').strip()
        video_url    = request.form.get('video_url', '').strip()
        image_url    = request.form.get('image_url', '').strip()
        rating       = float(request.form.get('rating', 7.0))
        duration     = int(request.form.get('duration', 90))

        if not title or not video_url:
            error = 'Başlık ve Video URL zorunludur!'
        else:
            # إنشاء كائن Content وحفظه في MySQL
            new_content = Content(
                title=title, description=description, year=year,
                content_type=content_type, category=category,
                video_url=video_url, image_url=image_url,
                rating=rating, duration=duration
            )
            new_content.save()
            return redirect('/')

    return render_template_string(ADD_CONTENT_TEMPLATE, session=session, error=error)


@content_bp.route('/edit/<int:content_id>', methods=['GET', 'POST'])
def edit_content(content_id):
    if 'user_id' not in session or session.get('user_type') != 'admin':
        return redirect('/')

    content = Content.find_by_id(content_id)
    if not content:
        return "Content not found", 404

    if request.method == 'POST':
        content.title        = request.form.get('title', '').strip()
        content.description  = request.form.get('description', '').strip()
        content.year         = int(request.form.get('year', 2024))
        content.content_type = request.form.get('content_type', 'film')
        content.category     = request.form.get('category', '').strip()
        content.video_url    = request.form.get('video_url', '').strip()
        image_url = request.form.get('image_url', '').strip()
        if image_url:
            content.image_url = image_url
        content.rating   = float(request.form.get('rating', 7.0))
        content.duration = int(request.form.get('duration', 90))
        content.save()
        return redirect('/')

    return render_template_string(EDIT_CONTENT_TEMPLATE,
                                  content=content.to_dict(), session=session)
