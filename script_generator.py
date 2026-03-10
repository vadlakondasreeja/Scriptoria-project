from utils.ai_client import generate
from prompts.script_prompt import create_script_prompt

def generate_script(topic,tone):

    prompt=create_script_prompt(topic,tone)

    return generate(prompt)