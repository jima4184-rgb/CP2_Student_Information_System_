import tkinter as tk
from tkinter import messagebox

from student_data import load_students
from student_gui import (
    open_add_student,
    open_view_students,
    open_search_student,
    open_delete_student,
    open_update_student,
)
from auth_gui import open_login, open_register

LIGHTBLUE = "#B0E2FF" 
LIGHTPINK = "#FFAEB9"

current_user = {"username": None, "role": None}

