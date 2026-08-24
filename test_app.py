import pytest

from app import (
    calculate_total,
    calculate_percentage,
    calculate_grade,
    get_result,
    get_performance_message,
    analyze_student,
)


def test_calculate_total():
    marks = [80, 70, 90]
    assert calculate_total(marks) == 240


def test_calculate_percentage():
    marks = [80, 70, 90]
    assert calculate_percentage(marks) == 80.0


def test_grade_a_plus():
    assert calculate_grade(95) == "A+"


def test_grade_a():
    assert calculate_grade(85) == "A"


def test_grade_b():
    assert calculate_grade(75) == "B"


def test_grade_c():
    assert calculate_grade(65) == "C"


def test_grade_d():
    assert calculate_grade(55) == "D"


def test_grade_e():
    assert calculate_grade(45) == "E"


def test_grade_f():
    assert calculate_grade(35) == "F"


def test_student_pass():
    marks = [80, 75, 90, 85]
    assert get_result(marks) == "PASS"


def test_student_fail():
    marks = [80, 35, 90, 85]
    assert get_result(marks) == "FAIL"


def test_performance_message_excellent():
    assert get_performance_message(95) == "Excellent performance!"


def test_performance_message_good():
    assert get_performance_message(65) == "Good performance."


def test_performance_message_poor():
    assert get_performance_message(30) == "Poor performance."


def test_analyze_student():
    marks = [80, 90, 70, 60, 100]

    result = analyze_student(marks)

    assert result["total"] == 400
    assert result["percentage"] == 80.0
    assert result["grade"] == "A"
    assert result["result"] == "PASS"


def test_empty_marks():
    with pytest.raises(ValueError):
        analyze_student([])


def test_invalid_marks():
    with pytest.raises(ValueError):
        calculate_percentage([80, 110, 70])


def test_negative_marks():
    with pytest.raises(ValueError):
        calculate_percentage([80, -10, 70])