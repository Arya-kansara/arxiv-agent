import re
from state import AgentState

def understand_query(state: AgentState) -> AgentState:

    query = state["query"].strip()

    # -------- URL --------
    url_match = re.search(r"arxiv\.org/(abs|pdf)/(\d{4}\.\d{4,5})", query)

    if url_match:
        state["query"] = url_match.group(2)
        state["is_topic_search"] = False
        return state

    # -------- Paper ID --------
    id_match = re.fullmatch(r"\d{4}\.\d{4,5}", query)

    if id_match:
        state["is_topic_search"] = False
        return state

    # -------- Topic --------
    state["is_topic_search"] = True
    return state