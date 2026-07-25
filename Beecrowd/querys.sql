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

-- 2608 - Maior e Menor Preço
SELECT MAX(price), MIN(price) FROM products;

-- 2609 - Produtos por Categoria
SELECT categories.name, SUM(products.amount)
FROM categories
JOIN products
ON categories.id = products.id_categories
GROUP BY categories.name;

-- 2610 - Valor Médio dos Produtos
SELECT ROUND(AVG(price),2) FROM products;

-- 2611 - Filmes de Ação
SELECT movies.id, name FROM movies
JOIN genres
ON movies.id_genres = genres.id
WHERE genres.description = 'Action';

-- 2615 - Expandindo o Negocio
SELECT DISTINCT city FROM customers;

