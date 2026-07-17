from langchain_core.tools import tool

KNOWLEDGE_MINI_BASE = {
    "kenya": (
        "Kenya is a country in East Africa.The capital city of Kenya is Nairobi."
    ),
    "python": (
        "Python is one of the high-level programming languages."
        "Was created by Guido Rossum."
    ),
    "groq": ("Groq offers an infrastructure for fast inference LLM's"),
    "langchain": (
        "Langchain is a fast pre-built framework for building"
        "LLM/ai-powered applications"
    ),
}


@tool
def search(query: str) -> str:
    """
    Search for general info.

    Raise or make an exception if no information is found.

    """

    query = query.lower().strip()

    if query == "404 Test":
        raise TimeoutError("Simulated search timeout.")

    if query in KNOWLEDGE_MINI_BASE:
        return KNOWLEDGE_MINI_BASE[query]

    raise LookupError("No search results found.")
