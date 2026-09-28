from state import AgentState
from utils.embeddings import create_embeddings
from utils.vectorstore import build_faiss_index

def create_vectorstore(state: AgentState) -> AgentState:

    embeddings = create_embeddings(state["chunks"])

    index = build_faiss_index(embeddings)

    state["vectorstore"] = index

    return state