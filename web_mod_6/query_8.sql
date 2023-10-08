SELECT AVG(grades.grade) as average_grade
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN grades ON subjects.id = grades.subject_id
WHERE teachers.name = :teacher_name;
