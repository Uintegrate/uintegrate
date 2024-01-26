from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import json


def create_service(access_token, API_SERVICE_NAME, API_VERSION):
    try:

        creds_data = json.loads(access_token)
        creds = Credentials.from_authorized_user_info(creds_data)
        if creds and creds.expired and creds.refresh_token:
            # in this case the token is expired and we need to get a new access token
            creds.refresh(Request())
        service = build(API_SERVICE_NAME, API_VERSION,
                        credentials=creds, static_discovery=False)

        print(API_SERVICE_NAME, API_VERSION, 'service created successfully')
        return service
    except Exception as e:
        print(e)
        print(f'Failed to create service instance for {API_SERVICE_NAME}')
        raise Exception(f'Failed to create service instance for {API_SERVICE_NAME}')


#############################################################################################################################

# Document Actions


def googleSheet_create_spreadsheet(access_token, API_SERVICE_NAME, API_VERSION, params):
    try:
        if "properties" in params and "title" in params["properties"] and params["properties"]["title"]:
            service = create_service(access_token, API_SERVICE_NAME, API_VERSION)
            spreadsheet = service.spreadsheets().create(body=params).execute()
            return spreadsheet
        else:
            raise SyntaxError("Missing input data")

    except Exception as error:
        raise SyntaxError(error)


def googleSheet_delete_spreadsheet(access_token, API_SERVICE_NAME, API_VERSION, params):
    try:
        if "spreadsheetId" in params:
            spreadsheet_id = params["spreadsheetId"]
            drive_service = create_service(access_token, API_SERVICE_NAME, API_VERSION)
            drive_service.files().delete(fileId=spreadsheet_id).execute()
            return {"Result": f"Deleted Spreadsheet ID: {spreadsheet_id}"}
        else:
            raise SyntaxError("Missing input data")

    except Exception as error:
        raise Exception(error)


def googleSheet_get_spreadsheet(access_token, API_SERVICE_NAME, API_VERSION, params):
    try:
        if "spreadsheetId" in params:
            id = params["spreadsheetId"]
            service = create_service(access_token, API_SERVICE_NAME, API_VERSION)
            response = service.spreadsheets().get(spreadsheetId=id).execute()
            return response
        else:
            raise SyntaxError("Missing input data")

    except Exception as error:
        raise Exception(error)


def googleSheet_list_spreadsheets(access_token, API_SERVICE_NAME, API_VERSION):
    try:
        query = "mimeType='application/vnd.google-apps.spreadsheet'"
        drive_service = create_service(access_token, API_SERVICE_NAME, API_VERSION)
        results = drive_service.files().list(q=query).execute()
        return results

    except Exception as error:
        raise Exception(error)


#############################################################################################################################

# Sheet Within Document Actions


def googleSheet_create_sheet(access_token, API_SERVICE_NAME, API_VERSION, params):
    try:
        if "spreadsheetId" in params and "requests" in params:
            id = params["spreadsheetId"]
            service = create_service(access_token, API_SERVICE_NAME, API_VERSION)
            data = {}
            for key, value in params.items():
                if key == "spreadsheetId":
                    continue
                if value:
                    data[key] = value
            response = service.spreadsheets().batchUpdate(spreadsheetId=id, body=data).execute()
            return response

        else:
            raise SyntaxError("Missing input data")

    except Exception as error:
        raise Exception(error)


def googleSheet_append_data_to_sheet(access_token, API_SERVICE_NAME, API_VERSION, params):
    try:
        if "spreadsheetId" in params and "sheetName" in params and "values" in params:
            id = params["spreadsheetId"]
            range_to_append = params["sheetName"]
            append_values_request = {"values": params["values"]}
            service = create_service(access_token, API_SERVICE_NAME, API_VERSION)
            response = service.spreadsheets().values().append(spreadsheetId=id, range=range_to_append, body=append_values_request, valueInputOption="RAW").execute()
            return response

        else:
            raise SyntaxError("Missing input data")
        
    except Exception as error:
        raise Exception(error)


def googleSheet_update_rows_in_sheet(access_token, API_SERVICE_NAME, API_VERSION, params):
    try:
        if "spreadsheetId" in params and "sheetName" in params and "range" in params and "values" in params:
            id = params["spreadsheetId"]
            range_to_update = f"'{params['sheetName']}'!{params['range']}"
            update_values_request = {"values": params["values"]}
            service = create_service(access_token, API_SERVICE_NAME, API_VERSION)
            response = service.spreadsheets().values().update(spreadsheetId=id, range=range_to_update, body=update_values_request, valueInputOption="RAW").execute()
            return response

        else:
            raise SyntaxError("Missing input data")
        
    except Exception as error:
        raise Exception(error)


def googleSheet_read_rows_in_sheet(access_token, API_SERVICE_NAME, API_VERSION, params):
    try:
        if "spreadsheetId" in params and "sheetName" in params:
            id = params["spreadsheetId"]
            if "range" in params:
                range_to_read = f"'{params['sheetName']}'!{params['range']}"
            else:
                range_to_read = params["sheetName"]

            majorDimension = "DIMENSION_UNSPECIFIED"
            if "majorDimension" in params:
                majorDimension = params["majorDimension"]

            service = create_service(access_token, API_SERVICE_NAME, API_VERSION)
            response = service.spreadsheets().values().get(spreadsheetId=id, range=range_to_read, majorDimension=majorDimension).execute()
            return response

        else:
            raise SyntaxError("Missing input data")
        
    except Exception as error:
        raise Exception(error)


def googleSheet_delete_ColOrRow_from_sheet(access_token, API_SERVICE_NAME, API_VERSION, params):
    try:
        if "spreadsheetId" in params and "requests" in params:
            id = params["spreadsheetId"]
            service = create_service(access_token, API_SERVICE_NAME, API_VERSION)
            data = {}
            for key, value in params.items():
                if key == "spreadsheetId":
                    continue
                if value:
                    data[key] = value
            response = service.spreadsheets().batchUpdate(spreadsheetId=id, body=data).execute()
            return response

        else:
            raise SyntaxError("Missing input data")

    except Exception as error:
        raise Exception(error)


def googleSheet_remove_sheet(access_token, API_SERVICE_NAME, API_VERSION, params):
    try:
        if "spreadsheetId" in params and "requests" in params:
            id = params["spreadsheetId"]
            service = create_service(access_token, API_SERVICE_NAME, API_VERSION)
            data = {}
            for key, value in params.items():
                if key == "spreadsheetId":
                    continue
                if value:
                    data[key] = value
            response = service.spreadsheets().batchUpdate(spreadsheetId=id, body=data).execute()
            return response

        else:
            raise SyntaxError("Missing input data")

    except Exception as error:
        raise Exception(error)


def googleSheet_clear_data_from_sheet(access_token, API_SERVICE_NAME, API_VERSION, params):
    try:
        if "spreadsheetId" in params and "sheetName" in params:
            id = params["spreadsheetId"]
            if "range" in params:
                range_to_delete = f"'{params['sheetName']}'!{params['range']}"
            else:
                range_to_delete = params["sheetName"]

            service = create_service(access_token, API_SERVICE_NAME, API_VERSION)
            response = service.spreadsheets().values().clear(spreadsheetId=id, range=range_to_delete).execute()
            return response

        else:
            raise SyntaxError("Missing input data")
        
    except Exception as error:
        raise Exception(error)
