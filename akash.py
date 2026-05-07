from utils.itinerary_helper import build_itinerary_prompt, validate_inputs
from utils.llm_client import GroqClient

destination = "Rishikesh"
budget = "Medium"
travellers = 2
days = 7

valid, msg = validate_inputs(destination, budget, travellers, days)

if not valid:
    print("❌ Validation failed:", msg)
else:
    prompt = build_itinerary_prompt(destination, budget, travellers, days)
    client = GroqClient()
    result = client.ask(prompt)
    print(result)