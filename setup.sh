#!/bin/bash

# プロジェクトのセットアップスクリプト

echo "2000年代風ポートフォリオサイトのセットアップを開始します..."

# 必要なディレクトリの作成
mkdir -p templates static/css static/js static/images

# 訪問者カウンターファイルの初期化
echo "0" > visitor_count.txt

# 必要なパッケージのインストール
echo "依存パッケージをインストールしています..."
pip install -r requirements.txt

echo "セットアップが完了しました！"
echo "サーバーを起動するには以下のコマンドを実行してください："
echo "python app.py"

# スクリプトに実行権限を付与
chmod +x setup.sh