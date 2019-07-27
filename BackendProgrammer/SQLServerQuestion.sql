-- Considering the database schema displayed in the SQLServer-style diagram
-- below, write a SQL query to return a list of all the invoices. For each
-- invoice, show the Invoice ID, the billing date, the customer’s name, and
-- the name of the customer who referred that customer (if any). The list
-- should be ordered by billing date.

-- create tables
CREATE TABLE customers (
    Id INT IDENTITY (1, 1) PRIMARY KEY,
    Name VARCHAR (255) NOT NULL,
    ReferedBy INT,
);

CREATE TABLE invoices (
    Id INT IDENTITY (1, 1) PRIMARY KEY,
    CustomerId INT NOT NULL,
    BillingDate DATE NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES customers (Id) ON DELETE CASCADE ON UPDATE CASCADE,
);

-- insert data
INSERT INTO customers(Name, ReferedBy) VALUES('AAAA', NULL);
INSERT INTO customers(Name, ReferedBy) VALUES('BBBB', 1);
INSERT INTO customers(Name, ReferedBy) VALUES('CCCC', 1);
INSERT INTO customers(Name, ReferedBy) VALUES('DDDD', NULL);
INSERT INTO customers(Name, ReferedBy) VALUES('EEEE', 2);

INSERT INTO invoices(CustomerId, BillingDate) VALUES(1,'20990213');
INSERT INTO invoices(CustomerId, BillingDate) VALUES(5,'20990212');
INSERT INTO invoices(CustomerId, BillingDate) VALUES(3,'20990514');
INSERT INTO invoices(CustomerId, BillingDate) VALUES(3,'20990215');
INSERT INTO invoices(CustomerId, BillingDate) VALUES(4,'10990213');
INSERT INTO invoices(CustomerId, BillingDate) VALUES(1,'20990215');

-- write a SQL query to return a list of all the invoices.
-- For each invoice, show the Invoice ID, the billing date,
-- the customer’s name, and the name of the customer who
-- referred that customer (if any). The list should be
-- ordered by billing date.
SELECT
    invoices.Id AS 'Invoice ID',
    invoices.BillingDate AS 'billing date',
    customers.name AS 'customer’s name',
    customers2.Name AS 'name of the customer who referred'
FROM 
    invoices
INNER JOIN customers ON invoices.CustomerId = customers.Id
LEFT JOIN customers customers2 ON customers.ReferedBy = customers2.Id
ORDER BY invoices.BillingDate DESC
;
