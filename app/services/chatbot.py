from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from app.services.gemini import ask_gemini
from app.services.vector_db import search_vector_db


class ChatState(TypedDict):
    message: str
    response: str


def chatbot_node(state: ChatState):

    # Search relevant information from ChromaDB
    search_result = search_vector_db(state["message"])

    documents = search_result.get("documents", [[]])[0]
    metadatas = search_result.get("metadatas", [[]])[0]

    # Prepare information for Gemini
    student_info = []

    for document, metadata in zip(documents, metadatas):
        student_info.append({
            "information": document,
            "student_id": metadata.get("student_id"),
            "name": metadata.get("name"),
            "course": metadata.get("course"),
            "year": metadata.get("year"),
        })

    prompt = f"""
You are a student database assistant.

Use the following information retrieved from the student database
to answer the user's question.

Retrieved student information:
{student_info}

User question:
{state["message"]}

Answer clearly and briefly.
Do not invent student information.
"""

    response = ask_gemini(prompt)

    return {
        "response": response
    }


graph = StateGraph(ChatState)

graph.add_node("chatbot", chatbot_node)

graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", END)

chatbot = graph.compile()