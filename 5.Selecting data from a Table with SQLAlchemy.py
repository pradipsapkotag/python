#by APP
# Import create_engine, MetaData, and Table
from sqlalchemy import create_engine, MetaData, Table, select

#Reflect census table from the engine: census
census=Table('census',metadata,autoload=True,autoload_with=engine)

# Biuld select statement for census table: stmt
# syntax for select statement: select([table_name]) # select all columns from census table
stmt = select([census])  # select all columns from census table using select() function

#print the emitted statement to see the SQL emitted
print(stmt)

# Execute the statement and print the results
results=connection.execute(stmt).fetchmany(size=10) # fetchmany() returns the first n rows of a query result. size is the number of rows to be returned.

# Print results
print(results)