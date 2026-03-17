import boto3
import json

secret_name = "myapp/db_credentials"
region_name = "us-east-1"

client = boto3.client("secretsmanager", region_name=region_name)

response = client.get_secret_value(SecretId=secret_name)

secret_string = response["SecretString"]

secret = json.loads(secret_string)

print("Fetching secret from AWS Secrets Manager")

print(secret)
