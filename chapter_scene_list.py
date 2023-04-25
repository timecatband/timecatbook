from gptagent import GPTAgent

def get_scene_prompt(chapter_outline, to_write):
    prompt = "The following is an outline for a novel: \n"
    prompt += chapter_outline + "\n"
    prompt += "Please write a detailed list of scenes for the following section (include writers notes)."
    prompt += " Begin each scene with a line of the form 'Scene: description'. Section:\n"
    prompt += to_write
    return prompt

def get_chapter_scene_list(chapter_outline, to_write, genre):
    prompt = get_scene_prompt(chapter_outline, to_write)
    agent = GPTAgent(f"You are a master {genre} writer.")
    return agent.get_completion(prompt)