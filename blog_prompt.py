def create_blog_prompt(topic,tone):

    return f"""
    Write a detailed blog post about {topic}.
    Tone should be {tone}.
    Include headings and subheadings.
    """