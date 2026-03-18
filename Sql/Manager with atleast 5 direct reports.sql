select m.name
from Employee m
join Employee  e on m.id=e.managerID
group by m.id,m.name
having count(m.id)>=5;
