import streamlit as st
import datetime

st.set_page_config(page_title="ChillSpace 🍷", page_icon="🍷", layout="centered")

# ---------------------- HEADER ---------------------- #
st.title("🍷 ChillSpace")
st.subheader("Your adult corner: Goals, Habits & Relaxation")

# Sidebar Menu
menu = ["🏠 Home", "✅ Goals", "📅 Habits", "🧘 Relax"]
choice = st.sidebar.radio("Menu", menu)

# ---------------------- HOME ---------------------- #
if choice == "🏠 Home":
    st.write("Welcome to ChillSpace — A calm place for grown folks to stay on track ✨")
    st.info("Use the sidebar to navigate through goals, habits, and relaxation tools.")

# ---------------------- GOALS ---------------------- #
elif choice == "✅ Goals":
    st.header("🎯 Set Your Goals")
    goal = st.text_input("Enter a new goal:")
    deadline = st.date_input("Deadline", datetime.date.today())
    if st.button("Add Goal"):
        st.success(f"Goal added: {goal} (Deadline: {deadline})")

# ---------------------- HABITS ---------------------- #
elif choice == "📅 Habits":
    st.header("📅 Habit Tracker")
    habit = st.text_input("Enter a habit you want to track:")
    freq = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])
    if st.button("Track Habit"):
        st.success(f"Habit '{habit}' set to {freq} tracking ✨")

# ---------------------- RELAX ---------------------- #
elif choice == "🧘 Relax":
    st.header("🧘 Chill Mode")
    st.write("Take a deep breath. Here are some adult vibes:")
    st.markdown("- 🍵 Sip some tea\n- 📖 Read a book\n- 🎶 Play some jazz\n- 🌙 Meditate for 5 mins")
    if st.button("Random Relax Quote"):
        import random
        quotes = [
            "Peace begins with a deep breath.",
            "Your vibe attracts your tribe.",
            "Slow down, you’re doing just fine.",
            "Rest is productive too."
        ]
        st.success(random.choice(quotes))
