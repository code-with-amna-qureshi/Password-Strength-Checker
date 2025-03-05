import re
import streamlit as st

# Page styling
st.set_page_config(page_title="🗝️Password Strength Checker By Amna Qureshi", page_icon="🏷️", layout="centered")

# CSS
st.markdown("""
    <style>
        .main {text-align: center;}
        .stTextInput {width: 60% !important; margin: auto;}
        .stButton {width:50%; background-color: blue; color: black; font-size: 18px;}
        .stButton button:hover { background-color:  lightyellow;}
    </style>
""", unsafe_allow_html=True)

# Page title and description
st.title("Password Strength Checker")
st.write("Enter your password below to check its security level.🔎")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    # Check for both uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    # Check for at least one digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    # Check for at least one special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*)**.")

    # Display password strength results
    if score == 4:
        st.success("✅ **Strong Password** is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")
        # Provide feedback on how to improve the password
        if feedback:
            with st.expander("**Improve Your Password**"):
                for item in feedback:
                    st.write(item)

# Password input field
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔒")

# Button to check strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first!")
