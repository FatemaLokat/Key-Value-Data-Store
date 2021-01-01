# Key-Value Data Store

  A key-value data store is a simple database that uses an associative array (dictionary) as the fundamental data model where in each key is associated with only one value in a collection. This relationship is referred to as a key-value pair.

In general, key-value stores have no query language. They provide a way to create, display and delete data using simple commands. the path to retrieve data is a direct request to the object in memory or on disk. The simplicity of this model makes a key-value store fast, simple to use, scalable, portable and very flexible.


## Time-To-Live (TTL) 
  TTL is a simple mechanism to set a lifespan of particular pair in the computer after which it gets erased form the memory.

## Errors are displayed to the users/clients when, 

1. File size exceeds 1GB.
2. Jason object value exceeds 16KB.
3. The key already exists in the database.
4. Time-to-live of the key is expired which retieving a pair.
5. Key does not mactch with ones in database.

**This key-value data store is compatible to all operating systems.
