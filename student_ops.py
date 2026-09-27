from calculations import calculate_letter_grade_and_gpa, calculate_student_stats
from storage import save_data


def add_student(data):
    """Adds a new student and their subject scores."""
    student_id = input("\nEnter Student ID (e.g., ST101): ").strip().upper()
    if student_id in data:
        print("Error: A student with this ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    subjects = {}

    print("\nEnter subject marks (type 'done' when finished):")
    while True:
        subject = input("  Subject name: ").strip().capitalize()
        if subject.lower() == "done":
            if not subjects:
                print("  Please enter at least one subject.")
                continue
            break

        try:
            score = float(input(f"  Enter score for {subject} (0-100): "))
            if 0 <= score <= 100:
                subjects[subject] = score
            else:
                print("  Score must be between 0 and 100.")
        except ValueError:
            print("  Invalid input! Please enter a numerical score.")

    data[student_id] = {"name": name, "subjects": subjects}
    save_data(data)
    print(f"\nStudent '{name}' ({student_id}) successfully added!")


def view_student_report(data):
    """Displays a detailed report card for a single student."""
    student_id = input("\nEnter Student ID: ").strip().upper()
    if student_id not in data:
        print("Error: Student ID not found.")
        return

    student = data[student_id]
    subjects = student["subjects"]
    avg_score, overall_gpa, overall_letter = calculate_student_stats(
        subjects
    )

    print("\n" + "=" * 45)
    print(f" REPORT CARD: {student['name'].upper()} ({student_id})")
    print("=" * 45)
    print(f"{'Subject':<20} | {'Score':<8} | {'Grade':<6} | {'GPA':<4}")
    print("-" * 45)

    for subj, score in subjects.items():
        letter, gpa = calculate_letter_grade_and_gpa(score)
        print(f"{subj:<20} | {score:<8.1f} | {letter:<6} | {gpa:<4.1f}")

    print("-" * 45)
    print(f"Overall Average: {avg_score}%")
    print(f"Overall GPA:     {overall_gpa} / 4.0 ({overall_letter})")
    print("=" * 45)