import json
import requests

def lambda_handler(event, context):
    # Define the API endpoint
    api_url = "https://api.restful-api.dev/objects"

    # Make the GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': json.dumps({'error': 'Failed to fetch data'})
        }