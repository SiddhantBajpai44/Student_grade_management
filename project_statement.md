# Project Specification Statement: Student Grade Management System

## 1. Problem Statement

In many academic settings, instructors, teaching assistants, and course coordinators still struggle with repetitive administrative tasks when tabulating student grades across multiple subjects. Calculating percentage averages, mapping raw scores to standardized 4.0 GPA scales, and ranking students manually is time-consuming and prone to human calculation errors.

While commercial grading tools exist, they are frequently bloated, require subscription plans, demand complex database configurations, or depend on continuous internet access. There is a strong need for a lightweight, self-contained, offline-first Python tool that automates grade conversions, produces class-wide statistics, and persists data reliably without any third-party software dependencies.

---

## 2. Scope of the Project

### In-Scope Capabilities
* **Interactive CLI Interface:** An intuitive terminal menu driving all system functions.
* **Flexible Grade Logging:** Ability to add unlimited subjects per student with numeric scores ranging from 0 to 100.
* **Standardized Grade Mapping:** Automatic conversion of numerical scores to 4.0 GPAs and letter grades (A–F).
* **Statistical Class Analytics:** Calculation of class-wide mean, median, and identification of the top academic performer.
* **Leaderboard & Ranking:** Sorting all enrolled students by GPA and average performance using Timsort algorithms.
* **Persistent Local Storage:** Automatic synchronization of student records to a structured `student_grades.json` file.

### Out-of-Scope (Future Enhancements)
* Multi-user role management and password authentication.
* Graphical User Interface (GUI) or web application frontend.
* Direct export of report cards into PDF or CSV formats.
* Custom credit-weighted GPA calculations per subject.

---

## 3. Target Users

| Target Audience | Primary Need & Benefit |
| :--- | :--- |
| **Professors & TAs** | Need a fast, offline tool to input student marks, view class performance metrics, and determine top performers at the end of a semester. |
| **College Students** | Want a simple program to log subject scores and calculate projected GPAs. |
| **Academic Advisors** | Require class rankings to identify students who excel or those who may need additional academic support. |

---

## 4. High-Level Feature Architecture

The system operates around five core architectural pillars:

1. **Input Validation Module:** Filters user inputs, enforces valid numerical boundaries ($0 \le \text{score} \le 100$), and prevents duplicate student ID creation.
2. **Grade Transformation Engine:** Converts percentage scores into standard letter grades and quality points on a 4.0 GPA scale.
3. **Statistical Processor:** Leverages Python's built-in `statistics` module to derive class averages, median trends, and peak performers.
4. **Ranking & Sorting Engine:** Utilizes Timsort key-based sorting to generate ordered class leaderboards.
5. **Persistence Handler:** Encapsulates JSON serialization and deserialization to preserve data across application sessions.