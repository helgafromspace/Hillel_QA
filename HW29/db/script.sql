
--1. Установить SQLite

--2. Создать таблицу Persons(name: string, favorite_color: string, profit: float)

--3. Создать таблицу Cars(model: string, color: string, price: float)

--4. Заполнить таблицы данными

--5. Вывести для каждого человека, который может купить автомобиль,самый дешевый автомобиль его любимого цвета,
-- который он может себе позволить (цена автомобиля должна быть меньше или равна дохода человека).Отсортировать по имени чловека в алфавитном порядке.

select Persons.name, Cars.model,Cars.color,Cars.price, Persons.profit from Persons JOIN Cars ON Persons.favourite_color = Cars.color where price <= profit GROUP BY name HAVING MIN(price) ORDER BY name ASC;

--6.Вывести для каждого человека...

select Persons.name, IIF( Cars.price > profit,NULL,Cars.model) AS model,Cars.color,IIF(Cars.price > profit,NULL,Cars.price) AS price, Persons.profit from Persons JOIN Cars ON Persons.favourite_color = Cars.color GROUP BY name ORDER BY name ASC;
