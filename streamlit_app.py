# from collections import namedtuple
# import altair as alt
# import math

import streamlit as st
import pandas as pd
import sqlite3  # 只有在使用SQLite时需要导入

# 创建数据库连接（仅在使用SQLite时需要）
conn = sqlite3.connect('english_dict.db')  # 将数据库文件名替换为您的实际文件名
cursor = conn.cursor()


def main():

    st.set_page_config(
        page_title="Dictionary",  # 设置自定义标题
        page_icon="📊",           # 设置自定义图标，可选
        # layout="wide"             # 设置页面布局，可选
    )
    
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    st.title("Mind Palace Dictionary App")
    st.write("Enter a word to get its definitions:")

    word = st.text_input("Enter a word:")

    if st.button("Search") or len(word) > 1:
        word_details = get_word_details(word)
        if word_details:
            st.write(f"Details for '{word}':")
            display_word_details(word_details)
        else:
            st.write(f"No details found for '{word}'.")


def display_word_details(word_details):
    # 将单词详细信息显示为表格，并应用样式
    df = pd.DataFrame.from_dict(word_details, orient='index', columns=['值'])
    df.index.name = '属性'  # 设置第一列的名称为“属性”
    st.dataframe(df, use_container_width=True)  # 设置表格高度


def get_word_details(word):
    # 查询数据库并返回定义（仅在使用SQLite时需要）
    cursor.execute(
        "SELECT * FROM english_dict WHERE word COLLATE NOCASE=?", (word,))
    result = cursor.fetchall()

    if result:
        _, word, pronunciation, definition, split, synthesis_method, association_method, example_sentence, translation = result[
            0]

        return {
            "单词": word,
            "音标": pronunciation,
            "释义": definition,
            "拆分": split,
            "综合法": synthesis_method,
            "联想法": association_method,
            "例句": example_sentence,
            "翻译": translation
        }
    else:
        return None


if __name__ == "__main__":
    main()
# https://hyhdict.streamlit.app/
