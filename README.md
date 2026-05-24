# 🎬 Netflux v2 — OOP + MySQL

## هيكل المشروع
```
netflux_v2/
├── app.py              ← نقطة التشغيل
├── models.py           ← كلاسات OOP (User, Admin, Content, ...)
├── schema.sql          ← إنشاء قاعدة البيانات
├── er_diagram.html     ← مخطط ER للبرزنتيشن
├── routes/
│   ├── auth_routes.py     ← login / logout / register
│   ├── content_routes.py  ← الصفحات الرئيسية
│   └── api_routes.py      ← REST API (JSON)
└── templates/
    ├── auth_templates.py
    ├── main_templates.py
    └── admin_templates.py
```

## خطوات التشغيل

### 1. تثبيت المكتبات
```bash
pip install flask mysql-connector-python
```

### 2. إنشاء قاعدة البيانات
```bash
mysql -u root -p < schema.sql
```

### 3. تعديل باسورد MySQL
في ملف `models.py`، ابحث عن:
```python
DB_CONFIG = {
    'host':     'localhost',
    'user':     'root',
    'password': '',   # ← ضع باسوردك هنا
    'database': 'netflux',
}
```

### 4. تشغيل التطبيق
```bash
python app.py
```

افتح المتصفح: http://localhost:5000

**Admin Login:**
- Email: admin@netflux.com
- Password: admin123

## الكلاسات (OOP)

| الكلاس | يرث من | المهمة |
|--------|--------|--------|
| `DatabaseConnection` | — | إدارة اتصال MySQL |
| `User` | — | المستخدم العادي |
| `Admin` | `User` | المشرف (Inheritance) |
| `Content` | — | الأفلام والمسلسلات |
| `Favorite` | — | المفضلة (Many-to-Many) |
| `WatchHistory` | — | سجل المشاهدة (Many-to-Many) |
| `WatchProgress` | — | تقدم المشاهدة |
