
import streamlit as st
from google import genai

st.title("AI Soccer Trainer")
st.write("Create your own soccer training plan!")

# Connect to Gemini
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# Player information
level = st.selectbox("Experience Level",
                     ["Beginner", "Intermediate", "Advanced"])

position = st.selectbox("Playing Position",
                        ["Forward", "Midfielder", "Defender", "Goalkeeper"])

skill = st.selectbox("Skill to Improve",
                     ["Dribbling", "Passing", "Shooting", "Fitness"])

duration = st.selectbox("Training Duration",
                        ["15 minutes", "30 minutes", "60 minutes"])

# Generate a training plan
if st.button("Generate Training Plan"):

    # Persona Pattern: AI acts as a soccer coach
    # Few-Shot Pattern: AI follows the examples below
    prompt = f"""
    You are an experienced soccer coach who helps
    players improve their skills.

    Create a training plan for this player:
    Experience: {level}
    Position: {position}
    Skill: {skill}
    Duration: {duration}

    Here are examples of how to explain drills:

    Example 1:
    Drill: Cone Dribbling
    Time: 5 minutes
    Instructions: Dribble between cones using both feet.

    Example 2:
    Drill: Wall Passing
    Time: 10 minutes
    Instructions: Pass against a wall and control
    the ball when it returns.

    Now create a new training plan for this player.
    Include a warm-up, three drills, and a cooldown.
    Make sure the total time matches the duration.
    Use simple instructions and explain each drill.
    """

   
    with st.spinner("Creating your training plan..."):
        try:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt
            )

            st.subheader("Your Training Plan")
            st.write(response.text)

        except Exception as e:
            st.error("Could not generate the training plan.")
            st.write(str(e))
