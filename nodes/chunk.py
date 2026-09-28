from state import AgentState
from utils.chunker import chunk_text

def create_chunks(state: AgentState) -> AgentState:

    chunks = chunk_text(state["full_text"])

    state["chunks"] = chunks

    return state