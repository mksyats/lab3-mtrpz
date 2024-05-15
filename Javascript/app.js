const express = require('express');
const moment = require('moment');

const app = express();
const port = 8080;

if (process.argv.length < 3) {
    console.log('Please provide a name as an argument.');
} else {
    const name = process.argv[2];

    app.get('/', (req, res) => {
        const message = `Hello ${name}. It is now ${moment().format('DD.MM.YYYY HH:mm')}`;
        res.send(message);
    });

    app.listen(port, '0.0.0.0', () => {
        console.log(`Server running at http://0.0.0.0:${port}/`);
    });
}
