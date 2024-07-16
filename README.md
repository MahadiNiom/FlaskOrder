Simple python web application where only authorized peoples will be able to register, login, and place an order


This application requires:

	*Python
	*pip
	*Visual studio code
	*SQLite studio

Open command line and navigate to the current directory.
then Execute below commands

	$ pip install flask
	$ pip install flask-login
	$ pip install flask-sqlalchemy
	$ py main.py

This should run your website at localhost:5000

you can try Signing in with your E-mail address but it will not work and will give an alert that you are not registerd.

To use this app go to instance folder and open database.db using SQLiteStudio.
Execute below Query:

	*INSERT INTO r_code VALUES("youremail@any.any")

Now you can sign in using "youremail@any.any" and place an order.

Your order information will be saved in "order" table.



 
