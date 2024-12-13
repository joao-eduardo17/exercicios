-- 2602 - Select Básico
SELECT name FROM customers WHERE state LIKE 'RS';

-- 2603 - Endereço dos clientes
SELECT name, street FROM customers WHERE city LIKE 'Porto Alegre';

-- 2604 - Menores que 10 ou Maiores que 100
SELECT id, name FROM products WHERE price < 10 OR price > 100;

-- 2605 - Representantes Executivos
SELECT p.name, pr.name FROM products p
	LEFT JOIN providers pr ON p.id_providers = pr.id
    WHERE p.id_categories = 6;

-- 2606 - Categorias
SELECT p.id, p.name FROM products p
	LEFT JOIN categories c ON p.id_categories = c.id
    WHERE c.name LIKE 'super%';

-- 2607 - Cidades em Ordem Alfabética
SELECT city FROM providers ORDER BY city;
