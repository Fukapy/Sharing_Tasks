#2024/2/24 Ryo Fukasawa
#Streamlitで手軽にWebアプリ開発
#https://www.alpha.co.jp/blog/202304_02/

#app.py
import streamlit as st

st.title("title") # タイトル
st.header("header") # ヘッダー
st.write("write") # 表示
st.markdown("# markdown") # マークダウンで表示
st.text("text") # テキスト表示

check = st.checkbox("check button") # チェックボタン

if check:
  st.button("button")
  st.selectbox("selectbox", ("select1", "select2"))
  st.multiselect("multiselectbox", ("select1", "select2"))
  st.radio("radiobutton", ("radio1", "radio2"))
  st.text_input("text input")
  st.text_area("text area")
  st.slider("slider", 0, 100, 50)
  st.file_uploader("Choose file")


st.button("button")
st.selectbox("selectbox", ("select1", "select2"))
st.multiselect("multiselectbox", ("select1", "select2"))
st.radio("radiobutton", ("radio1", "radio2"))
# 以下をサイドバーに表示
st.sidebar.text_input("text input")
st.sidebar.text_area("text area")
st.sidebar.slider("slider", 0, 100, 50)
st.sidebar.file_uploader("Choose file")