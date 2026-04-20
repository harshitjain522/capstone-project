from ecommerce_assistant.graph import app

thread_id = "user_1"

while True:
    q = input("You: ")

    result = app.invoke(
        {"question": q},
        config={"configurable": {"thread_id": thread_id}}
    )

    print("Bot:", result["answer"])