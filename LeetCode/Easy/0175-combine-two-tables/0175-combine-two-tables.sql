# Write your MySQL query statement below
SELECT p.firstName, p.lastName, addr.city, addr.state FROM Person as p
LEFT JOIN Address addr
ON p.personId = addr.personId