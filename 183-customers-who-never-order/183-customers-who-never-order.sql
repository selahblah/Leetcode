# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers LEFT JOIN Orders On Customers.id = Orders.customerID
WHERE customerId is NULL;