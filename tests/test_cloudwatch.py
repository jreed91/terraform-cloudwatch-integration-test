import pytest
import datetime
import time

@pytest.fixture
def cloudwatch_test(cloudwatch_client):
    cloudwatch_client.describe_alarms()
    yield


def test_get_alarm(cloudwatch_client, cloudwatch_test):
    alarm_name = cloudwatch_client.describe_alarms()[
                                                   'MetricAlarms'][0]['AlarmName']
    assert "my-alarm-3" in alarm_name


def test_alarm_is_breaching(cloudwatch_client, cloudwatch_test):
    response = cloudwatch_client.put_metric_data(
    Namespace='test',
    MetricData=[
        {
            'MetricName': 'Orders',
            'Value': 1},
    ])
    time.sleep(10)
    alarm_state = cloudwatch_client.describe_alarms()['MetricAlarms'][0]['StateValue']
    assert "ALARM" in alarm_state

