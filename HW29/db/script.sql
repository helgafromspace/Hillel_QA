
--1. Установить SQLite

--2. Создать таблицу Persons(name: string, favorite_color: string, profit: float)

--3. Создать таблицу Cars(model: string, color: string, price: float)

--4. Заполнить таблицы данными

--5. Вывести для каждого человека, который может купить автомобиль,самый дешевый автомобиль его любимого цвета,
-- который он может себе позволить (цена автомобиля должна быть меньше или равна дохода человека).Отсортировать по имени чловека в алфавитном порядке.

select Persons.name, Cars.model,Cars.color,Cars.price, Persons.profit from Persons JOIN Cars ON Persons.favourite_color = Cars.color where price <= profit GROUP BY name HAVING MIN(price) ORDER BY name ASC;

--6.Вывести для каждого человека самый дешевый автомобиль его любимого цвета, который он может себе позволить
--(цена автомобиля должна быть меньше или равна дохода человека).

-- Отсортировать по имени чловека в алфавитном порядке.

select Persons.name, IIF( Cars.price > profit,NULL,Cars.model) AS model,Cars.color,IIF(Cars.price > profit,NULL,Cars.price) AS price, Persons.profit from Persons JOIN Cars ON Persons.favourite_color = Cars.color GROUP BY name HAVING MIN(price) ORDER BY name ASC;

select Persons.name, Cars.model,Cars.color,Cars.price, Persons.profit from Persons JOIN Cars ON Persons.favourite_color = Cars.color where price <= profit GROUP BY name HAVING MIN(price) UNION select Persons.name, NULL as model,Cars.color,NULL AS price, Persons.profit from Persons JOIN Cars ON Persons.favourite_color = Cars.color GROUP BY name HAVING MIN(price) and price > profit ORDER BY name ASC;

select Persons2.name, IIF( Cars2.price > profit,NULL,Cars2.model) AS model,Cars2.color,IIF(Cars2.price > profit,NULL,Cars2.price) AS price, Persons2.profit from Persons2 JOIN Cars2 ON Persons2.favourite_color = Cars2.color GROUP BY name HAVING MIN(price) ORDER BY name ASC;

select Persons2.name, Cars2.model,Cars2.color,Cars2.price, Persons2.profit from Persons2 JOIN Cars2 ON Persons2.favourite_color = Cars2.color where price <= profit GROUP BY name HAVING MIN(price) UNION select Persons2.name, NULL as model,Cars2.color,NULL AS price, Persons2.profit from Persons2 JOIN Cars2 ON Persons2.favourite_color = Cars2.color GROUP BY name HAVING MIN(price) and price > profit ORDER BY name ASC;