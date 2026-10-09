"""Business logic layer: verilənlər bazasından və UI-dan asılı deyil."""
import config


def calculate_grade(score):
    """Balı hərf qiymətinə çevirir (91 -> A, 85 -> B, 72 -> C, 63 -> D, 48 -> F)."""
    if score >= config.GRADE_A_MIN_SCORE:
        return "A"
    if score >= config.GRADE_B_MIN_SCORE:
        return "B"
    if score >= config.GRADE_C_MIN_SCORE:
        return "C"
    if score >= config.GRADE_D_MIN_SCORE:
        return "D"
    return "F"


def calculate_statistics(scores):
    """Bal siyahısı üzrə ümumi statistikanı qaytarır."""
    if not scores:
        return {"total": 0, "average": 0.0, "highest": 0, "lowest": 0}
    return {
        "total": len(scores),
        "average": round(sum(scores) / len(scores), 1),
        "highest": max(scores),
        "lowest": min(scores),
    }


def is_valid_score(score):
    return config.MIN_SCORE <= score <= config.MAX_SCORE
