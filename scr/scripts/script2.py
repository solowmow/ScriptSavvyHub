# script2.py - ScriptSavvyHub

import os
import json

# Function to read a JSON file
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {file_path}")
        return None

# Function to write data to a JSON file
def write_to_json_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"Data successfully written to: {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Read sample JSON data
file_path = 'data/sample.json'
json_data = read_json_file(file_path)

if json_data:
    # Display the loaded JSON data
    print("Loaded JSON data:")
    print(json.dumps(json_data, indent=4))

    # Add advanced functionalities
    # 1. Data manipulation - Adding a new key-value pair
    json_data['new_key'] = 'new_value'

    # 2. Error handling - Trying to access a non-existent key
    try:
        non_existent = json_data['non_existent_key']
    except KeyError:
        print("Key 'non_existent_key' does not exist.")

    # 3. File handling - Create a directory if it doesn't exist
    directory_path = 'output/'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory created: {directory_path}")

    # 4. Data manipulation - Sorting keys in JSON data
    sorted_json_data = {k: json_data[k] for k in sorted(json_data)}
    
    # 5. File handling - Writing modified data to a new JSON file
    new_file_path = 'output/modified_data.json'
    write_to_json_file(sorted_json_data, new_file_path)

    print("Advanced functionalities executed successfully.")
# Data validation and cleaning
if 'email' in json_data:
    email = json_data['email']
    if '@' not in email or '.' not in email:
        print("Invalid email format.")
import logging

logging.basicConfig(filename='script_log.log', level=logging.INFO)
try:
    # Your code here
except Exception as e:
    logging.error(f"An error occurred: {e}")
from multiprocessing import Pool

# Define a function for multiprocessing
def process_data(data):
    # Process each item in data concurrently
    # Your processing code here

if __name__ == '__main__':
    data_to_process = json_data['data']
    with Pool() as pool:
        pool.map(process_data, data_to_process)
import requests

url = 'https://api.example.com/data'
response = requests.get(url)
if response.status_code == 200:
    api_data = response.json()
    # Process the received API data
import requests

url = 'https://api.example.com/data'
response = requests.get(url)
if response.status_code == 200:
    api_data = response.json()
    # Process the received API data

# Continuing from the previous code...

# 6. Data analysis - Calculate statistics from JSON data
def calculate_statistics(data):
    if isinstance(data, dict):
        # Count the number of keys in the JSON data
        num_keys = len(data.keys())
        print(f"Number of keys in JSON data: {num_keys}")

        # Calculate the average length of values in the JSON data
        values_lengths = [len(str(value)) for value in data.values()]
        if values_lengths:
            average_length = sum(values_lengths) / len(values_lengths)
            print(f"Average length of values: {average_length:.2f} characters")
    else:
        print("Invalid data format for statistics calculation.")

# 7. Data encryption - Encrypt sensitive information using hashlib
import hashlib

def encrypt_data(data):
    if isinstance(data, dict):
        # Encrypt sensitive information using SHA-256 hashing
        encrypted_data = {key: hashlib.sha256(str(value).encode()).hexdigest() for key, value in data.items()}
        return encrypted_data
    else:
        print("Invalid data format for encryption.")
        return None

# 8. File handling - Append data to an existing file
def append_to_file(data, file_path):
    try:
        with open(file_path, 'a') as file:
            file.write(json.dumps(data, indent=4))
            print(f"Data appended to file: {file_path}")
    except Exception as e:
        print(f"Error appending data to file: {e}")

# 9. Error handling - Custom exceptions for specific scenarios
class CustomDataError(Exception):
    pass

def process_data(data):
    try:
        # Simulating a specific data processing scenario
        if len(data) < 3:
            raise CustomDataError("Insufficient data for processing")
        else:
            print("Data processing completed successfully.")
    except CustomDataError as e:
        print(f"Custom Data Error: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")

# 10. Data validation - Ensure data meets certain criteria before processing
def validate_data(data):
    if isinstance(data, dict):
        # Check if specific keys exist in the data
        required_keys = ['key1', 'key2', 'key3']
        missing_keys = [key for key in required_keys if key not in data]
        if missing_keys:
            print(f"Missing keys: {', '.join(missing_keys)}")
        else:
            print("All required keys are present.")
    else:
        print("Invalid data format for validation.")

# Example usage of the added functionalities
calculate_statistics(json_data)
encrypted_data = encrypt_data(json_data)
append_to_file(encrypted_data, 'output/encrypted_data.txt')
process_data(json_data)
validate_data(json_data)

import sqlite3

# Connect to a database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create a table for JSON data
cursor.execute('''CREATE TABLE IF NOT EXISTS jsonData (
                    id INTEGER PRIMARY KEY,
                    jsonData TEXT
                )''')

# Insert JSON data into the database
cursor.execute('INSERT INTO jsonData (jsonData) VALUES (?)', (json.dumps(json_data),))
conn.commit()

# Retrieve JSON data from the database
cursor.execute('SELECT jsonData FROM jsonData WHERE id = ?', (1,))
retrieved_data = cursor.fetchone()
print(f"Retrieved data: {retrieved_data[0]}")
# ... (Previous code)

# 6. Data manipulation - Removing a specific key from JSON data
if 'key_to_remove' in json_data:
    del json_data['key_to_remove']
    print("Key 'key_to_remove' removed from JSON data.")
else:
    print("Key 'key_to_remove' does not exist.")

# 7. Data manipulation - Merging two JSON dictionaries
another_data = {'new_key_2': 'new_value_2', 'additional_key': 'additional_value'}
json_data.update(another_data)
print("Two JSON dictionaries merged.")

# 8. Error handling - Using try-except-else block
try:
    operation_result = 10 / 0  # Attempting a division by zero
except ZeroDivisionError:
    print("Error: Division by zero.")
else:
    print("Operation result:", operation_result)

# 9. File handling - Reading contents of a directory
directory_contents = os.listdir('output/')
print("Contents of 'output/' directory:", directory_contents)

# 10. Data manipulation - Filtering JSON data based on a condition
filtered_data = {k: v for k, v in json_data.items() if isinstance(v, str)}
print("Filtered JSON data (string values only):", filtered_data)

# ... (Rest of the code)
# ... (Previous code remains unchanged)

# 6. Data manipulation - Filtering data based on a condition
def filter_data_by_condition(data, condition):
    filtered_data = {k: v for k, v in data.items() if condition(k, v)}
    return filtered_data

# 7. Error handling - Handling specific exceptions with custom messages
def custom_error_handling():
    try:
        # Perform an operation that may raise an exception
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error occurred: {e}. Please check the operation.")

# 8. File handling - Checking file permissions
def check_file_permissions(file_path):
    try:
        access_mode = os.access(file_path, os.R_OK)
        if access_mode:
            print(f"File '{file_path}' is readable.")
        else:
            print(f"File '{file_path}' is not readable or does not exist.")
    except Exception as e:
        print(f"Error checking file permissions: {e}")

# 9. Data manipulation - Convert data to a different format (e.g., CSV)
import csv

def convert_to_csv(data, csv_file):
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for key, value in data.items():
                writer.writerow([key, value])
            print(f"Data successfully written to CSV file: {csv_file}")
    except Exception as e:
        print(f"Error converting data to CSV: {e}")

# 10. File handling - Deleting files
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError as e:
        print(f"Permission denied: {e}. Unable to delete file.")

# Execution of additional functionalities
if json_data:
    # ... (Previous code remains unchanged)
    # Call the additional functionalities here
    filtered_data = filter_data_by_condition(json_data, lambda k, v: isinstance(v, str))
    print("Filtered data based on condition (string values only):")
    print(filtered_data)

    custom_error_handling()

    file_to_check = 'data/sample.json'
    check_file_permissions(file_to_check)

    csv_output_file = 'output/data.csv'
    convert_to_csv(json_data, csv_output_file)

    file_to_delete = 'output/modified_data.json'
    delete_file(file_to_delete)

    print("Additional advanced functionalities executed successfully.")
# ... (Previous code remains unchanged)

# 6. Data manipulation - Removing a specific key from the JSON data
key_to_remove = 'unwanted_key'
if key_to_remove in json_data:
    del json_data[key_to_remove]
    print(f"Key '{key_to_remove}' removed from JSON data.")

# 7. File handling - Check file existence and permissions
file_to_check = 'data/sample.json'
if os.path.exists(file_to_check):
    if os.access(file_to_check, os.R_OK):
        print(f"File '{file_to_check}' exists and is readable.")
    else:
        print(f"File '{file_to_check}' is not readable.")
else:
    print(f"File '{file_to_check}' does not exist.")

# 8. Data manipulation - Merge two JSON objects
other_json_data = {'key1': 'value1', 'key2': 'value2'}
merged_json_data = {**json_data, **other_json_data}
print("Merged JSON data:")
print(json.dumps(merged_json_data, indent=4))

# 9. File handling - Renaming a file
old_file_name = 'data/sample.json'
new_file_name = 'data/renamed_sample.json'
try:
    os.rename(old_file_name, new_file_name)
    print(f"File '{old_file_name}' renamed to '{new_file_name}'.")
except FileNotFoundError:
    print(f"File '{old_file_name}' not found.")
except FileExistsError:
    print(f"File '{new_file_name}' already exists.")

# 10. Error handling - Handling different types of exceptions
try:
    result = 10 / 0  # ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
except Exception as e:
    print(f"Unhandled error occurred: {e}")
else:
    print("No error occurred.")
finally:
    print("Execution completed.")

