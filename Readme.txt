Steps to run the web app:

1.	

Download Django by typing:

		pip install django

into the terminal window.


2.

Navigate to the mysite folder and type:

			python manage.py migrate

3.

Now to run the program, type:

			python manage.py runserver

4.

Open your web browser and go to the address:

					127.0.0.1/8000/

This is also called localhost. Instead of the above, you can also type:

					localhost/8000/

5. To access logging information, you need to be logged in as the django administrator. To do this, go to the address:

				127.0.0.1/8000/admin

Use the username superuser and password superuser. Click on the Activity_log link to view recent user activities.