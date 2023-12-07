CREATE TABLE `telegram`.`grupos` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `nome` VARCHAR(255)
);

CREATE TABLE `telegram`.`usuarios` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `user` VARCHAR(255)
);
ALTER TABLE `telegram`.`usuarios`
CHANGE COLUMN `grupo_id` `grupo` VARCHAR(255);

SELECT * FROM Modo;

ALTER TABLE `usuarios`
ADD COLUMN `grupo` varchar(255);


CREATE TABLE `app-triade`.`mensagens` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `number` VARCHAR(255),
    `msg` MEDIUMTEXT,
    `status` VARCHAR(255),
    `status_msg` VARCHAR(550),
    `date_created` DATETIME,
    `visto` VARCHAR(255) default 0
);


ALTER TABLE `mensagens` CHANGE ´msg2´ `msg` MEDIUMTEXT;
ALTER TABLE `mensagens` DROP COLUMN `msg`;
SELECT * FROM mensagens;
SELECT * FROM mensagens WHERE number = 31989313830 AND visto = 0;

SELECT id, number, msg, status, status_msg, date_created FROM mensagens WHERE date_created > '2023-10-18T11:36:28.721Z' ORDER BY date_created;

UPDATE mensagens SET visto = 0 WHERE number = 31989313830 and id > 1;

SET SQL_SAFE_UPDATES = 0;

drop TABLE mensagens;

SELECT distinct mensagens.number,
       mensagens.msg,
       usuario.UID
FROM usuario
INNER JOIN mensagens ON mensagens.number = usuario.number
WHERE mensagens.visto = 1;

SELECT * FROM usuario;
SELECT * FROM mensagens
WHERE mensagens.visto = 1;

DELETE FROM `app-triade`.`mensagens` WHERE (`id` > '0');

select usuario.nome,
       usuario.number,
       usuario.UID
FROM usuario
inner join mensagens ON mensagens.number = usuario.NUMBER
WHERE usuario.number = '3199479990';

SELECT * FROM mensagens WHERE number = '31989313830'
ORDER BY date_created DESC;

