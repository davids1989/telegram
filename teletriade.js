const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');



const app = express();
app.use(bodyParser.json());

const connection = mysql.createPool({
  connectionLimit: 10,
  host: '38.156.3.8',
  port: 3306,
  user: 'david',
  password: 'Tri@#102030',
  database: 'telegram',
});

//connection.connect((err) => {
//  if (err) throw err;
//  console.log('conexão com o MySQL estabelecida com sucesso!!');
//});

// API PARA O TELEGRAM

app.get('/api/usuarios/', (req, res) => {
  connection.query('SELECT telegram_id FROM usuarios', (err, result) => {
    if (err) throw err;
    res.send(result);
  });
});

app.post('/api/usuarios', (req, res) => {
  const { username, grupo, telegram_id } = req.body;

  // Verificar se o telegram_id já existe
  connection.query('SELECT COUNT(*) as count FROM usuarios WHERE telegram_id = ?', [telegram_id], (selectErr, selectResult) => {
    if (selectErr) throw selectErr;

    const userCount = selectResult[0].count;

    if (userCount > 0) {
      // O usuário já existe no grupo
      res.status(400).send('Usuário já existe no grupo.');
    } else {
      // O usuário não existe, proceder com a inserção
      connection.query('INSERT INTO usuarios (username, grupo, telegram_id) VALUES (?, ?, ?)', [username, grupo, telegram_id], (insertErr, insertResult) => {
        if (insertErr) throw insertErr;
        res.send('Usuário Salvo!');
      });
    }
  });
});


app.delete('/api/usuarios/:id', (req, res) => {
  const id = req.params.id;
  connection.query('DELETE FROM usuarios WHERE telegram_id = ?', [id], (err, result) => {
    if (err) throw err;
    res.send('Usuario Excluído!');
  });
});
const port = 3002;
app.listen(port, () => {
  console.log(`API rodando em http://localhost:${port}`);
});