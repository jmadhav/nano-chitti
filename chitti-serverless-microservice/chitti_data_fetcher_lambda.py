import boto3
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
resource = boto3.resource('dynamodb')


def get_recordset(device_id):
    logging.info(datetime.now().isoformat(timespec='microseconds') + "::get_recordset")
    try:
        table = resource.Table("IOTData")
        response = table.query(
            KeyConditionExpression=Key('device_id').eq(device_id)
        )
        items,  = response['Items'], response['count']
        return [items, count]
    except Exception as e:
        logging.error(datetime.now().isoformat(timespec='microseconds') + "::get_recordset::EXCEPTION:: %s" % str(e))
        return False

def lambda_handler(event, context):
    # TODO implement
    operation = event['httpMethod']
    if operation == "Get"
        if event['queryStringParameters']['device_id']:
            result = get_recordset(event['queryStringParameters']['device_id'])
            if result:
                return {"items": result[0], "count",result[1]}
            else:
                returm {"error": "Something went wrong while fetching data"}
        else:
