import streamlit as st
import openai
import os
import streamlit.components.v1 as components
from openai import OpenAI
from dotenv import load_dotenv
from helpers import add_CSS
from helpers import create_auto_article
from helpers import rewrite_article
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

#ChatGPTによる文章生成


# Streamlitのタイトルを設定
st.title('記事自動生成')

# ユーザー入力用のテキストボックスを設置
user_input__SEO_keyword = st.text_area("SEOキーワード")
user_input_target = st.text_area("ターゲット")
user_input_target_ploblem= st.text_area("ターゲットの問題")
user_input_emotion= st.text_area("悩みから生まれる感情")
user_input_ploblem_reason= st.text_area("悩みの原因")
user_input_authority= st.text_area("権威")
user_input_goods= st.text_area("商品名")
user_input_appeal= st.text_area("アピール,訴求")
user_input_review= st.text_area("口コミ")
user_input_price= st.text_area("価格")
user_input_special_price= st.text_area("特別価格")
user_input_example_title=st.text_area("参考にしたい記事の見出し")
user_input_example_text=st.text_area("参考にしたい記事の本文")
#カスタムインプットを作りたいなら事前に何個か用意するのが良さそう
if st.button('生成開始'):
            
    result = create_auto_article(user_input_target,user_input_target_ploblem,
                          user_input_emotion,user_input_ploblem_reason,
                          user_input_authority,user_input_goods,user_input_appeal,
                          user_input_review,user_input_price,user_input_special_price,
                          user_input_example_title,user_input_example_text,
                          user_input__SEO_keyword)
    
    st.write("生成記事:")
    st.markdown(result, unsafe_allow_html=True)
    st.session_state["result"]=result

st.write("以上の生成を基にデザインした記事を出力")

user_target_design=st.radio("ターゲット", ("若い女性", "大人な女性", "若い男性","大人な男性"), horizontal=True)
text_position_design=st.radio("テキストの位置", ("中央寄せ", "左寄せ"), horizontal=True)
speech_bubble_color_design=st.radio("吹き出しの色", ("グレー", "青","オレンジ"), horizontal=True)
large_heading_color_design=st.radio("見出し(大)の色", ("グレー", "青","オレンジ"), horizontal=True)
font_design=st.radio("フォント", ("ゴシック", "明朝","ヒラギノ"), horizontal=True)

if st.button("デザイン"):
    generated_text=st.session_state["result"]
    design_result= add_CSS(generated_text,user_target_design,text_position_design,\
                    speech_bubble_color_design,large_heading_color_design,\
                    font_design)
    st.write("デザイン後記事")
    st.markdown(design_result,unsafe_allow_html=True)



user_input_rewrite_title=st.text_area("リライトしたい記事の見出し")
user_input_rewrite_text=st.text_area("リライトしたい記事の本文")
user_input_rewrite_add=st.text_area("追加したい内容")

if st.button("リライト"):
    rewrite_result= rewrite_article(user_input_rewrite_title,user_input_rewrite_text,
                                    user_input_rewrite_add)
    st.write("リライト後記事")
    st.markdown(rewrite_result,unsafe_allow_html=True)
    
    
    



