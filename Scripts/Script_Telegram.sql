SELECT * FROM usuariosgrupos where telegram_id = 1292043080 and grupo = "suporte_group";
select * from grupos;

ALTER TABLE usuarios MODIFY COLUMN id INT;

ALTER TABLE usuarios CHANGE id telegram_id INT;

ALTER TABLE usuarios MODIFY COLUMN telegram_id BIGINT;

ALTER TABLE usuarios DROP PRIMARY KEY;

ALTER TABLE usuarios ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY;


INSERT INTO usuarios (username, grupo, telegram_id) VALUES ('testeuser', 'grupo_teste', '123456')