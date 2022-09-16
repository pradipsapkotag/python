from sqlalchemy import create_engine,select,Table,metadata
engine = create_engine('mysql:///census.sqlite')  #census.sqlite is database name
connection = engine.connect()
census = Table('census',metadata,autoload =True,autoload_with = engine)
# Define a list of states for which we want results
states = ['New York', 'California', 'Texas']

# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in connection.execute(stmt):
    print(result.state, result.pop2000)
