def calculate_letter_grade_and_gpa(score):
    """Converts a numerical percentage score (0-100) to letter grade and GPA points."""
    if score >= 90:
        return "A", 4.0
    elif score >= 80:
        return "B", 3.0
    elif score >= 70:
        return "C", 2.0
    elif score >= 60:
        return "D", 1.0
    else:
        return "F", 0.0


def calculate_student_stats(subjects):
    """Calculates overall average score, overall GPA, and letter grade across all subjects."""
    if not subjects:
        return 0.0, 0.0, "N/A"

    scores = list(subjects.values())
    avg_score = sum(scores) / len(scores)

    gpa_points = [calculate_letter_grade_and_gpa(s)[1] for s in scores]
    overall_gpa = sum(gpa_points) / len(gpa_points)
    overall_letter, _ = calculate_letter_grade_and_gpa(avg_score)

    return round(avg_score, 2), round(overall_gpa, 2), overall_letter