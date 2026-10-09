"""Streamlit UI layer."""
import streamlit as st

import config
import database
import services


def build_student_rows(students):
    return [
        {"Name": name, "Score": score, "Grade": services.calculate_grade(score)}
        for name, score in students
    ]


def show_add_student_form():
    st.subheader("Add Student")
    student_name = st.text_input("Student Name")
    student_score = st.number_input(
        "Score", min_value=config.MIN_SCORE, max_value=config.MAX_SCORE, step=1
    )
    if st.button("Add Student"):
        if not student_name.strip():
            st.error("Student name boş ola bilməz.")
            return
        database.add_student(student_name.strip(), int(student_score))
        st.success(f"{student_name} əlavə olundu.")


def show_statistics(students):
    stats = services.calculate_statistics([score for _, score in students])
    columns = st.columns(4)
    columns[0].metric("Total Students", stats["total"])
    columns[1].metric("Average Score", stats["average"])
    columns[2].metric("Highest Score", stats["highest"])
    columns[3].metric("Lowest Score", stats["lowest"])


def show_student_list(students):
    st.subheader("Students")
    search_text = st.text_input("Search Student")
    visible_students = database.get_student(search_text) if search_text else students
    st.dataframe(build_student_rows(visible_students), use_container_width=True)


def main():
    st.title("Student Performance Dashboard")
    show_add_student_form()
    students = database.get_students()
    show_statistics(students)
    show_student_list(students)


main()
