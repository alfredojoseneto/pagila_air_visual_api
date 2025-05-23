from pandas import DataFrame
from ..util.sql_handler import SQLHandler


def pagila_all_cities() -> DataFrame:
    sql = """
    SELECT
        DISTINCT
        c3.country_id 
        ,c3.country
        ,a.address_id
        ,a.district
        ,c2.city_id
        ,c2.city
    --    ,count(*) AS clients_amount
    FROM payment p
    LEFT JOIN customer c ON P.customer_id = C.customer_id
    LEFT JOIN address a ON c.address_id = a.address_id 
    LEFT JOIN city c2 ON c2.city_id = a.city_id
    LEFT JOIN country c3 ON c2.country_id = c3.country_id
    --GROUP BY c3.country_id ,c3.country, a.address_id , a.district, c2.city_id, c2.city
    --HAVING count(*) > 10
    ORDER BY
        c3.country, a.district, c2.city
    """
    sql_handler = SQLHandler()
    return sql_handler.fetch_data(sql)


def exercise_01_data() -> DataFrame:
    """
    Recupere as cidades dos clientes com mais de 10 transações de acordo com
    a tabela de pagamento.
    """
    sql = """
        SELECT
            p.customer_id
            ,c2.city
            ,count(*) AS transactions_amount
        FROM payment p
        LEFT JOIN customer c ON P.customer_id = c.customer_id
        LEFT JOIN address a ON c.address_id = a.address_id
        LEFT JOIN city c2 ON c2.city_id = a.city_id
        GROUP BY p.customer_id, c2.city
        HAVING count(*) > 10
        ORDER BY 3 DESC
    """
    sql_handler = SQLHandler()
    return sql_handler.fetch_data(sql)


def exercise_02_data() -> DataFrame:
    """
    Cálculo da receita bruta por cidade
    """
    sql = """
    -- Receita Bruta por cidade
    SELECT
    --    p.customer_id
        c2.city
        ,SUM(p.amount) AS invoicing
    FROM payment p
    LEFT JOIN customer c ON P.customer_id = C.customer_id
    LEFT JOIN address a ON c.address_id = a.address_id
    LEFT JOIN city c2 ON c2.city_id = a.city_id
    GROUP BY c2.city
    --HAVING count(*) > 10
    ORDER BY 2 DESC
    """
    sql_handler = SQLHandler()
    return sql_handler.fetch_data(sql)


def exercise_03_data() -> DataFrame:
    """
    Quantidade de aluguéus
    """
    sql = """
    SELECT
        c3.country
        ,count(*) AS rents_amount
    FROM rental r
    LEFT JOIN customer c ON r.customer_id = c.customer_id
    LEFT JOIN address a ON c.address_id = a.address_id
    LEFT JOIN city c2 ON c2.city_id = a.city_id
    LEFT JOIN country c3 ON c3.country_id  = c2.country_id
    GROUP BY c3.country
    ORDER BY 2 DESC
    """
    sql_handler = SQLHandler()
    return sql_handler.fetch_data(sql)


def exercise_04_data() -> DataFrame:
    """
    Cidades com o maior número de clientes
    """
    sql = """
    SELECT
        c3.country
        ,a.district
        ,c2.city
        ,count(*) AS clients_amount
    FROM payment p
    LEFT JOIN customer c ON P.customer_id = C.customer_id
    LEFT JOIN address a ON c.address_id = a.address_id
    LEFT JOIN city c2 ON c2.city_id = a.city_id
    LEFT JOIN country c3 ON c2.country_id = c3.country_id
    GROUP BY c3.country, a.district, c2.city
    --HAVING count(*) > 10
    ORDER BY 4 DESC
    LIMIT 10
    """
    sql_handler = SQLHandler()
    return sql_handler.fetch_data(sql)


def exercise_04_data_aqi_150(*args) -> DataFrame:
    """
    Cidades com AQI maior que 150
    """
    sql = f"""
    SELECT
        f.title
        ,f.rental_rate
        ,c3.country
        ,c2.city
    FROM rental r
    INNER JOIN inventory i ON r.inventory_id = i.inventory_id
    INNER JOIN film f ON f.film_id = i.film_id
    INNER JOIN customer c ON c.customer_id = r.customer_id
    INNER JOIN address a ON c.address_id = a.address_id
    INNER JOIN city c2 ON c2.city_id = a.city_id
    INNER JOIN country c3 ON c3.country_id = c2.country_id
    WHERE 1=1
        AND f.rental_rate >= 4
        AND c2.city IN {args}
    """
    sql_handler = SQLHandler()
    return sql_handler.fetch_data(sql)


def exercise_05_data(*args) -> DataFrame:
    """
    Customer, cidade e país no qual o AQI é maior que 130
    """
    sql = f"""
    SELECT
        CONCAT(c.first_name, ' ', c.last_name) AS customer
        ,c2.city
        ,c3.country
        FROM customer c
    LEFT JOIN address a ON c.address_id = a.address_id 
    LEFT JOIN city c2 ON c2.city_id = a.city_id
    LEFT JOIN country c3 ON c2.country_id = c3.country_id
    WHERE 1=1
        AND c2.city IN {args}
    """
    sql_hander = SQLHandler()
    return sql_hander.fetch_data(sql=sql)


def exercise_06_data() -> DataFrame:
    """
    Valores dos pagamentos por cidade
    """
    sql = """
    SELECT
        c3.country
        ,c2.city
        ,SUM(p.amount) AS amount
    FROM payment p
    LEFT JOIN customer c ON P.customer_id = C.customer_id
    LEFT JOIN address a ON c.address_id = a.address_id 
    LEFT JOIN city c2 ON c2.city_id = a.city_id
    LEFT JOIN country c3 ON c2.country_id = c3.country_id
    GROUP BY c3.country, c2.city
    ORDER BY c3.country, c2.city
    """
    sql_handler = SQLHandler()
    return sql_handler.fetch_data(sql=sql)


def exercise_07_data() -> DataFrame:
    """
    Obtém a média de dias de aluguel de filmes por cidade e país
    """
    sql = """
    SELECT
        c2.city
        ,c3.country
        ,round(avg(extract(DAY FROM return_date::timestamp - rental_date::timestamp)), 2) avg_rent_days
    FROM rental r
    INNER JOIN customer c ON c.customer_id = r.customer_id
    INNER JOIN address a ON a.address_id = c.address_id
    INNER JOIN city c2 ON c2.city_id = a.city_id
    INNER JOIN country c3 ON c3.country_id = c2.country_id
    GROUP BY c2.city, c3.country
    """
    sql_handler = SQLHandler()
    return sql_handler.fetch_data(sql=sql)
