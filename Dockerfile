FROM python:3.11-slim

WORKDIR /app

# 依存関係のインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコピー
COPY . .

# 訪問者カウンターファイルの作成（存在しない場合）
RUN touch visitor_count.txt && echo "0" > visitor_count.txt

# 必要なディレクトリの作成
RUN mkdir -p static/images static/css static/js

# 権限の設定
RUN chmod -R 755 /app

# ポートの公開
EXPOSE 8000

# アプリケーションの実行
CMD ["python", "app.py"]