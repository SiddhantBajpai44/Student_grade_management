# Student Grade Management System

A lightweight, modular, zero-dependency Python CLI application designed to manage student records, compute GPAs and letter grades, compile class-wide statistical analytics, and generate ranked leaderboards.

---

## Overview

The **Student Grade Management System** simplifies academic performance tracking without requiring complex database setups or external packages. Built strictly using Python's standard library, it offers persistent JSON data storage, robust input validation, and statistical reporting—making it a portable, reliable tool for educators, teaching assistants, and students.

---

## Key Features

* **Grade & GPA Calculation:** Converts percentage scores (0–100) into standard letter grades (A–F) and 4.0 scale GPAs.
* **Multi-Subject Reporting:** Generates individualized report cards showing subject-by-subject scores, overall letter grades, and average GPAs.
* **Class Analytics:** Computes key aggregate metrics including class mean average, median average, and top academic performers.
* **Ranked Leaderboard:** Automatically sorts and ranks enrolled students by GPA and average percentage performance.
* **Persistent Data Storage:** Saves student records locally to `student_grades.json` so data remains saved across application restarts.
* **Zero External Dependencies:** Operates out of the box on any platform with standard Python installed.

---

## Technologies & Tools Used

* **Language:** Python 3.8+
* **Built-in Standard Library Modules:**
  * `json` – Structured file read/write operations for data persistence.
  * `os` – Path checking and environment handling.
  * `statistics` – Computation of class mean and median values.
* **Architecture:** Clean modular 5-file design (`main.py`, `student_ops.py`, `calculations.py`, `analytics.py`, `storage.py`).

---

## Project Structure

```text
student_grade_system/
├── main.py          # Main entry point and interactive CLI menu
├── student_ops.py   # Record entry and student report card display
├── calculations.py  # GPA, letter grade, and score average formulas
├── analytics.py     # Class statistics and ranking algorithms
└── storage.py       # JSON file reading and writing routines
```

---

## Installation & Running

Since this project relies exclusively on the Python standard library, no `pip install` commands or virtual environments are needed.

### Steps to Run:

1. **Clone or Download** all 5 project files into a single directory:
   ```bash
   git clone https://github.com/SiddhantBajpai44/Student_grade_management
   cd Student_grade_system
   ```

2. **Verify Python Installation** (Python 3.8 or higher is recommended):
   ```bash
   python3 --version
   ```

3. **Run the Application:**
   ```bash
   python3 main.py
   ```

---

## Instructions for Testing

Follow this step-by-step test plan to verify system functionality:

1. **Record Entry & Persistence Test:**
   * Select Option `1` from the main menu.
   * Enter a Student ID (e.g., `ST101`) and name.
   * Enter scores for 2–3 subjects and type `done` when finished.
   * Exit the application using Option `5`. Verify that `student_grades.json` was automatically created in your project folder.

2. **Input Validation Check:**
   * Select Option `1` again to add another student.
   * Try entering non-numeric characters (e.g., `abc`) or scores outside the valid range (e.g., `150`).
   * Confirm that the system gracefully handles the error and prompts for valid input without crashing.

3. **Report Card & Analytics Verification:**
   * Select Option `2` and enter `ST101` to view the formatted report card.
   * Select Option `3` to inspect overall class analytics (Mean, Median, Top Performer).
   * Select Option `4` to view the ranked student leaderboard.

---

## Terminal Interface Preview

```text
=== STUDENT GRADE MANAGEMENT SYSTEM ===
1. Add New Student & Grades
2. View Student Report Card
3. View Class Analytics & Summary
4. Rank Students (Leaderboard)
5. Exit
Select an option (1-5): 2

Enter Student ID: ST101

=============================================
 REPORT CARD: ALEX JOHNSON (ST101)
=============================================
Subject              | Score    | Grade  | GPA 
---------------------------------------------
Mathematics          | 92.0     | A      | 4.0 
Computer Science     | 88.0     | B      | 3.0 
Physics              | 79.5     | C      | 2.0 
---------------------------------------------
Overall Average: 86.5%
Overall GPA:     3.0 / 4.0 (B)
=============================================
```
