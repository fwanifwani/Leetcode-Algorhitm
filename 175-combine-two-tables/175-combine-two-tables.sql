/* Write your PL/SQL query statement below */

select p.firstName, p.LastName, a.City, a.State From Person p
left join Address a on a.PersonId = p.PersonId