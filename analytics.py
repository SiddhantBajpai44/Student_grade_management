import statistics
from calculations import calculate_student_stats


def view_class_analytics(data):
    """Uses statistical algorithms to compute class metrics."""
    if not data:
        print("\nNo student records available for analytics.")
        return

    all_averages = []
    top_student = None
    highest_avg = -1

    for sid, info in data.items():
        avg, gpa, _ = calculate_student_stats(info["subjects"])
        all_averages.append(avg)

        if avg > highest_avg:
            highest_avg = avg
            top_student = (info["name"], sid, avg)

    class_mean = round(statistics.mean(all_averages), 2)
    class_median = round(statistics.median(all_averages), 2)

    print("\n" + "=" * 40)
    print("        CLASS ANALYTICS SUMMARY       ")
    print("=" * 40)
    print(f"Total Students:   {len(data)}")
    print(f"Class Mean Avg:   {class_mean}%")
    print(f"Class Median Avg: {class_median}%")
    print(f"Highest Average:  {highest_avg}%")
    if top_student:
        print(
            f"Top Performer:    {top_student[0]} ({top_student[1]}) - {top_student[2]}%"
        )
    print("=" * 40)


def list_ranked_students(data):
    """Ranks and sorts all students by their overall GPA in descending order."""
    if not data:
        print("\nNo student records available.")
        return

    ranked = []
    for sid, info in data.items():
        avg, gpa, letter = calculate_student_stats(info["subjects"])
        ranked.append((gpa, avg, info["name"], sid, letter))

    # Sort descending by GPA, then by average score
    ranked.sort(reverse=True, key=lambda x: (x[0], x[1]))

    print("\n" + "=" * 55)
    print(f"{'Rank':<5} | {'ID':<8} | {'Name':<20} | {'GPA':<5} | {'Avg %':<6}")
    print("=" * 55)

    for rank, (gpa, avg, name, sid, letter) in enumerate(ranked, start=1):
        print(f"{rank:<5} | {sid:<8} | {name:<20} | {gpa:<5.2f} | {avg:<6.1f}%")

    print("=" * 55)