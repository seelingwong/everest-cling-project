
"""
This module provides functionality to interact with Amazon Bedrock to obtain text embeddings.

Functions:
    get_aws_embedding(text): Sends a request to the Amazon Bedrock service to get the embedding vector for the given text.

Dependencies:
    - boto3
    - json

Usage:
    Ensure that the AWS credentials and profile are correctly configured before using this module.
"""
import json
import boto3

# Initialize Amazon Bedrock client
session = boto3.Session(profile_name='AWS-local-sso')

bedrock = session.client(service_name="bedrock-runtime",
                         region_name="ap-southeast-2")


def get_aws_embedding(text):
    response = bedrock.invoke_model(
        modelId="amazon.titan-embed-text-v2:0",  # Specify the embeddings model
        contentType="application/json",
        accept="application/json",
        body='{"inputText": "' + text + '"}'
    )
    embedding_vector = json.loads(response["body"].read())["embedding"]

    return embedding_vector
