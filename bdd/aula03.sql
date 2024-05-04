DROP DATABASE aula03;

create database aula03;
use aula03;


CREATE TABLE Produto (
    codProduto int PRIMARY KEY UNIQUE,
    codFornecedor int,
    descricaoProduto CHAR(45),
    preco float
);

CREATE TABLE fornecedor (
    codFornecedor int PRIMARY KEY UNIQUE,
    nomeFornecedor CHAR(45)
);

CREATE TABLE contemItem (
    codProduto int PRIMARY KEY UNIQUE,
    numeronf int,
    quantidade float,
    precoUnitario real
);

CREATE TABLE notaFiscal (
    numNotaFiscal int PRIMARY KEY UNIQUE,
    codCliente int,
    Data date,
    total int
);

CREATE TABLE cliente (
    codCliente int PRIMARY KEY UNIQUE,
    nomeCliente CHAR(45),
    endereco CHAR(45)
);
 
ALTER TABLE Produto ADD CONSTRAINT FK_codFornecedor
    FOREIGN KEY (codFornecedor)
    REFERENCES fornecedor (codFornecedor)
    ;
 
ALTER TABLE contemItem ADD CONSTRAINT FK_numeronf
    FOREIGN KEY (numeronf) 
    REFERENCES notaFiscal (numNotaFiscal)
    ;
 
ALTER TABLE notaFiscal ADD CONSTRAINT FK_codCliente
    FOREIGN KEY (codCliente)
    REFERENCES cliente (codCliente)
    ;
    
    
    describe contemitem;    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

