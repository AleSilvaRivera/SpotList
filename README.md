# SpotList
my own spotList code and modifications
Steps: 

1) loging: 
http://localhost:8000/api/auth/login/  
With credentials or register and then log ing 

IF loged in as an admin: a list of user created in db would be display.
2) in the same url type: 
http://localhost:8000/api/users/
If regular user... The list of users won't be display





Debbugging:

password instead of PASSWORKD 
python manage.py migrate sessions
 'ENGINE': 'django.db.backends.postgresql_psycopg2',
make migrations api
