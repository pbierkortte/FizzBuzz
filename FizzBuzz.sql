with NUMBERS(I) as 
(               select   1 
    union all   select I+1                      from NUMBERS where I < 100
)
, CTE(I, S) as 
(               select I, 'FizzBuzz'            from NUMBERS where I % 15 = 0
    union all   select I, 'Fizz'                from NUMBERS where I %  3 = 0
    union all   select I, 'Buzz'                from NUMBERS where I %  5 = 0
    union all   select I, cast(I AS varchar(8)) from NUMBERS 
)
select max(S)
from CTE
group by I
;
