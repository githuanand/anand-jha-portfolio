
import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Anand Mohan Jha | Portfolio", layout="wide", page_icon="💻")

# --- SIDEBAR ---
with st.sidebar:
    # This assumes PHOTO1.png is uploaded to your GitHub repo root
    st.image("https://raw.githubusercontent.com/githuanand/anand-jha-portfolio/main/PHOTO1.png")
    st.title("Anand Mohan Jha")
    st.write("📧 aj1001194@gmail.com")
    st.write("📞 +91 9339824377")
    st.write("📍 Bangalore, India")
    st.markdown("---")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/anand-mohan-jha-55843924a)")
    st.write("🐙 [GitHub](https://github.com/githuanand)")
    st.write("🏆 [HackerRank](https://www.hackerrank.com/profile/aj29092001)")

# --- HEADER ---
st.title("Software Developer Portfolio")
st.subheader("Aspiring Software Developer | Python Full Stack Trainee")
st.write("Motivated fresher with strong coding fundamentals in Python, SQL, and Django.")

# --- EDUCATION ---
st.header("🎓 Education")
st.write("**B.Tech in Information Technology**")
st.write("MCKV Institute of Engineering, Howrah | 2021-2025")
st.write("Current CGPA: 7.81")

# --- PROJECTS ---
st.header("🚀 Projects")
col1, col2 = st.columns(2)
with col1:
    st.info("### Netflix Content Analytics")
    st.write("Data analysis using Python to uncover content trends.")
with col2:
    st.success("### Django Weather App")
    st.write("Real-time weather tracking application built with Django.")

# --- SKILLS ---
st.header("🛠️ Skills")
st.write("Python, SQL, Django, HTML, CSS, Github, Data Analysis.")
