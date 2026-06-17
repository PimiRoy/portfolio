import streamlit as st
import base64

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Pimika Portfolio",
    page_icon="logo.webp",
    layout="wide"
)

# ================= SOCIAL MEDIA ICONS =================
st.markdown("""
<style>
.social-icons {
    position: fixed !important;
    top: 150px;
    right: 30px;
    display: flex;
    flex-direction: column;
    gap: 15px;
    z-index: 999999;
}
.social-icons img {
    width: 40px;
    height: 40px;
    transition: transform 0.3s;
}
.social-icons img:hover {
    transform: scale(1.2);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="social-icons">
    <a href="https://github.com/PimiRoy" target="_blank">
        <img src="https://pngimg.com/uploads/github/github_PNG40.png" width="40">
    </a>
    <a href="https://www.linkedin.com/in/pimika7roy-data-analyst/" target="_blank">
        <img src="https://www.pngall.com/wp-content/uploads/18/Linkedin-Logo-Black-Business-Icon-PNG-thumb.png" width="40">
    </a>
</div>
""", unsafe_allow_html=True)

# ================= BACKGROUND IMAGE =================
page_bg = """
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://images.pexels.com/photos/3184460/pexels-photo-3184460.jpeg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
    right: 2rem;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["About", "Skills", "Projects", "Contact"])

# ================= ABOUT TAB =================
with tab1:
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <style>
        .profile-img img {
            width: 10px;
            height: 0px;
            margin-top: 10px;
            margin-left: 300px;
            object-fit: cover;
            border: 10px solid #00FFFF;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="profile-img">', unsafe_allow_html=True)
        st.image("anime.jpg", width=450)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <style>
        .about-tittle {
            font-size: 30px;
            color: black;
            line-height: 1.3;
            margin-top: 40px;
            margin-left: -150px;
            text-align: left;
            padding: 10px;
        }
        .about-header {
            font-size: 70px;
            color: black;
            line-height: 1.3;
            margin-top: -50px;
            margin-left: -180px;
            text-align: left;
            padding: 10px;
        }
        .about-subheader {
            font-size: 30px;
            color: black;
            line-height: 1;
            margin-top: -40px;
            margin-left: -150px;
            text-align: left;
            padding: 10px;
        }
        .about-write {
            font-size: 25px;
            color: black;
            line-height: 1.5;
            margin-top: 10px;
            margin-left: -150px;
            text-align: left;
            padding: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="about-tittle">hey I\'m</div>', unsafe_allow_html=True)
        st.markdown('<div class="about-header">Pimika Roy</div>', unsafe_allow_html=True)
        st.markdown('<div class="about-subheader">Data Analyst</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="about-write">
        I love working with data and creating insights.<br><br>
        My goal is to become a Data Analyst.
        </div>
        """, unsafe_allow_html=True)

    # ================= RESUME BUTTON =================
    st.markdown("""
    <style>
    div.stDownloadButton {
        margin-left: 900px;
        margin-top: -150px;
    }
    div.stDownloadButton > button {
        width: 120px;
        height: 45px;
        font-size: 22px;
        font-weight: bold;
        border-radius: 10px;
        border: 1px solid black;
        background-color: #ffffff;
        color: black;
    }
    </style>""", unsafe_allow_html=True)

    with open("PIMIKA ROY Resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="Resume",
        data=PDFbyte,
        file_name="PIMIKA_ROY_Resume.pdf",
        mime="application/pdf"
    )

# ================= SKILLS TAB =================
with tab2:
    # ======= EDUCATION SECTION =======
    st.markdown("""
    <style>
    .education-box li{
        display:flex;
        justify-content:space-between;
        padding:12px 0;
        border-bottom:1px solid #ccc;
        font-size:22px;
    }
    .course{ width:40%; text-align:left; color:black; }
    .institute{ width:40%; text-align:center; color:black; }
    .certificate{ width:40%; text-align:center; color:black; }
    .year{ width:40%; text-align:center; color:black; }
    .heading{ font-weight:bold; font-size:24px; }
    </style>

    <div class="education-box">
    <h2 style="color:black;">Education</h2>
    <ul>
        <li class="heading">
            <span class="course">Course</span>
            <span class="institute">Institute</span>
            <span class="certificate">Certificate</span>
            <span class="year">Year</span>
        </li>
        <li>
            <span class="course">Data Science & Analytics with AI</span>
            <span class="institute">IT VEDANT, New Delhi</span>
            <span class="certificate">Certificates</span>
            <span class="year">2025-2026</span>
        </li>
        <li>
            <span class="course">B.Com</span>
            <span class="institute">CCS University, Meerut</span>
            <span class="certificate">Degree</span>
            <span class="year">2023-2026</span>
        </li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    # ============== SKILL SECTION =============
    st.markdown("""
    <style>
    .main-skill-box{
        background: rgba(255,255,255,0.05);
        border-radius: 25px;
        padding: 30px;
        margin-top: 30px;
        margin-left: -40px;
        backdrop-filter: blur(10px);
    }
    .main-title{
        font-size: 35px;
        font-weight:bold;
        color: #000000;
        margin-bottom: 50px;
        text-align: center;
        margin-top: -40px;
    }
    .skill-grid{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }
    .skill-card{
        background: rgba(255,255,255,0.06);
        border: 2px solid black;
        border-radius: 20px;
        padding: 20px;
        transition: 0.3s;
        width:500px;
        height: 225px;
    }
    .skill-header{
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:15px;
    }
    .skill-header img{
        width:45px;
        height:45px;
        object-fit:contain;
    }
    .skill-name{
        font-size: 28px;
        font-weight: bold;
        color: #000000;
        margin:0;
    }
    .skill-tools{
        font-size: 22px;
        line-height: 1.9;
        color: black;
    }
    .skill-left{
        display:flex;
        align-items:center;
        gap:12px;
    }
    .cert-dropdown{
        position:relative;
        display:inline-block;
    }
    .cert-badge{
        color:black;
        padding:6px 12px;
        border-radius:12px;
        font-size:14px;
        font-weight:bold;
        cursor:pointer;
        border:1px solid #000000;
    }
    .cert-menu{
        display:none;
        position:absolute;
        top:40px;
        right:0;
        background:#FFFFFF;
        min-width:180px;
        border-radius:8px;
        box-shadow:0 4px 10px rgba(0,0,0,0.2);
        z-index:1000;
    }
    .cert-menu a{
        display:block;
        padding:10px;
        text-decoration:none;
        color:black;
    }
    .cert-menu a:hover{
        background:#EDEDED;
    }
    .cert-dropdown:hover .cert-menu{
        display:block;
    }
    .project-btn{
        display:inline-block;
        margin-top:10px;
        padding:8px 16px;
        background:none;
        text-decoration:none;
        border-radius:8px;
        font-weight:bold;
        transition:0.3s;
    }
    .project-btn:hover{
        transform:translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

    def skill_card(icon, title, tools, cert_text="", cert_links=None):
        cert_html = ""
        if cert_links:
            links_html = "".join(
                [f'<a href="{url}" target="_blank">{name}</a>'
                 for name, url in cert_links]
            )
            cert_html = f"""
            <div class="cert-dropdown">
                <div class="cert-badge">
                    <img src="https://cdn-icons-png.flaticon.com/512/1/1700.png"
                    style="width:25px;height:25px;vertical-align:middle;">
                    {cert_text}
                </div>
                <div class="cert-menu">
                    {links_html}
                </div>
            </div>
            """

        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-header">
                <div class="skill-left">
                    <img src="{icon}">
                    <div class="skill-name">{title}</div>
                </div>
                {cert_html}
            </div>
            <div class="skill-tools">
                {tools}
            </div>
        </div>
        """, unsafe_allow_html=True)

    skill_card(
        icon="https://cdn-icons-png.flaticon.com/512/5968/5968350.png",
        title="Python",
        tools="""
        Data Cleaning, Data Analysis <br>
        Automation Tasks, File Processing <br>
        Problem Solving, Data Visualization
        """,
        cert_text="3 Certificates",
        cert_links=[
            ("Python Programming Fundamentals", "LINK1"),
            ("NumPy And Statistical Analysis", "LINK2"),
            ("Applied Data Analysis With Python", "LINK3")
        ]
    )

# ================= PROJECTS TAB =================
with tab3:
    st.markdown("""
    <style>
    .project-card{
        background: rgba(255,255,255,0.5);
        padding:20px;
        border-radius:15px;
        border:1px solid #dcdcdc;
        box-shadow:0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom:20px;
    }
    .project-title{
        color:black !important;
        font-size:28px;
        font-weight:bold;
        margin-top:15px;
        margin-bottom:10px;
    }
    .project-desc{
        color:black !important;
        font-size:16px;
        line-height:1.6;
        margin-bottom:15px;
    }
    .tool-tag{
        display:inline-block;
        padding:6px 12px;
        border-radius:8px;
        background:#f0f0f0;
        color:black;
        font-weight:600;
    }
    .view-btn{
        display:inline-block;
        padding:10px 18px;
        border-radius:8px;
        text-decoration:none;
        border:2px solid #FFD700;
        color:black !important;
        font-weight:bold;
        transition:0.3s;
    }
    .view-btn:hover{
        transform:scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

    def project_card(image, title, desc, tools, link):
        st.markdown(f"""
        <div class="project-card">
            <img src="{image}" style="width:100%;height:220px;object-fit:cover;border-radius:10px;">
            <h3 class="project-title">{title}</h3>
            <p class="project-desc">{desc}</p>
            <div style="display:flex;justify-content:space-between;align-items:center;">
                <span class="tool-tag">{tools}</span>
                <a href="{link}" target="_blank" class="view-btn">🔗 View Project</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        project_card(
            image="https://themewagon.com/wp-content/uploads/2021/11/purple-react-1.png",
            title="📊 Supply Chain Dashboard",
            desc="Developed an interactive dashboard for inventory, sales and logistics analysis.",
            tools="Power BI, Excel",
            link="https://github.com/"
        )

    with col2:
        project_card(
            image="https://themewagon.com/wp-content/uploads/2021/11/purple-react-1.png",
            title="📈 Sales Dashboard",
            desc="Built a sales analytics dashboard to track revenue, profit and customer trends.",
            tools="Power BI, Excel",
            link="https://github.com/"
        )

# ================= CONTACT TAB =================
with tab4:
    st.title("Contact Me")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Send Message")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        if st.button("Send"):
            st.success("Message Sent Successfully!")

    with col2:
        st.markdown("""
        <style>
        .contact-box{ padding:25px; color:black; }
        .contact-row{ display:flex; align-items:center; gap:12px; margin-bottom:20px; }
        .contact-icon{ width:40px; height:40px; object-fit:contain; }
        .contact-link{ color:#000000; text-decoration:none; font-size:22px; transition:0.3s; }
        .contact-link:hover{ color:#000000; transform:scale(1.08); }
        .contact-text{ font-size:22px; color:black; }
        </style>

        <div class="contact-box">
        <h2>My Contact Details</h2>

        <div class="contact-row">
            <img src="https://seekicon.com/free-icon-download/github-square_2.png" class="contact-icon">
            <a href="https://github.com/PimiRoy" target="_blank" class="contact-link">GitHub</a>
        </div>

        <div class="contact-row">
            <img src="https://th.bing.com/th/id/R.a08f59f44e32ab5f5fe579b7b4088b97?rik=3E5gaOcXYtlNqw&riu=http%3a%2f%2fpluspng.com%2fimg-png%2flinkedin-icon-png--1600.png&ehk=hT4qxxosZ6XpSngPePNTaISdBNvqL%2fIw9mStnfVAkdg%3d&risl=&pid=ImgRaw&r=0" class="contact-icon">
            <a href="https://www.linkedin.com/in/pimika7roy-data-analyst/" target="_blank" class="contact-link">LinkedIn</a>
        </div>

        <div class="contact-row">
            <img src="https://clipartcraft.com/images/email-logo-png-background-2.png" class="contact-icon">
            <a href="mailto:pimikaroy2@gmail.com" class="contact-link">pimikaroy2@gmail.com</a>
        </div>

        <div class="contact-row">
            <img src="https://tse4.mm.bing.net/th/id/OIP.6BVAY1s7M_ezWBhYMryTzgHaJS?rs=1&pid=ImgDetMain&o=7&rm=3" class="contact-icon">
            <div class="contact-text">PIMIKA ROY Resume.pdf</div>
        </div>

        <div class="contact-row">
            <img src="https://clipground.com/images/location-icon-png-9.png" class="contact-icon">
            <div class="contact-text">Delhi, India</div>
        </div>

        </div>
        """, unsafe_allow_html=True)