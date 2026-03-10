from utils.ai_client import generate
from prompts.caption_prompt import create_caption_prompt

def generate_caption(topic,tone):

    prompt=create_caption_prompt(topic,tone)

    return generate(prompt)