/* Criação base de dados*/
create database aula03;

/*Destruir o banco de dados*/
DROP DATABASE aula03;
/*Utilizar o banco de dados*/
use aula03;

/*Criação de banco de dados*/
CREATE TABLE Produto (
    codProduto int PRIMARY KEY UNIQUE,
    codFornecedor int,
    descricaoProduto CHAR(45),
    preco float,
    FOREIGN KEY (codFornecedor) REFERENCES fornecedor (codFornecedor)
);

/*Descrever a estrutura da tabela*/
describe Produto;    

/*Inserir os dados*/
insert into cliente values ( '12345','Gabriel','rua um');
insert into cliente (cpfcliente,nome,endereco) values ( '45678','Maria','rua dois');

/*Selecionar uma tabela*/
select * from cliente;
select * from cliente where cpfcliente = '12345' or nome = 'g' ;
