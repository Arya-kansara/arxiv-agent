from graph import graph
from nodes.briefing import generate_briefing
from nodes.qa import answer_question
state = {
    "query": "https://arxiv.org/abs/1706.03762",
    "is_topic_search": False,
    "paper": None,
    "pdf_path": None,
    "full_text": "",
    "chunks": [],
    "vectorstore": None,
    "brief": "",
    "messages": []
}


# --- lang graph pipeline ---
state = graph.invoke(state)
print(state["brief"])

# --- Interactive QA ---
while True:
    question = input("Ask a question or (type 'quit' to exit) : ")

    if question.lower() == "exit":
        break

    reply = answer_question(state , question)

    print("Answer")
    print(reply)