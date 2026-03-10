def create_article_prompt(topic,tone):

    return f"""
    Write a professional article about {topic}.
    Tone: {tone}.
    """