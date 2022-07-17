
import boto3
import os
import pytest

endpoint_url = "http://localhost:4566"


@pytest.fixture
def cloudwatch_client():
    conn = boto3.client("cloudwatch", endpoint_url=endpoint_url)
    yield conn
