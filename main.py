from app.agent.router import router_chain

questions = [
    "Evaluate 12*15?",
    "Tell me more about Kenya as a country",
    "Who are you?",
]

for question in questions:
    decision = router_chain.invoke({"question": question})

    print(f"Question:{question}")
    print(f"Decision:{decision}")
    print("-" * 40)
