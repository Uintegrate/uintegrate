import json
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

def create_service(access_token, API_SERVICE_NAME, API_VERSION):
    try:
        creds_data = json.loads(access_token)
        creds = Credentials.from_authorized_user_info(creds_data)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        service = build(API_SERVICE_NAME, API_VERSION,
                        credentials=creds, static_discovery=False)
        return service
    except Exception as e:
        raise Exception(f'Failed to create service instance for docs')   
    
def googledocs_create(access_token,params):
    try:
        if 'title' in params:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            service = create_service(access_token,'docs','v1')
            doc = service.documents().create(body=data).execute()
            return doc
        else:
            raise Exception('Missing parameters')
    except Exception as e:
        raise Exception(str(e))  

def googledocs_get(access_token,params):
    try:
        if 'documentId' in params:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            service = create_service(access_token,'docs','v1')
            document = service.documents().get(**data).execute()       
            return document
        else:
            raise Exception('Missing parameters')
    except Exception as e:
        raise Exception(str(e)) 
    
def googledocs_update(access_token,params):
    try:
        if 'documentId' in params and 'requests' in params:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            service = create_service(access_token,'docs','v1')
            document = service.documents().batchUpdate(documentId=data['documentId'], body={'requests': data['requests']}).execute()       
            return document
        else:
            raise Exception('Missing parameters')
    except Exception as e:
        raise Exception(str(e))  