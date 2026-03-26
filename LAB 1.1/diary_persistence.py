from diary import Diary

class DiaryPersistence:
    @staticmethod
    def save_to_file(diary, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for entry in diary.entries:
                f.write(entry + "\n")

    @staticmethod
    def load_from_file(filename):
        diary = Diary()
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    diary.add_entry(line)
        return diary