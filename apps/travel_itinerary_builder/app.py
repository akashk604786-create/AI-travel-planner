import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from utils.llm_client import GroqClient
from utils.itinerary_helper import build_itinerary_prompt, validate_inputs


def main():
    st.set_page_config(
        page_title="AI Travel Planner",
        page_icon="✈️",
        layout="wide"
    )

    # 🔥 Custom Styling
    st.markdown("""
        <style>
        .main {
            background-color: #0f172a;
            color: white;
        }
        .stButton>button {
            background-color: #6366f1;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-weight: bold;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # 🔥 Header
    st.markdown("## ✈️ AI Travel Planner")
    st.caption("Plan smarter trips with AI-powered itineraries")

    st.markdown("---")

    # 🔥 Layout (2 columns)
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("🧳 Trip Details")

        destination = st.text_input(
            "Destination",
            placeholder="e.g. Goa, Bali, Rishikesh"
        )

        travellers = st.number_input(
            "Travellers",
            min_value=1,
            value=2
        )

        days = st.slider(
            "Trip Duration (Days)",
            min_value=1,
            max_value=14,
            value=3
        )

        budget = st.selectbox(
            "Budget",
            ["Low", "Medium", "High"]
        )

        generate = st.button("🚀 Generate Itinerary")

    with col2:
        st.subheader("🌍 Your Itinerary")

        if generate:
            is_valid, msg = validate_inputs(destination, budget, travellers, days)

            if not is_valid:
                st.warning(msg)
                return

            with st.spinner("✈️ Crafting your perfect trip..."):
                try:
                    prompt = build_itinerary_prompt(
                        destination=destination,
                        budget=budget,
                        travelers=travellers,
                        days=days
                    )

                    client = GroqClient()
                    result = client.ask(prompt)

                    # 🔥 Output Card
                    st.markdown("""
                        <div style="background-color:#1e293b;padding:20px;border-radius:15px;">
                    """, unsafe_allow_html=True)

                    st.markdown(result)

                    st.markdown("</div>", unsafe_allow_html=True)

                except Exception as e:
                    st.error(f"Error: {str(e)}")

        else:
            st.info("Fill details and click Generate 🚀")


if __name__ == "__main__":
    main()