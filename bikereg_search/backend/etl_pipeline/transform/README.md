# Transformations 

* EventAddress:
    * Uses Python Pandas vectorization with bool mask to convert all empty strings (i.e. len(string) == 1) to "NULL" for database null handling.
    * Vectorization was chosen over `apply` because pandas `apply` uses a loop in the background to apply function to all elements in specified axis. 

* EventCity