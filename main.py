from app.agent.agent import Agent

agent = Agent()

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    response = agent.run(question)

    print(f"\nSource : {response['source']}")
    print(f"Answer : {response['answer']}")
