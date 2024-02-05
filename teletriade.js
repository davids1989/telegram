const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const http = require('http');
const { parse } = require('querystring');



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
  const { username, grupo, telegram_id } = req.body;
  connection.query('INSERT INTO usuarios (username, grupo, telegram_id) VALUES (?, ?, ?)', [username, grupo, telegram_id], (err, result) => {
    if (err) throw err;
    res.send('Usuario Salvo!');
  });
});

app.delete('/api/usuarios/delete', jsonParser, (req, res) => {
  const { username } = req.query;
  const { grupo } = req.query;

  // Verificar se o usuário pertence ao grupo de tecnicos
  if (grupo === 'tecnicos_group') {
    // Remover o usuário do grupo de tecnicos
    Usuario.deleteOne({ username }, (err) => {
      if (err) {
        return res.status(500).json({ message: 'Erro ao remover o usuário do grupo de tecnicos.' });
      }

      return res.status(200).json({ message: 'Usuário removido do grupo de tecnicos com sucesso.' });
    });
  } else {
    return res.status(403).json({ message: 'Você não tem permissão para executar esta ação.' });
  }
});
const port = 3002;
app.listen(port, () => {
  console.log(`API rodando em http://localhost:${port}`);
});