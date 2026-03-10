def create_caption_prompt(topic,tone):

    return f"""
    Write an engaging Instagram caption about {topic}.
    Tone: {tone}
    Add hashtags.
    """