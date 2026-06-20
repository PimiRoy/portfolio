import streamlit as st
import base64

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Pimika Portfolio",
    page_icon="logo.webp",
    layout="wide"
)


# ================= BACKGROUND IMAGE =================
with open("background.jpg", "rb") as img:
    bg_img = base64.b64encode(img.read()).decode()

    page_bg = f"""
    <style>
    [data-testid="stAppViewContainer"]{{
        background-image: url("data:image/jpg;base64,{bg_img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"]{{
        background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"]{{
        right: 1rem;
    }}
    </style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Tabs
st.markdown("""
<style>
.stTabs [data-baseweb="tab-list"]{
    justify-content:center;
    gap:40px;
}
.stTabs [data-baseweb="tab"]{
    font-size: 24px;
    font-weight: 700;
    padding: 12px 25px;
   
}
</style>
""", unsafe_allow_html=True)
tab1, tab2, tab3, tab4 = st.tabs(["About", "Skills", "Projects", "Contact"])

# ================= ABOUT TAB =================
with tab1:

    st.markdown("""
    <style>
    .card {
    background: rgba(255,255,255,0.05);
    padding: 15px 10px;          /* ↓ padding kam */
    margin-top: 30px;       /* ↓ thoda niche */
    border-radius: 20px;
    box-shadow:0px 15px 25px rgba(0,0,0,0.15);
    text-align: center;

    height: 90%;          /* ↓ card size kam */
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    }


    .card img {
        width: 450px;
        border-radius: 15px;
        margin-top: -40px; 
        
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.4, 1.2])

    with col1:
        st.markdown("""
        <div class="card">
            <img src="https://raw.githubusercontent.com/PimiRoy/pimika-roy-portfolio/main/ChatGPT%20Image%20Jun%205%2C%202026%2C%2006_23_38%20PM%20(1).png">
        </div>
        """, unsafe_allow_html=True)

   
with col2:
        st.markdown("""
    <style>

    .about-card{
        background:rgba(255,255,255,0.05);
        padding:15px 10px;
        border-radius:25px;
        box-shadow:0px 15px 25px rgba(0,0,0,0.15);
        margin-top:30px;
        height:90%;
    }

    .about-title{
        font-size:28px;
        color:#44;
    }
    
    .about-header{
    font-size:clamp(35px, 5vw, 65px);
    font-weight:bold;
    color:44;
    line-height:1.1;
    white-space: nowrap;
    }

    .about-subheader{
        font-size:30px;
        color:#4;
        font-weight:600;
        margin-bottom:20px;
    }

    .about-write{
        font-size:22px;
        color:#333;
        line-height:1.5;
        margin-bottom:25px;
    }
    .action-row{
    display:flex;
    align-items:center;
    gap:10px;
    flex-wrap:wrap;
    }

    .resume-btn{
    color:black !important;
    padding:5px 20px;
    text-decoration:none !important;
    font-size:20px;
    font-weight:bold;
    display:inline-block;
    }

    

    

    </style>
<div class="about-card">
<div class="about-title">
    Hey I'm
    </div>

<div class="about-header">
    Pimika Roy
    </div>

<div class="about-subheader">
    Aspiring Data Analyst
    </div>

<div class="about-write">
    Passionate about data analytics and visualization.<br><br>

Skilled in SQL, Python, Power BI, and Excel with hands-on experience in data analysis, dashboard development, and business insights.
</div>

<div class="action-row">

<a class="resume-btn"
       href="https://drive.google.com/file/d/1aPVP8tzXZnMpTBxIc66j372OcfXppXbA/view?usp=drive_link"
       target="_blank">
       Resume
    </a>

<a class="resume-btn"
   href="https://mail.google.com/mail/?view=cm&fs=1&to=pimikaroy2@gmail.com"
   target="_blank">
   Gmail
    </a>

<a class="resume-btn"
       href="https://www.linkedin.com/in/pimika7roy-data-analyst/"
       target="_blank">
       LinkedIn
    </a>

<a class="resume-btn"
       href="https://github.com/PimiRoy"
       target="_blank">
       GitHub
    </a>

</div>


    """, unsafe_allow_html=True)
        
 #================= SKILLS TAB =================
with tab2:
 # ======= EDUCATION SECTION =======
    st.markdown("""
    <style>
    .education-box li{
        display:flex;
        justify-content:space-between;
        padding:12px 0;
        border-bottom:2px solid #cccccc;
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
            <span class="certificate">
            <a href="https://drive.google.com/file/d/1QaernAw_pzJEwG0yQPWDztHDT6SVWSnm/view?usp=drive_link" target="_blank">IBM</a>|
            <a href="https://drive.google.com/file/d/1dB8tjYX_-_CUIjh7CgRL_Ll6EIiQMvZu/view?usp=drive_link" target="_blank">ITVedant</a> 
            </span>
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
# ================= SKILLS SECTION =================

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
        /* Tablet */
        @media (max-width: 1200px){
            .skill-grid{
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        @media (max-width: 768px){
            .skill-grid{
                grid-template-columns: 1fr;
            }
        }
        
        .skill-card{
            background: rgba(255,255,255,0.06);
            box-shadow:0px 8px 25px rgba(0,0,0,0.15);
            border:2px solid black;
            border-radius:20px;
            padding:20px;
            width:100%;
            min-height:225px;
            box-sizing:border-box;
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
        
        <div class="main-skill-box">
        <div class="main-title">Skills & Tools</div>
        <div class="skill-grid">
        
        <!-- Soft Skill -->
        <div class="skill-card">
            <div class="skill-header">
                <div class="skill-left">
                    <img src="https://img.icons8.com/color/96/communication.png">
                    <div class="skill-name">Soft Skill</div>
                </div>
            </div>
            <div class="skill-tools">
                Analytical Thinking, Problem Solving <br>
                Communication, Attention to Detail <br>
                Time Management, Team Collaboration
            </div>
        </div>
        
        <!-- PYTHON -->
        <div class="skill-card">
            <div class="skill-header">
                <div class="skill-left">
                    <img src="https://cdn-icons-png.flaticon.com/512/5968/5968350.png">
                    <div class="skill-name">Python</div>
                </div>
                <div class="cert-dropdown">
                    <div class="cert-badge">
                        <img src="https://cdn-icons-png.flaticon.com/512/1/1700.png"
                        style="width:25px;height:25px;vertical-align:middle;">
                        2 Certificates
                    </div>
                    <div class="cert-menu">
                        <a href="https://drive.google.com/file/d/1iYaLzG7E6aHi7Ma-HF_z-9d_6r1HxKSf/view?usp=drive_link" target="_blank">Python for Data Science</a>
                        <a href="https://drive.google.com/file/d/1RUeKVI62DLLy_Zh2jDeeI470zS7aMdb3/view?usp=drive_link" target="_blank">Data Analysis with Python</a>
                    </div>
                </div>
            </div>
            <div class="skill-tools">
                Data Cleaning, Data Analysis <br>
                Automation Tasks, File Processing <br>
                Problem Solving, Data Visualization
            </div>
        </div>
        
        <!-- Power BI -->
        <div class="skill-card">
            <div class="skill-header">
                <div class="skill-left">
                    <img src="https://img.icons8.com/?size=100&id=3sGOUDo9nJ4k&format=png&color=000000">
                    <div class="skill-name">Power BI</div>
                </div>
                <div class="cert-dropdown">
                    <div class="cert-badge">
                        <img src="https://cdn-icons-png.flaticon.com/512/1/1700.png"
                        style="width:25px;height:25px;vertical-align:middle;">
                        Certificates
                    </div>
                    <div class="cert-menu">
                        <a href="https://drive.google.com/file/d/12F63aSNAyv05TY10KX1ERCFE_fDEoA46/view?usp=drive_link" target="_blank">Business Intelligence with Power BI</a>
                    </div>
                </div>
            </div>
            <div class="skill-tools">
                KPI Tracking, Business Reports <br>
                Data Visualization, Performance Analysis <br>
                Interactive Dashboards
            </div>
        </div>
        
        <!-- Excel -->
        <div class="skill-card">
            <div class="skill-header">
                <div class="skill-left">
                    <img src="https://img.icons8.com/color/96/microsoft-excel-2019.png">
                    <div class="skill-name">Excel</div>
                </div>
                <div class="cert-dropdown">
                    <div class="cert-badge">
                        <img src="https://cdn-icons-png.flaticon.com/512/1/1700.png"
                        style="width:25px;height:25px;vertical-align:middle;">
                        Certificates
                    </div>
                    <div class="cert-menu">
                        <a href="https://drive.google.com/file/d/1zkD_m6LSNcWAS2z5HYC8Yz4FuSc7tkEx/view?usp=drive_link" target="_blank">Advanced Excel</a>
                    </div>
                </div>
            </div>
            <div class="skill-tools">
                Data Analysis, Dashboard Creation <br>
                Report Automation, Data Validation <br>
                Business Reporting, Data Cleaning
            </div>
        </div>
        
        <!-- SQL -->
        <div class="skill-card">
            <div class="skill-header">
                <div class="skill-left">
                    <img src="https://img.icons8.com/?size=100&id=J6KcaRLsTgpZ&format=png&color=000000">
                    <div class="skill-name">SQL</div>
                </div>
                <div class="cert-dropdown">
                    <div class="cert-badge">
                        <img src="https://cdn-icons-png.flaticon.com/512/1/1700.png"
                        style="width:25px;height:25px;vertical-align:middle;">
                        Certificates
                    </div>
                    <div class="cert-menu">
                        <a href="https://drive.google.com/file/d/1FHFCeiOJ8qmiIYHIPD4HR5zapQnYWRd1/view?usp=drive_link" target="_blank">SQL Mastery</a>
                    </div>
                </div>
            </div>
            <div class="skill-tools">
                Extract Data, Analyze Large Datasets <br>
                Create Reports, Data Filtering <br>
                Database Queries, Decision Support
            </div>
        </div>
        
        <!-- Machine Learning -->
         <div class="skill-card">
            <div class="skill-header">
                <div class="skill-left">
                    <img src="https://cdn-icons-png.flaticon.com/512/4616/4616734.png">
                    <div class="skill-name">ML</div>
                    </div>
                <div class="cert-dropdown">
                    <div class="cert-badge">
                        <img src="https://cdn-icons-png.flaticon.com/512/1/1700.png"
                        style="width:25px;height:25px;vertical-align:middle;">
                        Certificates
                    </div>
                    <div class="cert-menu">
                        <a href="https://drive.google.com/file/d/1wMt9wKgFKWLZccwCvyIYfu1vMUt-8pLl/view?usp=drive_link" target="_blank">Machine Learning with Python</a>
                    </div>
                </div>
            </div>
            <div class="skill-tools">
                Predict Outcomes, Classification Models <br>
                Pattern Detection, Forecasting <br>
                Data-Driven Decisions, Model Evaluation
            </div>
        </div>
        
        <!-- Tableau -->
        <div class="skill-card">
            <div class="skill-header">
                <div class="skill-left">
                    <img src="https://img.icons8.com/color/96/tableau-software.png">
                    <div class="skill-name">Tableau</div>
                </div>
                <div class="cert-dropdown">
                    <div class="cert-badge">
                        <img src="https://cdn-icons-png.flaticon.com/512/1/1700.png"
                        style="width:25px;height:25px;vertical-align:middle;">
                        Certificates
                    </div>
                    <div class="cert-menu">
                        <a href="https://drive.google.com/file/d/1FHFCeiOJ8qmiIYHIPD4HR5zapQnYWRd1/view?usp=drive_link" target="_blank">Tableau Essentials</a>
                    </div>
                </div>
            </div>
            <div class="skill-tools">
                Visual Dashboards, Data Storytelling <br>
                Trend Analysis, Business Insights <br>
                Interactive Reports, Data Storytelling
            </div>
        </div>
        
        </div>
        </div>
        
        """, unsafe_allow_html=True)
# ================= PROJECTS TAB =================
with tab3:
    st.title("My Projects")

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
        
        padding:10px 18px;
        
        color:black !important;
        font-weight:Sami bold;
        transition:0.3s;
    }
    
    </style>
    """, unsafe_allow_html=True)

    def project_card(image, title, desc, tools, link):
        st.markdown(f"""
        <div class="project-card">
        <img src="{image}" style="
            width:100%;
            height:220px;
            object-fit:Cover;
            object-position:center;
            border-radius:10px;
        ">
        <h3 class="project-title">{title}</h3>
        <p class="project-desc">{desc}</p>

    <div style="display:flex;justify-content:space-between;align-items:center;">
            <span class="tool-tag">{tools}</span>
            <a href="{link}" target="_blank" class="view-btn">View Project</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


    # Function ke bahar
    col1, col2 = st.columns(2)

    with col1:
        project_card(
            image="https://raw.githubusercontent.com/PimiRoy/Supply-Chain-Power-BI/main/Supply%20Chain%20Dashboard.png",
            title="Supply Chain Dashboard",
            desc="Designed a Power BI dashboard providing insights into inventory management, sales performance, order fulfillment, and logistics operations.",
            tools="Power BI",
            link="https://github.com/PimiRoy/Supply-Chain-Power-BI"
        )
        project_card(
            image="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200",
            title="AI Uses by Students",
            desc="Analyzed student AI usage patterns, tool preferences, CGPA trends, and educational applications using SQL queries and data analysis.",
            tools="SQL",
            link="https://github.com/PimiRoy/AI-uses-by-Student-"
        )
        project_card(
            image="https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=1200",
            title="Second-Hand Cars Sales Analysis",
            desc="Built SQL queries to analyze second-hand car sales data, revealing insights into pricing, vehicle characteristics, and market demand.",
            tools="SQL",
            link="https://github.com/PimiRoy/second-hand-cars-sells"
        )
       

    with col2:
        project_card(
            image="https://raw.githubusercontent.com/PimiRoy/-Gaming-Behavior-Mental-Health-Impact/refs/heads/main/AI%20Era.png",
            title="Job in AI era dashboard",
            desc="Developed an interactive Power BI dashboard analyzing AI job trends, salary distributions, top skills, and job market growth across different years.",
            tools="Power BI",
            link="https://github.com/PimiRoy/-Job-in-AI-Era-And--Impact"
        )
        project_card(
            image="https://images.unsplash.com/photo-1567157577867-05ccb1388e66?w=1200",
            title="Mumbai House Pricing Analysis",
            desc="Analyzed Mumbai housing data using Python to identify price trends, location-wise variations, and key factors influencing property prices.",
            tools="Python | Pandas | Matplotlib",
            link="https://github.com/PimiRoy/Mumbai-House-pricing-"
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
        .contact-link{ color:black; text-decoration:none; font-size:22px; transition:0.3s; }
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
            <a href="https://mail.google.com/mail/?view=cm&fs=1&to=pimikaroy2@gmail.com"
            target="_blank"
            class="contact-link">
            pimikaroy2@gmail.com
            </a>
        </div>
        
        <div class="contact-row">
            <img src="https://tse4.mm.bing.net/th/id/OIP.6BVAY1s7M_ezWBhYMryTzgHaJS?rs=1&pid=ImgDetMain&o=7&rm=3"
                class="contact-icon">

        <div class="contact-text">
                <a href="https://drive.google.com/file/d/1aPVP8tzXZnMpTBxIc66j372OcfXppXbA/view?usp=drive_link"
                target="_blank"
                style="text-decoration:none; color:blue; font-size:22px;">
                Pimika Roy Resume
                </a>
        </div>
        </div>
        <div class="contact-row">
            <img src="https://clipground.com/images/location-icon-png-9.png" class="contact-icon">
            <div class="contact-text">Delhi, India</div>
        </div>

        </div>
        """, unsafe_allow_html=True)
