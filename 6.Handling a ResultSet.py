#by APP
#SQlalchemy allows list style access to the results of a query
#get the first row of the results by using an index on the results object: first_row
first_row=results[0]

#print the first row of the results
print(first_row)

#print the first column of the first row by using an index
print(first_row[0])

#print the 'state' column of the first row by using its name
print(first_row['state'])