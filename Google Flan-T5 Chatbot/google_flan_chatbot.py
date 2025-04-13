from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import gradio as gr

class Chatbot:
    def __init__(self, model_name="google/flan-t5-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def chat(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, padding=True)
        outputs = self.model.generate(**inputs, max_length=200, num_beams=5, early_stopping=True)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

chatbot = Chatbot()

def chat_with_history(message, history):
    max_tokens = 400  # Leave space for response generation
    conversation = ""
    token_count = 0

    # Build conversation from latest to oldest until token budget is met
    for user_msg, bot_msg in reversed(history):
        entry = f"User: {user_msg}\nBot: {bot_msg}\n"
        entry_tokens = len(chatbot.tokenizer.encode(entry, add_special_tokens=False))
        if token_count + entry_tokens > max_tokens:
            break
        conversation = entry + conversation
        token_count += entry_tokens

    # Add current message
    new_entry = f"User: {message}\nBot:"
    conversation += new_entry

    response = chatbot.chat(conversation)
    response = response.split("User:")[0].split("Bot:")[0].strip()
    return response


gr.ChatInterface(
    fn=chat_with_history,
    title="Flan-T5 Chatbot",
    description="Chatbot powered by Google Flan-T5. Press Ctrl+C in your terminal to exit the chatbot."
).launch(server_name="0.0.0.0", server_port=7860, share=False)