"""
templates/admin_templates.py
=============================
قوالب HTML للمشرف - Admin HTML Templates
يشمل:
  - ADD_CONTENT_TEMPLATE  : نموذج إضافة محتوى جديد
  - EDIT_CONTENT_TEMPLATE : نموذج تعديل محتوى موجود
"""

ADD_CONTENT_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>İçerik Ekle - Netflux</title>
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
                linear-gradient(135deg, #0a0a0a 0%, #1a0a0a 50%, #0a0a0a 100%);
            z-index: -1;
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
            font-size: 32px;
            font-weight: 900;
            background: linear-gradient(135deg, #e50914 0%, #ff4444 50%, #e50914 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shimmer 3s linear infinite;
            letter-spacing: -2px;
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
        }
        
        .nav a:hover {
            color: #fff;
            background: linear-gradient(135deg, rgba(229, 9, 20, 0.3) 0%, rgba(229, 9, 20, 0.1) 100%);
            transform: translateY(-2px);
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
            margin-bottom: 15px;
            background: linear-gradient(135deg, #fff 0%, #e50914 50%, #fff 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shimmer 4s linear infinite;
            letter-spacing: -2px;
        }
        
        .page-subtitle { 
            color: #b3b3b3;
            margin-bottom: 40px;
            font-size: 16px;
        }
        
        /* Form Card */
        .form-card { 
            background: linear-gradient(145deg, rgba(30,30,30,0.8) 0%, rgba(42,42,42,0.6) 100%);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
        }
        
        .form-group { 
            margin-bottom: 25px;
        }
        
        .form-group label { 
            display: block;
            margin-bottom: 10px;
            color: #e0e0e0;
            font-size: 14px;
            font-weight: 600;
        }
        
        .form-group input, .form-group select, .form-group textarea { 
            width: 100%;
            padding: 14px 18px;
            background: rgba(255, 255, 255, 0.05);
            border: 2px solid rgba(255, 255, 255, 0.1);
            color: white;
            border-radius: 12px;
            font-size: 14px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            transition: all 0.3s ease;
        }
        
        .form-group input:focus, .form-group select:focus, .form-group textarea:focus {
            outline: none;
            border-color: #e50914;
            background: rgba(255, 255, 255, 0.08);
            box-shadow: 0 0 20px rgba(229, 9, 20, 0.3);
        }
        
        .form-group textarea { 
            min-height: 120px;
            resize: vertical;
        }
        
        .form-group small { 
            color: #999;
            font-size: 12px;
            display: block;
            margin-top: 8px;
        }
        
        .form-row { 
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
        }
        
        /* Error Message */
        .error-message { 
            background: linear-gradient(135deg, #e50914 0%, #b0070f 100%);
            color: white;
            padding: 18px 25px;
            border-radius: 15px;
            margin-bottom: 25px;
            text-align: center;
            font-weight: 600;
            box-shadow: 0 5px 20px rgba(229, 9, 20, 0.4);
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
            font-size: 16px;
            font-weight: 600;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .btn-primary { 
            background: linear-gradient(135deg, #e50914 0%, #b0070f 100%);
            color: white;
            flex: 1;
            box-shadow: 0 5px 20px rgba(229, 9, 20, 0.4);
        }
        
        .btn-primary:hover { 
            transform: translateY(-3px);
            box-shadow: 0 8px 30px rgba(229, 9, 20, 0.6);
        }
        
        .btn-secondary { 
            background: rgba(255, 255, 255, 0.1);
            color: white;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        .btn-secondary:hover { 
            background: rgba(255, 255, 255, 0.15);
            transform: translateY(-2px);
        }
        
        /* Info Box */
        .info-box {
            background: linear-gradient(135deg, rgba(229, 9, 20, 0.1) 0%, rgba(229, 9, 20, 0.05) 100%);
            border-left: 4px solid #e50914;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
        }
        
        .info-box h3 { 
            color: #e50914;
            margin-bottom: 12px;
            font-size: 16px;
            font-weight: 700;
        }
        
        .info-box ul { 
            margin-left: 20px;
            color: #ccc;
        }
        
        .info-box li { 
            margin: 8px 0;
            line-height: 1.6;
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
            <a href="/add">İçerik Ekle</a>
            <a href="/logout">Çıkış</a>
        </div>
    </div>
    
    <div class="container">
        <h1 class="page-title">➕ Yeni İçerik Ekle</h1>
        <p class="page-subtitle">Film veya dizi eklemek için aşağıdaki formu doldurun</p>
        
        {% if error %}
        <div class="error-message">{{ error }}</div>
        {% endif %}
        
        <div class="info-box">
            <h3>📝 Önemli Notlar:</h3>
            <ul>
                <li><strong>YouTube videoları:</strong> https://www.youtube.com/embed/VIDEO_ID formatında olmalı</li>
                <li><strong>MP4 videoları:</strong> Doğrudan .mp4 dosya linki kullanın</li>
                <li><strong>Resim URL:</strong> Boş bırakırsanız otomatik oluşturulur</li>
            </ul>
        </div>
        
        <div class="form-card">
            <form method="POST">
                <div class="form-group">
                    <label>📺 Başlık *</label>
                    <input type="text" name="title" required placeholder="Örn: Recep İvedik 7">
                </div>
                
                <div class="form-group">
                    <label>📝 Açıklama</label>
                    <textarea name="description" placeholder="Film veya dizi hakkında kısa açıklama..."></textarea>
                </div>
                
                <div class="form-row">
                    <div class="form-group">
                        <label>📅 Yıl</label>
                        <input type="number" name="year" value="2024" min="1900" max="2030">
                    </div>
                    
                    <div class="form-group">
                        <label>🎬 Tip</label>
                        <select name="content_type">
                            <option value="film">Film</option>
                            <option value="dizi">Dizi</option>
                        </select>
                    </div>
                </div>
                
                <div class="form-group">
                    <label>🎭 Kategori</label>
                    <input type="text" name="category" placeholder="Örn: Komedi, Aksiyon, Drama">
                </div>
                
                <div class="form-group">
                    <label>🎥 Video URL *</label>
                    <input type="url" name="video_url" required placeholder="https://www.youtube.com/embed/... veya https://...video.mp4">
                    <small>YouTube için: https://www.youtube.com/embed/VIDEO_ID</small>
                </div>
                
                <div class="form-group">
                    <label>🖼️ Resim URL (İsteğe bağlı)</label>
                    <input type="url" name="image_url" placeholder="https://...image.jpg">
                </div>
                
                <div class="form-row">
                    <div class="form-group">
                        <label>⭐ Puan (0-10)</label>
                        <input type="number" name="rating" value="7.0" min="0" max="10" step="0.1">
                    </div>
                    
                    <div class="form-group">
                        <label>⏱️ Süre (dakika)</label>
                        <input type="number" name="duration" value="90" min="1">
                    </div>
                </div>
                
                <div class="btn-group">
                    <button type="submit" class="btn btn-primary">✅ İçeriği Ekle</button>
                    <a href="/" class="btn btn-secondary">❌ İptal</a>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
'''

EDIT_CONTENT_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>İçeriği Düzenle - Netflux</title>
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
                linear-gradient(135deg, #0a0a0a 0%, #1a0a0a 50%, #0a0a0a 100%);
            z-index: -1;
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
            font-size: 32px;
            font-weight: 900;
            background: linear-gradient(135deg, #e50914 0%, #ff4444 50%, #e50914 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shimmer 3s linear infinite;
            letter-spacing: -2px;
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
        }
        
        .nav a:hover {
            color: #fff;
            background: linear-gradient(135deg, rgba(229, 9, 20, 0.3) 0%, rgba(229, 9, 20, 0.1) 100%);
            transform: translateY(-2px);
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
            margin-bottom: 15px;
            background: linear-gradient(135deg, #fff 0%, #e50914 50%, #fff 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shimmer 4s linear infinite;
            letter-spacing: -2px;
        }
        
        .page-subtitle { 
            color: #b3b3b3;
            margin-bottom: 40px;
            font-size: 16px;
        }
        
        /* Form Card */
        .form-card { 
            background: linear-gradient(145deg, rgba(30,30,30,0.8) 0%, rgba(42,42,42,0.6) 100%);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
        }
        
        .form-group { 
            margin-bottom: 25px;
        }
        
        .form-group label { 
            display: block;
            margin-bottom: 10px;
            color: #e0e0e0;
            font-size: 14px;
            font-weight: 600;
        }
        
        .form-group input, .form-group select, .form-group textarea { 
            width: 100%;
            padding: 14px 18px;
            background: rgba(255, 255, 255, 0.05);
            border: 2px solid rgba(255, 255, 255, 0.1);
            color: white;
            border-radius: 12px;
            font-size: 14px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            transition: all 0.3s ease;
        }
        
        .form-group input:focus, .form-group select:focus, .form-group textarea:focus {
            outline: none;
            border-color: #e50914;
            background: rgba(255, 255, 255, 0.08);
            box-shadow: 0 0 20px rgba(229, 9, 20, 0.3);
        }
        
        .form-group textarea { 
            min-height: 120px;
            resize: vertical;
        }
        
        .form-group small { 
            color: #999;
            font-size: 12px;
            display: block;
            margin-top: 8px;
        }
        
        .form-row { 
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
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
            font-size: 16px;
            font-weight: 600;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
            text-decoration: none;
            text-align: center;
            display: inline-block;
        }
        
        .btn-primary { 
            background: linear-gradient(135deg, #e50914 0%, #b0070f 100%);
            color: white;
            flex: 1;
            box-shadow: 0 5px 20px rgba(229, 9, 20, 0.4);
        }
        
        .btn-primary:hover { 
            transform: translateY(-3px);
            box-shadow: 0 8px 30px rgba(229, 9, 20, 0.6);
        }
        
        .btn-secondary { 
            background: rgba(255, 255, 255, 0.1);
            color: white;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        .btn-secondary:hover { 
            background: rgba(255, 255, 255, 0.15);
            transform: translateY(-2px);
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
            <a href="/add">İçerik Ekle</a>
            <a href="/logout">Çıkış</a>
        </div>
    </div>
    
    <div class="container">
<!DOCTYPE html>
<html>
<head>
    <title>İçeriği Düzenle - Netflux</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial; background: #141414; color: white; }
        
        .header { background: #000; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 24px; color: #e50914; font-weight: bold; }
        .nav { display: flex; gap: 20px; }
        .nav a { color: white; text-decoration: none; transition: color 0.3s; }
        .nav a:hover { color: #e50914; }
        
        .container { padding: 40px; max-width: 700px; margin: 0 auto; }
        .page-title { font-size: 32px; margin-bottom: 10px; color: #e50914; }
        .page-subtitle { color: #999; margin-bottom: 30px; }
        
        .form-card { background: #222; padding: 30px; border-radius: 10px; }
        
        .form-group { margin-bottom: 20px; }
        .form-group label { 
            display: block; margin-bottom: 8px; color: #ccc; font-size: 14px; font-weight: 500;
        }
        .form-group input, .form-group select, .form-group textarea { 
            width: 100%; padding: 12px; background: #333; border: 1px solid #444; 
            color: white; border-radius: 5px; font-size: 14px; font-family: Arial;
        }
        .form-group input:focus, .form-group select:focus, .form-group textarea:focus {
            outline: none; border-color: #e50914; background: #3a3a3a;
        }
        .form-group textarea { min-height: 100px; resize: vertical; }
        .form-group small { color: #999; font-size: 12px; display: block; margin-top: 5px; }
        
        .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        
        .btn-group { display: flex; gap: 15px; margin-top: 30px; }
        .btn { 
            padding: 12px 30px; border: none; border-radius: 5px; 
            cursor: pointer; font-size: 16px; font-weight: 500; transition: all 0.3s;
            text-decoration: none; text-align: center;
        }
        .btn-primary { background: #e50914; color: white; flex: 1; }
        .btn-primary:hover { background: #b0070f; transform: translateY(-2px); }
        .btn-secondary { background: #666; color: white; }
        .btn-secondary:hover { background: #888; }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">🎬 Netflux</div>
        <div class="nav">
            <a href="/">Ana Sayfa</a>
            <a href="/add">İçerik Ekle</a>
            <a href="/logout">Çıkış</a>
        </div>
    </div>
    
    <div class="container">
        <h1 class="page-title">✏️ İçeriği Düzenle</h1>
        <p class="page-subtitle">{{ content.title }} - Bilgileri güncelleyin</p>
        
        <div class="form-card">
            <form method="POST">
                <div class="form-group">
                    <label>📺 Başlık *</label>
                    <input type="text" name="title" value="{{ content.title }}" required>
                </div>
                
                <div class="form-group">
                    <label>📝 Açıklama</label>
                    <textarea name="description">{{ content.description }}</textarea>
                </div>
                
                <div class="form-row">
                    <div class="form-group">
                        <label>📅 Yıl</label>
                        <input type="number" name="year" value="{{ content.year }}" min="1900" max="2030">
                    </div>
                    
                    <div class="form-group">
                        <label>🎬 Tip</label>
                        <select name="content_type">
                            <option value="film" {% if content.type == 'film' %}selected{% endif %}>Film</option>
                            <option value="dizi" {% if content.type == 'dizi' %}selected{% endif %}>Dizi</option>
                        </select>
                    </div>
                </div>
                
                <div class="form-group">
                    <label>🎭 Kategori</label>
                    <input type="text" name="category" value="{{ content.category }}">
                </div>
                
                <div class="form-group">
                    <label>🎥 Video URL *</label>
                    <input type="url" name="video_url" value="{{ content.video_url }}" required>
                </div>
                
                <div class="form-group">
                    <label>🖼️ Resim URL</label>
                    <input type="url" name="image_url" value="{{ content.image_url }}">
                </div>
                
                <div class="form-row">
                    <div class="form-group">
                        <label>⭐ Puan (0-10)</label>
                        <input type="number" name="rating" value="{{ content.rating }}" min="0" max="10" step="0.1">
                    </div>
                    
                    <div class="form-group">
                        <label>⏱️ Süre (dakika)</label>
                        <input type="number" name="duration" value="{{ content.duration }}" min="1">
                    </div>
                </div>
                
                <div class="btn-group">
                    <button type="submit" class="btn btn-primary">💾 Güncelle</button>
                    <a href="/" class="btn btn-secondary">❌ İptal</a>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
'''
