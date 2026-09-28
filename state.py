# --- Import Libraries ---
from typing import TypedDict , List , Dict , Any , Optional

class AgentState(TypedDict):
    # --- user input ---
    query : str                         # --- topic or arxiv id ---
    is_topic_search : bool              # --- True = Topic , False = paperID ---

    # --- Paper/Metadata
    paper : Optional[dict[str,Any]]     # --- Title , Author , Abstract , PDF url ---

    # --- PDF ---

    pdf_path : Optional[str]            # --- location of downloaded pdf ---
    full_text : str                     # --- extracted pdf text ---

    # --- RAG ---
    chunks : List[str]                  # --- split text into RAG ---
    vectorstore : Any                   # --- FAISS Index ---

    # --- output ---
    brief : str                         # --- final summary ---

    # --- conversation history ---
    messages : List[Dict[str , str]]    # --- QA Chat History ---