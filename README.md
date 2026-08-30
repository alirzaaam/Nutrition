# 🥗 Nutrition AI

An AI-powered diet plan generator built with Django and Ollama.

Nutrition AI collects a user's basic physical information, activity level,
weight-loss goal, and dietary preferences, then uses a locally hosted LLM
to generate a personalized diet plan.

> 🚧 Work in Progress — The project is actively being developed.

## Features

- Personalized diet plan generation
- Local LLM integration with Ollama
- User input for physical and dietary information
- Calorie and meal recommendations
- Water and exercise recommendations
- Weekly grocery list generation

## Tech Stack

- Python
- Django
- Ollama
- HTML / CSS
- SQLite

## How It Works

User Input → Django → Prompt → Ollama LLM → Diet Plan → Web UI

## Installation

```bash
git clone https://github.com/alirzaaam/Nutrition.git
cd Nutrition

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
