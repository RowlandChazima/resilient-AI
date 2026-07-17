# the orchestrator our supervisor ......:))

from app.agent.executor import Executor
from app.agent.router import router_chain


class Agent:
    def __init__(self):
        self.executor = Executor()

    def run(self, question: str):

        decision = router_chain.invoke({"question": question}).strip().lower()

        return self.executor.execute(  # type: ignore[attr-defined]
            decision,
            question,
        )


# the pipeline is like receive the question ask the router, get the decision,send it to the executor and return the answer
