from analytics import list_ranked_students, view_class_analytics
from storage import load_data, save_data
from student_ops import add_student, view_student_report


def main():
    data = load_data()

    while True:
        print("\n=== STUDENT GRADE MANAGEMENT SYSTEM ===")
        print("1. Add New Student & Grades")
        print("2. View Student Report Card")
        print("3. View Class Analytics & Summary")
        print("4. Rank Students (Leaderboard)")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_student_report(data)
        elif choice == "3":
            view_class_analytics(data)
        elif choice == "4":
            list_ranked_students(data)
        elif choice == "5":
            print("\nSaving data and exiting. Goodbye!")
            save_data(data)
            break
        else:
            print("Invalid selection. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()