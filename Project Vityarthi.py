class StudyHabitTracker:
    def __init__(self):
        self.study_data = {}  # store hours by subject

    def add_subject(self, subject):
        if subject in self.study_data:
            print(f"'{subject}' already exists.")
        else:
            self.study_data[subject] = 0
            print(f"Subject '{subject}' added successfully!")

    def log_study_time(self, subject, hours):
        if subject not in self.study_data:
            print(f"Subject '{subject}' not found. Add it first!")
        else:
            self.study_data[subject] += hours
            print(f"Logged {hours} hour(s) for {subject}.")

    def show_summary(self):
        print("\n----- STUDY SUMMARY -----")
        if not self.study_data:
            print("No data available.")
            return

        total = 0
        for subject, hrs in self.study_data.items():
            print(f"{subject}: {hrs} hour(s)")
            total += hrs

        print(f"\nTotal Study Time: {total} hour(s)")

        # Motivation
        if total >= 10:
            print("🔥 Excellent dedication! Keep going!")
        elif total >= 5:
            print("💪 Good job! Aim higher next week!")
        else:
            print("🙂 A good start. Try to study a bit more!")


def menu():
    tracker = StudyHabitTracker()

    while True:
        print("\n========== Study Habit Tracker ==========")
        print("1. Add Subject")
        print("2. Log Study Time")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            subject = input("Enter subject name: ")
            tracker.add_subject(subject)

        elif choice == "2":
            subject = input("Enter subject: ")
            try:
                hours = float(input("Enter hours studied: "))
                tracker.log_study_time(subject, hours)
            except ValueError:
                print("Please enter a valid number of hours.")

        elif choice == "3":
            tracker.show_summary()

        elif choice == "4":
            print("Exiting... Goodbye! 👋")
            break

        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    menu()
