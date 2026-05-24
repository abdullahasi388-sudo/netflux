"""
models.py
=========
الكلاسات (OOP) - Object Oriented Models
يحتوي على:
  - class DatabaseConnection : إدارة الاتصال بـ MySQL
  - class User               : المستخدم العادي
  - class Admin(User)        : المشرف (يرث من User)
  - class Content            : الفيلم أو المسلسل
  - class WatchHistory       : سجل المشاهدة
  - class WatchProgress      : تقدم المشاهدة
  - class Favorite           : المفضلة
"""

import mysql.connector
from datetime import datetime
import os

# ============================================
# كلاس إدارة الاتصال بقاعدة البيانات
# ============================================

class DatabaseConnection:
    """
    Singleton للاتصال بـ MySQL.
    يقرأ البيانات من Environment Variables تلقائياً (Railway)
    أو يستخدم القيم المحلية (localhost).
    """
    _connection = None

    DB_CONFIG = {
        'host':     os.environ.get('MYSQLHOST',     'localhost'),
        'port':     int(os.environ.get('MYSQLPORT', 3306)),
        'user':     os.environ.get('MYSQLUSER',     'root'),
        'password': os.environ.get('MYSQLPASSWORD', ''),
        'database': os.environ.get('MYSQLDATABASE', 'netflux'),
        'charset':  'utf8mb4'
    }

    @classmethod
    def get_connection(cls):
        """إرجاع الاتصال الحالي أو إنشاء اتصال جديد"""
        try:
            if cls._connection is None or not cls._connection.is_connected():
                cls._connection = mysql.connector.connect(**cls.DB_CONFIG)
                print("✅ MySQL connected")
        except mysql.connector.Error as e:
            print(f"❌ MySQL connection error: {e}")
            raise
        return cls._connection

    @classmethod
    def execute(cls, query, params=None, fetch=False, fetchone=False):
        """
        تنفيذ استعلام SQL.
        fetch=True     → إرجاع كل النتائج
        fetchone=True  → إرجاع نتيجة واحدة
        """
        conn   = cls.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(query, params or ())
            if fetchone:
                return cursor.fetchone()
            if fetch:
                return cursor.fetchall()
            conn.commit()
            return cursor.lastrowid
        except mysql.connector.Error as e:
            conn.rollback()
            print(f"❌ Query error: {e}\nQuery: {query}")
            raise
        finally:
            cursor.close()


# ============================================
# كلاس User — المستخدم
# ============================================

class User:
    """
    يمثل مستخدم عادي في النظام.
    يحتوي على عمليات CRUD الخاصة بالمستخدمين.
    """

    def __init__(self, id=None, name='', email='', password='', user_type='user', created_at=None):
        self.id         = id
        self.name       = name
        self.email      = email
        self.password   = password
        self.user_type  = user_type
        self.created_at = created_at or datetime.now()

    # ---------- دوال ثابتة (Class Methods) ----------

    @classmethod
    def find_by_email(cls, email):
        """البحث عن مستخدم بالإيميل"""
        row = DatabaseConnection.execute(
            "SELECT * FROM users WHERE email = %s", (email,), fetchone=True
        )
        return cls._from_row(row) if row else None

    @classmethod
    def find_by_id(cls, user_id):
        """البحث عن مستخدم بالـ ID"""
        row = DatabaseConnection.execute(
            "SELECT * FROM users WHERE id = %s", (user_id,), fetchone=True
        )
        return cls._from_row(row) if row else None

    @classmethod
    def get_all(cls):
        """جلب كل المستخدمين"""
        rows = DatabaseConnection.execute("SELECT * FROM users ORDER BY id", fetch=True)
        return [cls._from_row(r) for r in rows]

    @classmethod
    def _from_row(cls, row):
        """تحويل صف قاعدة البيانات إلى كائن User أو Admin"""
        if row['user_type'] == 'admin':
            return Admin(
                id=row['id'], name=row['name'], email=row['email'],
                password=row['password'], created_at=row.get('created_at')
            )
        return cls(
            id=row['id'], name=row['name'], email=row['email'],
            password=row['password'], user_type=row['user_type'],
            created_at=row.get('created_at')
        )

    # ---------- دوال Instance ----------

    def check_password(self, password):
        """التحقق من الباسورد"""
        return self.password == password

    def save(self):
        """حفظ المستخدم (إضافة جديد أو تحديث موجود)"""
        if self.id:
            DatabaseConnection.execute(
                "UPDATE users SET name=%s, password=%s WHERE id=%s",
                (self.name, self.password, self.id)
            )
        else:
            self.id = DatabaseConnection.execute(
                "INSERT INTO users (name, email, password, user_type) VALUES (%s,%s,%s,%s)",
                (self.name, self.email, self.password, self.user_type)
            )
        return self

    def to_dict(self):
        """تحويل الكائن إلى dict للاستخدام في الـ templates"""
        return {
            'id': self.id, 'name': self.name,
            'email': self.email, 'type': self.user_type
        }

    def is_admin(self):
        return self.user_type == 'admin'

    def __repr__(self):
        return f"<User id={self.id} email={self.email} type={self.user_type}>"


# ============================================
# كلاس Admin — يرث من User (Inheritance)
# ============================================

class Admin(User):
    """
    المشرف - يرث كل صلاحيات User ويضيف صلاحيات إضافية.
    مثال على OOP Inheritance.
    """

    def __init__(self, id=None, name='', email='', password='', created_at=None):
        super().__init__(id=id, name=name, email=email,
                         password=password, user_type='admin',
                         created_at=created_at)

    def delete_content(self, content_id):
        """حذف محتوى - صلاحية المشرف فقط"""
        DatabaseConnection.execute(
            "DELETE FROM content WHERE id = %s", (content_id,)
        )

    def get_all_users(self):
        """جلب كل المستخدمين - صلاحية المشرف فقط"""
        return User.get_all()

    def __repr__(self):
        return f"<Admin id={self.id} email={self.email}>"


# ============================================
# كلاس Content — المحتوى (فيلم أو مسلسل)
# ============================================

class Content:
    """
    يمثل فيلم أو مسلسل في النظام.
    يحتوي على عمليات CRUD الخاصة بالمحتوى.
    """

    def __init__(self, id=None, title='', description='', year=2024,
                 content_type='film', category='', video_url='',
                 image_url='', rating=7.0, duration=90, created_at=None):
        self.id           = id
        self.title        = title
        self.description  = description
        self.year         = year
        self.content_type = content_type   # 'film' أو 'dizi'
        self.category     = category
        self.video_url    = video_url
        self.image_url    = image_url or f'https://via.placeholder.com/300x450/1a1a1a/e50914?text={title}'
        self.rating       = rating
        self.duration     = duration
        self.created_at   = created_at or datetime.now()

    # ---------- دوال ثابتة ----------

    @classmethod
    def get_all(cls):
        """جلب كل المحتوى"""
        rows = DatabaseConnection.execute(
            "SELECT * FROM content ORDER BY created_at DESC", fetch=True
        )
        return [cls._from_row(r) for r in rows]

    @classmethod
    def get_by_type(cls, content_type):
        """جلب محتوى حسب النوع (film / dizi)"""
        rows = DatabaseConnection.execute(
            "SELECT * FROM content WHERE content_type = %s ORDER BY created_at DESC",
            (content_type,), fetch=True
        )
        return [cls._from_row(r) for r in rows]

    @classmethod
    def find_by_id(cls, content_id):
        """جلب محتوى بالـ ID"""
        row = DatabaseConnection.execute(
            "SELECT * FROM content WHERE id = %s", (content_id,), fetchone=True
        )
        return cls._from_row(row) if row else None

    @classmethod
    def _from_row(cls, row):
        """تحويل صف قاعدة البيانات إلى كائن Content"""
        return cls(
            id=row['id'], title=row['title'], description=row['description'],
            year=row['year'], content_type=row['content_type'],
            category=row['category'], video_url=row['video_url'],
            image_url=row['image_url'], rating=float(row['rating']),
            duration=row['duration'], created_at=row.get('created_at')
        )

    # ---------- دوال Instance ----------

    def save(self):
        """حفظ المحتوى (إضافة أو تحديث)"""
        if self.id:
            DatabaseConnection.execute(
                """UPDATE content SET title=%s, description=%s, year=%s,
                   content_type=%s, category=%s, video_url=%s,
                   image_url=%s, rating=%s, duration=%s WHERE id=%s""",
                (self.title, self.description, self.year, self.content_type,
                 self.category, self.video_url, self.image_url,
                 self.rating, self.duration, self.id)
            )
        else:
            self.id = DatabaseConnection.execute(
                """INSERT INTO content
                   (title, description, year, content_type, category, video_url, image_url, rating, duration)
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (self.title, self.description, self.year, self.content_type,
                 self.category, self.video_url, self.image_url, self.rating, self.duration)
            )
        return self

    def delete(self):
        """حذف المحتوى"""
        DatabaseConnection.execute("DELETE FROM content WHERE id = %s", (self.id,))

    def to_dict(self):
        """تحويل الكائن إلى dict للاستخدام في الـ templates"""
        return {
            'id': self.id, 'title': self.title, 'description': self.description,
            'year': self.year, 'type': self.content_type, 'content_type': self.content_type,
            'category': self.category, 'video_url': self.video_url,
            'thumbnail': self.image_url, 'image_url': self.image_url,
            'rating': self.rating, 'duration': self.duration
        }

    def __repr__(self):
        return f"<Content id={self.id} title='{self.title}' type={self.content_type}>"


# ============================================
# كلاس Favorite — المفضلة
# ============================================

class Favorite:
    """علاقة Many-to-Many بين User و Content"""

    @staticmethod
    def get_user_favorite_ids(user_id):
        """جلب IDs المحتوى المفضل للمستخدم"""
        rows = DatabaseConnection.execute(
            "SELECT content_id FROM favorites WHERE user_id = %s", (user_id,), fetch=True
        )
        return [r['content_id'] for r in rows]

    @staticmethod
    def toggle(user_id, content_id):
        """إضافة أو إزالة من المفضلة"""
        existing = DatabaseConnection.execute(
            "SELECT id FROM favorites WHERE user_id=%s AND content_id=%s",
            (user_id, content_id), fetchone=True
        )
        if existing:
            DatabaseConnection.execute(
                "DELETE FROM favorites WHERE user_id=%s AND content_id=%s",
                (user_id, content_id)
            )
            return False  # تمت الإزالة
        else:
            DatabaseConnection.execute(
                "INSERT INTO favorites (user_id, content_id) VALUES (%s,%s)",
                (user_id, content_id)
            )
            return True   # تمت الإضافة

    @staticmethod
    def get_user_content(user_id):
        """جلب المحتوى المفضل للمستخدم كاملاً"""
        rows = DatabaseConnection.execute(
            """SELECT c.* FROM content c
               JOIN favorites f ON c.id = f.content_id
               WHERE f.user_id = %s ORDER BY f.added_at DESC""",
            (user_id,), fetch=True
        )
        return [Content._from_row(r) for r in rows]


# ============================================
# كلاس WatchHistory — سجل المشاهدة
# ============================================

class WatchHistory:
    """علاقة Many-to-Many بين User و Content مع timestamp"""

    @staticmethod
    def add(user_id, content_id):
        """إضافة سجل مشاهدة"""
        DatabaseConnection.execute(
            "INSERT INTO watch_history (user_id, content_id) VALUES (%s,%s)",
            (user_id, content_id)
        )

    @staticmethod
    def get_user_content(user_id):
        """جلب المحتوى الذي شاهده المستخدم (بدون تكرار)"""
        rows = DatabaseConnection.execute(
            """SELECT DISTINCT c.* FROM content c
               JOIN watch_history h ON c.id = h.content_id
               WHERE h.user_id = %s ORDER BY h.watched_at DESC""",
            (user_id,), fetch=True
        )
        return [Content._from_row(r) for r in rows]


# ============================================
# كلاس WatchProgress — تقدم المشاهدة
# ============================================

class WatchProgress:
    """حفظ تقدم المشاهدة لكل مستخدم ومحتوى"""

    @staticmethod
    def get(user_id, content_id):
        """جلب التقدم المحفوظ"""
        row = DatabaseConnection.execute(
            "SELECT progress FROM watch_progress WHERE user_id=%s AND content_id=%s",
            (user_id, content_id), fetchone=True
        )
        return row['progress'] if row else 0

    @staticmethod
    def save(user_id, content_id, progress):
        """حفظ أو تحديث التقدم"""
        existing = DatabaseConnection.execute(
            "SELECT id FROM watch_progress WHERE user_id=%s AND content_id=%s",
            (user_id, content_id), fetchone=True
        )
        if existing:
            DatabaseConnection.execute(
                "UPDATE watch_progress SET progress=%s WHERE user_id=%s AND content_id=%s",
                (progress, user_id, content_id)
            )
        else:
            DatabaseConnection.execute(
                "INSERT INTO watch_progress (user_id, content_id, progress) VALUES (%s,%s,%s)",
                (user_id, content_id, progress)
            )
