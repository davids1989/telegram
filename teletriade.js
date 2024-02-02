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

app.get('/api/usuarios', (req, res) => {
  connection.query('SELECT * FROM usuarios', (err, result) => {
    if (err) throw err;
    res.send(result);
  });
});

app.post('/api/usuarios', (req, res) => {
  const { username, grupo } = req.body;
  connection.query('INSERT INTO usuarios (username, grupo) VALUES (?, ?)', [username, grupo], (err, result) => {
    if (err) throw err;
    res.send('Usuario Salvo!');
  });
});

app.delete('/api/usuarios/delete', (req, res) => {
  const { username, grupo } = req.params.id;
  connection.query('DELETE FROM usuarios WHERE id > 0 AND username = ? AND grupo = ? ', [username, grupo], (err, result) => {
    if (err) throw err;
    res.send('Usuario Excluído!');
  });
});
const port = 3002;
app.listen(port, () => {
  console.log(`API rodando em http://localhost:${port}`);
});