from gptagent import GPTAgent

def get_chapter_outline_prompt(novel_description):
    prompt = novel_description
    prompt += "\n Write a list of chapters for the above novel."
    prompt += "For each chapter include a description of events in the chapter (and associated detailed writers notes)"
    return prompt

def get_chapter_outline(novel_description, genre):
    prompt = get_chapter_outline_prompt(novel_description)
    agent = GPTAgent(f"You are a master {genre} writer.")
    return agent.get_completion(prompt)
    
