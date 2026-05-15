# NJ-Title-I-Schools-Analysis
Analysis of New Jersey Title I schools using Python, MySQL, and Google Looker Studio to identify county-level and school-level grades 5–8 enrollment patterns.
# NJ Title I Schools Analysis

## Overview

This project analyzes New Jersey Title I schools using multiple public datasets.

The project combines:

- New Jersey School Directory data
- Title I allocation data
- 2024/2025 enrollment data

The purpose of the analysis is to:

1. Rank New Jersey counties by grades 5–8 enrollment in Title I schools
2. Rank schools within Title I districts by grades 5–8 enrollment

---

## Tools Used

- Python
- pandas
- pdfplumber
- MySQL
- Google Looker Studio

---

## Workflow

1. Extracted Title I data from PDF format
2. Cleaned and standardized school names
3. Merged enrollment, Title I, and directory datasets
4. Calculated grades 5–8 enrollment totals
5. Queried results using MySQL
6. Built visualizations in Looker Studio

---

## Project Structure

```text
NJ-Title-I-Schools-Analysis/
│
├── data/
├── scripts/
├── sql/
├── outputs/
├── visuals/
└── README.md
```

---

## Key Findings

- Ocean County had the highest estimated grades 5–8 enrollment among Title I schools.
- Middlesex and Atlantic Counties also showed large concentrations of Title I middle-school enrollment.
- Enrollment distribution varied significantly across schools within districts.

---

## Example SQL Query

```sql
SELECT
    county,
    SUM(grade_5_8_total) AS total_students
FROM merged_schools
WHERE title1 = 'YES'
GROUP BY county
ORDER BY total_students DESC;
```

---

## Dashboard

(Add your Google Looker Studio dashboard link here)
