"""Database layer: yalnız SQL Server ilə əlaqəli əməliyyatlar."""
import pyodbc

import config


def create_connection():
    """SQL Server-ə qoşulma yaradır."""
    connection_string = (
        f"DRIVER={{{config.DB_DRIVER}}};"
        f"SERVER={config.DB_SERVER};"
        f"DATABASE={config.DB_NAME};"
        "TrustServerCertificate=yes;"
    )
    if config.DB_USER:
        connection_string += f"UID={config.DB_USER};PWD={config.DB_PASSWORD};"
    else:
        connection_string += "Trusted_Connection=yes;"
    return pyodbc.connect(connection_string)


def add_student(student_name, student_score):
    """Yeni tələbəni Students cədvəlinə əlavə edir."""
    with create_connection() as connection:
        connection.execute(
            "INSERT INTO Students (Name, Score) VALUES (?, ?)",
            student_name,
            student_score,
        )


def get_students():
    """Bütün tələbələri (name, score) kimi qaytarır."""
    with create_connection() as connection:
        rows = connection.execute("SELECT Name, Score FROM Students ORDER BY Id").fetchall()
    return [(row.Name, row.Score) for row in rows]


def get_student(student_name):
    """Adında axtarılan mətn olan tələbələri qaytarır."""
    with create_connection() as connection:
        rows = connection.execute(
            "SELECT Name, Score FROM Students WHERE Name LIKE ? ORDER BY Id",
            f"%{student_name}%",
        ).fetchall()
    return [(row.Name, row.Score) for row in rows]
