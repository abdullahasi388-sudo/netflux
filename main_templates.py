"""
templates/main_templates.py
============================
قوالب HTML الرئيسية - Main HTML Templates
يشمل:
  - INDEX_TEMPLATE   : الصفحة الرئيسية (شبكة المحتوى)
  - WATCH_TEMPLATE   : صفحة مشاهدة الفيديو
  - PROFILE_TEMPLATE : صفحة الملف الشخصي
"""

INDEX_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Netflux - Ana Sayfa</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #0a0a0a;
            color: white;
            min-height: 100vh;
            position: relative;
            overflow-x: hidden;
        }
        
        /* Animated Background */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(229, 9, 20, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(139, 0, 0, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 40% 20%, rgba(255, 26, 26, 0.1) 0%, transparent 50%),
                linear-gradient(135deg, #0a0a0a 0%, #1a0a0a 50%, #0a0a0a 100%);
            z-index: -2;
        }
        
        @keyframes backgroundShift {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.9; }
        }
        
        /* Header Styles */
        .header { 
            background: linear-gradient(180deg, rgba(10,10,10,0.98) 0%, rgba(10,10,10,0.95) 100%);
            padding: 20px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 30px rgba(229, 9, 20, 0.2), 0 0 100px rgba(229, 9, 20, 0.1);
            backdrop-filter: blur(20px) saturate(180%);
            position: sticky;
            top: 0;
            z-index: 100;
            border-bottom: 1px solid rgba(229, 9, 20, 0.2);
        }
        
        .logo { 
            font-size: 36px;
            font-weight: 900;
            background: linear-gradient(135deg, #e50914 0%, #ff4444 50%, #e50914 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shimmer 3s linear infinite;
            letter-spacing: -2px;
            text-shadow: 0 0 40px rgba(229, 9, 20, 0.6);
            cursor: pointer;
            transition: transform 0.3s ease;
        }
        
        .logo:hover {
            transform: scale(1.05);
        }
        
        @keyframes shimmer {
            to { background-position: 200% center; }
        }
        
        .nav { 
            display: flex;
            gap: 8px;
            align-items: center;
            background: rgba(255, 255, 255, 0.03);
            padding: 8px;
            border-radius: 50px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        .nav a { 
            color: #e0e0e0;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            padding: 12px 24px;
            border-radius: 50px;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }
        
        .nav a::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(229, 9, 20, 0.3), transparent);
            transition: left 0.5s ease;
        }
        
        .nav a:hover::before {
            left: 100%;
        }
        
        .nav a:hover {
            color: #fff;
            background: linear-gradient(135deg, rgba(229, 9, 20, 0.3) 0%, rgba(229, 9, 20, 0.1) 100%);
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(229, 9, 20, 0.4);
        }
        
        .nav a.active {
            background: linear-gradient(135deg, #e50914 0%, #b0070f 100%);
            color: white;
            box-shadow: 0 4px 20px rgba(229, 9, 20, 0.5);
        }
        
        /* Container */
        .container { 
            padding: 50px;
            max-width: 1800px;
            margin: 0 auto;
            position: relative;
        }
        
        .page-title { 
            font-size: 48px;
            font-weight: 900;
            margin: 40px 0 50px 0;
            text-align: center;
            background: linear-gradient(135deg, #fff 0%, #e50914 50%, #fff 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shimmer 4s linear infinite;
            letter-spacing: -2px;
            text-transform: uppercase;
            position: relative;
        }
        
        .page-title::after {
            content: '';
            position: absolute;
            bottom: -15px;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 4px;
            background: linear-gradient(90deg, transparent, #e50914, transparent);
            border-radius: 2px;
        }
        
        /* Content Grid */
        .content-grid { 
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 40px;
        }
        
        /* Content Card */
        /* ARAMA + FİLTRE BARI */
        .search-filter-bar {
            display: flex; gap: 12px; margin-bottom: 30px;
            flex-wrap: wrap; align-items: center;
        }
        .search-box {
            flex: 1; min-width: 220px; position: relative;
        }
        .search-icon {
            position: absolute; left: 14px; top: 50%;
            transform: translateY(-50%); font-size: 16px;
        }
        .search-box input {
            width: 100%; padding: 12px 16px 12px 42px;
            background: rgba(255,255,255,0.07);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 10px; color: white; font-size: 15px;
            transition: all 0.3s ease;
        }
        .search-box input:focus {
            outline: none; border-color: #e50914;
            background: rgba(255,255,255,0.1);
            box-shadow: 0 0 20px rgba(229,9,20,0.3);
        }
        .search-filter-bar select {
            padding: 12px 16px; background: rgba(255,255,255,0.07);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 10px; color: white; font-size: 14px;
            cursor: pointer; transition: all 0.3s;
        }
        .search-filter-bar select:focus { outline:none; border-color:#e50914; }
        .search-filter-bar select option { background: #1a1a1a; }
        .clear-btn {
            padding: 12px 18px; background: rgba(229,9,20,0.2);
            border: 1px solid #e50914; border-radius: 10px;
            color: #e50914; cursor: pointer; font-size: 14px;
            transition: all 0.3s;
        }
        .clear-btn:hover { background: #e50914; color: white; }

        /* YILDIZ PUANLAMA */
        .star-rating {
            display: flex; align-items: center; gap: 3px;
            padding: 6px 0; margin-bottom: 4px;
        }
        .star {
            font-size: 20px; color: #555; cursor: pointer;
            transition: color 0.2s, transform 0.1s;
        }
        .star:hover, .star.active { color: #f5c518; }
        .star:hover { transform: scale(1.2); }
        .rating-val {
            margin-left: 6px; font-size: 13px;
            color: #f5c518; font-weight: bold;
        }

        .content-card { 
            background: linear-gradient(145deg, rgba(30,30,30,0.6) 0%, rgba(42,42,42,0.4) 100%);
            border-radius: 12px;
            overflow: hidden;
            transition: all 0.3s ease;
            position: relative;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.05);
            content-visibility: auto;
            contain-intrinsic-size: 200px 380px;
        }
        
        .content-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(229, 9, 20, 0.15) 0%, transparent 100%);
            opacity: 0;
            transition: opacity 0.5s ease;
            z-index: 1;
            pointer-events: none;
        }
        
        .content-card:hover {
            transform: translateY(-15px) scale(1.03);
            box-shadow: 
                0 25px 70px rgba(229, 9, 20, 0.4),
                0 0 60px rgba(229, 9, 20, 0.2),
                inset 0 0 0 1px rgba(229, 9, 20, 0.3);
            border-color: rgba(229, 9, 20, 0.6);
        }
        
        .content-card:hover::before {
            opacity: 1;
        }
        
        .content-thumbnail { 
            width: 100%;
            height: 280px;
            background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
            position: relative;
            overflow: hidden;
        }
        
        .content-thumbnail::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 70%;
            background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, transparent 100%);
            z-index: 2;
        }
        
        .content-thumbnail img { 
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.7s cubic-bezier(0.4, 0, 0.2, 1);
            filter: brightness(0.9);
        }
        
        .content-card:hover .content-thumbnail img {
            transform: scale(1.2);
            filter: brightness(1.1);
        }
        
        .content-type-badge { 
            position: absolute;
            top: 15px;
            right: 15px;
            background: linear-gradient(135deg, rgba(229, 9, 20, 0.95) 0%, rgba(180, 7, 15, 0.95) 100%);
            color: white;
            padding: 8px 16px;
            border-radius: 25px;
            font-size: 12px;
            font-weight: 800;
            z-index: 3;
            box-shadow: 0 4px 20px rgba(229, 9, 20, 0.5);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .content-info { 
            padding: 25px;
            position: relative;
            z-index: 2;
        }
        
        .content-title { 
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 8px;
            color: #fff;
            line-height: 1.3;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }
        
        .content-meta { 
            font-size: 11px;
            color: #b3b3b3;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
            font-weight: 500;
        }
        
        .content-meta span {
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }
        
        .content-actions { 
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .btn { 
            padding: 8px 14px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            font-size: 13px;
            font-weight: 700;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .btn-play { 
            background: linear-gradient(135deg, #e50914 0%, #b0070f 100%);
            color: white;
            flex: 1;
            position: relative;
            overflow: hidden;
        }
        
        .btn-play::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }
        
        .btn-play:hover::before {
            width: 300px;
            height: 300px;
        }
        
        .btn-play:hover {
            background: linear-gradient(135deg, #ff1a1a 0%, #e50914 100%);
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(229, 9, 20, 0.6);
        }
        
        .btn-fav { 
            background: linear-gradient(145deg, rgba(42,42,42,0.8) 0%, rgba(26,26,26,0.8) 100%);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }
        
        .btn-fav:hover {
            background: linear-gradient(145deg, rgba(52,52,52,0.9) 0%, rgba(36,36,36,0.9) 100%);
            transform: translateY(-3px);
            border-color: rgba(229, 9, 20, 0.5);
            box-shadow: 0 8px 25px rgba(229, 9, 20, 0.3);
        }
        
        .btn-edit { 
            background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
            color: white;
        }
        
        .btn-edit:hover {
            background: linear-gradient(135deg, #0088ff 0%, #007bff 100%);
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0, 123, 255, 0.5);
        }
        
        .btn-delete { 
            background: linear-gradient(135deg, #666 0%, #444 100%);
            color: white;
        }
        
        .btn-delete:hover {
            background: linear-gradient(135deg, #777 0%, #555 100%);
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(100, 100, 100, 0.5);
        }
        
        /* Animations */
        @keyframes slideIn {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        
        @keyframes slideOut {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(100%);
                opacity: 0;
            }
        }
        
        /* Notification */
        .notification {
            position: fixed;
            top: 100px;
            right: 30px;
            background: linear-gradient(135deg, #e50914 0%, #b0070f 100%);
            color: white;
            padding: 18px 28px;
            border-radius: 15px;
            z-index: 1000;
            animation: slideIn 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 10px 40px rgba(229, 9, 20, 0.6);
            font-weight: 700;
            border: 1px solid rgba(255, 255, 255, 0.3);
            backdrop-filter: blur(10px);
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 12px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(10, 10, 10, 0.5);
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #e50914 0%, #b0070f 100%);
            border-radius: 6px;
            border: 2px solid rgba(10, 10, 10, 0.5);
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(180deg, #ff1a1a 0%, #e50914 100%);
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">🎬 Netflux</div>
        <div class="nav">
            <a href="/">Ana Sayfa</a>
            <a href="/movies">Filmler</a>
            <a href="/series">Diziler</a>
            <a href="/favorites">Favoriler</a>
            <a href="/history">İzleme Geçmişi</a>
            <a href="/profile">Profil</a>
            {% if session.user_type == 'admin' %}
            <a href="/add">İçerik Ekle</a>
            {% endif %}
            <a href="/logout">Çıkış ({{ session.user_name }})</a>
        </div>
    </div>
    
    <div class="container">
        <h2 class="section-title">🔥 Popüler İçerikler</h2>
        
        <!-- ARAMA + FİLTRELEME BARI -->
        <div class="search-filter-bar">
            <div class="search-box">
                <span class="search-icon">🔍</span>
                <input type="text" id="searchInput" placeholder="Film veya dizi ara..." oninput="filterContent()">
            </div>
            <select id="typeFilter" onchange="filterContent()">
                <option value="">Tümü</option>
                <option value="film">🎬 Filmler</option>
                <option value="dizi">📺 Diziler</option>
            </select>
            <select id="categoryFilter" onchange="filterContent()">
                <option value="">Tüm Kategoriler</option>
                <option value="Aksiyon">Aksiyon</option>
                <option value="Drama">Drama</option>
                <option value="Komedi">Komedi</option>
                <option value="Romantik">Romantik</option>
                <option value="Korku">Korku</option>
                <option value="Belgesel">Belgesel</option>
                <option value="Bilim Kurgu">Bilim Kurgu</option>
                <option value="Anime">Anime</option>
                <option value="Çocuk">Çocuk ve Aile</option>
            </select>
            <select id="ratingFilter" onchange="filterContent()">
                <option value="">Tüm Puanlar</option>
                <option value="9">⭐ 9+</option>
                <option value="8">⭐ 8+</option>
                <option value="7">⭐ 7+</option>
            </select>
            <button onclick="clearFilters()" class="clear-btn">✕ Temizle</button>
        </div>
        <div id="noResults" style="display:none; text-align:center; color:#888; padding:40px; font-size:18px;">
            🔍 Sonuç bulunamadı
        </div>
        
        <div class="content-grid" id="contentGrid">
            {% for content in content %}
            <div class="content-card" data-id="{{ content.id }}"
                 data-title="{{ content.title|lower }}"
                 data-type="{{ content.type }}"
                 data-category="{{ content.category|lower }}"
                 data-rating="{{ content.rating }}">
                <div class="content-thumbnail">
                    <img src="{{ content.thumbnail }}" alt="{{ content.title }}" loading="lazy" decoding="async" onerror="this.src='https://picsum.photos/seed/{{ content.id }}/300/450'; this.onerror=null;">
                    <div class="content-type-badge">
                        {% if content.type == 'dizi' %}📺 Dizi{% else %}🎬 Film{% endif %}
                    </div>
                </div>
                <div class="content-info">
                    <div class="content-title">{{ content.title }}</div>
                    <div class="content-meta">
                        {{ content.year }} • {{ content.category }} • {{ content.duration }} dk • ⭐ {{ content.rating }}
                    </div>
                    <!-- PUANLAMA YILDIZLARI -->
                    <div class="star-rating" id="stars-{{ content.id }}">
                        <span onclick="rateContent({{ content.id }}, 1, this)" class="star" data-val="1">★</span>
                        <span onclick="rateContent({{ content.id }}, 2, this)" class="star" data-val="2">★</span>
                        <span onclick="rateContent({{ content.id }}, 3, this)" class="star" data-val="3">★</span>
                        <span onclick="rateContent({{ content.id }}, 4, this)" class="star" data-val="4">★</span>
                        <span onclick="rateContent({{ content.id }}, 5, this)" class="star" data-val="5">★</span>
                        <span class="rating-val" id="rval-{{ content.id }}">{{ content.rating }}</span>
                    </div>
                    <div class="content-actions">
                        <a href="/watch/{{ content.id }}" class="btn btn-play">▶ Oynat</a>
                        <button class="btn btn-fav" id="fav-{{ content.id }}" onclick="toggleFavorite({{ content.id }}, this)">🤍 Favori</button>
                        {% if session.user_type == 'admin' %}
                        <a href="/edit/{{ content.id }}" class="btn btn-edit">✏️ Düzenle</a>
                        <button class="btn btn-delete" onclick="deleteContent({{ content.id }}, '{{ content.title }}')">🗑️ Sil</button>
                        {% endif %}
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    
    <script>
        // Load user favorites on page load
        window.addEventListener('DOMContentLoaded', function() {
            fetch('/api/favorites')
                .then(response => response.json())
                .then(data => {
                    data.favorites.forEach(contentId => {
                        const button = document.getElementById('fav-' + contentId);
                        if (button) {
                            button.innerHTML = '❤️ Favori';
                            button.style.background = '#e50914';
                        }
                    });
                });
        });
        
        function toggleFavorite(id, button) {
            fetch('/api/favorite', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({content_id: id})
            })
            .then(response => response.json())
            .then(data => {
                // Change button appearance based on favorite status
                if (data.is_favorite) {
                    button.innerHTML = '❤️ Favori';
                    button.style.background = '#e50914';
                } else {
                    button.innerHTML = '🤍 Favori';
                    button.style.background = '#333';
                }
                
                // Show notification
                showNotification(data.message);
            });
        }
        
        function showNotification(message) {
            // Create notification element
            const notification = document.createElement('div');
            notification.textContent = message;
            notification.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: #e50914;
                color: white;
                padding: 15px 25px;
                border-radius: 5px;
                z-index: 1000;
                animation: slideIn 0.3s ease-out;
            `;
            
            document.body.appendChild(notification);
            
            // Remove after 3 seconds
            setTimeout(() => {
                notification.style.animation = 'slideOut 0.3s ease-out';
                setTimeout(() => notification.remove(), 300);
            }, 3000);
        }
        
        // ===== ARAMA + FİLTRELEME =====
        function filterContent() {
            const search   = document.getElementById('searchInput').value.toLowerCase();
            const type     = document.getElementById('typeFilter').value;
            const category = document.getElementById('categoryFilter').value.toLowerCase();
            const rating   = parseFloat(document.getElementById('ratingFilter').value) || 0;
            
            const cards = document.querySelectorAll('.content-card');
            let visible = 0;
            
            cards.forEach(card => {
                const title    = card.dataset.title || '';
                const cardType = card.dataset.type  || '';
                const cardCat  = card.dataset.category || '';
                const cardRat  = parseFloat(card.dataset.rating) || 0;
                
                const matchSearch   = !search   || title.includes(search);
                const matchType     = !type     || cardType === type;
                const matchCategory = !category || cardCat.includes(category);
                const matchRating   = !rating   || cardRat >= rating;
                
                if (matchSearch && matchType && matchCategory && matchRating) {
                    card.style.display = '';
                    visible++;
                } else {
                    card.style.display = 'none';
                }
            });
            
            document.getElementById('noResults').style.display = visible === 0 ? 'block' : 'none';
        }
        
        function clearFilters() {
            document.getElementById('searchInput').value = '';
            document.getElementById('typeFilter').value = '';
            document.getElementById('categoryFilter').value = '';
            document.getElementById('ratingFilter').value = '';
            filterContent();
        }
        
        // ===== PUANLAMA =====
        function rateContent(contentId, rating, starEl) {
            // Update stars visually
            const container = document.getElementById('stars-' + contentId);
            const stars = container.querySelectorAll('.star');
            stars.forEach((s, i) => {
                s.classList.toggle('active', i < rating);
            });
            
            // Send rating to server
            fetch('/api/rate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({content_id: contentId, rating: rating})
            })
            .then(r => r.json())
            .then(data => {
                if (data.new_rating) {
                    document.getElementById('rval-' + contentId).textContent = data.new_rating;
                    // Update card data-rating for filter
                    const card = container.closest('.content-card');
                    if (card) card.dataset.rating = data.new_rating;
                }
                showNotification(data.message || 'Puan verildi!');
            });
        }
        
        // Load saved ratings on page load - do NOT call filterContent on load
        window.addEventListener('DOMContentLoaded', function() {
            // Make sure all cards are visible on page load
            document.querySelectorAll('.content-card').forEach(c => c.style.display = '');
            document.getElementById('noResults').style.display = 'none';
            
            fetch('/api/my_ratings')
                .then(r => r.json())
                .then(data => {
                    if (data.ratings) {
                        Object.entries(data.ratings).forEach(([cid, rating]) => {
                            const container = document.getElementById('stars-' + cid);
                            if (container) {
                                container.querySelectorAll('.star').forEach((s, i) => {
                                    s.classList.toggle('active', i < rating);
                                });
                            }
                        });
                    }
                });
        });

        function deleteContent(id, title) {
            if (!confirm(`"${title}" içeriğini silmek istediğinizden emin misiniz?`)) {
                return;
            }
            
            fetch(`/api/delete/${id}`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'}
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showNotification(data.message);
                    // Remove card from page
                    setTimeout(() => {
                        location.reload();
                    }, 1000);
                } else {
                    alert(data.message);
                }
            })
            .catch(error => {
                alert('Silme işlemi başarısız oldu!');
                console.error('Error:', error);
            });
        }
        
        // Add CSS animations
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideIn {
                from { transform: translateX(400px); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            @keyframes slideOut {
                from { transform: translateX(0); opacity: 1; }
                to { transform: translateX(400px); opacity: 0; }
            }
        `;
        document.head.appendChild(style);
        
        // استبدال الصور المكسورة أو الفارغة بصور عشوائية
        document.querySelectorAll('.content-thumbnail img').forEach((img, index) => {
            const seed = (img.closest('[data-id]') ? img.closest('[data-id]').dataset.id : index) || index;
            img.onerror = function() {
                this.src = 'https://picsum.photos/seed/' + seed + '/300/450';
                this.onerror = null;
            };
            if (!img.src || img.src.includes('placeholder') || img.src === '') {
                img.src = 'https://picsum.photos/seed/' + (seed + 10) + '/300/450';
            }
        });
    </script>
</body>
</html>
'''

WATCH_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>{{ content.title }} - Netflux</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial; background: #000; color: white; overflow: hidden; }
        
        .video-container { position: relative; width: 100%; height: 100vh; background: #000; }
        
        video, iframe { width: 100%; height: 100%; object-fit: contain; border: none; }
        
        .back-btn { 
            position: absolute; top: 20px; left: 20px; background: rgba(0,0,0,0.8); 
            color: white; border: none; padding: 12px 24px; border-radius: 25px; 
            cursor: pointer; font-size: 16px; z-index: 100; transition: all 0.3s;
            font-weight: 500;
        }
        
        .back-btn:hover { background: #e50914; transform: scale(1.05); }
        
        .title-overlay {
            position: absolute; top: 20px; right: 20px; background: rgba(0,0,0,0.8);
            padding: 15px 25px; border-radius: 8px; z-index: 100; max-width: 400px;
        }
        
        .title-text { font-size: 18px; font-weight: bold; margin-bottom: 5px; }
        .meta-text { font-size: 12px; color: #ccc; }
        
        .progress-indicator {
            position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%);
            background: rgba(0,0,0,0.8); padding: 10px 20px; border-radius: 20px;
            z-index: 100; font-size: 14px; display: none;
        }
        
        .progress-indicator.show { display: block; }
        
        /* Resume Dialog - Netflix Style */
        .resume-dialog {
            position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0, 0, 0, 0.85); z-index: 1000;
            display: none; align-items: center; justify-content: center;
            backdrop-filter: blur(5px);
        }
        
        .resume-dialog.show { display: flex; }
        
        .resume-content {
            background: linear-gradient(145deg, #1a1a1a 0%, #2d2d2d 100%);
            border-radius: 15px; padding: 40px; max-width: 500px; width: 90%;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
            animation: slideIn 0.3s ease-out;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        @keyframes slideIn {
            from { transform: translateY(-50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        
        .resume-icon {
            text-align: center; font-size: 60px; margin-bottom: 20px;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        
        .resume-title {
            font-size: 24px; font-weight: bold; text-align: center;
            margin-bottom: 15px; color: #fff;
        }
        
        .resume-message {
            text-align: center; color: #ccc; font-size: 16px;
            margin-bottom: 10px; line-height: 1.5;
        }
        
        .resume-time {
            text-align: center; font-size: 32px; font-weight: bold;
            color: #e50914; margin: 20px 0; text-shadow: 0 0 20px rgba(229, 9, 20, 0.5);
        }
        
        .resume-buttons {
            display: flex; gap: 15px; margin-top: 30px;
        }
        
        .resume-btn {
            flex: 1; padding: 15px 30px; border: none; border-radius: 8px;
            font-size: 16px; font-weight: 600; cursor: pointer;
            transition: all 0.3s; text-transform: uppercase; letter-spacing: 1px;
        }
        
        .resume-btn-primary {
            background: linear-gradient(135deg, #e50914 0%, #b20710 100%);
            color: white; box-shadow: 0 5px 15px rgba(229, 9, 20, 0.4);
        }
        
        .resume-btn-primary:hover {
            transform: translateY(-2px); box-shadow: 0 8px 25px rgba(229, 9, 20, 0.6);
        }
        
        .resume-btn-secondary {
            background: rgba(255, 255, 255, 0.1); color: white;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }
        
        .resume-btn-secondary:hover {
            background: rgba(255, 255, 255, 0.2); border-color: rgba(255, 255, 255, 0.5);
        }
    </style>
</head>
<body>
    <button class="back-btn" onclick="goBack()">← Geri</button>
    
    <div class="title-overlay">
        <div class="title-text">{{ content.title }}</div>
        <div class="meta-text">{{ content.year }} • {{ content.category }} • {{ content.duration }} dakika</div>
    </div>
    
    <div class="progress-indicator" id="progressIndicator">
        💾 Kaydedildi...
    </div>
    
    <!-- Resume Dialog -->
    <div class="resume-dialog" id="resumeDialog">
        <div class="resume-content">
            <div class="resume-icon">⏯️</div>
            <div class="resume-message">Kaldığınız yer</div>
            <div class="resume-time" id="resumeTimeDisplay">0:00</div>
            <div class="resume-message">Kaldığınız yerden devam etmek ister misiniz?</div>
            <div class="resume-buttons">
                <button class="resume-btn resume-btn-primary" onclick="resumeFromSaved()">
                    ▶️ İzlemeye Devam Et
                </button>
                <button class="resume-btn resume-btn-secondary" onclick="startFromBeginning()">
                    🔄 Baştan Başla
                </button>
            </div>
        </div>
    </div>
    
    <div class="video-container">
        {% if 'youtube.com' in content.video_url or 'youtu.be' in content.video_url %}
            <!-- YouTube Video with API -->
            <div id="player"></div>
            <script src="https://www.youtube.com/iframe_api"></script>
            <script>
                const contentId = {{ content.id }};
                let player;
                let savedProgress = 0;
                let saveInterval;
                
                // Extract video ID from URL
                const videoUrl = "{{ content.video_url }}";
                const videoId = videoUrl.split('/').pop().split('?')[0];
                
                // Load saved progress — pause until user chooses
                fetch(`/api/progress/${contentId}`)
                    .then(r => r.json())
                    .then(data => {
                        if (data.progress && data.progress > 30) {
                            savedProgress = data.progress;
                            document.getElementById('resumeTimeDisplay').textContent = formatTime(savedProgress);
                            document.getElementById('resumeDialog').classList.add('show');
                            video.pause();
                        } else {
                            video.play();
                        }
                    });
                
                // YouTube API ready
                function onYouTubeIframeAPIReady() {
                    player = new YT.Player('player', {
                        height: '100%',
                        width: '100%',
                        videoId: videoId,
                        playerVars: {
                            'autoplay': 0,
                            'controls': 1,
                            'rel': 0,
                            'modestbranding': 1
                        },
                        events: {
                            'onReady': onPlayerReady,
                            'onStateChange': onPlayerStateChange
                        }
                    });
                }
                
                function onPlayerReady(event) {
                    // Just start the interval — dialog already shown, wait for user
                    saveInterval = setInterval(() => {
                        saveProgress();
                    }, 10000);
                }
                
                function resumeFromSaved() {
                    document.getElementById('resumeDialog').classList.remove('show');
                    if (player && player.seekTo) {
                        player.seekTo(savedProgress, true);
                        player.playVideo();
                    }
                }
                
                function startFromBeginning() {
                    document.getElementById('resumeDialog').classList.remove('show');
                    savedProgress = 0;
                    if (player && player.seekTo) {
                        player.seekTo(0, true);
                        player.playVideo();
                    }
                }
                
                function onPlayerStateChange(event) {
                    // Save when paused or ended
                    if (event.data == YT.PlayerState.PAUSED || event.data == YT.PlayerState.ENDED) {
                        saveProgress();
                    }
                }
                
                function saveProgress() {
                    if (player && player.getCurrentTime) {
                        const currentTime = Math.floor(player.getCurrentTime());
                        if (currentTime > 0) {
                            fetch('/api/progress', {
                                method: 'POST',
                                headers: {'Content-Type': 'application/json'},
                                body: JSON.stringify({
                                    content_id: contentId,
                                    progress: currentTime
                                })
                            }).then(() => {
                                showProgressIndicator();
                            });
                        }
                    }
                }
                
                function showProgressIndicator() {
                    const indicator = document.getElementById('progressIndicator');
                    indicator.classList.add('show');
                    setTimeout(() => {
                        indicator.classList.remove('show');
                    }, 2000);
                }
                
                function formatTime(seconds) {
                    const m = Math.floor(seconds / 60);
                    const s = Math.floor(seconds % 60);
                    return `${m}:${s.toString().padStart(2, '0')}`;
                }
                
                function goBack() {
                    clearInterval(saveInterval);
                    if (player && player.getCurrentTime) {
                        const currentTime = Math.floor(player.getCurrentTime());
                        if (currentTime > 0) {
                            navigator.sendBeacon('/api/progress', JSON.stringify({
                                content_id: contentId, progress: currentTime
                            }));
                        }
                    }
                    window.location.href = '/';
                }
            </script>
        {% else %}
            <!-- MP4 Video -->
            <video id="videoPlayer" controls>
                <source src="{{ content.video_url }}" type="video/mp4">
                متصفحك لا يدعم تشغيل الفيديو
            </video>
            <script>
                const contentId = {{ content.id }};
                const video = document.getElementById('videoPlayer');
                let savedProgress = 0;
                
                // Load saved progress — pause until user chooses
                fetch(`/api/progress/${contentId}`)
                    .then(r => r.json())
                    .then(data => {
                        if (data.progress && data.progress > 30) {
                            savedProgress = data.progress;
                            document.getElementById('resumeTimeDisplay').textContent = formatTime(savedProgress);
                            document.getElementById('resumeDialog').classList.add('show');
                            video.pause();
                        } else {
                            video.play();
                        }
                    });
                
                function resumeFromSaved() {
                    document.getElementById('resumeDialog').classList.remove('show');
                    if (video.readyState >= 1) {
                        video.currentTime = savedProgress;
                        video.play();
                    } else {
                        video.addEventListener('loadedmetadata', function() {
                            video.currentTime = savedProgress;
                            video.play();
                        }, { once: true });
                    }
                }
                
                function startFromBeginning() {
                    document.getElementById('resumeDialog').classList.remove('show');
                    video.currentTime = 0;
                    video.play();
                }
                
                function saveProgress() {
                    if (video.currentTime > 0) {
                        fetch('/api/progress', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({
                                content_id: contentId,
                                progress: Math.floor(video.currentTime)
                            })
                        }).then(() => {
                            showProgressIndicator();
                        });
                    }
                }
                
                function showProgressIndicator() {
                    const indicator = document.getElementById('progressIndicator');
                    indicator.classList.add('show');
                    setTimeout(() => {
                        indicator.classList.remove('show');
                    }, 2000);
                }
                
                function formatTime(seconds) {
                    const m = Math.floor(seconds / 60);
                    const s = Math.floor(seconds % 60);
                    return `${m}:${s.toString().padStart(2, '0')}`;
                }
                
                function goBack() {
                    if (video.currentTime > 0) {
                        navigator.sendBeacon('/api/progress', JSON.stringify({
                            content_id: contentId, progress: Math.floor(video.currentTime)
                        }));
                    }
                    window.location.href = '/';
                }
                
                // Auto-save every 10 seconds
                setInterval(() => {
                    if (!video.paused && video.currentTime > 0) {
                        saveProgress();
                    }
                }, 10000);
                
                // Save on pause
                video.addEventListener('pause', saveProgress);
            </script>
        {% endif %}
    </div>
</body>
</html>
'''

PROFILE_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Profil - Netflux</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #0a0a0a;
            color: white;
            min-height: 100vh;
            position: relative;
            overflow-x: hidden;
        }
        
        /* Animated Background */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(229, 9, 20, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(139, 0, 0, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 40% 20%, rgba(255, 26, 26, 0.1) 0%, transparent 50%),
                linear-gradient(135deg, #0a0a0a 0%, #1a0a0a 50%, #0a0a0a 100%);
            z-index: -2;
        }
        
        @keyframes backgroundShift {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.9; }
        }
        
        /* Header */
        .header { 
            background: linear-gradient(180deg, rgba(10,10,10,0.98) 0%, rgba(10,10,10,0.95) 100%);
            padding: 20px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 30px rgba(229, 9, 20, 0.2);
            backdrop-filter: blur(20px);
            position: sticky;
            top: 0;
            z-index: 100;
            border-bottom: 1px solid rgba(229, 9, 20, 0.2);
        }
        
        .logo { 
            font-size: 36px;
            font-weight: 900;
            background: linear-gradient(135deg, #e50914 0%, #ff4444 50%, #e50914 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shimmer 3s linear infinite;
            letter-spacing: -2px;
            cursor: pointer;
        }
        
        @keyframes shimmer {
            to { background-position: 200% center; }
        }
        
        .nav { 
            display: flex;
            gap: 8px;
            background: rgba(255, 255, 255, 0.03);
            padding: 8px;
            border-radius: 50px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        .nav a { 
            color: #e0e0e0;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            padding: 12px 24px;
            border-radius: 50px;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .nav a:hover {
            color: #fff;
            background: linear-gradient(135deg, rgba(229, 9, 20, 0.3) 0%, rgba(229, 9, 20, 0.1) 100%);
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(229, 9, 20, 0.4);
        }
        
        /* Container */
        .container { 
            padding: 50px;
            max-width: 900px;
            margin: 0 auto;
        }
        
        .page-title { 
            font-size: 42px;
            font-weight: 900;
            margin: 30px 0 40px 0;
            text-align: center;
            background: linear-gradient(135deg, #fff 0%, #e50914 50%, #fff 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shimmer 4s linear infinite;
            letter-spacing: -2px;
        }
        
        /* Cards */
        .profile-card, .info-box { 
            background: linear-gradient(145deg, rgba(30,30,30,0.8) 0%, rgba(42,42,42,0.6) 100%);
            padding: 35px;
            border-radius: 20px;
            margin-bottom: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
        }
        
        .info-box {
            border-left: 4px solid #e50914;
        }
        
        /* Alerts */
        .alert { 
            padding: 18px 25px;
            border-radius: 15px;
            margin-bottom: 25px;
            text-align: center;
            font-weight: 600;
            backdrop-filter: blur(10px);
            border: 1px solid;
        }
        
        .alert-success { 
            background: linear-gradient(135deg, rgba(40, 167, 69, 0.3) 0%, rgba(40, 167, 69, 0.2) 100%);
            color: #4ade80;
            border-color: rgba(40, 167, 69, 0.4);
        }
        
        .alert-error { 
            background: linear-gradient(135deg, rgba(229, 9, 20, 0.3) 0%, rgba(229, 9, 20, 0.2) 100%);
            color: #ff6b6b;
            border-color: rgba(229, 9, 20, 0.4);
        }
        
        /* Form */
        .form-group { 
            margin-bottom: 25px;
        }
        
        .form-group label { 
            display: block;
            margin-bottom: 10px;
            color: #e0e0e0;
            font-size: 15px;
            font-weight: 600;
        }
        
        .form-group input { 
            width: 100%;
            padding: 16px 20px;
            background: rgba(255, 255, 255, 0.05);
            border: 2px solid rgba(255, 255, 255, 0.1);
            color: white;
            border-radius: 12px;
            font-size: 15px;
            transition: all 0.3s ease;
            font-weight: 500;
        }
        
        .form-group input:focus {
            outline: none;
            background: rgba(255, 255, 255, 0.08);
            border-color: #e50914;
            box-shadow: 0 0 25px rgba(229, 9, 20, 0.3);
            transform: translateY(-2px);
        }
        
        .form-group small { 
            color: #999;
            font-size: 13px;
            display: block;
            margin-top: 8px;
        }
        
        /* Buttons */
        .btn-group { 
            display: flex;
            gap: 15px;
            margin-top: 35px;
        }
        
        .btn { 
            padding: 16px 32px;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            font-size: 15px;
            font-weight: 700;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .btn-primary { 
            background: linear-gradient(135deg, #e50914 0%, #b0070f 100%);
            color: white;
            flex: 1;
            box-shadow: 0 8px 25px rgba(229, 9, 20, 0.4);
        }
        
        .btn-primary:hover {
            background: linear-gradient(135deg, #ff1a1a 0%, #e50914 100%);
            transform: translateY(-3px);
            box-shadow: 0 12px 35px rgba(229, 9, 20, 0.6);
        }
        
        .btn-secondary { 
            background: linear-gradient(145deg, rgba(102,102,102,0.8) 0%, rgba(68,68,68,0.8) 100%);
            color: white;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        }
        
        .btn-secondary:hover {
            background: linear-gradient(145deg, rgba(119,119,119,0.9) 0%, rgba(85,85,85,0.9) 100%);
            transform: translateY(-3px);
        }
        
        /* Info Items */
        .info-item { 
            margin: 18px 0;
            padding: 15px;
            background: rgba(255, 255, 255, 0.02);
            border-radius: 10px;
        }
        
        .info-label { 
            color: #999;
            font-size: 13px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }
        
        .info-value { 
            color: white;
            font-size: 18px;
            font-weight: 700;
        }
        
        h2 {
            font-size: 24px;
            font-weight: 800;
            margin-bottom: 25px;
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">🎬 Netflux</div>
        <div class="nav">
            <a href="/">Ana Sayfa</a>
            <a href="/movies">Filmler</a>
            <a href="/series">Diziler</a>
            <a href="/profile">Profil</a>
            {% if session.user_type == 'admin' %}
            <a href="/add">İçerik Ekle</a>
            {% endif %}
            <a href="/logout">Çıkış</a>
        </div>
    </div>
    
    <div class="container">
        <h1 class="page-title">👤 Profil Ayarları</h1>
        
        {% if success %}
        <div class="alert alert-success">✅ {{ success }}</div>
        {% endif %}
        
        {% if error %}
        <div class="alert alert-error">❌ {{ error }}</div>
        {% endif %}
        
        <div class="info-box">
            <div class="info-item">
                <div class="info-label">E-posta</div>
                <div class="info-value">{{ session.user_email }}</div>
            </div>
            <div class="info-item">
                <div class="info-label">Hesap Tipi</div>
                <div class="info-value">{{ session.user_type }}</div>
            </div>
        </div>
        
        <div class="profile-card">
            <h2 style="margin-bottom: 20px;">✏️ Profili Düzenle</h2>
            <form method="POST">
                <div class="form-group">
                    <label>👤 İsim</label>
                    <input type="text" name="name" value="{{ session.user_name }}" required>
                </div>
                
                <div class="form-group">
                    <label>🔒 Yeni Şifre (İsteğe bağlı)</label>
                    <input type="password" name="password" placeholder="Değiştirmek istemiyorsanız boş bırakın">
                    <small>Şifrenizi değiştirmek istemiyorsanız bu alanı boş bırakın</small>
                </div>
                
                <div class="form-group">
                    <label>🔒 Yeni Şifre Tekrar</label>
                    <input type="password" name="confirm_password" placeholder="Yeni şifreyi tekrar girin">
                </div>
                
                <div class="btn-group">
                    <button type="submit" class="btn btn-primary">💾 Kaydet</button>
                    <a href="/" class="btn btn-secondary" style="text-align: center; text-decoration: none; line-height: 1.5;">❌ İptal</a>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
'''
