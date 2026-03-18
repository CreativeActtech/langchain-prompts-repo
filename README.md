
# CreativeAct Enterprise LangChain Prompts

This repository contains a collection of structured prompt templates designed for LangChain integration.
The prompts cover enterprise use cases including **Fraud Detection, Strategy, Operations, HR, and AI Governance**.

<br>

## Table of Contents

- [CreativeAct Enterprise LangChain Prompts](#creativeact-enterprise-langchain-prompts)
  - [Table of Contents](#table-of-contents)
  - [Structure](#structure)
  - [Setup](#setup)
    - [Venv Setup and Dependencies](#venv-setup-and-dependencies)
  - [Usage](#usage)
    - [Loading a Prompt](#loading-a-prompt)
    - [Using with an LLM (OpenAI)](#using-with-an-llm-openai)
    - [Using with a Local LLM (Ollama)](#using-with-a-local-llm-ollama)
  - [📚 Available Categories](#-available-categories)
  - [🤝 Contributing](#-contributing)
- [📄 License](#-license)

<br>

## Structure

- `prompts/`: Contains JSON files categorized by domain. Each file holds an array of prompt objects.
- `src/loader.py`: A custom utility to load prompts into LangChain PromptTemplate objects.

## Setup

### Venv Setup and Dependencies

```bash
# create venv
python3 -m venv venv
```

```bash
# activate
.venv/scripts/activate
```

```bash
pip install -r requirements.txt
```

<br>

## Usage

### Loading a Prompt

Load a specific prompt by its ID and format it with your data.

```python
from src.loader import PromptRepoLoader

# 1. Initialize the loader pointing to the 'prompts' folder
loader = PromptRepoLoader("./prompts")

# 2. Load a specific prompt (e.g., FRAUD-001 from the Fraud category)
prompt = loader.get_prompt_by_id("fraud_detection_security.json", "FRAUD-001")

# 3. Define your input variables
inputs = {
    "new_claim": "My vehicle was stolen from the parking lot."
}

# 4. Format the prompt
formatted_text = prompt.format(**inputs)

print(formatted_text)
```

<br>

### Using with an LLM (OpenAI)

If you have an OpenAI API key, you can connect these prompts directly to a model.

```python
import os
from langchain_openai import ChatOpenAI
from src.loader import PromptRepoLoader

# Set your API Key
os.environ["OPENAI_API_KEY"] = "sk-your-key-here"

loader = PromptRepoLoader("./prompts")
prompt = loader.get_prompt_by_id("knowledge_management.json", "KM-002")

# Initialize the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Create a chain: Prompt -> Model
chain = prompt | model

# Invoke the chain
response = chain.invoke({
    "PROJECT_NAME": "Project Phoenix",
    "PROJECT_ARTIFACTS": "We missed the deadline because the API key expired."
})

print(response.content)
```

<br>

### Using with a Local LLM (Ollama)

For air-gapped environments or local execution, you can use these prompts with **Ollama**.

**Prerequisites:**

1. Install and run [Ollama](https://ollama.com/).
2. Pull your desired model (e.g., `ollama pull llama3`).
3. Ensure the Ollama service is running (usually on `http://localhost:11434`).
4. Install the LangChain Ollama integration: `pip install langchain-ollama`.

**Implementation:**

```python
from langchain_ollama import ChatOllama
from src.loader import PromptRepoLoader

# 1. Initialize the loader
loader = PromptRepoLoader("./prompts")
prompt = loader.get_prompt_by_id("strategy_market_intelligence.json", "STRAT-001")

# 2. Initialize the Local Ollama Model
# Ensure you have pulled the model (e.g., 'llama3' or 'mistral') via Ollama CLI
model = ChatOllama(model="llama3", base_url="http://localhost:11434")

# 3. Create a chain
chain = prompt | model

# 4. Invoke the chain
response = chain.invoke({
    "COMPETITOR_DATA": "Competitor X has lowered prices by 20%.",
    "MARKET_CONTEXT": "Inflation is rising, consumer spending is down."
})

print(response.content)
```

<br>

## 📚 Available Categories

| Category File | Content Description | Prompt IDs |
|---------------|---------------------|------------|
| `fraud_detection_security.json` | Coordinated fraud, insider threats, scam detection. | `FRAUD-001` to `FRAUD-015` |
| `risk_compliance_governance.json` | Project risk, cybersecurity posture, ethical red teaming. | `RISK-001` to `RISK-005` |
| `strategy_market_intelligence.json` | Competitive analysis, market entry, ESG initiatives. | `STRAT-001` to `STRAT-004` |
| `product_innovation.json` | Feature prioritization, innovation bottlenecks. | `PROD-001` to `PROD-002` |
| `marketing_sales.json` | Customer personas, objection handling. | `MKT-001` to `MKT-002` |
| `operations_process.json` | Process optimization, cost management, customer journeys. | `OPS-001` to `OPS-005` |
| `hr_talent.json` | Engagement surveys, skills gaps, burnout analysis. | `HR-001` to `HR-003` |
| `technology_ai.json` | Tech adoption, AI readiness, human-AI workflows. | `TECH-001` to `TECH-003` |
| `knowledge_management.json` | Knowledge ecosystems, lessons learned, taxonomy. | `KM-001` to `KM-005` |

<br>

## 🤝 Contributing

To add a new prompt:

1. Open the relevant JSON file in the prompts/ directory.
2. Add a new object following the existing schema (ensure you assign a unique id).

```json
   {
  "id": "UNIQUE-ID",
  "name": "Prompt Name",
  "description": "Brief description of the use case.",
  "tags": ["relevant", "tags"],
  "input_variables": ["var1", "var2"],
  "template": "Your prompt text with {var1} placeholders.",
  "template_format": "f-string"
}
```

1. Validate your JSON syntax before committing.
2. Submit a pull request.

---

<br>

# 📄 License

This project is licensed under **Apache 2.0** - see the LICENSE file for details.

>**@ 2026** [CreativeAct Technologies](https://github.com/CreativeActtech)
