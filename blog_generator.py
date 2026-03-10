from utils.ai_client import generate

def generate_blog(topic, tone):

    prompt = f"Write a {tone} blog about {topic}"

    return generate(prompt)