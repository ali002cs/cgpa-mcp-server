"""Plain Python CGPA tools. No LangChain, no MCP in here - just functions.
(Replace / extend with the tools from your own Assignment 2.)"""

CREDIT_HOURS = {1: 17.0, 2: 18.0, 3: 18.0, 4: 18.0, 5: 18.0, 6: 19.0, 7: 16.0, 8: 15.0}


def get_credit_hours(semesters: list[int]) -> float:
    """Return the total credit hours for the given semester numbers, e.g. [5, 6]."""
    return sum(CREDIT_HOURS.get(s, 0) for s in semesters)


def marks_to_grade_points(marks: int) -> float:
    """Convert an exam mark (0-100) to a grade point on the 4.0 scale."""
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    if marks >= 85: return 4.0
    if marks >= 80: return 3.7
    if marks >= 75: return 3.3
    if marks >= 70: return 3.0
    if marks >= 65: return 2.7
    if marks >= 60: return 2.3
    if marks >= 55: return 2.0
    if marks >= 50: return 1.0
    return 0.0


def calculate_cgpa(grade_points: list[float], credit_hours: list[float]) -> float:
    """Weighted CGPA: sum(grade_point * credit_hours) / sum(credit_hours).
    The two lists must have the same length (one entry per course)."""
    if len(grade_points) != len(credit_hours):
        raise ValueError("grade_points and credit_hours must have the same length.")
    total = sum(credit_hours)
    if total == 0:
        raise ValueError("Total credit hours cannot be zero.")
    return round(sum(g * c for g, c in zip(grade_points, credit_hours)) / total, 2)


def required_gpa_for_target(current_cgpa: float, completed_credit_hours: float,
                            target_cgpa: float, upcoming_credit_hours: float) -> float:
    """GPA needed in the upcoming semester(s) to reach target_cgpa.
    A result above 4.0 means the target is not reachable in that time."""
    if upcoming_credit_hours <= 0:
        raise ValueError("upcoming_credit_hours must be positive.")
    needed = (target_cgpa * (completed_credit_hours + upcoming_credit_hours)
              - current_cgpa * completed_credit_hours) / upcoming_credit_hours
    return round(needed, 2)
