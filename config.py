"""Application configuration. Values can be overridden with environment variables."""
import os

DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
DB_SERVER = os.getenv("DB_SERVER", "localhost")
DB_NAME = os.getenv("DB_NAME", "UniversityDB")
DB_USER = os.getenv("DB_USER", "")          # boşdursa Windows Authentication
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

MIN_SCORE = 0
MAX_SCORE = 100

# Grade hədləri (magic number-lər əvəzinə adlandırılmış sabitlər)
GRADE_A_MIN_SCORE = 90
GRADE_B_MIN_SCORE = 80
GRADE_C_MIN_SCORE = 70
GRADE_D_MIN_SCORE = 60
