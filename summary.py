from gptagent import GPTAgent

def get_summary_prompt(novel_description):
    return f"Write a summary of {novel_description}. Include key details"

def get_summary(novel_description, genre):
    prompt = get_summary_prompt(novel_description)
    agent = GPTAgent(f"You are a master {genre} writer.")
    return agent.get_completion(prompt)