from state import AgentState
from utils.pdf_parser import extract_text

def parse_pdf(state: AgentState) -> AgentState:

    text = extract_text(state["pdf_path"])

    state["full_text"] = text

    return state