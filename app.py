import streamlit as st

from generators.blog_generator import generate_blog
from generators.caption_generator import generate_caption
from generators.script_generator import generate_script
from generators.article_generator import generate_article

st.title("Scriptoria AI Content Creator")

topic = st.text_input("Enter Topic")

content_type = st.selectbox(
"Select Content Type",
["Blog","Instagram Caption","YouTube Script","Article"]
)

tone = st.selectbox(
"Select Tone",
["Professional","Casual","Creative"]
)

if st.button("Generate Content"):
    with st.spinner("AI is generating your content..."):
        result = generate_article(topic, tone)
        st.write(result)

    if topic:

        if content_type=="Blog":
            result=generate_blog(topic,tone)

        elif content_type=="Instagram Caption":
            result=generate_caption(topic,tone)

        elif content_type=="YouTube Script":
            result=generate_script(topic,tone)

        else:
            result=generate_article(topic,tone)

        st.subheader("Generated Content")
        st.write(result)

    else:
        st.warning("Please enter a topic")