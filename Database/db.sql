craete DATABASE contact;
use contact;

CRAETE TABLE users
(
	 id int(100) auto_increment primary key,
	 username varchar(100),
	 email varchar(100),
	 password varchar(100));
);


CREATE TABLE add_new 
(
	id int(10) auto_increment primary key,
	phone_no1 int(11),	
	name varchar(20),
	email varchar(50),	
	phone_no2 varchar(50),
	company varchar(90),
	group_name varchar(20)
);
