import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

class GPTAgent():
    def __init__(self, prompt):
        self.system_content = prompt
        
    def create_messages(self, prompt):
        return [
            {"role": "system", "content": self.system_content},
            {"role": "user", "content": prompt},
        ]
    def get_completion(self, prompt):
        messages = self.create_messages(prompt)
        return openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages).choices[0].message.content
