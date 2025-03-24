import streamlit as st

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("🔢 Password should be at least 8 characters long.")

    # Upper and Lower Case Check
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        strength += 1
    else:
        feedback.append("🔠 Use both uppercase and lowercase letters.")

    # Digit Check
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("🔢 Include at least one digit.")

    # Special Character Check
    if any(c in "!@#$%^&*(),.?\":{}|<>" for c in password):
        strength += 1
    else:
        feedback.append("✨ Add a special character (!, @, #, etc.).")

    # Password Strength Level
    if strength == 4:
        return "🟢 Strong", feedback
    elif strength == 3:
        return "🟡 Moderate", feedback
    else:
        return "🔴 Weak", feedback

def main():
    st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 3em;
             color: #800080;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 1.2em;
            color: #888;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>🔐 Password Strength Meter</div>", unsafe_allow_html=True)

    password = st.text_input("Enter your password:", type="password")

    if st.button("Check Strength"):
        if password:
            strength, feedback = check_password_strength(password)

            st.markdown(f"<h2 style='color: #2196F3;'>Password Strength: {strength}</h2>", unsafe_allow_html=True)

            if feedback:
                st.markdown("### 🛠️ Suggestions to Improve:")
                for tip in feedback:
                    st.write(f"- {tip}")

    st.markdown("<div class='footer'>✨ Design by Aamna</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
