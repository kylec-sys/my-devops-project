from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>🚀 Hello, DevOps!</h1><p>自动化部署成功！</p><p>版本: v1.0</p>'

@app.route('/health')
def health():
    return '{"status": "healthy", "service": "devops-app"}'

@app.route('/info')
def info():
    return '{"name": "DevOps训练项目", "technology": ["Flask", "Docker", "Git"]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
