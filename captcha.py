import random, string, os, json, time
from http.server import HTTPServer, BaseHTTPRequestHandler

def generate_captcha(length=6):
    characters = string.digits + string.ascii_uppercase
    return ''.join(random.choice(characters) for _ in range(length))

def progress_bar():
    """生成带颜色进度条（模拟处理过程，以文本形式返回）"""
    total = 50
    lines = ["🚀 开始处理任务...\n"]
    for i in range(total + 1):
        percent = i / total * 100
        filled = i
        empty = total - i
        bar = "█" * filled + "·" * empty
        lines.append(f"进度：{bar} {percent:.1f}%")
    lines.append("\n✅ 任务完成！")
    return lines

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            return self.send_json({"status": "ok", "service": "captcha", "uptime": round(time.time() - start_time, 1)})

        if self.path == '/progress':
            steps = progress_bar()
            return self.send_json({"steps": steps, "total": len(steps)})

        length = 6
        if self.path.startswith('/captcha/'):
            try:
                length = int(self.path.split('/')[-1])
                length = max(1, min(20, length))
            except: pass
        code = generate_captcha(length)
        self.send_json({"captcha": code, "length": length})

    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())

if __name__ == '__main__':
    start_time = time.time()
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), Handler)
    print(f'🚀 API running on http://localhost:{port}')
    print(f'   GET /captcha/6    验证码')
    print(f'   GET /progress     进度条')
    print(f'   GET /health       健康检查')
    server.serve_forever()
