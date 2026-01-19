
import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Anand Mohan Jha | Portfolio", layout="wide", page_icon="💻")

# --- SIDEBAR ---
with st.sidebar:
    st.title("Anand Mohan Jha")
    st.write("📧 aj1001194@gmail.com")
    st.write("📞 +91 9339824377")
    [cite_start]st.write("📍 Bangalore, India [cite: 6]")
    st.markdown("---")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/anand-mohan-jha-55843924a)")
    st.write("🐙 [GitHub](https://github.com/githuanand)")
    st.write("🏆 [HackerRank](https://www.hackerrank.com/profile/aj29092001)")

# --- HEADER ---
st.title("Software Developer Portfolio")
[cite_start]st.subheader("Aspiring Software Developer | Python Full Stack Trainee [cite: 49]")
[cite_start]st.write("Motivated fresher with strong coding fundamentals in Python, SQL, and Django[cite: 3, 20].")

# --- EDUCATION ---
st.header("🎓 Education")
[cite_start]st.write("**B.Tech in Information Technology** [cite: 9]")
[cite_start]st.write("MCKV Institute of Engineering, Howrah | 2021-2025 [cite: 10, 11]")
[cite_start]st.write("Current CGPA: 7.81 [cite: 23]")

# --- PROJECTS ---
st.header("🚀 Projects")
col1, col2 = st.columns(2)
with col1:
    [cite_start]st.info("### Netflix Content Analytics [cite: 43]")
    [cite_start]st.write("Data analysis using Python to uncover content trends[cite: 54, 56].")
with col2:
    [cite_start]st.success("### Django Weather App [cite: 44]")
    [cite_start]st.write("Real-time weather tracking application built with Django[cite: 58].")

# --- SKILLS ---
st.header("🛠️ Skills")
[cite_start]st.write("Python, SQL, Django, HTML, CSS, Github, Data Analysis[cite: 20, 21, 22, 24, 28].")
