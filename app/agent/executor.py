# the routers job here is like given the decision of the router, execute or evn do the appropriate action/task

from app.llm.groq_client import llm
from app.tools.registry import TOOLS


class Executor:
    def executer(self, decision: str, question: str):

        if decision == "none":
            response = llm.invoke(question)

            return {
                "source": "llm",
                "answer": response.content,
            }

        tool = TOOLS.get(decision)

        if tool is None:
            raise ValueError(f"Unknown tool:{decision}")

        result = tool.invoke(question)

        return {
            "source": decision,
            "answer": result,
        }
