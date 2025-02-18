import random
import time
import gradio as gr


def random_response(message, history):
    print(message)
    __import__("pprint").pprint(history)
    return random.choice(["Yes", "No"])


def agree_disagree(message, history):
    if len([h for h in history if h["role"] == "assistant"]) % 2 == 0:
        return f"Yes, I do think that: {message}"
    else:
        return "No, I do not think that."


def respond_slowly(message, history):
    for i in range(len(message)):
        time.sleep(0.3)
        yield f"You typed: {message[: i + 1]}"


def main():
    gr.ChatInterface(
        fn=respond_slowly,
        type="messages",
        title="The BOT",
        description="Discuss with me, the BOT :D !",
        examples=["Hello", "Am I cool?", "Are tomatoes vegetables?"],
        cache_examples=True,
        theme="ocean",
        chatbot=gr.Chatbot(height=300, type="messages"),
        textbox=gr.Textbox(
            placeholder="Ask me a yes or no question", container=False, scale=7
        ),
    ).launch(debug=True)


if __name__ == "__main__":
    main()
