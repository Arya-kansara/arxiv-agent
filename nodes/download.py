from state import AgentState
from utils.arxiv_client import search_arxiv
from utils.pdf_downloader import save_pdf

def download_pdf(state: AgentState) -> AgentState:

    result = search_arxiv(
        state["query"],
        state["is_topic_search"]
    )

    if result is None:
        raise ValueError("Paper not found.")

    pdf_path = save_pdf(
        pdf_url=result.pdf_url,
        paper_id=result.get_short_id()
    )

    state["pdf_path"] = pdf_path

    return state