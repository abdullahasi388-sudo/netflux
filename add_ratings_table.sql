USE netflux;

-- جدول تقييمات المستخدمين
CREATE TABLE IF NOT EXISTS user_ratings (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    user_id    INT NOT NULL,
    content_id INT NOT NULL,
    rating     INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id)    REFERENCES users(id)   ON DELETE CASCADE,
    FOREIGN KEY (content_id) REFERENCES content(id) ON DELETE CASCADE,
    UNIQUE KEY unique_rating (user_id, content_id)
);
