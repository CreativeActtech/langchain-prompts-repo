import sys
from pathlib import Path

# Add the src directory to the system path so we can import our loader
sys.path.append(str(Path(__file__).parent))

from src.loader import PromptRepoLoader

def main():
    print("--- Initializing Prompt Repository ---")
    
    # Initialize the loader pointing to the 'prompts' directory
    try:
        loader = PromptRepoLoader("./prompts")
        print("✅ Repository loaded successfully.\n")
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        return

    # --- TEST 1: Load a Fraud Detection Prompt ---
    print("--- Test 1: Loading FRAUD-001 (Narrative Similarity) ---")
    try:
        prompt_fraud = loader.get_prompt_by_id("fraud_detection_security.json", "FRAUD-001")
        
        # Define input variables
        input_data = {
            "new_claim": "My car was stolen from the parking lot at 5 PM. It was a red sedan."
        }
        
        # Format the prompt
        formatted_prompt = prompt_fraud.format(**input_data)
        
        print(f"Prompt Name: {prompt_fraud.template[:50]}...")
        print("-" * 20)
        print("Formatted Output:")
        print(formatted_prompt)
        print("-" * 20 + "\n")
        
    except Exception as e:
        print(f"❌ Test 1 Failed: {e}\n")

    # --- TEST 2: Load a Knowledge Management Prompt ---
    print("--- Test 2: Loading KM-002 (Lessons Learned) ---")
    try:
        prompt_km = loader.get_prompt_by_id("knowledge_management.json", "KM-002")
        
        input_data = {
            "PROJECT_NAME": "Website Redesign",
            "PROJECT_ARTIFACTS": "The project was delayed by 2 weeks because the design team used outdated brand guidelines."
        }
        
        formatted_prompt = prompt_km.format(**input_data)
        
        print("Formatted Output:")
        print(formatted_prompt)
        print("-" * 20 + "\n")
        
    except Exception as e:
        print(f"❌ Test 2 Failed: {e}\n")

if __name__ == "__main__":
    main()