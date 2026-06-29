DROP PROCEDURE Place_Order;

select * from products;

select * from customers;

select * from orders;

select * from order_items;

SELECT NVL(MAX(product_id), 300) + 1 AS next_id FROM Products;

SELECT max(product_id) FROM Products;

INSERT INTO Customers (customer_id, name, email, phone)
VALUES (seq_customer_id.NEXTVAL, 'Kiran Mala3', 'kiran.malaa3@example.com', '9216349850');


select * from customers order by customer_id ;

delete from customers where customer_id = 225;

DELETE FROM Orders WHERE customer_id = 225;
DELETE FROM Customers WHERE customer_id = 225;

SELECT * FROM Orders WHERE customer_id = 225;

SELECT * FROM Order_Items WHERE order_id IN ( SELECT order_id FROM Orders WHERE customer_id = 225 );


-- 1. Delete order items first
DELETE FROM Order_Items
WHERE order_id IN (
    SELECT order_id FROM Orders WHERE customer_id = 225
);

-- 2. Then delete orders
DELETE FROM Orders WHERE customer_id = 225;

-- 3. Finally, delete the customer
DELETE FROM Customers WHERE customer_id = 225;
