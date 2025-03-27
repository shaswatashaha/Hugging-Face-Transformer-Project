# app.py
from transformers import pipeline
import gradio as gr


print('Gradio Version: ', gr.__version__)


# Load sentiment-analysis model
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Function to predict sentiment
def analyze_sentiment(text):
    results = classifier(text)
    label = results[0]['label']
    score = round(results[0]['score'], 3)
    
    color = "MediumSeaGreen" if label == "POSITIVE" else "red"
    emoji = "😊" if label == "POSITIVE" else "😞"
    return f"""
    <div style="border:2px solid #ddd; padding: 20px; border-radius:10px; background:#f9f9f9;">
        <h3 style="color: black"; font-size:16px;> Sentiment: <b style='color:{color};'>{label}</b> {emoji}</h3>
        <h3 style="color: black"; style="font-size:16px;">Confidence: <b style='color:{color}'>{score}%</b></h3>
    </div>
    """


custom_theme = gr.themes.Base(
    primary_hue="blue",
    neutral_hue="gray"
).set(
    body_background_fill="#ffffff",     # White background
    body_text_color="DodgerBlue",          
    button_primary_background_fill="#2d89ef",  # Blue button
    button_primary_text_color="#ffffff",       # White button text
)



# Gradio UI
interface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=4, placeholder="Enter text here..."),
    outputs=gr.HTML(),
    title="Hugging Face Sentiment Analyzer",
    description=" Built with Transformers and Gradio ",
    theme= custom_theme,
    allow_flagging= 'never', 
    
)

interface.launch()