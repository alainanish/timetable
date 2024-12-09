const express = require('express')
const app = express();
const mysql = require('mysql2');
const path = require('path');
const port = 3000;
const ejs = require('ejs')
const bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view-engine', 'ejs');
app.use(express.urlencoded({ extended: false }));
app.set('views', path.join(__dirname, 'views')); // Sets the correct directory for EJS files
app.use(express.static(__dirname + '/views'));




//custom hash function
function hash(password) {
    let hash_value = 0;
    const prime = 31; //prime to increase complexity and ensure uniqueness
    for (let i = 0; i < password.length; i++) {
        let char = password[i];
        //use bigint to handle large intermediate values
        let charCode = BigInt(char.charCodeAt(0)); //get ASCII value of character
        let primePower = BigInt(prime) ** BigInt(i + 1); //compute prime^(i + 1) using bigint
        //add modded result of characters contribution
        hash_value += Number((charCode * primePower) % BigInt(100000));
    }
    //mod the final hash value so it's 5 digits
    hash_value = hash_value % 100000;
    return hash_value; //return  final integer
}

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname + '/views/homepage.html'));
});

app.get('/homepage', (req, res) => {
    res.render('homepage.ejs');
   
 });

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname + '/views/login.html'));
});


app.get('/login', (req, res) => {
    res.render('login.ejs');
});


app.get('/timetable', (req, res) => {
    res.render('timetable.ejs');
});




// MySQL Database Connection
const db = mysql.createConnection({
    host: 'localhost', // Replace with your database host
    user: 'root', // Your MySQL username
    password: 'Libraries4Life!', // Your MySQL password
    database: 'sys', // Database name
});


db.connect((err) => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('Connected to MySQL database');
});




// POST route for login
app.post('/login', async (req, res) => {
    const userInputUsername = req.body.username; // Username entered by the user
    const userInputPassword = req.body.password; // Password entered by the user


    // SQL query to retrieve all usernames, passwords, and hashed values
    const fetchCredentialsQuery = `
        SELECT
            students.student_username,
            pass_hashes.user_pass,
            pass_hashes.pass_hash
        FROM students, pass_hashes
        WHERE students.student_pass = pass_hashes.user_pass
        ;`
        ;


    db.query(fetchCredentialsQuery, (err, results) => {
        if (err) {
            console.error('Error retrieving credentials:', err);
            return res.status(500).send('Database error.');
        }
   
        // Create a dictionary to store credentials in the format { username: { password, hashedPassword } }
        const credentialsDict = {};
        results.forEach(row => {
            credentialsDict[row.student_username] = {
                password: row.user_pass,
                hashedPassword: row.pass_hash,
            };
        });
        //console.log('Final Credentials Dictionary:', credentialsDict);
   


        // Iterate through the dictionary to find a matching username
        let usernameFound = false;
   
        for (const [username, credentials] of Object.entries(credentialsDict)) {
            if (userInputUsername === username) {
                usernameFound = true;
   
                // Compare the input password with the stored password
                if (userInputPassword === credentials.password) {
                    //return res.send('Login successful! Welcome to your account.');
                    res.send({ message: 'Login successful! Welcome to your account.', redirectUrl: '/homepage' })  
                    //res.render('homepage.ejs', { name: user.student_fname });
                    ;
                    // // Hash the user input password using your hash function
                    // const hashedInputPassword = hash(userInputPassword);
                    // // Compare the hashed user input password with the stored hashed password
                    // if (hashedInputPassword === credentials.hashedPassword) {
                    //     return res.send('Login successful! Welcome to your account.');
                    // } else {
                    //     return res.status(401).send('Hash does not match. Please try again.');
                    // }


                } else {
                    return res.status(401).send('Invalid password. Please try again.');
                }
            }
        }
       


        // If no username is found after iterating through the dictionary
        if (!usernameFound) {
            return res.status(401).send('Invalid username. Please try again.');
        }
    });
    // console.log('User Input Password:', userInputPassword);
    // console.log('Hashed Input Password:', hash(userInputPassword));
    // console.log('Stored Hashed Password:', credentials.hashedPassword);
});


// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});


















app.get('/timetable', function(req, res) {
    const className = '9z1'; // Example class name, can be dynamic
 
    db.query('SELECT * FROM student_timetables WHERE student_class = ?', [className], function(err, result) {
        if (err) {
            console.error(err);
            return res.status(500).send("Error retrieving timetable data.");
        }
 
        // Pass both data and className to the timetable.ejs template
        res.render('timetable.ejs', {
            data: result,
            className: className
        });
    });
  });


 
app.get('/timetable', function(req, res) {
    const className = req.query.className; // e.g., /timetable?className=9z1
 
    db.query('SELECT * FROM student_timetables WHERE student_class = ?', [className], function(err, result) {
        if (err) {
            console.error(err);
            return res.status(500).send("Error retrieving timetable data.");
        }
 
        res.render('timetable.ejs', {
            data: result,
            className: className
        });
    });
  });