from langgraph.graph import StateGraph, END

from state import AgentState

from nodes.understand import understand_query
from nodes.retrieve import retrieve_paper
from nodes.download import download_pdf
from nodes.parse_pdf import parse_pdf
from nodes.chunk import create_chunks
from nodes.embed import create_vectorstore
from nodes.briefing import generate_briefing


builder = StateGraph(AgentState)

builder.add_node("understand", understand_query)
builder.add_node("retrieve", retrieve_paper)
builder.add_node("download", download_pdf)
builder.add_node("parse", parse_pdf)
builder.add_node("chunk", create_chunks)
builder.add_node("embed", create_vectorstore)
builder.add_node("brief", generate_briefing)

builder.set_entry_point("understand")

builder.add_edge("understand", "retrieve")
builder.add_edge("retrieve", "download")
builder.add_edge("download", "parse")
builder.add_edge("parse", "chunk")
builder.add_edge("chunk", "embed")
builder.add_edge("embed", "brief")
builder.add_edge("brief", END)

graph = builder.compile()