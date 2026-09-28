from state import AgentState
import ollama

def generate_briefing(state: AgentState) -> AgentState:

    prompt = f"""
Create a complete Executive Briefing.

Title: {state["paper"]["title"]}
Authors: {", ".join(state["paper"]["authors"])}

Paper:
{state["full_text"][:22000]}

Return Markdown with:
- Why this paper matters
- Problem Statement
- Method / Approach
- Key Results
- Limitations
- Suggested Follow-up Questions
"""

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    state["brief"] = response["message"]["content"]

    return state