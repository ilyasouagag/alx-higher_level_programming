-- ists all cities contained in the database hbtn_0d_usa.
SELECT id,name
FROM cities
RIGHT JOIN states ON cities.state_id = states.id;
