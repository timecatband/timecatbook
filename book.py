import os
from gptagent import GPTAgent
from summary import get_summary
from chapter_outline import get_chapter_outline
from chapter_scene_list import get_chapter_scene_list
from chapter_outline import get_chapter_outline
from scene import get_scene

def make_agent(instructions):
    return GPTAgent(instructions)

class Book():
    def __init__(self, book_dir, description, genre):
        self.book_dir = book_dir
        self.summary = None
        self.chapter_outline = None
        # Create bookdir if it doesn't exist
        if not os.path.exists(book_dir):
            os.makedirs(book_dir)
        else:
            # Load summary and chapter outline
            self.load_summary()
            self.load_chapter_outline()
        self.description = description
        self.genre = genre

    def load_summary(self):
        if not os.path.exists(os.path.join(self.book_dir, "summary.txt")):
            return
        with open(os.path.join(self.book_dir, "summary.txt"), "r") as f:
            self.summary = f.read()
    def load_chapter_outline(self):
        if not os.path.exists(os.path.join(self.book_dir, "chapter_outline.txt")):
            return
        with open(os.path.join(self.book_dir, "chapter_outline.txt"), "r") as f:
            self.chapter_outline = f.read()
    def save_summary(self):
        with open(os.path.join(self.book_dir, "summary.txt"), "w") as f:
            f.write(self.summary)
    def save_chapter_outline(self):
        with open(os.path.join(self.book_dir, "chapter_outline.txt"), "w") as f:
            f.write(self.chapter_outline)
    
    def ensure_summary(self):
        if (self.summary is None):
            print("Generating summary...")
            self.summary = get_summary(self.description, self.genre)
            self.save_summary()
        else:
            print("Summary already exists. Skipping...")   
    def ensure_chapter_outline(self):
        if (self.chapter_outline is None):
            self.chapter_outline = get_chapter_outline(self.summary, self.genre)
            self.save_chapter_outline()
        else:
            print("Chapter outline already exists. Skipping...")
    
    def parse_chapter_outline(self):
        split_chapters = self.chapter_outline.split("Chapter")
        split_chapters = [chapter for chapter in split_chapters if chapter != ""]
        parsed_chapters = []
        for i, chapter in enumerate(split_chapters):
            split = chapter.split("\n")
            chapter_name = split[0]
            chapter_description = "\n".join(split[1:])
            parsed_chapters.append({
                "name": "Chapter " + chapter_name,
                "description": chapter_description,
                "number": i
            })
        self.parsed_chapters = parsed_chapters
        
    def ensure_chapter_scene_list(self, chapter):
        chapter_file = os.path.join(self.book_dir, f"chapteroutline_{chapter['number']}.txt")
        if os.path.exists(chapter_file):
            with open(chapter_file, "r") as f:
                chapter_scene_list = f.read()
                self.chapter_scene_list.append(chapter_scene_list)
        else:
            chapter_scene_list = get_chapter_scene_list(self.chapter_outline, chapter["description"], self.genre)
            with open(chapter_file, "w") as f:
                f.write(chapter_scene_list)
            self.chapter_scene_list.append(chapter_scene_list)
    def parse_chapter_scene_list(self, list):
        split_scenes = list.split("Scene")
        split_scenes = [scene for scene in split_scenes if scene != ""]
        parsed_scenes = []
        for i, scene in enumerate(split_scenes):
            split = scene.split("\n")
            scene_name = split[0]
            scene_description = "\n".join(split[1:])
            parsed_scenes.append({
                "name": "Scene " + scene_name,
                "description": scene_description,
                "number": i
            })
        return parsed_scenes
    
    def ensure_chapter_text(self, chapter):
        print("Working on chapter text: " + chapter["name"] + "...")
        chapter_file = os.path.join(self.book_dir, f"chapter_{chapter['number']}.txt")
        if os.path.exists(chapter_file):
            with open(chapter_file, "r") as f:
                chapter_text = f.read()
                self.chapter_text.append(chapter_text)
            return
        chapter_text = ""
        for scene in self.parsed_chapter_scene_lists[chapter["number"]]:
            print("Writing scene: " + scene["name"] + "...")
            scene_text = get_scene(self.summary, scene["description"], self.genre)
            chapter_text += scene_text
        with open(chapter_file, "w") as f:
            f.write(chapter_text)
        self.chapter_text.append(chapter_text)
    
    def generate_book(self):
        print(f"Generating {self.genre} book...{self.description}")
        self.ensure_summary()
        self.ensure_chapter_outline()
        self.parse_chapter_outline()
        self.chapter_scene_list = []
        self.parsed_chapter_scene_lists = []
        for chapter in self.parsed_chapters:
            self.ensure_chapter_scene_list(chapter)
            scene_list = self.chapter_scene_list[chapter["number"]]
            self.parsed_chapter_scene_lists.append(self.parse_chapter_scene_list(scene_list))
        for chapter in self.parsed_chapters:
            self.ensure_chapter_text(chapter)
        self.book_text = "\n"
        for chapter in self.parsed_chapters:
            self.book_text += chapter["name"] + "\n"
            self.book_text += self.chapter_text[chapter["number"]]
        return self.book_text
        