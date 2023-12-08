import pymongo
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
database = client["location"]  # Replace with your actual database name
collection = database["provinces"]  # Replace with your actual collection name

# Your JSON data
json_data = [
    {
        "province_id": 4,
        "formal_name": "Province no. 4",
        "province_name": "Gandaki Pradesh",
    },
    {
        "province_id": 6,
        "formal_name": "Province no. 6",
        "province_name": "Karnali Pradesh",
    },
    {
        "province_id": 1,
        "formal_name": "Province no. 1",
        "province_name": "Koshi Pradesh",
    },
    {
        "province_id": 2,
        "formal_name": "Province no. 2",
        "province_name": "Madhesh Pradesh",
    },
    {
        "province_id": 3,
        "formal_name": "Province no. 3",
        "province_name": "Bagmati Pradesh",
    },
    {
        "province_id": 5,
        "formal_name": "Province no. 5",
        "province_name": "Lumbini Pradesh",
    },
    {
        "province_id": 7,
        "formal_name": "Province no. 7",
        "province_name": "Sudurpashchim Pradesh",
    },
]

# Create a new file to store province_id and objectid mappings
with open("state.txt", "w") as state_file:
    for data in json_data:
        # Insert data into MongoDB
        result = collection.insert_one(
            {"initialName": data["formal_name"], "provinceName": data["province_name"]}
        )

        # Write province_id and objectid to the file
        state_file.write(f"{data['province_id']}, {result.inserted_id}\n")

# Close the MongoDB connection
client.close()
