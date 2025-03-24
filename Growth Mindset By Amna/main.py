# Growth Mindset Challenge - Streamlit Web App by Amna

import streamlit as st

# Store reflections 
reflections = []

def main():
    st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")

    st.title("🌱 Growth Mindset Challenge")
    st.write("Embrace challenges, learn from mistakes, and unlock your true potential!")

   
    st.header("📚 What is a Growth Mindset?")
    st.markdown("""
    - **Embrace Challenges:** See difficulties as opportunities to learn.
    - **Learn from Mistakes:** Mistakes are a natural part of growth.
    - **Persist Through Difficulties:** Stay determined, even when things get tough.
    - **Celebrate Effort:** Recognize and reward the process of learning.
    - **Keep an Open Mind:** Adapt and stay curious!

    Your abilities are not fixed—You can improve with effort and persistence!
    """)

    # Section: Share Your Growth Journey
    st.header("📝 Share Your Growth Journey")
    with st.form("reflection_form"):
        name = st.text_input("Your Name:")
        challenge = st.text_area("Describe a recent challenge you faced:")
        lesson = st.text_area("What did you learn from it?")

        if st.form_submit_button("Submit Reflection"):
            if name and challenge and lesson:
                reflections.append({"name": name, "challenge": challenge, "lesson": lesson})
                st.success("✅ Reflection submitted successfully!")
            else:
                st.error("❌ Please fill out all fields before submitting.")

   
    st.header("🌟 Community Reflections")
    if reflections:
        for reflection in reflections[::-1]:
            st.subheader(f"🧠 {reflection['name']}")
            st.write(f"**Challenge:** {reflection['challenge']}")
            st.write(f"**Lesson Learned:** {reflection['lesson']}")
            st.markdown("---")
    else:
        st.info("No reflections yet. Be the first to share your journey!")

    # Footer
    st.sidebar.title("About the Project")
    st.sidebar.info("This project is part of the Growth Mindset Challenge. Share your experiences and inspire others!")

 # Design Credit
    st.markdown("---")
    st.markdown("### 🎉 Design by Amna")

if __name__ == "__main__":
    main()
