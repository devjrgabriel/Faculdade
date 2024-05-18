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


/*1. Listar nome,vencimento e valor de cada duplicata da tabela. */
select nome,vencimento,valor from duplicata;
/*2. Apresentar as duplicatas depositadas no banco Itaú */
select* from duplicata where banco = 'Itau';
/*3. Apresentar o número (quantidade) de duplicatas depositadas no banco Itaú*/
select count(banco) from duplicata where banco like 'Itau';
/*4. Quais são as duplicatas (número, vencimento, valor e nome) que vencem no ano de 2023. */
select numero,vencimento,valor,nome from duplicata where vencimento like '2023%'
/*5. Apresentar as duplicatas (número, vencimento, valor e nome) que não estão
depositadas nos bancos Itaú e Santander.*/
 select numero,vencimento,valor,nome from duplicata where banco not like'Itau' and not like 'Santander';
/*6. Quanto é o valor da divida o cliente PAPELARIA SILVA, e quais são as duplicatas?*/
/*7. Retirar da tabela a duplicata 770710 do cliente LIVRARIA FERNANDES, por ter
sido devidamente quitada.*/
/*8. Apresentar uma listagem em ordem alfabética por nome do cliente de todos os
campos da tabela.*/
/*9. Apresentar uma listagem em ordem de data de vencimento com o nome do cliente,
banco, valor e vencimento.*/
/*10.As duplicatas do Banco do Brasil foram transferidas para o Santander. Proceder o
ajuste dos registros.
*/
/*11.Quais são os clientes que possuem suas duplicatas depositadas no Banco
Bradesco?*/
/*12.Qual é a previsão de recebimento no período de 01/01/2022 até 31/12/2022?*/
/*13.Quanto a empresa tem para receber no período de 01/08/2022 até 30/08/2022?*/
/*14.Quais foram os itens adquiridos pelo cliente ABC PAPELARIA?*/
/*15.Acrescentar uma multa de 15% para todos os títulos que se encontram vencidos no
período de 01/01/2022 até*/
/*16.Acrescentar uma multa de 5% para todos os títulos vencidos entre 01/01/2023 e
31/05/2023 que sejam do cliente LER E*/
/*17.Qual é a média aritmética dos valores das duplicatas do ano de 2022?*/
/*18.Exiba as duplicatas e nome dos respectivos clientes que possuem duplicatas com
valor superior a 10000,00?*/
/*19.Qual o valor total das duplicatas lançadas para o banco Santander?*/
/*20.Quais são os clientes que possuem suas duplicatas depositadas nos Bancos
Bradesco ou Itaú?*/

