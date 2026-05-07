from pathlib import Path
import json

def load_itinerary_prompt() -> dict:
    """
    Loads the itinerary prompt JSON template.
    """
    prompt_path = Path(__file__).resolve().parent / "prompts" / "itinerary_prompt.json"
    if not prompt_path.exists():
        raise FileNotFoundError(f"Itinerary prompt JSON not found at: {prompt_path}")

    with prompt_path.open("r", encoding="utf-8") as f:
        return json.load(f)
    

def validate_inputs(destination:str, budget:str, travellers:int, days:int) -> tuple[bool, str]:
    if not destination or destination.strip() == "":
        return False, "Destination cannot be empty."
    
    if travellers <= 0:
        return False, "Number of days must be at least 1"

    if days <= 0:
        return False, "Destination cannot be empty."

    if budget not in ["Low", "Medium", "High"]:
        return False, "Budget must be Low or Medium or High."   

    return True, ""         


def build_itinerary_prompt(destination: str, budget: str, travelers: int, days: int) -> str:
    """
    Build the final prompt combining system instructions + user inputs.
    """
    prompt_json = load_itinerary_prompt()

    system_instruction = prompt_json["system_instruction"]
    template = prompt_json["user_prompt_template"]

    # Insert values
    filled_prompt = (
        system_instruction
        + "\n\n"
        + template.replace("{{DESTINATION}}", destination.strip())
                  .replace("{{BUDGET}}", budget.strip())
                  .replace("{{TRAVELERS}}", str(travelers))
                  .replace("{{DAYS}}", str(days))
    )

    return filled_prompt