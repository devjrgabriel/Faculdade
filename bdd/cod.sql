create database AulasCampoReal;

USE AulasCampoReal;

create table if not exists cliente(
	cpfcliente int not null auto_increment,
    nome varchar(45) not null,
    endereco varchar(45),
    primary key (cpfcliente)
);
insert into cliente values ( '12345','Gabriel','rua um');

insert into cliente (cpfcliente,nome,endereco) values ( '45678','Maria','rua dois');

select * from cliente;
select * from cliente where cpfcliente = '12345' or nome = 'g' ;

12