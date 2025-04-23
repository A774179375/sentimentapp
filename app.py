import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="تحليل المشاعر", layout="centered", initial_sidebar_state="collapsed")

st.title("تطبيق تحليل المشاعر")
st.write("أدخل أي نص، وسنخبرك إن كان إيجابي أو سلبي أو محايد")

user_input = st.text_area("اكتب النص هنا:")

if st.button("تحليل"):
    if user_input.strip() == "":
        st.warning("الرجاء إدخال نص أولًا")
    else:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0:
            sentiment = "إيجابي"
        elif polarity < 0:
            sentiment = "سلبي"
        else:
            sentiment = "محايد"

        st.subheader("النتائج:")
        st.write(f"المشاعر: {sentiment}")
        st.write(f"التحيّز الشخصي (Subjectivity): {round(subjectivity, 2)}")
        st.write(f"الإيجابية/السلبية (Polarity): {round(polarity, 2)}")