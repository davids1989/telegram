const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');

const connection = mysql.createPool({
  connectionLimit: 10,
  host: 'mysql',
  port: 3306,
  user: 'david',
  password: 'Tri@#102030',
  database: 'telegram',
});



const express = require('express');
const app = express();
app.use(express.json());


// API PARA O TELEGRAM

app.get('/api/usuarios/', (req, res) => {
  pool.query('SELECT * FROM usuarios', (err, result) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Erro ao buscar usuários.');
    }
    res.send(result);
  });
});

app.post('/api/usuarios', (req, res) => {
  const { username, grupo, telegram_id } = req.body;

  // Verificar se o telegram_id já existe
  pool.query(
    'SELECT COUNT(*) as count FROM usuarios WHERE telegram_id = ? AND grupo = ?', 
    [telegram_id, grupo], 
    (selectErr, selectResult) => {
      if (selectErr) {
        console.error(selectErr);
        return res.status(500).send('Erro ao verificar usuário.');
      }

      const userCount = selectResult[0].count;

      if (userCount > 0) {
        // O usuário já existe no grupo
        return res.status(400).send('Usuário já existe no grupo.');
      } else {
        // O usuário não existe, proceder com a inserção
        pool.query(
          'INSERT INTO usuarios (username, grupo, telegram_id) VALUES (?, ?, ?)', 
          [username, grupo, telegram_id], 
          (insertErr, insertResult) => {
            if (insertErr) {
              console.error(insertErr);
              return res.status(500).send('Erro ao salvar usuário.');
            }
            res.send('Usuário Salvo!');
          }
        );
      }
    }
  );
});

app.delete('/api/usuarios/:id/:grupo', (req, res) => {
  const id = req.params.id;
  const grupo = req.params.grupo;

  pool.query(
    'DELETE FROM usuarios WHERE telegram_id = ? AND grupo = ?', 
    [id, grupo], 
    (err, result) => {
      if (err) {
        console.error(err);
        return res.status(500).send('Erro ao excluir usuário.');
      }
      res.send('Usuario Excluído!');
    }
  );
});

const port = 3002;
app.listen(port, () => {
  console.log(`API rodando em http://localhost:${port}`);
});