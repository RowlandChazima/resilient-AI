import math

from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Solve the following maths problems:

    Like :
        "12*15"
        "sqrt(625) +10"

    """

    allowed = {"sqrt": math.sqrt, "pow": pow, "abs": abs, "round": round}

    try:
        result = eval(expression, {"__builtins": {}}, allowed)
        return str(result)

    except Exception as e:
        raise ValueError(f"Calculation failed: {e}")


# Exceptions in code communicate that sth went wrong, allowing the fallback logic to decide to what to do next.
