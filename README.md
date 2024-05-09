🌐 The Solution : World Needs More Food Trucks!

Instructions given below for the Set-Up of Project are based on Ubuntu 22.04.4 System

🕹️ Install pyENV and Python

Step 1: Update System Packages

Open terminal and start by updating the system’s package list to ensure access to the latest software versions:

        sudo apt update -y

Step 2: Install Required Dependencies

PyENV may require certain dependencies to function optimally. You can install these using the following command:

        sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

Step 3: Installing PyENV

Use this command to download and execute the PyENV:

        git clone https://github.com/pyenv/pyenv.git ~/.pyenv

Step 4: Setting Up Environment Variables

Post-installation, incorporate PyENV into your system’s PATH with these steps:

        echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc

        echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

        echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc

Step 5: Refresh Your Shell

Activate the new settings by refreshing your shell:

        exec "$SHELL"

Step 6: Confirming PyENV Installation

Ensure that PyENV is correctly installed:

        pyenv --version

Step 7: Python Version Installation

For example, to install Python 3.12.3:

        pyenv install 3.12.3

Step 8: Select the Installed Version as Default

To make this version the default for Python commands:

        pyenv global 3.12.3

🕹️ Install PostgreSQL

Step 1: Import the repository signing key

        sudo apt install curl ca-certificates
        sudo install -d /usr/share/postgresql-common/pgdg
        sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc

Step 2: Create the repository configuration file

        sudo sh -c 'echo "deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

Step 3: Update the package lists

        sudo apt update

Step 4: Install the latest version of PostgreSQL

        sudo apt -y install postgresql

🕹️ Install pgAdmin 4

Step 1: Install the public key for the repository 

        curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

Step 2: Create the repository configuration file

        sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

Step 3: Install for both desktop and web modes

        sudo apt install pgadmin4

Step 4: Configure the webserver, if you installed pgadmin4-web

        sudo /usr/pgadmin4/bin/setup-web.sh

🕹️ Installing Geospatial Libraries

On Debian/Ubuntu, you are advised to install the following packages which will install, directly or by dependency, the required geospatial libraries:

        sudo apt-get install binutils libproj-dev gdal-bin

GEOS API

GEOS stands for Geometry Engine - Open Source, and is a C++ library, ported from the Java Topology Suite.

        sudo apt-get install libgeos++

PROJ.4

PROJ is a generic coordinate transformation software, that transforms geospatial coordinates from one coordinate reference system (CRS) to another.
   
        sudo apt-get install proj-bin

GDAL API

GDAL stands for Geospatial Data Abstraction Library, and is a veritable “Swiss army knife” of GIS data functionality.

        sudo apt install gdal-bin

🕹️ Install Postgis and add Extension to PostgreSQL

Step 1: Install Postgis 

        sudo apt-get install postgis

Step 2: Change password for postres database in PostgreSQL

        sudo -i -u postgres

        psql

        \password postgres

Step 3: Connect PostgreSQL with pgAdmin 4 and add extension to postgres database by running query in Query Tool

        CREATE EXTENSION postgis;

🕹️ Setup GeoDjango Project

Step 1: Create folder P1-Submission [Your Name] in Desktop folder and create virtual environment in it

Use this command to create virtual environment:

        python -m venv venv

Step 2: Activate virtual environment venv

Use this command to activate virtual environment:

        source venv/bin/activate

Step 3: Install required packages

Use this command to install packages in virtual environment:

        cat requirements.txt | xargs -n 1 pip install

Step 4: Start Django Project 

Use this command to start project:

        django-admin startproject World_Needs_More_Food_Trucks

Step 5: Create facility_app 

Use this command to create app:

        python manage.py startapp facility_app

Step 6: Add apps in INSTALLED_APPS and connect with Postgres Database in seetings.py file

![alt text](<Screenshot from 2024-05-09 11-09-43.png>)

![alt text](<Screenshot from 2024-05-08 16-42-56.png>)

Step 7: Create Model, makemigrations and migrate  

Use these commands for migrations:

        python manage.py makemigrations

        python manage.py migrate

Step 8: Load data by running script load_data_script.py

Use this command for loading data:

        python facility_app/scripts/load_data_script.py

![alt text](<Screenshot from 2024-05-09 11-44-33.png>)

Step 9: Last run the Django project

Before running the django project please add the environment .json file which is specific to the environment at the manage.py file level. The sample file screenshot is shown below.

![alt text](<Screenshot from 2024-05-09 17-25-41.png>)

        python manage.py runserver

🎉 Demonstration of the App

There are two API's I have created in this project. The Approach notes for these API's are also added in repo.

  1: To list all facilities available in the database

        /api/facility/all/

![alt text](<Screenshot from 2024-05-09 11-12-36.png>)

  2: To list minimum 5 nearby specific facilities from given latitude and longitude available in the database

        /api/facility/nearby/

![alt text](<Screenshot from 2024-05-09 11-15-02.png>)


Note: I added Pagination for better performance. Please find the Artifacts in postman collection file.


Thank you....