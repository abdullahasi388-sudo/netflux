"""
templates/auth_templates.py
============================
قوالب HTML للمصادقة - Auth HTML Templates
يشمل:
  - LOGIN_TEMPLATE          : صفحة تسجيل الدخول
  - REGISTER_TEMPLATE       : صفحة إنشاء حساب
  - REGISTER_SUCCESS_TEMPLATE: صفحة نجاح التسجيل
"""

LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Netflux - Giriş</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #0a0a0a;
            color: white;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }
        
        /* Cinematic Background */
        body::before {
            content: '';
            position: fixed;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: 
                radial-gradient(circle at 30% 40%, rgba(229, 9, 20, 0.25) 0%, transparent 40%),
                radial-gradient(circle at 70% 60%, rgba(139, 0, 0, 0.2) 0%, transparent 40%),
                radial-gradient(circle at 50% 50%, rgba(255, 26, 26, 0.15) 0%, transparent 50%);
            animation: rotate 30s linear infinite;
            z-index: -2;
        }
        
        body::after {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                linear-gradient(135deg, rgba(10,10,10,0.9) 0%, rgba(26,10,10,0.85) 50%, rgba(10,10,10,0.9) 100%),
                repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(229, 9, 20, 0.03) 3px, rgba(229, 9, 20, 0.03) 6px);
            z-index: -1;
        }
        
        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Floating particles */
        .particle {
            position: fixed;
            width: 3px;
            height: 3px;
            background: rgba(229, 9, 20, 0.6);
            border-radius: 50%;
            animation: float 15s infinite;
            z-index: -1;
        }
        
        @keyframes float {
            0%, 100% {
                transform: translateY(0) translateX(0);
                opacity: 0;
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translateY(-100vh) translateX(50px);
                opacity: 0;
            }
        }
        
        .container { 
            max-width: 480px;
            width: 100%;
            background: linear-gradient(145deg, rgba(30,30,30,0.95) 0%, rgba(42,42,42,0.9) 100%);
            padding: 60px 50px;
            border-radius: 25px;
            box-shadow: 
                0 30px 90px rgba(0, 0, 0, 0.7),
                0 0 80px rgba(229, 9, 20, 0.3),
                inset 0 0 0 1px rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px) saturate(180%);
            position: relative;
            z-index: 1;
        }
        
        .container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, transparent, #e50914, transparent);
            border-radius: 25px 25px 0 0;
        }
        
        .logo { 
            text-align: center;
            font-size: 56px;
            font-weight: 900;
            background: linear-gradient(135deg, #e50914 0%, #ff4444 50%, #e50914 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 50px;
            animation: shimmer 3s linear infinite;
            letter-spacing: -3px;
            filter: drop-shadow(0 0 30px rgba(229, 9, 20, 0.6));
        }
        
        @keyframes shimmer {
            to { background-position: 200% center; }
        }
        
        h2 {
            text-align: center;
            margin-bottom: 35px;
            font-size: 30px;
            font-weight: 800;
            color: #fff;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .error {
            background: linear-gradient(135deg, rgba(229, 9, 20, 0.25) 0%, rgba(180, 7, 15, 0.25) 100%);
            color: #ff6b6b;
            padding: 18px;
            border-radius: 15px;
            margin-bottom: 25px;
            text-align: center;
            border: 1px solid rgba(229, 9, 20, 0.4);
            font-weight: 600;
            backdrop-filter: blur(10px);
        }
        
        input { 
            width: 100%;
            padding: 18px 24px;
            margin: 15px 0;
            background: rgba(255, 255, 255, 0.05);
            border: 2px solid rgba(255, 255, 255, 0.1);
            color: white;
            border-radius: 15px;
            font-size: 15px;
            transition: all 0.4s ease;
            font-weight: 500;
        }
        
        input:focus {
            outline: none;
            background: rgba(255, 255, 255, 0.08);
            border-color: #e50914;
            box-shadow: 0 0 30px rgba(229, 9, 20, 0.4), inset 0 0 20px rgba(229, 9, 20, 0.1);
            transform: translateY(-2px);
        }
        
        input::placeholder {
            color: rgba(255, 255, 255, 0.4);
        }
        
        button { 
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #e50914 0%, #b0070f 100%);
            color: white;
            border: none;
            border-radius: 15px;
            font-size: 17px;
            font-weight: 800;
            cursor: pointer;
            margin-top: 25px;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 10px 30px rgba(229, 9, 20, 0.5);
            text-transform: uppercase;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
        }
        
        button::before {
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
        
        button:hover::before {
            width: 400px;
            height: 400px;
        }
        
        button:hover {
            background: linear-gradient(135deg, #ff1a1a 0%, #e50914 100%);
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(229, 9, 20, 0.7);
        }
        
        button:active {
            transform: translateY(-1px);
        }
        
        .back-link { 
            text-align: center;
            margin-top: 35px;
            color: #b3b3b3;
            font-size: 14px;
            font-weight: 500;
        }
        
        .back-link a { 
            color: #e50914;
            text-decoration: none;
            font-weight: 700;
            transition: all 0.3s ease;
            position: relative;
        }
        
        .back-link a::after {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 0;
            height: 2px;
            background: #e50914;
            transition: width 0.3s ease;
        }
        
        .back-link a:hover {
            color: #ff1a1a;
        }
        
        .back-link a:hover::after {
            width: 100%;
        }
    </style>
</head>
<body>
    <!-- Floating particles -->
    <div class="particle" style="left: 10%; animation-delay: 0s;"></div>
    <div class="particle" style="left: 20%; animation-delay: 2s;"></div>
    <div class="particle" style="left: 30%; animation-delay: 4s;"></div>
    <div class="particle" style="left: 40%; animation-delay: 1s;"></div>
    <div class="particle" style="left: 50%; animation-delay: 3s;"></div>
    <div class="particle" style="left: 60%; animation-delay: 5s;"></div>
    <div class="particle" style="left: 70%; animation-delay: 2.5s;"></div>
    <div class="particle" style="left: 80%; animation-delay: 4.5s;"></div>
    <div class="particle" style="left: 90%; animation-delay: 1.5s;"></div>
    
    <div class="container">
        <div class="logo">🎬 Netflux</div>
        <h2>Giriş Yap</h2>
        
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
        
        <form method="POST" id="loginForm">
            <input type="email" name="email" id="emailInput" placeholder="E-posta adresinizi girin" required>
            <input type="password" name="password" id="passwordInput" placeholder="Şifrenizi girin" required>
            
            <div style="display:flex; align-items:center; gap:10px; margin:15px 0;">
                <input type="checkbox" name="remember" id="rememberMe" value="1"
                       style="width:20px; height:20px; margin:0; cursor:pointer; accent-color:#e50914;">
                <label for="rememberMe" style="color:#b3b3b3; font-size:14px; cursor:pointer;">
                    Beni Hatırla
                </label>
            </div>
            
            <button type="submit">Giriş Yap</button>
        </form>
        
        <div class="back-link">
            <p>Netflux'ta yeni misiniz? <a href="/register">Üye olun</a></p>
        </div>
    </div>
    
    <script>
        // Cookie helper functions
        function setCookie(name, value, days) {
            const expires = new Date(Date.now() + days * 864e5).toUTCString();
            document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/';
        }
        function getCookie(name) {
            return document.cookie.split('; ').reduce((r, v) => {
                const parts = v.split('=');
                return parts[0] === name ? decodeURIComponent(parts[1]) : r;
            }, '');
        }
        
        // Auto-fill saved email/password
        const savedEmail = getCookie('netflux_email');
        const savedPass  = getCookie('netflux_pass');
        if (savedEmail) {
            document.getElementById('emailInput').value = savedEmail;
            document.getElementById('rememberMe').checked = true;
        }
        if (savedPass) {
            document.getElementById('passwordInput').value = savedPass;
        }
        
        // Save to cookie on submit
        document.getElementById('loginForm').addEventListener('submit', function() {
            if (document.getElementById('rememberMe').checked) {
                setCookie('netflux_email', document.getElementById('emailInput').value, 30);
                setCookie('netflux_pass',  document.getElementById('passwordInput').value, 30);
            } else {
                // Clear saved cookies if unchecked
                setCookie('netflux_email', '', -1);
                setCookie('netflux_pass',  '', -1);
            }
        });
    </script>
</body>
</html>
'''

REGISTER_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Kayıt Ol - Netflux</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #0a0a0a; color: white; min-height: 100vh;
            display: flex; align-items: center; justify-content: center;
            padding: 20px; position: relative; overflow: hidden;
        }
        body::before {
            content: ''; position: fixed; top: -50%; left: -50%;
            width: 200%; height: 200%;
            background: radial-gradient(circle at 30% 40%, rgba(229, 9, 20, 0.25) 0%, transparent 40%),
                        radial-gradient(circle at 70% 60%, rgba(139, 0, 0, 0.2) 0%, transparent 40%);
            animation: rotate 30s linear infinite; z-index: -2;
        }
        @keyframes rotate { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .container { 
            max-width: 480px; width: 100%;
            background: linear-gradient(145deg, rgba(30,30,30,0.95) 0%, rgba(42,42,42,0.9) 100%);
            padding: 60px 50px; border-radius: 25px;
            box-shadow: 0 30px 90px rgba(0, 0, 0, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px); position: relative; z-index: 1;
        }
        .logo { 
            text-align: center; font-size: 56px; font-weight: 900;
            background: linear-gradient(135deg, #e50914 0%, #ff4444 50%, #e50914 100%);
            background-size: 200% auto; -webkit-background-clip: text;
            -webkit-text-fill-color: transparent; margin-bottom: 50px;
            animation: shimmer 3s linear infinite; letter-spacing: -3px;
        }
        @keyframes shimmer { to { background-position: 200% center; } }
        h2 { text-align: center; margin-bottom: 35px; font-size: 30px; font-weight: 800; color: #fff; text-transform: uppercase; letter-spacing: 1px; }
        .error { background: linear-gradient(135deg, rgba(229, 9, 20, 0.25) 0%, rgba(180, 7, 15, 0.25) 100%); color: #ff6b6b; padding: 18px; border-radius: 15px; margin-bottom: 25px; text-align: center; border: 1px solid rgba(229, 9, 20, 0.4); font-weight: 600; }
        input { width: 100%; padding: 18px 24px; margin: 15px 0; background: rgba(255, 255, 255, 0.05); border: 2px solid rgba(255, 255, 255, 0.1); color: white; border-radius: 15px; font-size: 15px; transition: all 0.4s ease; font-weight: 500; }
        input:focus { outline: none; background: rgba(255, 255, 255, 0.08); border-color: #e50914; box-shadow: 0 0 30px rgba(229, 9, 20, 0.4); transform: translateY(-2px); }
        input::placeholder { color: rgba(255, 255, 255, 0.4); }
        button { width: 100%; padding: 18px; background: linear-gradient(135deg, #e50914 0%, #b0070f 100%); color: white; border: none; border-radius: 15px; font-size: 17px; font-weight: 800; cursor: pointer; margin-top: 25px; transition: all 0.4s ease; box-shadow: 0 10px 30px rgba(229, 9, 20, 0.5); text-transform: uppercase; letter-spacing: 1px; }
        button:hover { background: linear-gradient(135deg, #ff1a1a 0%, #e50914 100%); transform: translateY(-3px); box-shadow: 0 15px 40px rgba(229, 9, 20, 0.7); }
        .back-link { text-align: center; margin-top: 35px; color: #b3b3b3; font-size: 14px; font-weight: 500; }
        .back-link a { color: #e50914; text-decoration: none; font-weight: 700; transition: all 0.3s ease; }
        .back-link a:hover { color: #ff1a1a; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🎬 Netflux</div>
        <h2>Kayıt Ol</h2>
        {% if error %}
        <div class="error">{ error }</div>
        {% endif %}
        <form method="POST">
            <input type="text" name="name" placeholder="Adınız Soyadınız" required>
            <input type="email" name="email" placeholder="E-posta adresiniz" required>
            <input type="password" name="password" placeholder="Şifre (en az 6 karakter)" required minlength="6">
            <input type="password" name="confirm_password" placeholder="Şifre Tekrar" required>
            <button type="submit">Kayıt Ol</button>
        </form>
        <div class="back-link">
            <p>Zaten hesabınız var mı? <a href="/">Giriş yapın</a></p>
        </div>
    </div>
</body>
</html>
'''

REGISTER_SUCCESS_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Kayıt Başarılı - Netflux</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: #0a0a0a; color: white; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 20px; }
        .container { max-width: 480px; width: 100%; background: linear-gradient(145deg, rgba(30,30,30,0.95) 0%, rgba(42,42,42,0.9) 100%); padding: 60px 50px; border-radius: 25px; box-shadow: 0 30px 90px rgba(0,0,0,0.7); text-align: center; }
        .logo { font-size: 56px; font-weight: 900; background: linear-gradient(135deg, #e50914 0%, #ff4444 50%, #e50914 100%); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 30px; animation: shimmer 3s linear infinite; }
        @keyframes shimmer { to { background-position: 200% center; } }
        .success-icon { font-size: 80px; margin: 20px 0; }
        h2 { font-size: 28px; margin-bottom: 15px; color: #4CAF50; }
        p { color: #b3b3b3; margin-bottom: 30px; font-size: 16px; }
        a { display: inline-block; padding: 18px 40px; background: linear-gradient(135deg, #e50914 0%, #b0070f 100%); color: white; text-decoration: none; border-radius: 15px; font-weight: 700; transition: all 0.3s ease; }
        a:hover { transform: translateY(-3px); box-shadow: 0 15px 40px rgba(229, 9, 20, 0.7); }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🎬 Netflux</div>
        <div class="success-icon">✅</div>
        <h2>Kayıt Başarılı!</h2>
        <p>Hesabınız oluşturuldu. Şimdi giriş yapabilirsiniz.</p>
        <a href="/">Giriş Yap</a>
    </div>
</body>
</html>
'''
