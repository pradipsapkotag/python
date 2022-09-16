# Import create_engine, MetaData, and Table
from sqlalchemy import create_engine, MetaData, Table

# Create engine: engine
engine = create_engine('sqlite:///census.sqlite')

# Create a metadata object: metadata
metadata = MetaData()

# Reflect census table via engine: census
# fromat table('table_name',metadata,autoload=True,autoload_with=engine)
census = Table('census',metadata,autoload=True,autoload_with=engine) # autoload_with is used to specify the engine to use for loading the table metadata from the database. 

#reflection is the process of reading the database and building the metadata based on that information. It's the opposite of creating a Table by hand and is very useful for working with existing databases.

# Print census table metadata
print(repr(census))