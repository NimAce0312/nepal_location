# Nepal Location Data Repository

This repository contains Python scripts to store location data of Nepal, specifically provinces, districts, and municipalities, in a MongoDB database. The data is sourced from Wikipedia as of 2022 and might not reflect the current state.

## Files

1. **state.py**: This script stores the names of provinces of Nepal in MongoDB.
2. **district.py**: This script stores the districts of the corresponding provinces in MongoDB.
3. **municipality.py**: This script stores the municipalities of the corresponding districts in MongoDB.

## Usage

1. Clone the repository to your local machine.
2. Ensure you have MongoDB installed and running locally on your machine.
3. Install the required Python packages (`pymongo`) if not already installed. You can do this by running `pip install pymongo`.
4. Run each Python script (`state.py`, `district.py`, `municipality.py`) to populate the respective data into your MongoDB database.

## Note

- Make sure to replace the MongoDB connection string (`"mongodb://localhost:27017/"`) in each Python script with your actual connection string if necessary.
- The JSON data in each script is as follows:
    - `state.py`: Contains data about provinces.
    - `district.py`: Contains data about districts.
    - `municipality.py`: Contains data about municipalities.

## Data Source

The data was sourced from Wikipedia in 2022.

## Data Structure

### Province Data
- `province_id`: Unique identifier for the province.
- `formal_name`: Formal name of the province.
- `province_name`: Commonly used name of the province.

### District Data
- `district_id`: Unique identifier for the district.
- `district_name`: Name of the district.
- `province_id`: ObjectID referencing the corresponding province in MongoDB.

### Municipality Data
- `municipality_id`: Unique identifier for the municipality.
- `municipality_name`: Name of the municipality.
- `district_id`: ObjectID referencing the corresponding district in MongoDB.
