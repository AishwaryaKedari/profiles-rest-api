# Django rest applicaion
# install  ppa 
    sudo add-apt-repository ppa:deadsnakes/ppa -y

# Update apt
    sudo apt update

# Install python verion rquired for project 
    sudo apt install python3.11

# 
    which python3
    cd /usr/bin
    ls -ltr

# create virtial environment
    virtualenv venv --python=python3.11

# Activate virtual environment
    source env/bin/activate

# install requirement.txt file
    pip3 install -r requirements.txt

# start project
    django-admin startproject profiles_project .  
    (. is for creating root location project otherwise it creates sub folder of this project)

#
    python manage.py makemigrations profiles_api

    python manage.py migrate profiles_api


# 
    python manage.py runserver 0.0.0.0:8000
    http://127.0.0.1:8000