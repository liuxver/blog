drop database if exists awesome;
create database awesome;

use awesome;

grant select,insert,update,delete on awesome.* to 'www-data'@'localhost' identified by 'www-data';

create table users(
`id` varchar(50) not null,
`email` varchar(50) not null,
`password` varchar(50) not null,
`admin` bool not null,
`name` varchar(50) not null,
`image` varchar(50) not null,
`create_at` real not null,
unique key `idx_email`(`email`),
key `idx_create_at`(`create_at`),
primary key(`id`)
)engine=innodb default charset=utf8;

insert users values('liuxver','1369058574@qq.com','1234',True,'liuxver','a default image',5201314);



create table blogs(
`id` varchar(50) not null primary key,
`blog_id` varchar(50) not null,
`user_name` varchar(50) not null,
`user_image` varchar(500) not null,
`name` varchar(50) not null,
`summary` varchar(500) not null,
`content` mediumtext not null,
`create_at` real not null,
key `idx_create_at`(`create_at`)
)engine=innodb default charset=utf8;





create table comments(
`id` varchar(50) not null primary key,
`blog_id` varchar(50) not null,
`user_id` varchar(50) not null,
`user_name` varchar(50) not null,
`user_image` varchar(500) not null,
`content` mediumtext not null,
`create_at` real not null,
key `idx_create_at`(`create_at`)
)engine=innodb default charset=utf8;