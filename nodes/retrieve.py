from state import AgentState
from utils.arxiv_client import search_arxiv

def retrieve_paper(state : AgentState) -> AgentState:
    results = search_arxiv(
        state['query'],
        state['is_topic_search']
    )


    if results is None:
        raise ValueError("No Paper found on arXiv")

    state['paper'] = {
        "title"     : results.title,
        "authors"   : [author.name for author in results.authors],
        "summary"   : results.summary,
        "pdf_url"   : results.pdf_url,
        "published" : str(results.published.date()),
        "entry_id"  : results.entry_id
    }

    return state