import pymongo
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
database = client["location"]  # Replace with your actual database name
district_collection = database["districts"]  # Replace with your actual district collection name

# Read the state.txt file to get province_id and corresponding objectid mappings
province_id_mapping = {}
with open("state.txt", "r") as state_file:
    for line in state_file:
        province_id, objectid = line.strip().split(", ")
        province_id_mapping[province_id] = objectid

# Your district JSON data
district_json_data = [
 {
  "district_id": 1,
  "district_name": "Bhojpur",
  "province_id": 1
 },
 {
  "district_id": 2,
  "district_name": "Dhankuta",
  "province_id": 1
 },
 {
  "district_id": 3,
  "district_name": "Ilam",
  "province_id": 1
 },
 {
  "district_id": 4,
  "district_name": "Jhapa",
  "province_id": 1
 },
 {
  "district_id": 5,
  "district_name": "Khotang",
  "province_id": 1
 },
 {
  "district_id": 6,
  "district_name": "Morang",
  "province_id": 1
 },
 {
  "district_id": 7,
  "district_name": "Okhaldhunga",
  "province_id": 1
 },
 {
  "district_id": 8,
  "district_name": "Panchthar",
  "province_id": 1
 },
 {
  "district_id": 9,
  "district_name": "Sankhuwasabha",
  "province_id": 1
 },
 {
  "district_id": 10,
  "district_name": "Solukhumbu",
  "province_id": 1
 },
 {
  "district_id": 11,
  "district_name": "Sunsari",
  "province_id": 1
 },
 {
  "district_id": 12,
  "district_name": "Taplejung",
  "province_id": 1
 },
 {
  "district_id": 13,
  "district_name": "Terhathum",
  "province_id": 1
 },
 {
  "district_id": 14,
  "district_name": "Udayapur",
  "province_id": 1
 },
 {
  "district_id": 15,
  "district_name": "Saptari",
  "province_id": 2
 },
 {
  "district_id": 16,
  "district_name": "Siraha",
  "province_id": 2
 },
 {
  "district_id": 17,
  "district_name": "Dhanusha",
  "province_id": 2
 },
 {
  "district_id": 18,
  "district_name": "Mahottari",
  "province_id": 2
 },
 {
  "district_id": 19,
  "district_name": "Sarlahi",
  "province_id": 2
 },
 {
  "district_id": 20,
  "district_name": "Bara",
  "province_id": 2
 },
 {
  "district_id": 21,
  "district_name": "Parsa",
  "province_id": 2
 },
 {
  "district_id": 22,
  "district_name": "Rautahat",
  "province_id": 2
 },
 {
  "district_id": 23,
  "district_name": "Sindhuli",
  "province_id": 3
 },
 {
  "district_id": 24,
  "district_name": "Ramechhap",
  "province_id": 3
 },
 {
  "district_id": 25,
  "district_name": "Dolakha",
  "province_id": 3
 },
 {
  "district_id": 26,
  "district_name": "Bhaktapur",
  "province_id": 3
 },
 {
  "district_id": 27,
  "district_name": "Dhading",
  "province_id": 3
 },
 {
  "district_id": 28,
  "district_name": "Kathmandu",
  "province_id": 3
 },
 {
  "district_id": 29,
  "district_name": "Kavrepalanchowk",
  "province_id": 3
 },
 {
  "district_id": 30,
  "district_name": "Lalitpur",
  "province_id": 3
 },
 {
  "district_id": 31,
  "district_name": "Nuwakot",
  "province_id": 3
 },
 {
  "district_id": 32,
  "district_name": "Rasuwa",
  "province_id": 3
 },
 {
  "district_id": 33,
  "district_name": "Sindhupalchok",
  "province_id": 3
 },
 {
  "district_id": 34,
  "district_name": "Chitwan",
  "province_id": 3
 },
 {
  "district_id": 35,
  "district_name": "Makwanpur",
  "province_id": 3
 },
 {
  "district_id": 36,
  "district_name": "Baglung",
  "province_id": 4
 },
 {
  "district_id": 37,
  "district_name": "Gorkha",
  "province_id": 4
 },
 {
  "district_id": 38,
  "district_name": "Kaski",
  "province_id": 4
 },
 {
  "district_id": 39,
  "district_name": "Lamjung",
  "province_id": 4
 },
 {
  "district_id": 40,
  "district_name": "Manang",
  "province_id": 4
 },
 {
  "district_id": 41,
  "district_name": "Mustang",
  "province_id": 4
 },
 {
  "district_id": 42,
  "district_name": "Myagdi",
  "province_id": 4
 },
 {
  "district_id": 43,
  "district_name": "Nawalpur",
  "province_id": 4
 },
 {
  "district_id": 44,
  "district_name": "Parbat",
  "province_id": 4
 },
 {
  "district_id": 45,
  "district_name": "Syangja",
  "province_id": 4
 },
 {
  "district_id": 46,
  "district_name": "Tanahun",
  "province_id": 4
 },
 {
  "district_id": 47,
  "district_name": "Kapilvastu",
  "province_id": 5
 },
 {
  "district_id": 48,
  "district_name": "Parasi",
  "province_id": 5
 },
 {
  "district_id": 49,
  "district_name": "Rupandehi",
  "province_id": 5
 },
 {
  "district_id": 50,
  "district_name": "Arghakhanchi",
  "province_id": 5
 },
 {
  "district_id": 51,
  "district_name": "Gulmi",
  "province_id": 5
 },
 {
  "district_id": 52,
  "district_name": "Palpa",
  "province_id": 5
 },
 {
  "district_id": 53,
  "district_name": "Dang",
  "province_id": 5
 },
 {
  "district_id": 54,
  "district_name": "Pyuthan",
  "province_id": 5
 },
 {
  "district_id": 55,
  "district_name": "Rolpa",
  "province_id": 5
 },
 {
  "district_id": 56,
  "district_name": "Eastern Rukum",
  "province_id": 5
 },
 {
  "district_id": 57,
  "district_name": "Banke",
  "province_id": 5
 },
 {
  "district_id": 58,
  "district_name": "Bardiya",
  "province_id": 5
 },
 {
  "district_id": 59,
  "district_name": "Western Rukum",
  "province_id": 6
 },
 {
  "district_id": 60,
  "district_name": "Salyan",
  "province_id": 6
 },
 {
  "district_id": 61,
  "district_name": "Dolpa",
  "province_id": 6
 },
 {
  "district_id": 62,
  "district_name": "Humla",
  "province_id": 6
 },
 {
  "district_id": 63,
  "district_name": "Jumla",
  "province_id": 6
 },
 {
  "district_id": 64,
  "district_name": "Kalikot",
  "province_id": 6
 },
 {
  "district_id": 65,
  "district_name": "Mugu",
  "province_id": 6
 },
 {
  "district_id": 66,
  "district_name": "Surkhet",
  "province_id": 6
 },
 {
  "district_id": 67,
  "district_name": "Dailekh",
  "province_id": 6
 },
 {
  "district_id": 68,
  "district_name": "Jajarkot",
  "province_id": 6
 },
 {
  "district_id": 69,
  "district_name": "Kailali",
  "province_id": 7
 },
 {
  "district_id": 70,
  "district_name": "Achham",
  "province_id": 7
 },
 {
  "district_id": 71,
  "district_name": "Doti",
  "province_id": 7
 },
 {
  "district_id": 72,
  "district_name": "Bajhang",
  "province_id": 7
 },
 {
  "district_id": 73,
  "district_name": "Bajura",
  "province_id": 7
 },
 {
  "district_id": 74,
  "district_name": "Kanchanpur",
  "province_id": 7
 },
 {
  "district_id": 75,
  "district_name": "Dadeldhura",
  "province_id": 7
 },
 {
  "district_id": 76,
  "district_name": "Baitadi",
  "province_id": 7
 },
 {
  "district_id": 77,
  "district_name": "Darchula",
  "province_id": 7
 }
]

# Create a new file to store district_id and objectid mappings
with open("district.txt", "w") as district_file:
    for data in district_json_data:
        # Replace province_id with corresponding objectid from state.txt
        province_id = str(data["province_id"])
        if province_id in province_id_mapping:
            data["province_id"] = province_id_mapping[province_id]

            # Insert data into MongoDB
            result = district_collection.insert_one({"districtName": data["district_name"], "provinceID": data["province_id"]})

            # Write district_id and objectid to the file
            district_file.write(f"{data['district_id']}, {result.inserted_id}\n")

# Close the MongoDB connection
client.close()
