
## Créer un environement virtuel avec venv :
> python3.10 -m venv .env

## Sourcer l'environnement virtuel :
> source .env/bin/activate

## Sortir de l'environnement virtuel :
> deactivate

## Mise à jour pip :
> pip3.10 install --upgrade pip

## Installer Django 3.1.6 :
> pip3.10 install django==3.1.6

## Vérification de la version de Django (et de son installation) :
> pip -m django --version

## Sauvegarder (Geler) l'environnement dans un fichier 'requirements.txt'
> pip3.10 freeze > requirements.txt

## Réinstaller toutes les bibliothèques de l'environnement via le fichier 'requirements.txt' :
> pip3.10 install -r requirements.txt

####  Créer le projet DJANGO  ####
> django-admin startproject {nom-du-projet}

######  Lancer un serveur local de développement  ######
( Permet d'afficher les pages, il n'est pas prévu pour la production UNIQUEMENT DEVELOPPEMENT LOCAL!!)
> python manage.py runserver

##  Appliquer les migrations  ##
( Créé la BDD et les entrées pour l'interface d'administration)
> python manage.py migrate


############# BASE DE DONNEES #####################

## Lancer le shell SQL :
> psql

## Créer un utilisateur Admin :
> CREATE USER blogadmin WITH ENCRYPTED PASSWORD '1234';

## Modification de l'encodage pour le bon fonctionnement de la BDD :
> ALTER ROLE blogadmin SET client_encoding TO 'utf8';

## Modification du "default_trasaction_isolation" :
> ALTER ROLE blogadmin SET default_transaction_isolation TO 'read committed';

## Donner tous les droits d'accès à l'utilisateur, à cette BDD :
> GRANT ALL PRIVILEGES ON DATABASE blog TO blogadmin;

## Commande qui liste les utilisateurs ##
> \du

## Commande qui liste le DB ##
> \l

## Commande pour sortir du Shell ##
> \q

########  !! Il faut modifier des paramètres dans settings.py  !! ########


#############################

- dans la partie 'Database' :

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'blogadmin',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
############################

 !!!! VERIFIER QUE L ENVIRONNEMENT VIRTUEL EST BIEN SOURCE  !!!!


 ########  CREATION DE L'APP POSTS :  #######
 > python manage.py startapp posts


########  !! Il faut modifier des paramètres dans settings.py  !! ########

--> Il faut renseigner le nom de l'application créée dans le fichiers "settings.py" : INSTALLED_APP :

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts', <--- ICI ---<<<<
]