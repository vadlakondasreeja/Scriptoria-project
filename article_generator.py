from utils.ai_client import generate
from prompts.article_prompt import create_article_prompt

def generate_article(topic,tone):

    prompt=create_article_prompt(topic,tone)

    return generate(prompt)


