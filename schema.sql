-- ============================================
-- schema.sql
-- إنشاء قاعدة بيانات Netflux
-- شغّل هذا الملف مرة واحدة قبل تشغيل التطبيق:
--   mysql -u root -p < schema.sql
-- ============================================

CREATE DATABASE IF NOT EXISTS netflux CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE netflux;

-- ============================================
-- جدول المستخدمين
-- ============================================
CREATE TABLE IF NOT EXISTS users (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    email      VARCHAR(150) NOT NULL UNIQUE,
    password   VARCHAR(255) NOT NULL,
    user_type  ENUM('admin', 'user') DEFAULT 'user',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- جدول المحتوى (أفلام + مسلسلات)
-- ============================================
CREATE TABLE IF NOT EXISTS content (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    title        VARCHAR(200) NOT NULL,
    description  TEXT,
    year         INT,
    content_type ENUM('film', 'dizi') DEFAULT 'film',
    category     VARCHAR(100),
    video_url    VARCHAR(500) NOT NULL,
    image_url    VARCHAR(500),
    rating       FLOAT DEFAULT 7.0,
    duration     INT DEFAULT 90,
    created_at   DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- جدول المفضلة  (Many-to-Many: users <-> content)
-- ============================================
CREATE TABLE IF NOT EXISTS favorites (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    user_id    INT NOT NULL,
    content_id INT NOT NULL,
    added_at   DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id)    REFERENCES users(id)   ON DELETE CASCADE,
    FOREIGN KEY (content_id) REFERENCES content(id) ON DELETE CASCADE,
    UNIQUE KEY unique_fav (user_id, content_id)
);

-- ============================================
-- جدول سجل المشاهدة  (Many-to-Many: users <-> content)
-- ============================================
CREATE TABLE IF NOT EXISTS watch_history (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    user_id    INT NOT NULL,
    content_id INT NOT NULL,
    watched_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id)    REFERENCES users(id)   ON DELETE CASCADE,
    FOREIGN KEY (content_id) REFERENCES content(id) ON DELETE CASCADE
);

-- ============================================
-- جدول تقدم المشاهدة
-- ============================================
CREATE TABLE IF NOT EXISTS watch_progress (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    user_id    INT NOT NULL,
    content_id INT NOT NULL,
    progress   FLOAT DEFAULT 0,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id)    REFERENCES users(id)   ON DELETE CASCADE,
    FOREIGN KEY (content_id) REFERENCES content(id) ON DELETE CASCADE,
    UNIQUE KEY unique_progress (user_id, content_id)
);

-- ============================================
-- بيانات افتراضية - Admin + محتوى تجريبي
-- ============================================
INSERT IGNORE INTO users (name, email, password, user_type)
VALUES ('Admin', 'admin@netflux.com', 'admin123', 'admin');

INSERT IGNORE INTO content (title, description, year, content_type, category, video_url, image_url, rating, duration)
VALUES (
    'The Present',
    'A brilliant animated short film about a boy and his dog.',
    2020, 'film', 'Drama',
    'https://www.youtube.com/embed/WjqiU5FgsYc',
    'https://img.youtube.com/vi/WjqiU5FgsYc/maxresdefault.jpg',
    8.7, 7
);
