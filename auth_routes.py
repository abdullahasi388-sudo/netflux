"""
routes/auth_routes.py
مسارات المصادقة — تستخدم كلاسات User و Admin
"""

from flask import Blueprint, render_template_string, request, redirect, session
from models import User, DatabaseConnection
from auth_templates import LOGIN_TEMPLATE, REGISTER_TEMPLATE, REGISTER_SUCCESS_TEMPLATE
import json, os
from datetime import datetime

def save_users_to_file():
    """يحفظ كل الحسابات إلى users_export.json تلقائياً"""
    try:
        rows = DatabaseConnection.execute(
            "SELECT id, name, email, password, user_type, created_at FROM users ORDER BY id",
            fetch=True
        )
        users = []
        for r in rows:
            users.append({
                'id':        r['id'],
                'name':      r['name'],
                'email':     r['email'],
                'password':  r['password'],
                'user_type': r['user_type'],
                'created_at': str(r['created_at']) if r['created_at'] else ''
            })
        output = {
            'exported_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_users': len(users),
            'users': users
        }
        with open('users_export.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"users_export.json save error: {e}")

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'user_id' in session:
            return redirect('/')
        return render_template_string(LOGIN_TEMPLATE, error=None)

    email    = request.form.get('email', '').strip()
    password = request.form.get('password', '').strip()

    # استخدام كلاس User للبحث والتحقق
    user = User.find_by_email(email)

    if user and user.check_password(password):
        session['user_id']    = user.id
        session['user_email'] = user.email
        session['user_name']  = user.name
        session['user_type']  = user.user_type
        save_users_to_file()  # حفظ تلقائي عند الدخول
        return redirect('/')
    else:
        return render_template_string(LOGIN_TEMPLATE, error='E-posta veya şifre hatalı!')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    error = None

    if request.method == 'POST':
        name             = request.form.get('name', '').strip()
        email            = request.form.get('email', '').strip()
        password         = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        if not name or not email or not password or not confirm_password:
            error = 'Tüm alanları doldurun'
        elif password != confirm_password:
            error = 'Şifreler eşleşmiyor'
        elif len(password) < 6:
            error = 'Şifre en az 6 karakter olmalı'
        elif User.find_by_email(email):
            error = 'Bu e-posta zaten kayıtlı'
        else:
            # إنشاء كائن User وحفظه في MySQL
            new_user = User(name=name, email=email, password=password, user_type='user')
            new_user.save()
            save_users_to_file()  # حفظ تلقائي عند التسجيل
            return render_template_string(REGISTER_SUCCESS_TEMPLATE)

    return render_template_string(REGISTER_TEMPLATE, error=error)
