def calculate_total(marks):
    """Calculate total marks."""
    return sum(marks)


def calculate_percentage(marks):
    """Calculate percentage from subject marks."""
    if not marks:
        raise ValueError("Marks cannot be empty.")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Each mark must be between 0 and 100.")

    return (sum(marks) / (len(marks) * 100)) * 100


def calculate_grade(percentage):
    """Calculate grade based on percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def get_result(marks):
    """Determine whether the student passed or failed."""
    if any(mark < 40 for mark in marks):
        return "FAIL"

    return "PASS"


def get_performance_message(percentage):
    """Return a performance message."""
    if percentage >= 90:
        return "Excellent performance!"
    elif percentage >= 75:
        return "Very good performance!"
    elif percentage >= 60:
        return "Good performance."
    elif percentage >= 40:
        return "Needs improvement."
    else:
        return "Poor performance."


def analyze_student(marks):
    """Generate complete student performance analysis."""

    if not marks:
        raise ValueError("Marks cannot be empty.")

    percentage = calculate_percentage(marks)

    return {
        "total": calculate_total(marks),
        "percentage": percentage,
        "grade": calculate_grade(percentage),
        "result": get_result(marks),
        "message": get_performance_message(percentage),
    }


def main():
    marks = [85, 78, 92, 88, 76]

    result = analyze_student(marks)

    print("Student Performance")
    print("--------------------")
    print(f"Marks      : {marks}")
    print(f"Total      : {result['total']}")
    print(f"Percentage : {result['percentage']:.2f}%")
    print(f"Grade      : {result['grade']}")
    print(f"Result     : {result['result']}")
    print(f"Message    : {result['message']}")


if __name__ == "__main__":
    main()