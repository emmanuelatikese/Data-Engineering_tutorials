# import faker, csv

# creating a csv file and writing to it
# fake = faker.Faker()
# with open("createCsv.csv", "w") as f:
#     csvWriter = csv.writer(f)
#     csvWriter.writerow(["name", "age", "state", "zipcode"])
#     for x in range(1000):
#         csvWriter.writerow([fake.name(), fake.random_int(18, 100, 2), fake.street_address(),fake.zipcode()])
    
    
#reading from a csv file


# with open("createCsv.csv", "r") as f:
#     reader = csv.DictReader(f) #reading from a csv file
#     # header = next(reader) # this line of code skip the first line of rows containing values not headers but values 
#     # it seems the code know that it a csv file hence would treat the first row of the file as header.
#     for x in reader: print(x['name'])


# working with pandas lib using a csv file
# import pandas as pd
# df_csv = pd.read_csv("createCsv.csv")
# print(df_csv.head(10))

#creating my own dataframe and a csv file to store it
# import pandas as pd
# df = pd.DataFrame({"name": ['bob', 'marvis'], "age": [11, 12]})
# df.to_csv("anotherCsv.csv")


# working with json - writing and json
# from faker import Faker
# fake = Faker()
# data = {"record":[]}

# with open("createJson.json", 'w') as f:
#     for x in range(50):
#         var_data = {
#             "name": fake.name(), "age": fake.random_int(18, 80, 2)
#         }
#         data["record"].append(var_data)
#     import json
#     json.dump(data, f)


#working on json file and pandas

# #how to read a json
# import json
# with open("createJson.json", 'r') as f:
#     datafile = json.load(f) # first have to load the json file using the json lib inorder to read it.
#     print(datafile["record"])



#how to work with json and pandas
# import pandas as pd
# with open("createJson.json", "r") as f:
#     pdJson = pd.read_json(f) #convert json straight to dataframe
#     print(pdJson.head(10)) #dataframe
#     print(pdJson.head(2).to_json())
