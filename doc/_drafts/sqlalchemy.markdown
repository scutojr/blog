
# Query


use **session**:


```
Session = sessionmaker()
session = Session()

# need to specify mapper or class when executing
result = session.execute("select * from table where id=:id", {'id':7}, mapper=MyMappedClass)

result = session.execute(select([mytable], mytable.c.id==7), mapper=MyMappedClass)

connection = session.connection(MyMappedClass)
```


use **connection**:
```
```

pool?


how to keep connection alive?


[working with engine and connection](http://docs.sqlalchemy.org/en/latest/core/connections.html)
[execute raw sql by Connection/Engine](http://docs.sqlalchemy.org/en/latest/core/connections.html#sqlalchemy.engine.Connection.execute)




# Warn

1. session can not conceive the change from other session and client, you should always use a new session before querying
