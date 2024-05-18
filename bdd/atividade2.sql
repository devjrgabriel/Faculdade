drop database aula2;
create database aula2;
use aula2;
create table if not exists duplicata(
    numero int PRIMARY KEY not null UNIQUE,
    nome char(40),
    valor decimal(10,2),
    vencimento date,
    banco varchar(20)
);

alter table duplicata modify banco char(45);

INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('ABC PAPELARIA', '100100', '5000', '2023-01-20', 'Itau');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('LIVRARIA FERNANDES', '100110', '2500', '2023-01-22', 'Itau');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('LIVRARIA FERNANDES', '100120', '1500', '2022-10-15', 'Bradesco');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('ABC PAPELARIA', '100130', '8000', '2022-10-15', 'Santander');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('LER E SABER', '200120', '10500', '2024-04-26', 'Banco Do Brasil');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('LIVROS E CIA', '200125', '2000', '2024-04-26', 'Banco Do Brasil');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('LER E SABER', '200130', '11000', '2024-09-26', 'Itau');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('PAPELARIA SILVA', '250350', '1500', '2024-01-26', 'Bradesco');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('LIVROS MM', '250360', '500', '2024-12-18', 'Santander');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('LIVROS MM', '250370', '3400', '2024-04-26', 'Santander');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('PAPELARIA SILVA', '250380', '3500', '2024-04-26', 'Banco Do Brasil');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('LIVROS E CIA', '453360', '1500', '2024-06-15', 'Itau');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('LIVROS MM', '453365', '5400', '2024-06-15', 'Bradesco');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('PAPELARIA SILVA', '453370', '2350', '2023-12-27', 'Itau');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('LIVROS E CIA', '453380', '1550', '2023-12-27', 'Banco Do Brasil');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('ABC PAPELARIA', '980130', '4000', '2022-12-11', 'Itau');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('LIVRARIA FERNANDES', '770710', '2500', '2022-11-15', 'Santander');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('ABC PAPELARIA', '985001', '3000', '2022-09-11', 'Itau');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('PAPEL E AFINS', '985002', '2500', '2022-03-12', 'Santander');
INSERT INTO duplicata (nome, numero, valor, vencimento, banco) VALUES ('LER E SABER', '888132', '2500', '2023-03-05', 'Itau');


/*Exercicio 01 */
select nome,vencimento,valor from duplicata;

/*Exercicio 02 */
select* from duplicata where banco = 'Itau';

/*Exercicio 03 */
select numero,vencimento,valor,nome from duplicata where vencimento like '2023%'


