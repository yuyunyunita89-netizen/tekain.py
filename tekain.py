import streamlit as st

# Define the questions and correct answers
questions = {
    "She ___ (read) a book every day.": "reads",
    "He ___ (not/play) football.": "does not play",
    "___ she like apples?": "Does",
    "They ___ (go) to school every morning.": "go",
    "My father ___ (work) in an office.": "works",
    "We ___ (not/eat) fast food every day.": "do not eat",
    "___ you speak English?": "Do",
    "He ___ (watch) TV every night.": "watches",
    "The sun ___ (rise) in the east.": "rises",
    "I ___ (like) chocolate.": "like",
    "My mother ___ (cook) delicious food.": "cooks",
    "They ___ (not/play) basketball.": "do not play",
    "___ your brother play the guitar?": "Does",
    "She ___ (study) English every evening.": "studies",
    "The train ___ (leave) at 7 a.m.": "leaves",
    "We ___ (go) shopping every weekend.": "go",
    "He ___ (not/drink) coffee.": "does not drink",
    "___ they live in Jakarta?": "Do",
    "My sister ___ (clean) her room on Sunday.": "cleans",
    "The cat ___ (sleep) on the sofa.": "sleeps",
    "I ___ (not/like) spicy food.": "do not like",
    "___ she go to school by bus?": "Does",
    "The students ___ (study) hard before exams.": "study",
    "My father ___ (drive) to work every day.": "drives",
    "They ___ (not/watch) horror movies.": "do not watch",
    "___ you read books every night?": "Do",
    "She ___ (teach) English at a school.": "teaches",
    "He ___ (fix) the car in the garage.": "fixes",
    "We ___ (not/go) to the park on Monday.": "do not go",
    "The dog ___ (bark) loudly at strangers.": "barks"
}

# Initialize the session state for tracking score and user answers
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0

# Function to handle quiz logic
def check_answer(user_answer, correct_answer):
    if user_answer.strip().lower() == correct_answer.lower():
        st.session_state.score += 1
        return True
    return False

# Display title
st.title("Latihan Soal Bahasa Inggris - Simple Present Tense")

# Get the current question and answer
question = list(questions.keys())[st.session_state.current_question]
correct_answer = questions[question]

# Display question
st.write(f"**Question {st.session_state.current_question + 1}:** {question}")

# Get user's answer
user_answer = st.text_input("Jawabanmu:", key=f"answer_{st.session_state.current_question}")

# Check the answer if the user submits an answer
if user_answer:
    if check_answer(user_answer, correct_answer):
        st.success("✅ Benar!")
    else:
        st.error(f"❌ Salah. Jawaban yang benar: {correct_answer}")
    
    # Go to next question
    st.session_state.current_question += 1

# Display current score
st.sidebar.write(f"**Skor kamu:** {st.session_state.score}/{len(questions)}")

# When the user reaches the last question
if st.session_state.current_question >= len(questions):
    st.write("### Quiz Selesai!")
    st.write(f"**Skor akhir kamu:** {st.session_state.score}/{len(questions)}")
    if st.button("Ulangi Quiz"):
        # Reset the session state for a new quiz
        st.session_state.score = 0
        st.session_state.current_question = 0
