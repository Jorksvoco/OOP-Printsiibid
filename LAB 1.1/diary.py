class Diary:
    def __init__(self):
        self.entries = []

    def add_entry(self, text):
        self.entries.append(text)

    def remove_entry(self, index):
        del self.entries[index]

    def __str__(self):
        return "\n".join(
            f"{i+1}. {entry}" 
            for i, entry in enumerate(self.entries)
        )