import json
from datetime import datetime
import pytz

def lambda_handler(event, context):
    timezone = pytz.timezone('Europe/Rome')
    ora_italia = datetime.now(timezone)
    risposta = {
        'ora': ora_italia.strftime('%H:%M:%S'),
        'data': ora_italia.strftime('%d/%m/%Y'),
        'timezone': 'Europe/Rome',
        'messaggio': 'Lab 4 funzionante'
    }
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'application/json' },
        'body': json.dumps(risposta)
    }
