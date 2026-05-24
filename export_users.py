"""
export_users.py
===============
يصدّر كل الحسابات المسجلة من MySQL إلى ملف users_export.json
شغّل هذا الملف من Terminal:
    python export_users.py
"""

import json
import os
from datetime import datetime

try:
    from models import DatabaseConnection

    rows = DatabaseConnection.execute(
        "SELECT id, name, email, password, user_type, created_at FROM users ORDER BY id",
        fetch=True
    )

    users = []
    for r in rows:
        users.append({
            'id':         r['id'],
            'name':       r['name'],
            'email':      r['email'],
            'password':   r['password'],
            'user_type':  r['user_type'],
            'created_at': str(r['created_at']) if r['created_at'] else ''
        })

    output = {
        'exported_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_users': len(users),
        'users': users
    }

    with open('users_export.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n✅ {len(users)} kullanıcı kaydedildi → users_export.json\n")
    for u in users:
        print(f"  [{u['user_type'].upper()}] {u['name']} — {u['email']} / {u['password']}")

except Exception as e:
    print(f"❌ Hata: {e}")
    print("MySQL bağlantısını kontrol edin (models.py → DB_CONFIG)")
