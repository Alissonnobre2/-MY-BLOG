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

# Inicializa os dados na sessão caso não existam (Permite alteração em tempo de execução)
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
# (Estágio I — HL 0070, UFC DELILT)
# ---------------------------------------------------------
if "ACADEMIC_WORK" not in st.session_state:
    st.session_state.ACADEMIC_WORK = {
        "creed": {
            "title": "My Pedagogical Creed",
            "subtitle": "HL 0070 · ESL Teaching Methods and the Development of PIP",
            "date": "Estágio I · 2026.1 · UFC",
            "status": "Completed",
            "tags": ["Reflection", "Teaching Philosophy"],
            "sections": [
                {
                    "heading": "What Makes an Effective Teacher",
                    "text": "The most effective teacher I ever had was my high school English teacher. She made every lesson interesting and relevant to students' lives, relying not only on lectures but on group discussions, games, role-plays, and project-based learning. These strategies pushed us to use the language in authentic contexts and built our confidence to communicate in English.\n\nShe was also approachable, patient, enthusiastic, and genuinely interested in our progress. The classroom felt welcoming and respectful, so students felt safe asking questions and sharing opinions without fear of judgment, and she made sure every doubt was resolved so the whole class moved forward together.\n\nFeedback was a core part of her practice, given both orally and in writing. Instead of focusing only on mistakes, she highlighted our strengths and offered constructive suggestions — which motivated us to see errors as part of learning rather than as failures.",
                },
                {
                    "heading": "Lessons From an Ineffective Teacher",
                    "text": "On the other hand, the least effective teacher I had during my degree relied almost entirely on traditional lectures and memorization. Classes were teacher-centered, with little room for interaction, and questions were sometimes ignored or answered impatiently, which created an uncomfortable atmosphere.\n\nFeedback was limited to test grades, with little explanation of mistakes or guidance on how to improve. Many students felt discouraged and disconnected from the learning process — a clear reminder of why active participation and real feedback matter so much.",
                },
                {
                    "heading": "My Experience as a Teacher",
                    "text": "I have been teaching English for approximately 6 months, working in a private language institute with kids up to 10 years old. The school follows a bilingual CLIL methodology guided by the BNCC, with classes 3 times a week (45 minutes each).\n\nMy teaching is grounded in a communicative approach, mainly through Task-Based Language Teaching — I believe language learning happens through meaningful interaction and active participation, not memorization alone. I use the Primary Bilingual Program (UNOi) as the main textbook, supplemented with authentic materials, videos, songs, games, and digital resources.\n\nEach class has around 10–15 students aged 6 to 10, with mixed proficiency levels that call for differentiated, flexible teaching. Assessment combines written tests, oral presentations, participation, homework, projects, and continuous observation.\n\nWhat works best in my lessons is interactive, communicative activity — pair work, group discussions, games, and role-plays — because it increases motivation and creates authentic opportunities to use English, with students as the real protagonists of the 45 minutes. What I'm still improving is classroom time management: with only 45 minutes per class, keeping students' attention throughout is a real challenge I'm actively working on.",
                },
                {
                    "heading": "Three Principles for Effective ESL Teaching",
                    "text": "1. Student-centered learning — students learn best when they actively participate and take responsibility for their own learning.\n\n2. Meaningful communication — English should be taught as a tool for real interaction, not just a set of isolated grammar rules.\n\n3. Supportive, constructive feedback — students need guidance that helps them recognize progress, understand difficulties, and gain the confidence to communicate.\n\nUltimately, effective teaching isn't only about helping students acquire a new language — it's about empowering them to become active, independent, lifelong learners.",
                },
            ],
        },
        "pip": {
            "title": "Pedagogical Intervention Plan — \"English Only Time\"",
            "subtitle": "Incentivando a produção oral em língua inglesa por meio do projeto \"English Only Time\"",
            "date": "Estágio I · 2026.1 · UFC DELILT · CCI Benfica",
            "status": "Completed",
            "tags": ["Research", "Intervention Plan", "Co-authored"],
            "authors": "Co-authored with Ana Luiza Lima Alves · Advisor: Dra. Lidia Cardoso",
            "sections": [
                {
                    "heading": "Abstract",
                    "text": "This Pedagogical Intervention Plan was developed from the observation of three EFL classes at CCI Benfica. Although students showed good listening comprehension, most answered the teacher's questions in Portuguese, limiting opportunities to practice oral production. In response, this paper proposes the \"English Only Time\" project: a pedagogical intervention that encourages English use during class interactions through three complementary strategies — a dedicated period for exclusive English use, communicative activities, and linguistic scaffolding to support oral production. The proposal aims to increase students' confidence, expand their participation in English interactions, and foster the gradual development of communicative competence.",
                },
                {
                    "heading": "The Problem We Observed",
                    "text": "During the observations at CCI Benfica, classes of about 15–20 students aged 16–17 used Touchstone 3 (Cambridge) and were conducted largely in English following Communicative Language Teaching principles — with listening, speaking, and pair-work activities creating constant exposure to the language.\n\nEven so, students consistently understood the teacher's English questions and instructions but answered in Portuguese. Their answers were accurate, showing good comprehension — but oral production in English remained rare. This contrast between strong listening skills and limited speaking output motivated the intervention proposal.",
                },
                {
                    "heading": "Theoretical Basis",
                    "text": "The proposal draws on Swain's (1985) idea that producing language — not just receiving it — is what pushes learners to notice gaps in their knowledge and refine how they express ideas. It also follows Richards & Rodgers (2001) and Long (1996) on Communicative Language Teaching: language should be used for real interaction, and meaningful negotiation of meaning drives acquisition. Harmer (2007) and Brown (2007) support pair and small-group work as a way to increase speaking time and authentic participation. Since many learners understand English but avoid speaking it out of insecurity or fear of mistakes, linguistic scaffolding — models, useful expressions, vocabulary, and ongoing feedback — is treated as essential support.",
                },
                {
                    "heading": "The Proposed Intervention",
                    "text": "The core of the proposal is a dedicated 10–15 minute \"English Only Time\" within the lesson, where students are invited to use English as the priority language to interact with classmates and the teacher, in an environment where mistakes are treated as part of learning.\n\nThis period is paired with communicative activities — interviews, role-plays, games, guided discussions, and pair/small-group tasks — that give students a real reason to use English, turning communication into a means to an end rather than an obligation.\n\nLinguistic scaffolding supports the whole process: before and during activities, the teacher provides model structures, topic-related vocabulary, common expressions, and continuous feedback, so students can take part with more confidence and autonomy.",
                },
                {
                    "heading": "Discussion & Expected Outcomes",
                    "text": "The students' main difficulty wasn't comprehension — it was that Portuguese answers were routinely accepted, so there was never a real need to use English. \"English Only Time\" aims to give English a clear purpose in the classroom: rather than simply asking students to answer in English, it creates situations where using the target language makes sense within the activity itself.\n\nThis plan has not yet been implemented, but it is expected to expand opportunities for oral production, strengthen students' confidence, and encourage more active participation — helping English become not just a language students understand, but one they actually use.",
                },
                {
                    "heading": "References",
                    "text": "Brown, H. D. (2007). Teaching by Principles: An Interactive Approach to Language Pedagogy (3rd ed.). Pearson Education.\nHarmer, J. (2007). The Practice of English Language Teaching (4th ed.). Pearson Longman.\nLong, M. H. (1996). The Role of the Linguistic Environment in Second Language Acquisition. In W. C. Ritchie & T. K. Bhatia (Eds.), Handbook of Second Language Acquisition (pp. 413–468). Academic Press.\nRichards, J. C., & Rodgers, T. S. (2001). Approaches and Methods in Language Teaching (2nd ed.). Cambridge University Press.\nSwain, M. (1985). Communicative Competence: Some Roles of Comprehensible Input and Comprehensible Output in Its Development. In S. Gass & C. Madden (Eds.), Input in Second Language Acquisition (pp. 235–253). Newbury House.",
                },
            ],
        },
        "observation": {
            "title": "Observation Report",
            "subtitle": "Classroom Observation — CCI Benfica",
            "date": "Estágio I · 2026.1 · UFC DELILT",
            "status": "In Progress",
            "tags": ["Observation", "In Progress"],
            "authors": "",
            "sections": [
                {
                    "heading": "Coming Soon",
                    "text": "This is the next deliverable of my Estágio I internship. It will bring a detailed account of the three EFL classes I observed at CCI Benfica — classroom dynamics, the teacher's strategies, and the reflections that led to the \"English Only Time\" intervention plan. I'm currently writing it up and will publish it here as soon as it's finished!",
                },
            ],
        },
    }



# =========================================================
# DESIGN SYSTEM — navy & gold
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Inter:wght@400;500;600;700&display=swap');
:root{
    --navy:#1B2A4A;
    --navy-light:#27406e;
    --gold:#D9A441;
    --gold-light:#F8EFD9;
    --bg:#F7F8FA;
    --text:#1B2A4A;
    --muted:#6B7280;
}
html, body, [class*="css"]{
    font-family:'Inter', sans-serif;
    color:var(--text);
}
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
.stApp{
    background:var(--bg);
}
.block-container{
    max-width:1180px;
    padding-top:1.2rem;
}
/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"]{
    background:var(--navy);
    border-right:none;
}
section[data-testid="stSidebar"] *{
    color:#EDEFF5 !important;
}
section[data-testid="stSidebar"] input, section[data-testid="stSidebar"] textarea, section[data-testid="stSidebar"] select{
    color: var(--navy) !important;
}
section[data-testid="stSidebar"] img{
    border-radius:14px;
    border:3px solid var(--gold);
}
section[data-testid="stSidebar"] hr{
    border-color:rgba(255,255,255,.15);
}
section[data-testid="stSidebar"] button{
    background:var(--gold) !important;
    color:var(--navy) !important;
    border:none !important;
    font-weight:700 !important;
    border-radius:30px !important;
}
/* ---------- Navbar ---------- */
.navbar{
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:14px 6px 22px 6px;
    border-bottom:1px solid #E5E7EB;
    margin-bottom:30px;
}
.navbar .brand{
    display:flex;
    align-items:center;
    gap:10px;
    font-family:'Playfair Display', serif;
    font-weight:700;
    font-size:20px;
    color:var(--navy);
}
.navbar .brand-icon{
    background:var(--gold);
    color:var(--navy);
    width:34px;
    height:34px;
    border-radius:9px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:18px;
}
.navbar .badge{
    background:var(--gold-light);
    color:#8A6A1E;
    border:1px solid #F0DBA0;
    padding:6px 16px;
    border-radius:30px;
    font-size:13px;
    font-weight:600;
}
/* Functional nav buttons row */
div[data-testid="stHorizontalBlock"] button{
    background:transparent !important;
    border:none !important;
    color:var(--navy) !important;
    font-weight:600 !important;
    font-size:15px !important;
    box-shadow:none !important;
}
div[data-testid="stHorizontalBlock"] button:hover{
    color:var(--gold) !important;
}
/* ---------- Eyebrow / section labels ---------- */
.eyebrow{
    display:flex;
    align-items:center;
    gap:10px;
    color:var(--gold);
    font-weight:700;
    font-size:13px;
    letter-spacing:1.5px;
    margin-bottom:14px;
}
.eyebrow::before{
    content:"";
    width:24px;
    height:2px;
    background:var(--gold);
    display:inline-block;
}
h1.serif, h2.serif{
    font-family:'Playfair Display', serif;
    color:var(--navy);
    font-weight:700;
    line-height:1.15;
}
/* ---------- Stat cards ---------- */
.stat-card{
    background:var(--gold-light);
    border:1px solid #F0DBA0;
    border-left:5px solid var(--gold);
    border-radius:14px;
    padding:18px 20px;
}
.stat-card .stat-icon{
    font-size:20px;
    margin-bottom:8px;
}
.stat-card .stat-number{
    font-family:'Playfair Display', serif;
    font-size:26px;
    font-weight:700;
    color:var(--navy);
}
.stat-card .stat-label{
    color:#8A6A1E;
    font-size:13px;
}
/* ---------- Generic content card ---------- */
.card{
    background:white;
    border:1px solid #ECEEF2;
    border-radius:16px;
    padding:28px;
    box-shadow:0 6px 18px rgba(27,42,74,.05);
    margin-bottom:22px;
}
.card h2, .card h3{
    font-family:'Playfair Display', serif;
    color:var(--navy);
}
.icon-circle{
    width:42px;
    height:42px;
    border-radius:10px;
    background:var(--navy);
    color:var(--gold);
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:18px;
    margin-bottom:14px;
}
.pill{
    display:inline-block;
    background:var(--gold-light);
    color:#8A6A1E;
    border:1px solid #F0DBA0;
    padding:4px 14px;
    border-radius:30px;
    font-size:12px;
    font-weight:700;
    margin-right:6px;
}
.pill.status-progress{
    background:#FDEFE0;
    color:#B5631C;
    border-color:#F3C895;
}
.pill.status-done{
    background:#E7F4EA;
    color:#2F7A43;
    border-color:#BFE3C8;
}
.checkline{
    color:var(--muted);
    font-size:14px;
    margin:4px 0;
}
.checkline b{ color:var(--gold); }
.word-box{
    margin-top:24px;
    background:var(--navy);
    color:white;
    border-left:6px solid var(--gold);
    padding:20px;
    border-radius:12px;
}
.word-box h4{ color:var(--gold); margin-top:0; }
.caption-muted{
    text-align:center;
    color:var(--muted);
    font-size:13px;
}
.home-photo img{
    border-radius:14px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HELPERS
# =========================================================
def status_pill(status: str) -> str:
    cls = "status-progress" if status.lower() in ("in progress", "ongoing") else "status-done"
    return f"<span class='pill {cls}'>{status}</span>"

def render_academic_card(work: dict):
    tags_html = "".join(f"<span class='pill'>{t}</span>" for t in work.get("tags", []))
    authors_html = f"<p class='caption-muted' style='text-align:left;'>{work['authors']}</p>" if work.get("authors") else ""
    st.markdown(f"""
    <div class="card">
        <div style="display:flex; justify-content:space-between; align-items:flex-start;">
            <h2 style="margin-bottom:4px;">{work['title']}</h2>
            {status_pill(work['status'])}
        </div>
        <p class="caption-muted" style="text-align:left;">{work.get('subtitle','')}</p>
        <p class="caption-muted" style="text-align:left;">{work.get('date','')}</p>
        {authors_html}
        <div style="margin:10px 0 18px 0;">{tags_html}</div>
    """, unsafe_allow_html=True)
    for sec in work["sections"]:
        with st.expander(sec["heading"], expanded=(len(work["sections"]) == 1)):
            st.write(sec["text"])
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# SIDEBAR & MODO EDIÇÃO
# =========================================================
with st.sidebar:
    # Botão de Ativação do Modo de Edição
    st.session_state.edit_mode = st.toggle("✏️ Edit Mode", value=st.session_state.edit_mode)

    st.markdown("---")

    if st.session_state.edit_mode:
        st.markdown("### 🛠️ Panel Editor")

        # Categoria para Editar Academic Work (Creed / PIP / Observation)
        with st.expander("🎓 Manage Academic Work"):
            work_key = st.selectbox(
                "Select Document",
                options=list(st.session_state.ACADEMIC_WORK.keys()),
                format_func=lambda k: st.session_state.ACADEMIC_WORK[k]["title"],
            )
            work = st.session_state.ACADEMIC_WORK[work_key]
            work["title"] = st.text_input("Title", work["title"], key=f"{work_key}_title")
            work["subtitle"] = st.text_input("Subtitle", work["subtitle"], key=f"{work_key}_subtitle")
            work["date"] = st.text_input("Date / Course", work["date"], key=f"{work_key}_date")
            work["status"] = st.selectbox(
                "Status", ["Completed", "In Progress"],
                index=0 if work["status"] == "Completed" else 1,
                key=f"{work_key}_status",
            )
            st.caption("Section texts can be edited below:")
            for i, sec in enumerate(work["sections"]):
                sec["heading"] = st.text_input(f"Section {i+1} — Heading", sec["heading"], key=f"{work_key}_h_{i}")
                sec["text"] = st.text_area(f"Section {i+1} — Text", sec["text"], key=f"{work_key}_t_{i}", height=120)

        # Categoria para Editar Vocabulário
        with st.expander("📘 Manage Vocabulary"):
            vocab_words = [v["word"] for v in st.session_state.VOCAB]
            selected_v_idx = vocab_words.index(st.selectbox("Select Word", vocab_words))

            st.session_state.VOCAB[selected_v_idx]["word"] = st.text_input("Word", st.session_state.VOCAB[selected_v_idx]["word"])
            st.session_state.VOCAB[selected_v_idx]["meaning"] = st.text_input("Meaning", st.session_state.VOCAB[selected_v_idx]["meaning"])
            st.session_state.VOCAB[selected_v_idx]["example"] = st.text_input("Example", st.session_state.VOCAB[selected_v_idx]["example"])

            if st.button("➕ Add New Blank Word"):
                st.session_state.VOCAB.append({"word": "New Word", "meaning": "Meaning", "example": "Example"})
                st.rerun()

        # Categoria para Editar Academic Journey
        with st.expander("🧭 Manage Academic Journey"):
            journey_titles = [j["title"] for j in st.session_state.JOURNEY]
            selected_j_idx = journey_titles.index(st.selectbox("Select Journey Card", journey_titles))

            st.session_state.JOURNEY[selected_j_idx]["title"] = st.text_input("Card Title", st.session_state.JOURNEY[selected_j_idx]["title"])
            st.session_state.JOURNEY[selected_j_idx]["status"] = st.text_input("Status / Hours", st.session_state.JOURNEY[selected_j_idx]["status"])
            st.session_state.JOURNEY[selected_j_idx]["subtitle"] = st.text_input("Institution / Date", st.session_state.JOURNEY[selected_j_idx]["subtitle"])
            st.session_state.JOURNEY[selected_j_idx]["items"] = st.text_area("Items (one per line)", st.session_state.JOURNEY[selected_j_idx]["items"])
    else:
        # Perfil Padrão se o Modo de Edição estiver desligado
        st.markdown("## 👩 About Me")
        try:
            st.image("student.jpg", width=220)
        except Exception:
            st.warning("Add the file student.jpg")
        st.markdown("---")
        st.write("""
        Hello! 👋
        My name is Ana Sigrid. I'm a Letras/Inglês student at UFC (5th semester) and an English teacher,
        currently completing my Estágio I observational internship.
        **Here you'll find:** 🎓 My Pedagogical Creed
        📋 My Intervention Plan (PIP)
        👀 My Observation Report
        📘 Daily Vocabulary
        📖 Grammar Tips
        """)
        st.button("🌻 Follow My Journey", use_container_width=True)

# =========================================================
# NAVBAR
# =========================================================
st.markdown("""
<div class="navbar">
    <div class="brand"><span class="brand-icon">🌻</span> Only English Time</div>
    <div class="badge">Letras · English · 2026</div>
</div>
""", unsafe_allow_html=True)

menu_cols = st.columns(5)
# Alterado conforme solicitado:
menu_items = ["HOME", "PEDAGOGICAL CREED", "PEDAGOGICAL INTERVENTION PLAN", "OBSERVATION REPORT", "ABOUT"]
for col, item in zip(menu_cols, menu_items):
    with col:
        st.button(item, use_container_width=True, on_click=go_to, args=(item,))

st.write("")

# =========================================================
# PAGE: HOME
# =========================================================
if st.session_state.page == "HOME":
    st.markdown('<div class="eyebrow">ABOUT ME</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="serif">Future Educator, <i>Language Enthusiast</i></h1>', unsafe_allow_html=True)
    st.write(
        "A 5th semester English student and teacher at the beginning of her journey, sharing my experiences "
        "from the observational internship for the course **HL 0070 — Estágio I: Observação e elaboração de "
        "projetos de intervenção para o ensino da língua inglesa em cursos livres**."
    )

    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="home-photo">', unsafe_allow_html=True)
        st.image("https://picsum.photos/seed/onlyenglishtime-books/500/350", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="home-photo">', unsafe_allow_html=True)
        st.image("https://picsum.photos/seed/onlyenglishtime-classroom/500/350", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="home-photo">', unsafe_allow_html=True)
        st.image("https://picsum.photos/seed/onlyenglishtime-campus/500/350", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown(f"""<div class="stat-card"><div class="stat-icon">🎓</div>
        <div class="stat-number">{len(st.session_state.ACADEMIC_WORK)}</div><div class="stat-label">Academic Deliverables</div></div>""", unsafe_allow_html=True)
    with s2:
        st.markdown(f"""<div class="stat-card"><div class="stat-icon">📘</div>
        <div class="stat-number">{len(st.session_state.VOCAB)}</div><div class="stat-label">Words Learned</div></div>""", unsafe_allow_html=True)
    with s3:
        st.markdown("""<div class="stat-card"><div class="stat-icon">👩‍🏫</div>
        <div class="stat-number">6mo</div><div class="stat-label">Teaching Experience</div></div>""", unsafe_allow_html=True)

    st.write("")
    left, right = st.columns([2.2, 1])
    with left:
        st.markdown('<div class="eyebrow">FROM MY INTERNSHIP — ESTÁGIO I</div>', unsafe_allow_html=True)
        for key, work in st.session_state.ACADEMIC_WORK.items():
            with st.container(border=True):
                st.markdown(f"**{work['title']}** \n*{work['subtitle']}*")
                st.markdown(status_pill(work["status"]), unsafe_allow_html=True)
                if st.button("Read more →", key=f"home_read_{key}"):
                    # Redireciona para as novas páginas correspondentes
                    if key == "creed":
                        go_to("PEDAGOGICAL CREED")
                    elif key == "pip":
                        go_to("PEDAGOGICAL INTERVENTION PLAN")
                    elif key == "observation":
                        go_to("OBSERVATION REPORT")
                    st.rerun()

        word_obj = st.session_state.VOCAB[0] if st.session_state.VOCAB else {"word": "---", "meaning": "---", "example": "---"}
        st.markdown(f"""
        <div class="word-box">
            <h4>📘 Word of the Day</h4>
            <b>{word_obj['word']}</b><br><br>
            Meaning: {word_obj['meaning']}<br>
            <i>Example: {word_obj['example']}</i>
        </div>
        """, unsafe_allow_html=True)
    with right:
        st.image(
            "https://picsum.photos/seed/onlyenglishtime-hero/700/900",
            use_container_width=True,
        )
        st.markdown("<p class='caption-muted'>Learning — and teaching — English every day.</p>", unsafe_allow_html=True)

    st.divider()
    st.markdown('<div class="eyebrow">ACADEMIC JOURNEY</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="serif">Where I Have Been Learning</h2>', unsafe_allow_html=True)
    j1, j2, j3 = st.columns(3)
    for col, j in zip([j1, j2, j3], st.session_state.JOURNEY):
        with col:
            lines = j["items"].split("\n")
            items_html = "".join(f"<div class='checkline'><b>✓</b> {line}</div>" for line in lines if line.strip())
            st.markdown(f"""
            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div class="icon-circle">{j['icon']}</div>
                    <span class="pill">{j['status']}</span>
                </div>
                <h3 style="margin-bottom:0;">{j['title']}</h3>
                <p class="caption-muted" style="text-align:left; margin-top:2px;">{j['subtitle']}</p>
                {items_html}
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# PAGE: PEDAGOGICAL CREED (Antigo VOCABULARY)
# =========================================================
elif st.session_state.page == "PEDAGOGICAL CREED":
    st.markdown('<div class="eyebrow">ESTÁGIO I — HL 0070</div>', unsafe_allow_html=True)
    render_academic_card(st.session_state.ACADEMIC_WORK["creed"])

# =========================================================
# PAGE: PEDAGOGICAL INTERVENTION PLAN (Antigo GRAMMAR)
# =========================================================
elif st.session_state.page == "PEDAGOGICAL INTERVENTION PLAN":
    st.markdown('<div class="eyebrow">ESTÁGIO I — HL 0070</div>', unsafe_allow_html=True)
    render_academic_card(st.session_state.ACADEMIC_WORK["pip"])

# =========================================================
# PAGE: OBSERVATION REPORT (Antigo WRITING)
# =========================================================
elif st.session_state.page == "OBSERVATION REPORT":
    st.markdown('<div class="eyebrow">ESTÁGIO I — HL 0070</div>', unsafe_allow_html=True)
    render_academic_card(st.session_state.ACADEMIC_WORK["observation"])

# =========================================================
# PAGE: ABOUT
# =========================================================
elif st.session_state.page == "ABOUT":
    st.markdown('<div class="eyebrow">ABOUT ME</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="serif">My Profile</h2>', unsafe_allow_html=True)
    st.write("Section content goes here.")
