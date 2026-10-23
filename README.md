# AI Soccer Trainer

## Project Description

AI Soccer Trainer is a Python application that creates personalized soccer training plans using Google's Gemini AI. The application helps soccer players improve their skills by providing training exercises based on their experience level, playing position, and training goals.

## Features

- Select experience level: Beginner, Intermediate, or Advanced.
- Choose playing position: Forward, Midfielder, Defender, or Goalkeeper.
- Select a skill to improve: Dribbling, Passing, Shooting, or Fitness.
- Choose a training duration: 15, 30, or 60 minutes.
- Generate a personalized soccer training plan using AI.

## Technologies Used

- Python
- Streamlit
- Google Gemini API

## Prompt Engineering Techniques

**Persona Pattern:** The AI is instructed to act as an experienced soccer coach to provide helpful training recommendations.

**Few-Shot Pattern:** The AI is given examples of soccer drills to guide how it generates training plans.

## How to Run

1. Install Python.
2. Install the required packages using `pip install -r requirements.txt`.
3. Create a `.streamlit/secrets.toml` file containing `GEMINI_API_KEY = "your_api_key_here"`.
4. Run the application using `python -m streamlit run app.py`.
5. Open the application in your browser.

## Future Improvements

In the future, the application could include weekly training schedules, player progress tracking, and more personalized training options.