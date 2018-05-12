# Mongoengine


self reference for **EmbeddedDocumentListField**

**EmbeddedDocumentListField** accepts the document class as the first
parameter. However, if we need a hierachy structure that are organized
by the some document type, we will encounter a python class error because
we try to use this class before its creation.

To solve it, we will use a string instead. This string is a class path
separated by dot, mongoengine will find out the proper class as long as
postfix of this string matches exactly one of the document class name.




# Skill

```
from bson import json_util # don't use json package


Document.to_mongo() # instance of bson

Cursor.as_pymongo() # instance of bson

Cursor.to_json() # instance of str

```

# FAQ

**how to update an embedded document in mongoengine**




