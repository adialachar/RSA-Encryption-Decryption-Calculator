# RSA Encryption / Decryption Calculator


Date Written: 7/11/18

Last Update: 8/1/18



This is a webpage that can calculate the value either to *be* encrypted (Encryption Calculator) or the value that *is* encrypted (Decryption Calculator)

The back-end of the webpage is done using the Flask framework and is written in Python. The front-end is written in HTML/CSS.

## Features

1. Encryption of Data, given the right data

2. Decryption of Data, given the right data

3. A home page with background about RSA Encryption

4. Ability to access past calculation from SQLite Database

5. Program is Dockerized, meaning you should be able to run it from any system so long as docker.io is installed on your machine



## Installation (Docker Method)

After Installing Docker for your machine, execute the stament

docker run -p 90:5000 adialachar/rsaencdec

On your machine




## Installation (Traditional)

Note: You will need Python 2.7 or higher to run the program

1. git pull https://github.com/adialachar/RSA-Encryption-Decryption-Calculator.git


2. execute the statment "python app.py"



## Future work


In the future I would like to 


1. Docker-ize the program so that it can be run from anywhere

2. Connect the application to a SQLite database and Docker-ize the database

3. Improve the look of the website using tools like JavaScript, AJAX, and jQuery

4. Add the ability to encrypt phrases of words to simulate how passwords are encrypted
