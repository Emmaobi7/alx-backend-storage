-- no table for a meeting

-- create view based on conditions
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80 AND (last_meeting is NULL OR last_meeting < NOW() - INTERVAL 1 MONTH);
