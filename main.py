import random
import time
import gradio as gr


def random_response(message, history):
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


def give_options(message, history):
    yield gr.ChatMessage(
        content=f"You typed: {message}. Are you satisfied ?",
        options=[{"value": "1", "label": "Yes"}, {"value": "0", "label": "No"}],
    )


def main():
    io = gr.ChatInterface(
        fn=give_options,
        type="messages",
        title="The BOT",
        description="Discuss with me, the BOT :D !",
        examples=["Hello", "Am I cool?", "Are tomatoes vegetables?"],
        cache_examples=False,
        theme="ocean",
        api_name=False,
    )
    io.launch(debug=True)


if __name__ == "__main__":
    main()
