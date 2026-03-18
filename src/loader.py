import json
from pathlib import Path
from typing import Union, List
# UPDATED IMPORT: Use langchain_core for modern versions
from langchain_core.prompts import PromptTemplate

class PromptRepoLoader:
    """
    A custom loader to fetch prompts from the structured JSON repository.
    """
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        if not self.base_path.exists():
            raise FileNotFoundError(f"Directory not found: {self.base_path}")

    def _load_json_file(self, filename: str) -> List[dict]:
        """Helper to load a specific JSON file."""
        file_path = self.base_path / filename
        if not file_path.exists():
            raise FileNotFoundError(f"Prompt file not found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_prompt_by_id(self, filename: str, prompt_id: str) -> PromptTemplate:
        """
        Retrieves a specific prompt by its unique ID from a specific category file.
        """
        prompts_data = self._load_json_file(filename)
        
        for item in prompts_data:
            if item.get("id") == prompt_id:
                return PromptTemplate(
                    input_variables=item.get("input_variables", []),
                    template=item["template"],
                    template_format=item.get("template_format", "f-string")
                )
        
        raise ValueError(f"Prompt ID '{prompt_id}' not found in '{filename}'")

    def get_all_prompts_in_category(self, filename: str) -> List[PromptTemplate]:
        """
        Loads all prompts from a specific category file.
        """
        prompts_data = self._load_json_file(filename)
        prompt_objects = []
        
        for item in prompts_data:
            prompt_objects.append(
                PromptTemplate(
                    input_variables=item.get("input_variables", []),
                    template=item["template"],
                    template_format=item.get("template_format", "f-string")
                )
            )
        return prompt_objects