SELECT * FROM usuarios;
select * from grupos;

ALTER TABLE usuarios MODIFY COLUMN id INT;

ALTER TABLE usuarios CHANGE id telegram_id INT;