from langchain_core.output_parsers import StrOutputParser

from app.llm.groq_client import llm
from app.prompts.router_prompt import router_prompt

router_chain = router_prompt | llm | StrOutputParser()
