import streamlit as st 

# =========================================================
# CONFIG
# =========================================================
st.set_page_config(
    page_title="Only English Time",
    page_icon="🌻",
    layout="wide",
)

# =========================================================
# SESSION STATE (Gerenciamento de Dados Dinâmicos)
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "HOME"
if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False

def go_to(page_name: str):
    st.session_state.page = page_name

# Inicializa os dados na sessão caso não existam
if "VOCAB" not in st.session_state:
    st.session_state.VOCAB = [
        {"word": "Breathtaking", "meaning": "Something extremely beautiful or surprising.", "example": "The sunset over the mountains was breathtaking."},
        {"word": "Resilient", "meaning": "Able to recover quickly from difficulties.", "example": "She stayed resilient even after losing her job."},
        {"word": "Overwhelmed", "meaning": "Having too much to deal with at once.", "example": "I felt overwhelmed by all the homework this week."},
        {"word": "Scaffolding", "meaning": "Temporary support (models, vocabulary, feedback) given to help a learner perform a task.", "example": "The teacher used scaffolding to help students join the discussion in English."},
    ]
if "GRAMMAR_TIPS" not in st.session_state:
    st.session_state.GRAMMAR_TIPS = [
        {"title": "Present Perfect vs Past Simple", "text": "Use Present Perfect for actions connected to now ('I have studied English for 2 years'); use Past Simple for finished actions with a specific time ('I studied English in 2022')."},
        {"title": "Articles: A / An / The", "text": "Use 'a/an' for something not specific or mentioned for the first time. Use 'the' when both speaker and listener know exactly what is being referred to."},
        {"title": "Common mistake: Make vs Do", "text": "'Make' is for creating something (make a cake, make a decision). 'Do' is for activities/tasks (do homework, do exercise)."},
    ]

# ---------------------------------------------------------
# ACADEMIC WORK — Pedagogical Creed / PIP / Observation Report
# ---------------------------------------------------------
if "ACADEMIC_WORK" not in st.session_state:
    st.session_state.ACADEMIC_WORK = {
        "creed": {
            "title": "My Pedagogical Creed",
            "subtitle": "HL 0070 · ESL Teaching Methods and the Development of PIP",
            "date": "Estágio I · 2026.1 · UFC",
            "status": "Completed",
            "tags": ["Reflection", "Teaching Philosophy"],
            "sections":
