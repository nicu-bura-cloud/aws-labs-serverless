import boto3
import urllib.parse

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    
    print(f"File caricato: {key} nel bucket: {bucket}")
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')
        
        print("Contenuto del file:")
        print(content)
        
        return {
            'statusCode': 200,
            'body': f'File {key} processato correttamente'
        }
        
    except Exception as e:
        print(f"Errore: {str(e)}")
        raise e
