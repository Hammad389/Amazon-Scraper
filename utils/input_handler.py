import json

# MODULE TO HANDLE THE INPUT USER QUERIES
def load_queries(file_path='user_queries.json'):
    with open(file_path, 'r') as file:
        queries = json.load(file)
    return queries
