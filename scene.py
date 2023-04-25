from gptagent import GPTAgent

def get_scene_prompt(summary, to_write):
    prompt = "Following is a description of the novel you are working on: \n"
    prompt += summary + "\n"
    prompt += "Please write the following section. Respond only with text appropriate for a masterpiece novel.\n"
    prompt += "Section:\n"
    prompt += to_write
    return prompt

def get_scene(summary, to_write, genre):
    prompt = get_scene_prompt(summary, to_write)
    agent = GPTAgent(f"You are a master {genre} writer.")
    return agent.get_completion(prompt)
    
