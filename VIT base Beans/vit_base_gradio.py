import tensorflow as tf
from transformers import AutoFeatureExtractor, TFAutoModelForImageClassification
from PIL import Image
import numpy as np
import gradio as gr

# Load a lightweight ViT model (fine-tuned on beans dataset)
model_name = "nateraw/vit-base-beans"
extractor = AutoFeatureExtractor.from_pretrained(model_name)
model = TFAutoModelForImageClassification.from_pretrained(model_name, from_pt=True)

# Inference function
def classify_image(image):
    # Resize and format image
    inputs = extractor(images=image, return_tensors="tf")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = tf.argmax(logits, axis=-1).numpy()[0]
    label = model.config.id2label[predicted_class]
    return label

# Gradio interface
gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs="label",
    title="TF ViT Image Classifier",
    description="Classifies beans using a TensorFlow Vision Transformer model"
).launch()