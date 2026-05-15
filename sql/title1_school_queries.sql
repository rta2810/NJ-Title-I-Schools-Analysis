-- County Ranking Query
SELECT
    county,
    SUM(grade_5_8_total) AS total_students
FROM merged_schools
WHERE title1 = 'YES'
GROUP BY county
ORDER BY total_students DESC;

-- School Ranking Query
SELECT
    district,
    school_name,
    grade_5_8_total
FROM merged_schools
WHERE title1 = 'YES'
ORDER BY district, grade_5_8_total DESC;
