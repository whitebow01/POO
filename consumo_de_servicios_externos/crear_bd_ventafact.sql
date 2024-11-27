create database empresa;
use empresa;

create table ventafact (
    numfact int primary key,
    fechafact date,
    rutcli varchar(10),
    monto float
) engine=innodb;

insert into ventafact values (3420089, '2023-03-05', '11454980-k', 56000);
insert into ventafact values (3420090, '2023-03-12', '10499891-2', 89000);
insert into ventafact values (3420091, '2023-03-22', '11450081-7', 120000);
