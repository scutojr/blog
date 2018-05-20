---
title: Quick Overlook of Mongodb
tags:
  - mongodb
categories:
  - ojr
  - test
  - category
date: 2018-05-07 00:20:20
---


# Table of Content

- Overview
- Data model and pattern
- Performance
- Example/Frequently used function

---

# Data Model

## Document Relationship Between Documents

Document relationship includes:
- **one-to-one**
- **one-to-many**

Relationship are maintained with:
- **document references**
- **embedded documents**

</> | Advantage | Disadvantage
--- | --- | ---
embedded documents | benefit from data localization | introduction large document problem and trigger space relocation if document is too large especially using an embedded array [MMAPv1](https://docs.mongodb.com/manual/core/data-model-operations/#data-model-document-growth)
document references | a. avoid document repetition<br> b. reduce single document size | need to issue multiple query to refer to other docuement


### One-to-One Relationships

{% codeblock lang:json With Referencing%}
// patron document
{
   _id: "joe",
   name: "Joe Bookreader"
}

// address document
{
   patron_id: "joe",
   street: "123 Fake Street",
   city: "Faketon",
   state: "MA",
   zip: "12345"
}
{% endcodeblock %}

Apply embedded document If the address data is frequently retrieved with the name information,
which is known as data localization:

{% codeblock lang:json With Embedded Document%}
{
  _id: "joe",
  name: "Joe Bookreader",
  address: {
    street: "123 Fake Street",
    city: "Faketon",
    state: "MA",
    zip: "12345"
  }
}
{% endcodeblock %}


### One-to-Many Relationships

Use **embedded document** when the **patron** has multiple **address** entities:

{% codeblock lang:json With Embedded Document%}
{
  _id: "joe",
  name: "Joe Bookreader",
  addresses: [
    {
      street: "123 Fake Street",
      city: "Faketon",
      state: "MA",
      zip: "12345"
    },
    {
      street: "1 Some Other Street",
      city: "Boston",
      state: "MA",
      zip: "12345"
    }
  ]
}
{% endcodeblock %}


**Referencing** over embedding to **avoid repetition** in this example that maps
publisher and book relationships. Storing the books reference **inside an array**
of publisher **if number of books per publisher is small with limited growth**: 

{% codeblock lang:json %}
// Publisher document
{
  name: "O'Reilly Media",
  founded: 1980,
  location: "CA",
  books: [123456789, 234567890, ...]
}

// Book document
{
    _id: 123456789,
    title: "MongoDB: The Definitive Guide",
    author: [ "Kristina Chodorow", "Mike Dirolf" ],
    published_date: ISODate("2010-09-24"),
    pages: 216,
    language: "English"
}

// Book document
{
   _id: 234567890,
   title: "50 Tips and Tricks for MongoDB Developer",
   author: "Kristina Chodorow",
   published_date: ISODate("2011-05-06"),
   pages: 68,
   language: "English"
}
{% endcodeblock %}


To **avoid mutable, growing arrays**, store the publisher reference inside the book document:

{% codeblock lang:json %}
// Publisher document
{
   _id: "oreilly",
   name: "O'Reilly Media",
   founded: 1980,
   location: "CA"
}

// Book document
{
   _id: 123456789,
   title: "MongoDB: The Definitive Guide",
   author: [ "Kristina Chodorow", "Mike Dirolf" ],
   published_date: ISODate("2010-09-24"),
   pages: 216,
   language: "English",
   publisher_id: "oreilly"
}

// Book document
{
   _id: 234567890,
   title: "50 Tips and Tricks for MongoDB Developer",
   author: "Kristina Chodorow",
   published_date: ISODate("2011-05-06"),
   pages: 68,
   language: "English",
   publisher_id: "oreilly"
}
{% endcodeblock %}


## Model specific application context 

- Model Data to Support Keyword Search by adding key word to an array:
- Model Data for Atomic Operations


### Model Data to Support Keyword Search by adding key word to an array:

{% codeblock lang:json %}
{ title : "Moby-Dick" ,
  author : "Herman Melville" ,
  published : 1851 ,
  ISBN : 0451526996 ,
  topics : [ "whaling" , "allegory" , "revenge" , "American" ,
    "novel" , "nautical" , "voyage" , "Cape Cod"
  ]
}
{% endcodeblock %}

Create an index on the topics array:

{% codeblock lang:javascript %}
db.volumes.createIndex( { topics: 1 } )
{% endcodeblock %}

Query based on the key word:

{% codeblock lang:javascript %}
db.volumes.findOne( { topics : "voyage" }, { title: 1 } )
{% endcodeblock %}


### Model Data for Atomic Operations

Operation within a document is atomic. For fields that must be updated together, embedding the fields within the same document ensures that the fields can be updated atomically.

The available copies of the book and the checkout information should be in sync:

{% codeblock lang:json %}
{
  _id: 123456789,
  title: "MongoDB: The Definitive Guide",
  author: [ "Kristina Chodorow", "Mike Dirolf" ],
  published_date: ISODate("2010-09-24"),
  pages: 216,
  language: "English",
  publisher_id: "oreilly",
  available: 3,
  checkout: [ { by: "joe", date: ISODate("2012-10-15") } ]
}
{% endcodeblock %}

Update with new checkout information:

{% codeblock lang:javascript %}
db.books.update (
   { _id: 123456789, available: { $gt: 0 } },
   {
     $inc: { available: -1 },
     $push: { checkout: { by: "abc", date: new Date() } }
   }
)
{% endcodeblock %}


---


# Performance

- query over reference, across collections?
- index
- shard

## Index

[TODO] b+,b-,lsm comparison

[TODO] penalty while creating index for large number of small index


Indexes can **improve query efficiency** in MongoDB. Without indexes, MongoDB must **scan the whole collection** to select those documents that match the query statement. 

Index in MongoDB use a **B-tree** data structure.

By default, MongoDB creates a **unique index** on the _id field.


### Create index

{% codeblock lang:javascript Mongo Shell %}
db.collection.createIndex( <key and index type specification>, <options> )
{% endcodeblock %}

{% codeblock lang:javascript Create a descending index on name field %}
db.collection.createIndex( { name: -1 } )
{% endcodeblock %}


### Index Types

#### Single Field

![image](https://docs.mongodb.com/manual/_images/index-ascending.bakedsvg.svg)

{% codeblock lang:json Record %}
{
  "_id": ObjectId("570c04a4ad233577f97dc459"),
  "score": 1034,
  "location": { state: "NY", city: "New York" }
}
{% endcodeblock %}

{% codeblock lang:javascript creates an ascending index on the score field %}
db.collection.createIndex( { name: -1 } )
{% endcodeblock %}

{% codeblock lang:javascript Create an Index on an Embedded Field %}
db.records.createIndex( { "location.state": 1 } )
{% endcodeblock %}

{% codeblock lang:javascript Create an Index on Embedded Document %}
db.records.createIndex( { location: 1 } )
{% endcodeblock %}

#### Compound Index

MongoDB supports index on multiple field. For example, { userid: 1, score: -1 }, the index sorts first by userid and then, within each userid value, sorts by score.

#### Multikey index

 If you index a field that holds an **array value**, MongoDB creates separate index entries for every element of the array.

![image](https://docs.mongodb.com/manual/_images/index-multikey.bakedsvg.svg)

#### Geospatial Index

[2d Index Internals](https://docs.mongodb.com/manual/core/geospatial-indexes/)

#### Text Indexes

MongoDB provides a text index type that supports searching for string content such as language, case sensitivity, etc

[Text Indexes](https://docs.mongodb.com/manual/core/index-text/)


#### Hashed Indexes

To support [hash based sharding](https://docs.mongodb.com/manual/core/hashed-sharding/#sharding-hashed-sharding), MongoDB provides a [hashed index](https://docs.mongodb.com/manual/core/index-hashed/) type, which indexes the hash of the value of a field.

### Index Properties

[Unique Indexes](https://docs.mongodb.com/manual/core/index-unique/). A unique index ensures that the indexed fields do not store duplicate values.
{% codeblock lang:javascript Create Index on multiple field%}
db.members.createIndex(
  {
    groupNumber: 1,
    lastname: 1, firstname: 1
  },
  {
    unique: true
  }
)
{% endcodeblock %}

[Partial indexes](https://docs.mongodb.com/manual/core/index-unique/). Partial indexes only index the documents in a collection that meet a specified filter expression and it has **lower storage requirements** and **reduced performance costs** for index creation and maintenance
{% codeblock lang:javascript Create partial index%}
db.restaurants.createIndex(
   { cuisine: 1 },
   { partialFilterExpression: { rating: { $gt: 5 } } }
)
{% endcodeblock %}


[Sparse Indexes](https://docs.mongodb.com/manual/core/index-sparse/). Sparse indexes only contain entries for documents that have the indexed field, even if the index field contains a null value.
{% codeblock lang:javascript Create Sparse Index with Unique Constraint %}
db.scores.createIndex( { score: 1 } , { sparse: true, unique: true } )
{% endcodeblock %}


[TTL indexes](https://docs.mongodb.com/manual/core/index-ttl/). MongoDB can use to automatically remove documents from a collection after a certain amount of time. data like Event data, logs, and session information only need to persist for a finite amount of time.

The _id field does not support TTL indexes.

{% codeblock lang:javascript Create TTL Index %}
db.eventlog.createIndex( { "lastModifiedDate": 1 }, { expireAfterSeconds: 3600 } )
{% endcodeblock %}


[Index Limitation](https://docs.mongodb.com/manual/reference/limits/#index-limitations)

[TODO] index overhead, performance penalization ?


## Shard

https://docs.mongodb.com/manual/reference/glossary/#term-chunk

https://docs.mongodb.com/manual/sharding/

https://docs.mongodb.com/manual/core/sharding-shard-key/

shard architecture?

chunks (default to 64MB) ---> shard 

index and shard key

how to route data based on the shard key?

load balance and migration based on chunk


### mongodb operation & limitation

> https://docs.mongodb.com/manual/core/data-model-operations

> https://docs.mongodb.com/manual/reference/limits/#Size-of-Namespace-File

index size
namespace?

rolling up small document:
  - involve sequential reads and fewer random disk accesses
  - smaller index?

**Storage Optimization for Small Documents**
Each MongoDB document contains a certain amount of overhead. This overhead is normally insignificant but becomes significant if all documents are just a few bytes, as might be the case if the documents in your collection only have one or two fields.

- cutomize _id field
- shorter field name
- [embed document](https://docs.mongodb.com/manual/core/data-model-operations/#faq-developers-embed-documents)

**data lifecycle management**
- TTL
- capped collection, FIFO


## Atomic operation

> https://docs.mongodb.com/manual/core/data-model-operations/#data-model-atomicity

are atomic on the level of a single document.

embedding the available field and the checkout field within the same document ensures that you can update the two fields atomically.

https://docs.mongodb.com/manual/core/data-model-operations/#data-model-atomicity

https://docs.mongodb.com/manual/core/capped-collections/

https://stackoverflow.com/questions/2811299/mongodb-index-ram-relationship?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

http://jasonwilder.com/blog/2012/02/08/optimizing-mongodb-indexes/

https://docs.mongodb.com/manual/tutorial/ensure-indexes-fit-ram/


- index
- capped collections: update & index & avoid scan; 
- use reference to reduce space usage


---


# Example

- Manipulation: query, aggregate
- command line
- mongoengine

**find + forEach**
```
db.clothes.find( { $and : [ { price: { $exists: true } }, { price: { $type: "string" } } ] } ).forEach( function( doc ) {
  doc.priceDec = NumberDecimal( doc.price );
  db.clothes.save( doc );
} );
```


**group + push all document to an array**

{% codeblock lang:javascript%}
db.event.aggregate([    {$group:{_id: '$event_name', events:{$push: '$$CURRENT'}}}    ])
or
db.event.aggregate([    {$group:{_id: '$event_name', events:{$push: '$$ROOT'}}}    ])
{% endcodeblock %}

{% codeblock lang:json%}
{
        "_id" : "Node Update Avg Time",
        "events" : [
                {
                        "_id" : ObjectId("5af011a0684220858c1f3839"),
                        "tags" : {

                        },
                        "event_name" : "Node Update Avg Time",
                        "endpoint" : "resourcemanager02-bdyf.qiyi.hadoop",
                        "start_at" : NumberLong("1525682592206"),
                        "status" : "problem",
                        "value" : "not yet supported",
                        "message" : "resourcemanager02-bdyf.qiyi.hadoop\\n10.19.56.154\\nService Output:80.25\\nDate/Time: Mon May 7 16:43:12 CST 2018\\nComment: \\n",
                        "badges" : {
                                "source" : "nagios",
                                "cluster" : "BD"
                        },
                        "tasks" : [ ]
                },
                {
                        "_id" : ObjectId("5af018a7684220858c1f3845"),
                        "tags" : {

                        },
                        "event_name" : "Node Update Avg Time",
                        "endpoint" : "resourcemanager02-bdyf.qiyi.hadoop",
                        "start_at" : NumberLong("1525684391608"),
                        "status" : "ok",
                        "value" : "not yet supported",
                        "message" : "resourcemanager02-bdyf.qiyi.hadoop\\n10.19.56.154\\nService Output:0.97\\nDate/Time: Mon May 7 17:13:11 CST 2018\\nComment: \\n",
                        "badges" : {
                                "source" : "nagios",
                                "cluster" : "BD"
                        },
                        "tasks" : [ ]
                }
        ]
}
{% endcodeblock %}


# Reference


# Temporary note

join & avoid join   https://docs.mongodb.com/manual/reference/database-references/


---



---
title: Mongo Note
categories: []
---


Notice
1. provide both json and mongoengine example
2. data model and design pattern
3. index
4. lock & atomic operation
5. query over reference, across collections?
6. sharded?

https://docs.mongodb.com/manual/data-modeling/

[Operational Factors and Data Models](https://docs.mongodb.com/manual/core/data-model-operations/#data-model-atomicity)


# Document Relationship

- embeded document: improve retrive performance
- document reference: reduce repeatition of document

one2one
one2many
many2many

join query?

## One to One


## Model Tree Structures

https://docs.mongodb.com/manual/applications/data-models/

[create index on array field](https://docs.mongodb.com/manual/tutorial/model-tree-structures-with-child-references/)
```
db.categories.createIndex( { children: 1 } )
```

## join & avoid join

https://docs.mongodb.com/manual/reference/database-references/


---

其他临时的记录


# Overview/Limit

> https://docs.mongodb.com/manual/reference/limits/#mongodb-limits-and-thresholds

- storage capacity of a single mongodb and sharding mongodb
- max capacity of a single doc, collection and db
- read & write performance: latency, throughput
- usage scenario

> [how to join in mongodb](https://www.mongodb.com/blog/post/thinking-documents-part-1?jmp=docs&_ga=2.238184258.318970262.1525591177-1340608169.1525101104)
reference, embedded

RDBMS	| MongoDB
---|---
Database | Database
Table |	Collection
Row	| Document
Index	| Index
JOIN | Embedded Document or Reference


---


# Data model and pattern

> [Operational Factors and Data Models](https://docs.mongodb.com/manual/core/data-model-operations/)

- document structure: references & embedded document
- write operations are atomic at the document level
- document growth, [MMAPv1](https://docs.mongodb.com/manual/core/data-model-operations/#data-model-document-growth)
- data use and performance: [Capped Collections](https://docs.mongodb.com/manual/core/capped-collections/), use index for frequent read operation


### Operational Factors and Data Models

- Document Growth
- Atomicity
- Sharding
- Indexes
- Large Number of Collections
- Collection Contains Large Number of Small Documents
- Storage Optimization for Small Documents
- Data Lifecycle Management






# Design model, pattern



https://docs.mongodb.com/manual/data-modeling/


https://docs.mongodb.com/manual/core/data-model-design/#data-modeling-embedding


# Index

https://docs.mongodb.com/manual/indexes/

what is index in mongo? index for different field type: array?

how to create index?

index overhead, performance penalization ?

mongo index is implemented based on B tree, thus, it's ordered

[interview] b+,b-,lsm comparison

# Shard

https://docs.mongodb.com/manual/reference/glossary/#term-chunk

https://docs.mongodb.com/manual/sharding/

https://docs.mongodb.com/manual/core/sharding-shard-key/

shard architecture?

chunks (default to 64MB) ---> shard 

index and shard key

how to route data based on the shard key?

load balance and migration based on chunk


# Atomic operation

> https://docs.mongodb.com/manual/core/data-model-operations/#data-model-atomicity

Are atomic on the level of a single document.

embedding the available field and the checkout field within the same document ensures that you can update the two fields atomically.


# Performance


https://docs.mongodb.com/manual/core/data-model-operations/#data-model-atomicity

https://docs.mongodb.com/manual/core/capped-collections/

https://stackoverflow.com/questions/2811299/mongodb-index-ram-relationship?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

http://jasonwilder.com/blog/2012/02/08/optimizing-mongodb-indexes/

https://docs.mongodb.com/manual/tutorial/ensure-indexes-fit-ram/


- index
- capped collections: update & index & avoid scan; 
- use reference to reduce space usage


---


# Example


**find + forEach**
```
db.clothes.find( { $and : [ { price: { $exists: true } }, { price: { $type: "string" } } ] } ).forEach( function( doc ) {
  doc.priceDec = NumberDecimal( doc.price );
  db.clothes.save( doc );
} );
```