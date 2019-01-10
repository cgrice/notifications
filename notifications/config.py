import boto3
import json
import os

def get_config():
    bucket = os.environ.get("NOTIFICATIONS_CONFIG_BUCKET", "nobucket")
    key = os.environ.get("NOTIFICATIONS_CONFIG_FILE", "config.json")
    s3 = boto3.resource("s3")
    obj = s3.Object(bucket, key)
    config = obj.get()["Body"].read().decode("utf-8")
    return json.loads(config)
