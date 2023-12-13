
from openai import OpenAI

def create_auto_article(user_input_target,user_input_target_ploblem,
                          user_input_emotion,user_input_ploblem_reason,
                          user_input_authority,user_input_goods,user_input_appeal,
                          user_input_review,user_input_price,user_input_special_price,
                          user_input_example_title,user_input_example_text,
                          user_input__SEO_keyword):

    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
    {"role": "system", "content": "あなたは記事広告を生成する人です。\
     また、SEO対策を考えた文書を生成してください。SEO対策として、SEOキーワードを盛り込んでください。\
     ブログとして、十分な量の記事を生成してください\
     これをそのまま記事として使います"},
    {"role": "user", "content": f"あなたは以下のデータを基に記事を作成します。\
     ある程度の長さの文章を生成してください。\
     SEOキーワードは{user_input__SEO_keyword}\
     ターゲットは{user_input_target}\
    ターゲットの問題は{user_input_target_ploblem}\
    悩みから生まれる感情は{user_input_emotion}\
    悩みの原因は{user_input_ploblem_reason}\
    権威は{user_input_authority}\
    商品名は{user_input_goods}\
    アピール,訴求は{user_input_appeal}\
    レビューは{user_input_review}\
    価格は{user_input_price}\
    特別価格は{user_input_special_price}\
    参考にする記事の見出しは{user_input_example_title}\
    参考にする記事の本文は{user_input_example_text}"},
    ]
    )
    return  response.choices[0].message.content

def add_CSS(generated_text,user_target_design,text_position_design,\
                    speech_bubble_color_design,large_heading_color_design,\
                    font_design):
    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
    {"role": "system", "content": "あなたはブログ記事を生成する人です。\
      必ずHTML形式で出力してください。デザインを施してください。\
     h2タグ、h3タグ、タイトルタグを適切に用いて生成してください\
     ブログとして、十分な量の記事を生成してください。"},

    {"role": "user", "content": f"あなたは以下のデータを基に記事を作成します。\
     また、必ずHTML形式で出力してください。\
     テキストに色やデザインを施してください。\
     テキストに背景色などを適切に用いてください。\
     ブログ記事のように縦に長くなるようにしてください。\
     ブログ記事のように多めに空白を入れてください。\
     項目とすることろはh2タグを用いてください。\
     次のテキストに対してデザインを施してください{generated_text}\
    以降はデザインをする際に参考にするデータです。\
    ターゲットは{user_target_design}\
    テキストの位置は{text_position_design}\
    吹き出しの色は{speech_bubble_color_design}\
    見出し(大)の色は{large_heading_color_design}\
    フォントは{font_design}"},
    ]
    )
    return  response.choices[0].message.content



def rewrite_article(user_input_rewrite_title,user_input_rewrite_text,user_input_rewrite_add):

    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
    {"role": "system", "content": "あなたは記事広告を生成する人です。\
     また、SEO対策を考えた文書を生成してください。SEO対策として、SEOキーワードを盛り込んでください。\
     ブログとして、十分な量の記事を生成してください\
     これをそのまま記事として使います"},
    {"role": "user", "content": f"あなたは以下のデータを基に記事を作成します。\
     ある程度の長さの文章を生成してください。\
     あなたは記事をリライトします。\
     リライトは追加する内容を\
     リライトする記事の見出しは{user_input_rewrite_title}\
      リライトする記事の本文は{user_input_rewrite_text}\
      リライトする記事に全体的に反映する内容は{user_input_rewrite_add}"},
    ]
    )
    return  response.choices[0].message.content

    