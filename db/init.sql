CREATE TABLE Item (
    id serial primary key,
    name varchar(256) not null,
    description varchar(1024) not null,
    price decimal not null
);