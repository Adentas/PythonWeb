SELECT students.name, grades.grade
FROM students
JOIN groups ON students.group_id = groups.id
JOIN grades ON students.id = grades.student_id
JOIN subjects ON subjects.id = grades.subject_id
WHERE groups.name = :group_name AND subjects.name = :subject_name
ORDER BY grades.date DESC
LIMIT 1;
