import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# 環境変数を設定して重みのロードを制御
os.environ['PYTORCH_WEIGHTS_ONLY'] = '0'

# タイトルと説明
st.title("YOLOv8リアルタイム物体検出アプリ")
st.write("画像をアップロードするか、カメラで撮影して物体を検出しましょう")

# モデルのロード
@st.cache_resource
def load_model():
    return YOLO('yolov8s.pt')

model = load_model()

# サイドバー
st.sidebar.title("設定")
confidence = st.sidebar.slider("検出信頼度", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
display_labels = st.sidebar.checkbox("ラベルを表示", value=True)

# タブを作成
tab1, tab2 = st.tabs(["画像アップロード", "カメラ撮影"])

# 画像アップロードタブ
with tab1:
    uploaded_file = st.file_uploader("画像をアップロードしてください", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # 画像を処理
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # オリジナル画像を表示
        st.image(image_rgb, caption="アップロードされた画像", use_column_width=True)
        
        with st.spinner("物体検出を実行中..."):
            # 物体検出の実行
            results = model(image_rgb, conf=confidence)
            
            # 結果を描画
            result_image = results[0].plot()
            st.image(result_image, caption="検出結果", use_column_width=True)
            
            # 検出された物体の集計
            detected = results[0].boxes.cls.cpu().numpy().tolist()
            counts = {}
            for obj in detected:
                cls_name = results[0].names[int(obj)]
                counts[cls_name] = counts.get(cls_name, 0) + 1
            
            if counts:
                # 検出結果表示
                st.subheader("検出された物体")
                
                # テーブル表示
                st.table({"物体": list(counts.keys()), "個数": list(counts.values())})
                
                # グラフ表示
                fig, ax = plt.subplots()
                ax.bar(counts.keys(), counts.values())
                ax.set_ylabel("number")
                ax.set_xlabel("object")
                plt.xticks(rotation=45)
                st.pyplot(fig)
            else:
                st.warning("物体が検出されませんでした")

# カメラ撮影タブ
with tab2:
    st.write("カメラにアクセスして画像を撮影します")
    
    camera_img = st.camera_input("カメラ")
    
    if camera_img is not None:
        # 画像を処理
        file_bytes = np.asarray(bytearray(camera_img.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        with st.spinner("物体検出を実行中..."):
            # 物体検出の実行
            results = model(image_rgb, conf=confidence)
            
            # 結果を描画
            result_image = results[0].plot()
            st.image(result_image, caption="検出結果", use_column_width=True)
            
            # 検出された物体の集計
            detected = results[0].boxes.cls.cpu().numpy().tolist()
            counts = {}
            for obj in detected:
                cls_name = results[0].names[int(obj)]
                counts[cls_name] = counts.get(cls_name, 0) + 1
            
            if counts:
                # 検出結果表示
                st.subheader("検出された物体")
                
                # テーブル表示
                st.table({"物体": list(counts.keys()), "個数": list(counts.values())})
                
                # グラフ表示
                fig, ax = plt.subplots()
                ax.bar(counts.keys(), counts.values())
                ax.set_ylabel("number")
                ax.set_xlabel("object")
                plt.xticks(rotation=45)
                st.pyplot(fig)
            else:
                st.warning("物体が検出されませんでした")

# アプリ情報
st.sidebar.markdown("---")
st.sidebar.info("このアプリはStreamlitとYOLOv8を使用して作成されています") 