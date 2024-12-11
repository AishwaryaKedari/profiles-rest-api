# Django rest applicaion
# install  ppa 
    sudo add-apt-repository ppa:deadsnakes/ppa -y

# Update apt
    sudo apt update

# Install specific python verion rquired for project 
    sudo apt install python3.11

# 
    which python3
    cd /usr/bin
    ls -ltr

# create virtial environment
# Below command is used to create virtualenvironment in specific python version.  
    virtualenv venv --python=python3.11

# Activate virtual environment
    source venv/bin/activate

# install requirement.txt file
# To install all the libraries from requirement.txt
    pip3 install -r requirements.txt

# start project
# for creating and starting new project.
    django-admin startproject profiles_project .  
    (. is for creating root location project otherwise it creates sub folder of this project)

#  Django is used to create new migration files whenever you make changes to your models. These migration files are essentially a set of instructions that Django uses to update your database schema to match your updated models. 
    python manage.py makemigrations profiles_api

    python manage.py migrate profiles_api


# 
    python manage.py runserver 0.0.0.0:8000
    http://127.0.0.1:8000




#To receive content which is post by post method - serializer