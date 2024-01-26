import json
from io import BytesIO
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaIoBaseUpload
import requests

status=[200, 201, 202, 204, 206, 207, 208]

def create_service(access_token, API_SERVICE_NAME, API_VERSION):
    try:
        creds_data = json.loads(access_token)
        creds = Credentials.from_authorized_user_info(creds_data)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        service = build(API_SERVICE_NAME, API_VERSION,
                        credentials=creds, static_discovery=False)
        print(API_SERVICE_NAME, API_VERSION, 'service created successfully')
        return service
    except Exception as e:
        print(f'Failed to create service instance for {API_SERVICE_NAME}')
        raise Exception(
            f'Failed to create service instance for {API_SERVICE_NAME}')
 
def googledrive_create_folder(access_token,params):
    try:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            service = create_service(access_token,'drive', 'v3')
            response = service.files().create(**data).execute()
            return response
    except Exception as e:
        raise Exception(str(e))
      
def googledrive_delete_file(access_token,params):
    try:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            service = create_service(access_token,'drive', 'v3')
            if 'body'in data :
                response = service.files().update(**data).execute()
                return response
            else:
                response = service.files().delete(**data).execute()
                return "Folder deleted successfully"
    except Exception as e:
        raise Exception(str(e))
    
def googledrive_share_file(access_token,params):
    try:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            service = create_service(access_token,'drive', 'v3')
            response = service.permissions().create(**data).execute()
            return response 
    except Exception as e:
        raise Exception(str(e))
    
def googledrive_copy_file(access_token,params):
    try:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            service = create_service(access_token,'drive', 'v3')
            response = service.files().copy(**data).execute()
            return response 
    except Exception as e:
        raise Exception(str(e))
       
def googledrive_move_file(access_token,params):
    try:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            service = create_service(access_token,'drive', 'v3')
            response = service.files().update(**data).execute()
            return response 
    except Exception as e:
        raise Exception(str(e))

def googledrive_create_file_text(access_token,params):
    try:
            data = {}
            for key, value in params.items():
                if key=='content':
                     continue
                if value:
                    data[key] = value
            service = create_service(access_token,'drive', 'v3')
            media = MediaIoBaseUpload(
            BytesIO(params['content'].encode('utf-8')),
            mimetype='text/plain',
            resumable=True
        )
            response = service.files().create(**data,media_body=media).execute()
            return response
    except Exception as e:
        raise Exception(str(e))    

def googledrive_upload_file(access_token,params):
    try:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            service = create_service(access_token,'drive', 'v3')
            if 'data' in data:
                media = MediaIoBaseUpload(BytesIO(data['data']), mimetype='application/octet-stream', resumable=True)
                response = service.files().create(body=data['body'],media_body=media).execute()
                return response
            elif 'url' in data:
                 response = requests.get(data['url'])
                 if response.status_code in status:
                    file_content = response.content
                    media = MediaIoBaseUpload(BytesIO(file_content), mimetype='application/octet-stream', resumable=True)
                    url = service.files().create(body=data['body'],media_body=media).execute()
                    return url
    except Exception as e:
        raise Exception(str(e))
    

def googledrive_update_file(access_token,params):
    try:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            service = create_service(access_token,'drive', 'v3')
            file_metadata = service.files().get(fileId=data['fileId']).execute()
            new_file_name = data['body']['name'] if 'name' in data['body'] and data['body']['name']!='' else file_metadata['name']
            data['body']['name']= new_file_name
            media = MediaIoBaseUpload(BytesIO(data['data']), mimetype='application/octet-stream', resumable=True)
            response = service.files().update(fileId=data['fileId'],body=data['body'],media_body=media).execute()
            return response
    except Exception as e:
        raise Exception(str(e))
       
def googledrive_get_many_files(access_token,params):
    try:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            query_parts = []
            query_parts.append("mimeType != 'application/vnd.google-apps.folder'") 
            if 'query' in data:
                query_parts.append(data['query'])
            if 'name' in data:
                query_parts.append(f"name contains '{data['name']}'")
            if 'type' in data:
                type_queries = []
                for type_value in data['type']:
                    type_queries.append(f"({type_value})")
                type_query = " or ".join(type_queries)
                type_query = f"({type_query})"
                query_parts.append(type_query)
            if 'parent' in data:
                 query_parts.append((f"'{data['parent']}' in parents"))
            if 'trashed' in data:
                query_parts.append(f"trashed={data['trashed']}")
            query = " and ".join(query_parts)
            service = create_service(access_token,'drive', 'v3')
            if not query:
                files = service.files().list(**data).execute()
            else:
                data2 = {}
                for key, value in data.items():
                    if key=='name':
                        continue
                    if key=='type':
                         continue
                    if key=='query':
                         continue
                    if key=='parent':
                         continue
                    if key=='trashed':
                         continue
                    if value:
                        data2[key] = value
                files = service.files().list(**data2,q=query).execute()
            return files
    except Exception as e:
        raise Exception(str(e))

def googledrive_get_many_folders(access_token,params):
    try:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            query_parts = []
            query_parts.append("mimeType ='application/vnd.google-apps.folder'") 
            if 'query' in data:
                query_parts.append(data['query'])
            if 'name' in data:
                query_parts.append(f"name contains '{data['name']}'")
            if 'parent' in data:
                 query_parts.append((f"'{data['parent']}' in parents"))
            if 'trashed' in data:
                query_parts.append(f"trashed={data['trashed']}")
            query = " and ".join(query_parts)
            service = create_service(access_token,'drive', 'v3')
            if not query:
                files = service.files().list(**data).execute()
            else:
                data2 = {}
                for key, value in data.items():
                    if key=='name':
                        continue
                    if key=='query':
                         continue
                    if key=='parent':
                         continue
                    if key=='trashed':
                         continue
                    if value:
                        data2[key] = value
                files = service.files().list(**data2,q=query).execute()
            return files
    except Exception as e:
        raise Exception(str(e))    
    
# def googledrive_download_file(access_token,params):
#     try:
#         data = {}
#         for key, value in params.items():
#             if value:
#                 data[key] = value
#         service = create_service(access_token, 'drive', 'v3')
#         file_metadata = service.files().get(fileId=data['fileId']).execute()
#         user_downloads_path = os.path.expanduser('~') 
#         destination_path = os.path.join(user_downloads_path, 'Downloads')
#         if 'name' in data:
#             destination = os.path.join(destination_path, data['name'])
#         elif 'name' not in data:
#             destination = os.path.join(destination_path, file_metadata['name'])
#         request = service.files().get_media(fileId=data['fileId'])
#         with open(destination, 'wb') as local_file:
#             downloader = MediaIoBaseDownload(local_file, request)
#             done = False
#             while not done:
#                 status, done = downloader.next_chunk()

#         return 'downloaded successfully'
#     except Exception as e:
#         raise Exception(str(e))