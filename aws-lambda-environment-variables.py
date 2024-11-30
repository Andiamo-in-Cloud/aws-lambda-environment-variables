# Andiamo in Cloud: il canale in Italiano per imparare a sviluppare applicazioni in Cloud
# il CANALE https://www.youtube.com/@andiamoincloud
# il VIDEO di questo ESEMPIO: https://youtu.be/5hPZ_S2Jn18

import json, os

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(os.environ.get('GREETING'))
    }
