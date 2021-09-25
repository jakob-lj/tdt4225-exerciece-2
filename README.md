## Excercise 2 in tdt4225

Using mysql on local machine as it's not enough machines for all students.

Remember that the program expects to find the dataset at ../dataset/. The dataset can be found in the exercice description.

### Running the database and connect to terminal

Start by creating the docker container:

```bash
    ./runDb.sh
```

Then, connect to mysq trough docker bash

```bash
    docker exec -it mysql-server bash
```

Password is password as seen in runDb script.

This is not a security issue as the port is not shared outside the development computer.

```bash
    mysql -u root -p
```

Now create the database used in the exercices:

```mysql
    CREATE DATABASE tdt4225
```

### Running python

Before you can start development in python. Initialize the virutal environment.

This requires python3 module venv to be installed

```bash
    python3 -m venv venv
```

The venv folder is in gitignore.

Activate the environment with (mac)

```bash
    source venv/bin/activate
```

Now you should be able to run the python scripts.

Use -B in order to prevent creating **\_\_pycache\_\_**

```bash
    python3 -B main.py
```
