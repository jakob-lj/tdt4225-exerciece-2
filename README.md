## Excercise 2 in tdt4225

Using mysql on local machine as it's not enough machines for all students.

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
