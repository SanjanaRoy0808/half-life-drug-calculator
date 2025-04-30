import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Configure page
st.set_page_config(page_title="💊 Drug Half-Life Explorer", page_icon="💊", layout="centered")

# Inject CSS for extra visual polish
st.markdown("""
    <style>
        body {
            background-color: #f7f9fa;
        }
        .main {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
        }
        h1, h2, h3 {
            color: #4CAF50;
        }
        .stButton>button {
            background-color: #6A1B9A;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1em;
        }
        .stButton>button:hover {
            background-color: #8E24AA;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center;'>💊 Drug Half-Life Explorer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Explore how long a drug stays in your system 📉</p>", unsafe_allow_html=True)
st.markdown("---")

# Input Section
st.markdown("### 🔢 Enter Drug Properties")
col1, col2 = st.columns(2)
with col1:
    vd = st.number_input("📦 Volume of Distribution (Vd) in Liters", min_value=0.1, value=70.0)
with col2:
    cl = st.number_input("🚰 Clearance Rate (CL) in Liters/hour", min_value=0.1, value=5.0)

# Pharmacokinetic Calculation
half_life = (0.693 * vd) / cl
elimination_time = half_life * 5

if st.button("🚀 Calculate & Show Graph"):
    st.markdown("### 🧪 Pharmacokinetic Results")
    st.success(f"🧬 *Half-Life*: {half_life:.2f} hours")
    st.info(f"⏳ *Approximate Full Elimination Time*: {elimination_time:.1f} hours (~5 half-lives)")

    # Plot Concentration Curve
    time = np.linspace(0, elimination_time, 150)
    concentration = 100 * (0.5) ** (time / half_life)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(time, concentration, color='mediumvioletred', linewidth=2.5, label='Drug Concentration')
    ax.axhline(y=5, color='darkred', linestyle='--', linewidth=1.5, label='5% Threshold')
    ax.set_facecolor('#fdfdfd')
    ax.set_title("📊 Drug Concentration vs Time", fontsize=14, color="#6A1B9A")
    ax.set_xlabel("Time (hours)")
    ax.set_ylabel("Concentration (%)")
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.legend()
    st.pyplot(fig)

    # Educational Content
    st.markdown("---")
    st.markdown("## 📘 Learn About Half-Life")

    st.markdown("""
    *💡 What is Half-Life?*  
    The *half-life* is the time it takes for a drug’s concentration in the bloodstream to reduce by *50%*.

    *Why it matters:*  
    - 🕐 Helps determine *dosing schedules*
    - 🩺 Affects *drug accumulation*
    - ⚠ Impacts *drug safety and interactions*

    *✨ Quick Facts:*
    - 🔄 After *5 half-lives, about **97%* of the drug is gone.
    - 🧠 Long half-life drugs may only need *once-daily dosing*.
    - ⚡ Rapid-clearance drugs may wear off quickly — even within *hours*!

    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<p style='text-align: center;'>🧪 Made with ❤ using Streamlit and Python</p>", unsafe_allow_html=True)