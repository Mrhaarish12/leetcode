-- create table employee (
--     emp_id int primary key,
--     first_name varchar(40),
--     last_name varchar(40),
--     birth_day DATE,
--     sex varchar(1),
--     salary int,
--     super_id int,
--     branch_id int
-- );


-- create table branch (
--     branch_id int primary key, 
--     branch_name varchar(40),
--     mgr_id int,
--     mgr_start_date DATE,
--     foreign key(mgr_id) REFERENCES employee(emp_id) on delete set NULL

-- );

-- now setting up the foreign key in employee table

-- alter table employee
-- add foreign key(branch_id)
-- references branch(branch_id)
-- on delete set null;

-- alter table employee 
-- add foreign key(super_id)
-- references employee(emp_id)
-- on delete set null;


-- create table client (
--     cliend_id int primary key,
--     client_name varchar(40),
--     branch_id int,
--     foreign key(branch_id) references branch(branch_id) on delete set NULL
-- );

-- alter table client rename column cliend_id to client_id;
-- create table works_with (
--     emp_id int,
--     client_id int,
--     total_sales int,
--     primary key(emp_id, client_id),
--     foreign key(emp_id) references employee(emp_id) on delete cascade,
--     foreign key(client_id) references client(client_id) on delete cascade
    
-- );

create table branch_supplier (
    branch_id int,
    supplier_name varchar(40),
    supply_type varchar(40),
    primary key(branch_id, supplier_name),
    foreign key(branch_id) references branch(branch_id) on delete cascade
);
show tables;

-- desc table branch;
