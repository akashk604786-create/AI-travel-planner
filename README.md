# AI Travel Planner ✈️

Generate a day-by-day travel itinerary for any destination using an LLM (Groq + Llama 3.1).

## Features

- Enter a destination, number of travellers, trip length and budget
- Get a personalised day-wise itinerary in seconds
- Clean Streamlit UI

## Tech Stack

- Python, Streamlit
- Groq API (`llama-3.1-8b-instant`)

## Run Locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key
```

Start the app:

```bash
streamlit run apps/travel_itinerary_builder/app.py
```

Open http://localhost:8501.

## Project Structure

```
apps/travel_itinerary_builder/   Streamlit app + prompts
utils/                           Groq client, prompt builders, helpers
config/config.yaml               Model settings (name, temperature, tokens)
```
