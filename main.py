import random
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


def main():
    gr.ChatInterface(fn=agree_disagree, type="messages").launch(debug=True)


if __name__ == "__main__":
    main()
