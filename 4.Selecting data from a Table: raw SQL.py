#by APP
# Import create_engine function
from sqlalchemy import create_engine, MetaData, Table

# Create an engine to the census database
connection = create_engine('sqlite:///census.sqlite')

#build select statement for census table:stmt
# syntax for select statement: select column_name from table_name
stmt = 'SELECT * FROM census' # select all columns from census table

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall() # execute() method on engine returns a ResultProxy and fetchall() method on ResultProxy returns a list of tuples. #fetchall() returns all the rows of a query result. 

# Print results
print(results)