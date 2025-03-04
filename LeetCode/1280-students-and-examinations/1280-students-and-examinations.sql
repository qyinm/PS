select s.student_id, s.student_name, s.subject_name, if(ISNULL(e.subject_name), 0, count(*)) as attended_exams
from (select * from students cross join subjects) as s
left outer join examinations as e
on s.student_id = e.student_id and s.subject_name = e.subject_name
group by s.student_id, s.subject_name
order by s.student_id asc, s.subject_name

-- select * from students cross join subjects