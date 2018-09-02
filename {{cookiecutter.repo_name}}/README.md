# Understanding {{cookiecutter.app_name}}

This template application is based on Miguel Grinberg's tutorial.  To understand the different parts of the template, please go to the [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

# Running {{cookiecutter.app_name}}

**Mac OSX pre-requisites**

* Install Python
```
$ brew install python3
```
* Install Virtualenv
```
$ pip install virtualenv
```
* [Install PostgreSQL](https://wiki.postgresql.org/wiki/Detailed_installation_guides)
* I would highly suggest installing[Postgress.app](https://postgresapp.com/).  For an Admin Tool, I recommend[PgAdmin](https://www.pgadmin.org/).

**Step 1: Clone the git repo**
```
$ git clone https://github.com/erwindev/flask-seed.git  
```

**Step 2: Create the virtual environment.**  
```
$ virtualenv -p /usr/local/bin/python3 venv
$ source venv/bin/activate
```
**Step 3: Install the modules**
```
$ pip install -r requirements.txt
```
**Step 4: Create the database**
* If you installed Postgress.app, it will come with `psql`.
* Connect to the database
```
$ psql postgres
```
* Check users that are installed
```
postgres-# \du
```
* Create a user and assign `CREATEDB` role
```
postgres=# CREATE ROLE erwin WITH LOGIN PASSWORD 'my-very-secure-password';
postgres=# ALTER ROLE erwin CREATEDB;
postgres=# \q

```
* Create a database and grant privileges to the user
```
$ psql postgres -U erwin
postgres=> CREATE DATABASE erwindb;
postgres=> GRANT ALL PRIVILEGES ON DATABASE erwindb to erwin;
```
* Update the config settings in your `env.current` file.  
```
export SERVICE_NAME=SampleService
export ENV_CONFIG=DEV
export CURRENT_VERSION=0.0.LOCAL
export DB_USER=erwin
export DB_PASSWORD=my-very-secure-password
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=erwindb
```

**Step 5: Run the application**
```
$ sh run-service.sh
```
**Step 6: Go to you favorite browser**

[http://localhost:5000](http://localhost:5000)

# Required modules
```
flask
sqlalchemy
flask_sqlalchemy
flask_script
flask_migrate
psycopg2
flask_restplus
```
** Doing a pip install of requirements.txt will install all of this.

# Generate database tables from the models
We use SQLAlchemy as our ORM tool.  To be able to activate generate tables, you will need to run the following.  You are only required to run this once.  This will generate a migrations folder.

```
python application.py db init
```

Classes defined in the models.py will be auto-generated to tables in the database.  You must run the following anytime you update the classes in models.py.
```
python application.py db migrate -m "sample table"
python application.py db upgrade
```

# Running the tests
```
run-test.sh
```

# Questions
Talk to:

* {{cookiecutter.contact_name}} - {{cookiecutter.contact_email}}
