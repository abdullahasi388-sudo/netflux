#!/usr/bin/env python3
"""
app.py — نقطة تشغيل التطبيق
قبل التشغيل:
  1. شغّل: mysql -u root -p < schema.sql
  2. عدّل DB_CONFIG في models.py (user/password)
  3. pip install flask mysql-connector-python
  4. python app.py
"""

try:
    from flask import Flask
    import mysql.connector
except ImportError:
    print("❌ مكتبات ناقصة!")
    print("📥 شغّل: pip install flask mysql-connector-python")
    input("Press Enter to exit...")
    exit(1)

app = Flask(__name__)
app.secret_key = 'netflux_secret_key_2024'

# تسجيل الـ Blueprints
from routes.auth_routes    import auth_bp
from routes.content_routes import content_bp
from routes.api_routes     import api_bp

app.register_blueprint(auth_bp)
app.register_blueprint(content_bp)
app.register_blueprint(api_bp)


def get_local_ip():
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"


if __name__ == '__main__':
    # اختبار الاتصال بـ MySQL
    from models import DatabaseConnection
    try:
        DatabaseConnection.get_connection()
    except Exception as e:
        print(f"\n❌ فشل الاتصال بـ MySQL: {e}")
        print("تأكد من:")
        print("  1. MySQL شغّال")
        print("  2. عدّلت DB_CONFIG في models.py")
        print("  3. شغّلت schema.sql\n")
        exit(1)

    ip = get_local_ip()
    print("\n" + "="*60)
    print("🎬 NETFLUX v2 — OOP + MySQL")
    print("="*60)
    print(f"🖥️  http://localhost:5000")
    print(f"📱  http://{ip}:5000")
    print("="*60)
    print("🔐 Admin: admin@netflux.com / admin123")
    print("="*60 + "\n")

    app.run(host='0.0.0.0', debug=True, port=5000)
