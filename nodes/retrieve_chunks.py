from state import AgentState
from utils.retriever import retrieve_chunks

def retrieve_context(state: AgentState, question: str):

    context = retrieve_chunks(
        question,
        state["chunks"],
        state["vectorstore"]
    )

    return context