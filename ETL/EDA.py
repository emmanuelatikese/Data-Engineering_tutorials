import pandas as pd

df = pd.read_csv("scooter.csv")

# #checking out check columns or header
# print(df.columns)

# #checking the type
# print(df.dtypes)


# #size 
# print(df.size)


# #showing some rows in the csv
# print(df.head)

#to show the number of column
# pd.set_option('display.max_columns', 500)

#showing tail of the dataframe
# print(df.tail)

#this give of random samples of data of 10 from df
# print(df.sample(10))

#just taking data from 0 - 19
# print(df[:20])

#just taking data from duration header only
# print(df['DURATION'])

#taking data from one that one header
# print(df[["trip_id", "DURATION", "user_id"]])


#this check a specific row or position and gives everything in it
# print(df.loc[234])

#this is used to find rows with the attribute with the same val
# print(df.where(df['user_id'] == 8417864))

# checks rows with both attributes vals
# one = df['user_id'] == 8417864
# two = df['trip_ledger_id'] == 1488838
# df.where(one & two)


#this will give you just a row with more than two conditions
one = df['user_id'] == 8417864
two = df['trip_ledger_id'] == 1488838
print(df[one & two])



