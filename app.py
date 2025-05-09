# app.py
from sanic import Sanic
from sanic.response import html
from jinja2 import Environment, FileSystemLoader
import os
import time

app = Sanic("RetroPortfolio")

# 静的ファイル（CSS, 画像など）の設定
app.static('/static', './static')

# Jinja2テンプレートの設定
env = Environment(loader=FileSystemLoader('templates'))

# カウンター機能
counter_file = 'visitor_count.txt'

def get_visitor_count():
    if not os.path.exists(counter_file):
        with open(counter_file, 'w') as f:
            f.write('0')
        return 0
    
    with open(counter_file, 'r') as f:
        count = int(f.read().strip() or '0')
    return count

def increment_visitor_count():
    count = get_visitor_count()
    count += 1
    with open(counter_file, 'w') as f:
        f.write(str(count))
    return count

# ルート
@app.route('/')
async def home(request):
    count = increment_visitor_count()
    template = env.get_template('index.html')
    
    # 現在の日時データ
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    
    return html(template.render(
        title="マイ・レトロポートフォリオ",
        visitor_count=count,
        current_time=current_time
    ))

# プロフィールページ
@app.route('/profile')
async def profile(request):
    template = env.get_template('profile.html')
    return html(template.render(title="プロフィール"))

# プロジェクトページ
@app.route('/projects')
async def projects(request):
    template = env.get_template('projects.html')
    return html(template.render(title="プロジェクト"))

# リンク集ページ
@app.route('/links')
async def links(request):
    template = env.get_template('links.html')
    return html(template.render(title="リンク集"))

# ゲストブックページ
@app.route('/guestbook')
async def guestbook(request):
    template = env.get_template('guestbook.html')
    return html(template.render(title="ゲストブック"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)