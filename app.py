import streamlit as st

st.set_page_config(page_title="My English Blog", page_icon="🌻", layout="centered")

# A FRASE GRANDE NO INÍCIO
st.title("✨ Welcome to My English Learning Journey! ✨")
st.markdown("---")

with st.sidebar:
    st.header("About Me 🙋‍♀️")
    st.write("Hello! I am an English student sharing my progress, tips, and daily vocabulary.")
    st.button("Say Hello! 👋")

st.header("📖 Latest Post: My First Day Writing in English")
st.caption("Published today")

st.write("""
Welcome to my very first blog post! I decided to create this space to practice my writing skills 
and share my journey with everyone. Learning a new language is challenging, but it's also highly rewarding!

**Today's Goals:**
* Write a short text in English.
* Learn 3 new words.
* Don't be afraid to make mistakes!
""")

st.info("**Word of the Day:** *Breathtaking* (adjective) - extremely exciting, beautiful or surprising.")

st.markdown("---")
st.write("Let's learn together!")
