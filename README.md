# YOLOv8 Streamlit 物体検出アプリケーション

このアプリケーションは、YOLOv8モデルを使用して画像内の物体を検出するStreamlitアプリです。

## 機能

- 画像のアップロード機能
- カメラからの画像撮影機能
- 検出された物体の可視化
- 検出結果のグラフ表示
- 検出信頼度の調整

## セットアップ手順

### 1. リポジトリのクローン

```bash
git clone https://github.com/your-username/yolo-streamlit.git
cd yolo-streamlit
```

### 2. 環境の準備

#### Dockerを使用する場合（推奨）

1. DockerとDocker Composeがインストールされていることを確認
   ```bash
   docker --version
   docker-compose --version
   ```

2. アプリケーションの起動
   ```bash
   docker-compose up -d
   ```

3. ブラウザでアクセス
   ```
   http://localhost:8501
   ```

#### ローカル環境で実行する場合

1. Python 3.10以上がインストールされていることを確認
   ```bash
   python --version
   ```

2. 必要なパッケージのインストール
   ```bash
   pip install -r requirements.txt
   ```

3. アプリケーションの起動
   ```bash
   streamlit run app.py
   ```

## 使用方法

1. ブラウザで http://localhost:8501 にアクセス

2. 以下の機能が利用可能です：
   - 画像のアップロード
   - カメラでの撮影
   - 検出信頼度の調整（サイドバー）
   - 検出結果の表示
   - 検出物体の統計情報のグラフ表示

## 注意事項

- カメラ機能を使用するには、ブラウザでのカメラへのアクセス許可が必要です
- YOLOv8モデルは初回起動時にダウンロードされる場合があります
- Dockerを使用する場合、十分なメモリ（2GB以上）を確保してください

## トラブルシューティング

### カメラが動作しない場合
- ブラウザのカメラアクセス許可を確認
- カメラが正しく接続されているか確認

### 検出が遅い場合
- Dockerのメモリ割り当てを増やす
- 検出信頼度の閾値を調整

### エラーが発生する場合
- ログを確認
  ```bash
  docker-compose logs
  ```
- 必要なパッケージが正しくインストールされているか確認

## 技術スタック

- Streamlit: インタラクティブなWebアプリケーションのフレームワーク
- YOLOv8: 最新の物体検出モデル
- OpenCV: 画像処理ライブラリ
- Matplotlib: データ可視化ライブラリ

## ライセンス

[MIT](LICENSE)
