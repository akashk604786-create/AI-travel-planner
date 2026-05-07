from __future__ import annotations
import os
from typing import Optional

from groq import Groq
from dotenv import load_dotenv
from config.model_config import load_config

load_dotenv()

class GroqClient:   # (name same, as you requested earlier)
    def __init__(self, api_key: Optional[str] = None, config_path: Optional[str] = None):
        self.app_config = load_config(config_path)
        self.model_cfg = self.app_config.model

        self.api_key = api_key or os.getenv("GROQ_API_KEY")

        if not self.api_key:
            raise ValueError("❌ GROQ_API_KEY not found")

        self.client = Groq(api_key=self.api_key)

    def ask(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model_cfg.name,
                messages=[
                    {"role": "system", "content": "You are a helpful travel assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.model_cfg.temperature,
                max_tokens=self.model_cfg.max_output_tokens,
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"❌ Error: {str(e)}"