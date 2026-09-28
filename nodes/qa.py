from state import AgentState
from utils.retriever import retrieve_chunks
from utils.llm import ask_llm

def answer_question(state: AgentState, question: str):

    q = question.lower().strip()

    if "title" in q:
        return state["paper"]["title"]

    if "author" in q or "authors" in q:
        return ", ".join(state["paper"]["authors"])

    if "year" in q or "published" in q:
        return state["paper"]["published"]

    context = retrieve_chunks(
        question,
        state["chunks"],
        state["vectorstore"],
        k=8
    )

    answer = ask_llm(
        question,
        context,
        state["paper"]["title"]
    )

    state["messages"].append({
        "role": "user",
        "content": question
    })

    state["messages"].append({
        "role": "assistant",
        "content": answer
    })

    return answer