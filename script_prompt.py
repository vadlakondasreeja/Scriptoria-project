def create_script_prompt(topic,tone):

    return f"""
    Write a YouTube video script about {topic}.
    Tone: {tone}
    Include introduction, body and conclusion.
    """