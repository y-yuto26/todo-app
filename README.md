# Todoアプリ（Docker × Flask × MySQL × AWS EC2）

## 概要
Dockerを用いてFlaskアプリケーションを構築し、AWS EC2上にデプロイしたTODOアプリです。  
タスクの追加・削除・完了機能・フィルター機能を実装しています。

---

## 使用技術
- Python（Flask）
- MySQL
- Docker / Docker Compose
- AWS EC2

---

## 機能一覧
- タスク追加
- タスク削除
- 完了チェック機能
- フィルター機能（全て / 未完了 / 完了）

---

## 環境構築手順

### ① リポジトリをクローン
 - git clone　https://github.com/y-yuto26/todo-app.git
 - cd todo-app
### ② .envファイル作成
### ①.env.web
MYSQL_HOST=db
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=todo_db
### ②.env.db
MYSQL_ROOT_PASSWORD=your_password
MYSQL_DATABASE=todo_db
### ③ Docker起動
docker-compose up -d --build


---

## 工夫した点
- Dockerを使用し、環境構築を簡略化
- MySQLの初期化をinit.sqlで自動化
- 環境変数を.envで管理し、セキュリティと再現性を向上
- コンテナ間通信（web ⇔ db）を構築

---

## 苦労した点
- MySQLコンテナとの接続エラー（host設定や環境変数の扱い）
- Dockerネットワークによるコンテナ間通信の理解
- EC2上でのポート設定とアクセス確認
