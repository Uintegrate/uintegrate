from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from googleapiclient.errors import Error
import json
def create_service(ACCESS_TOKEN,API_SERVICE_NAME,API_VERSION):
    try:
        creds_data = json.loads(ACCESS_TOKEN)
        creds = Credentials.from_authorized_user_info(creds_data)
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        service = build(API_SERVICE_NAME,API_VERSION,
                        credentials=creds, static_discovery=False)
        return service
    except Exception as e:
        raise Exception(f'Failed to create service instance {e}')
    
def Google_Calendar_get_all_events(ACCESS_TOKEN,API_SERVICE_NAME,API_VERSION,params):
  try:
        if "calendarId" in params:
         events = {}
         for key, value in params.items():
            if value:
                events[key] = value
         service = create_service(ACCESS_TOKEN, API_SERVICE_NAME, API_VERSION)
         response = service.events().list(**events).execute()
         return response
        else:
            raise Exception("email required")
  except Exception as error:
        raise Exception(error)
      
def Google_Calendar_create_event(ACCESS_TOKEN,API_SERVICE_NAME,API_VERSION,params):
 try:
  if 'start' in params and 'end' in params and 'calendarId' in params:
   to_create = {}
   keys_to_skip = ["calendarId"]
   for key, value in params.items():
     if key in keys_to_skip:
            continue
     if value:
         to_create[key] = value
   service=create_service(ACCESS_TOKEN,API_SERVICE_NAME,API_VERSION)
   response = service.events().insert(calendarId=params['calendarId'],body=to_create).execute()
   return response
  else:
      raise Exception("missing input data")
 except Exception as error:
        raise Exception(error)

def Google_Calendar_get_event(ACCESS_TOKEN,API_SERVICE_NAME,API_VERSION,params):
 try:
  if 'calendarId' in params and 'eventId' in params:
    service=create_service(ACCESS_TOKEN,API_SERVICE_NAME,API_VERSION)
    response = service.events().get(calendarId=params['calendarId'], eventId=params['eventId']).execute()
    return response
  else:
      raise Exception("missing input data")
  
 except Exception as error:
        raise Exception(error)

def Google_Calendar_delete_event(ACCESS_TOKEN,API_SERVICE_NAME,API_VERSION,params):
 try:
  if 'calendarId' in params and 'eventId' in params:
   service=create_service(ACCESS_TOKEN,API_SERVICE_NAME,API_VERSION)
   response = service.events().delete(calendarId=params['calendarId'], eventId=params['eventId']).execute()
   return f"Event with ID : {params['eventId']} deleted successfully "
  else:
      raise Exception("missing input data")
 except Exception as error:
        raise Exception(error)

def Google_Calendar_update_event(ACCESS_TOKEN,API_SERVICE_NAME,API_VERSION,params):
  try:
    if 'calendarId' in params and 'eventId' in params and 'start' in params and 'end' in params:
      to_update = {}
      keys_to_skip = ["calendarId","eventId"]
      for key, value in params.items():
       if key in keys_to_skip:
              continue
       if value:
          to_update[key] = value
      service=create_service(ACCESS_TOKEN,API_SERVICE_NAME,API_VERSION)
      response = service.events().update(calendarId=params['calendarId'], eventId=params['eventId'], body=to_update).execute()
      return response 
    else:
        raise Exception("Missing input data")
  
  except Exception as error:
        raise Exception(error)

def Google_Calendar_get_calendar(ACCESS_TOKEN,API_SERVICE_NAME,API_VERSION,params):
 try:
    if 'calendarId' in params:
      service=create_service(ACCESS_TOKEN,API_SERVICE_NAME,API_VERSION)
      response = service.calendars().get(calendarId=params['calendarId']).execute()
      return response
    else:
        raise Exception("missing calendar email")
 except Exception as error:
        raise Exception(error)
