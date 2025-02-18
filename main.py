import random
import gradio as gr


def random_response(message, history):
    return random.choice(["Yes", "No"])


def main():
    gr.ChatInterface(fn=random_response, type="messages").launch(debug=True)


if __name__ == "__main__":
    main()
