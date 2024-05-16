create database atividade;

use atividade;

create table produto(
    id_produto int PRIMARY KEY not null UNIQUE,
    id_cliente int,
    tipo_produto varchar(20),
    valor_produto decimal,
    FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
);
/*atibuto ID_CLIENTE NA TABELA DE PRODUTOS (Deveria ter uma tabela relacionamento "Compra") */
/*Atributo: valor_produto poderia ter o dominio como "REAL"*/


create table clientes(
    id_cliente int PRIMARY KEY not null UNIQUE,
    nome varchar(50),
    cpf int,
    telefone varchar(20)
);

create table caes(
    id_cao int PRIMARY KEY not null UNIQUE,
    id_cliente int,
    nome varchar(50),
    ano_nasc date,
    raca varchar(30),
    FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente)
);


create table veterinario(
    id_veterinario int PRIMARY KEY not null UNIQUE,
    id_cliente int,
    crmv varchar(20),
    nome varchar(50),
    data_emissao date,
    salario decimal,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

/*atributo id_cliente como chave estrangeira na tabela veterinario*/
/*atributo salario poderia ter o dominio como "REAL"*/

create table consulta(
    id_consulta int PRIMARY KEY not null UNIQUE,
    id_cliente int,
    id_cao int,
    id_veterinario int,
    `data` date,
    hora datetime,
    motivo varchar(100),
    FOREIGN KEY(id_veterinario) REFERENCES veterinario(id_veterinario),
    FOREIGN KEY(id_cao) REFERENCES caes(id_cao),
    FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente)
);
/*atributo hora poderia ter como dominio apenas "time" visto que existe o atributo data */

describe consulta;