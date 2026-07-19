import random
import string
import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

def generate_captcha(length=6):
    """生成随机验证码（数字+大写字母）"""
    characters = string.digits + string.ascii_uppercase
    return ''.join(random.choice(characters) for _ in range(length))

class CaptchaHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            return self.send_json({"status": "ok", "service": "captcha"})

        length = 6
        if self.path.startswith('/captcha/'):
            try:
                length = int(self.path.split('/')[-1])
                length = max(1, min(20, length))
            except: pass

        code = generate_captcha(length)
        self.send_json({
            "captcha": code,
            "length": length,
            "hint": f"验证码有效期5分钟（演示）"
        })

    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), CaptchaHandler)
    print(f'🚀 Captcha API running on http://localhost:{port}')
    print(f'   GET  /             → API 信息')
    print(f'   GET  /captcha/6    → 6位验证码')
    print(f'   GET  /captcha/8    → 8位验证码')
    print(f'   GET  /health       → 健康检查')
    server.serve_forever()
