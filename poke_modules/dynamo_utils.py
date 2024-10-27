import boto3
from botocore.exceptions import ClientError

def upload_to_dynamodb(pokemon, table_name):
    """
    Uploads a Pokemon object to a specified DynamoDB table.

    Args:
        pokemon (Pokemon): An instance of the Pokemon class containing the data to upload.
        table_name (str): The name of the DynamoDB table to which the data will be uploaded.
    """
    # Initialize DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Prepare the item to be uploaded
    item = {
        'id': pokemon.id,
        'name': pokemon.name,
        'abilities': pokemon.abilities,
        'url': pokemon.url,
        'image_url': pokemon.image_url
    }

    # Attempt to insert the item into the DynamoDB table
    try:
        table.put_item(Item=item)
        print(f"Successfully uploaded {pokemon.name} (ID: {pokemon.id}) to DynamoDB.")
    except ClientError as e:
        print(f"Failed to upload {pokemon.name} to DynamoDB: {e.response['Error']['Message']}")
