# app.py
from sanic import Sanic
from sanic.response import html
from jinja2 import Environment, FileSystemLoader
import os
import time

# 環境変数からポートを取得（Renderではこれが必要）
PORT = int(os.environ.get("PORT", 8000))
HOST = os.environ.get("HOST", "0.0.0.0")

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
    # 現在の日時データ
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    return html(template.render(
        title="プロフィール",
        visitor_count=get_visitor_count(),
        current_time=current_time
    ))

# プロジェクトページ
@app.route('/projects')
async def projects(request):
    template = env.get_template('projects.html')
    # 現在の日時データ
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    return html(template.render(
        title="プロジェクト",
        visitor_count=get_visitor_count(),
        current_time=current_time
    ))

# リンク集ページ
@app.route('/links')
async def links(request):
    template = env.get_template('links.html')
    # 現在の日時データ
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    return html(template.render(
        title="リンク集",
        visitor_count=get_visitor_count(),
        current_time=current_time
    ))

# ゲストブックページ
@app.route('/guestbook')
async def guestbook(request):
    template = env.get_template('guestbook.html')
    # 現在の日時データ
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    return html(template.render(
        title="ゲストブック",
        visitor_count=get_visitor_count(),
        current_time=current_time
    ))

# ヘルスチェックエンドポイント（Render用）
@app.route('/health')
async def health(request):
    return html("<h1>OK</h1>")

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)