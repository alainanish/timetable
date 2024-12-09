// const express = require('express');
// const bodyParser = require('body-parser');
// const path = require('path');
// const app = express();
// const port = 3000;

// // Middleware setup
// app.use(bodyParser.json());
// app.use(bodyParser.urlencoded({ extended: true }));
// app.set('view engine', 'ejs');
// app.set('views', path.join(__dirname, 'views'));
// app.use(express.static(path.join(__dirname, 'views')));

// // Import routes
// const routes = require('./server');

// // Use imported routes
// app.use(routes);

// // Start the server
// app.listen(port, () => {
//     console.log(`Server running at http://localhost:${port}`);
// });
