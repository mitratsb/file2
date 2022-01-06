use uni
/***1**/
create view v1
as select l.st_id,st_name,l_name,p_name
from student s inner join lessons l
on s.st_id=l.st_id inner join professor p 
on l.p_id=p.p_id

select * from v1
/***2**/
create view v2
as select p.p_id,p_name,p_family,p_degree,sum(l_ncourse) as co_no
from professor p inner join lessons l
on p.p_id=l.p_id
group by p.p_id,p_name,p_family,p_degree
having p.p_id=1

select * from v2
/**3***/
create procedure p3 @stid int
as select s.st_id,st_name,st_family,st_fname,st_degree,st_year,st_major,l_name
from student s inner join lessons l
on s.st_id=l.st_id
where s.st_id=@stid

execute p3 4
/***4***/
create procedure p4 @lname varchar(50)
as
select count(s.st_id) as st_no
from student s inner join lessons l
on s.st_id=l.st_id group by l_name
having l_name=@lname

execute p4 'mathematic'
