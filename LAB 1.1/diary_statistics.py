class DiaryStatistics:
    @staticmethod
    def print_statistics(diary):
        count = len(diary.entries)
        if count == 0:
            print("Sissekandeid pole.")
            return
        avg_len = sum(len(e) for e in diary.entries) / count
        print(f"Sissekandeid: {count}")
        print(f"Keskmine pikkus: {avg_len:.1f} tähemärki")