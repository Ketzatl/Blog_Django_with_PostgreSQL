
HOW TO RUN THIS SCRIPT:

Create virual environment with venv :
> python3.10 -m venv .env

Source virtual environment 
> source .env/bin/activate

## Stop virtual environment
> deactivate

Update pip :
> pip3.10 install --upgrade pip

Install Django 3.1.6 :
> pip3.10 install django==3.1.6

Verify Django version:
> pip -m django --version

Freeze environment in 'requirements.txt'
> pip3.10 freeze > requirements.txt

## re-install all librairies with 'requirements.txt' :
> pip3.10 install -r requirements.txt

Source the environment (in root directory)
>> source .env/bin/activate

Run the application
>> cd src/
>> python manage.py runserver

Go to : http://localhost:8000/blog

