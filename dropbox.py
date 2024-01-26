
import requests
import base64
def create_access_token(app_key,app_secret,refresh_token):
    """
       Creates an access token that will be used for authorization purposes.
    
    :param str app_key: (str,required) used for authentication
    :param str app_secret: (str,required) for the calendar, it's 'calendar'
    :param str refresh_token: (str,required) the version used is v3  
    :return: access token 
    :rtype: dict  
    """
    data = {
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }
    auth_header = base64.b64encode(f"{app_key}:{app_secret}".encode()).decode('utf-8')
    headers = {
        "Authorization": f"Basic {auth_header}",
    }
    try:
        response = requests.post("https://api.dropbox.com/oauth2/token", data=data, headers=headers)
        response_data = response.json()
        return response_data['access_token']
    except Exception as e:
         raise Exception(response_data.get('error_description', 'Unknown error'))

def dropbox_create_folder(access_token,params):
    """
     Creates a dropbox folder with custom properties if added

    :param str access_token: (str, required) Used for authentication.
    :param dict params: contains properties to be added to the created folder
    
        - :path: (str, Required) Path in the user's Dropbox to create.
        - :autorename: (bool) If there's a conflict, have the Dropbox server try to autorename the
                  folder to avoid the conflict.
    :return: Details about the created folder
    :rtype: dict
    """
    try:
        if 'path' in params:
            create_folder_url = "https://api.dropboxapi.com/2/files/create_folder_v2"
            headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
        
            response = requests.post(create_folder_url, headers=headers, json=params)
            if response.status_code == 200:
             return response.json()
            else:
             raise Exception(response.json()) 
        else:
            raise Exception("missing folder path") 
    except Exception as e:
        raise Exception(e)

def dropbox_list_folder(access_token,params):
    """
     Starts returning the contents of a folder.

    :param str access_token: (str, required) Used for authentication.
    :param dict params: Filters the properties to be returned for each event.
    
        - :path: (str, Required) A unique identifier for the file.
        - :include_deleted: (bool) If true, the results will include entries for files
                            and folders that used to exist but were deleted
        - :include_has_explicit_shared_members: (bool) If true, the results will include a flag for each file
                                                indicating whether or not that file has any explicit members
        - :include_mounted_folders: (bool) If true, the results will include entries under mounted folders which 
                                     includes app folder, shared folder and team folder.
        - :include_non_downloadable_files: (bool) If true, include files that are not downloadable.
        - :recursive: (bool) If true, the list folder operation will be applied recursively to all 
                      subfolders and the response will contain contents of all subfolders
    :return: Details about the folder content
    :rtype: dict
    """
    try:
        if 'path' in params:
            copy_folder_url = "https://api.dropboxapi.com/2/files/list_folder"
            headers = {'Authorization': f'Bearer {access_token}',
                    'Content-Type': 'application/json'}
            response = requests.post(copy_folder_url, headers=headers, json=params)
            if response.status_code == 200:
             return response.json()
            else:
             raise Exception(response.json())
        else:
            raise Exception("missing folder path")
    except Exception as e:
        raise Exception(e)

def dropbox_copy_folder(access_token,params):
    """
     Copies a folder to a different location in the user's Dropbox

    :param str access_token: (str, required) Used for authentication.
    :param dict params: Filters the properties to be returned for each event.
    
        - :from_path: (str, Required) Path in the user's Dropbox to be copied or moved.
        - :to_path: (str, Required) Path in the user's Dropbox that is the destination
        - :allow_ownership_transfer: (bool) Allow moves by owner even if it would result
                                      in an ownership transfer for the content being moved
        - :autorename: (bool) If there's a conflict, have the Dropbox server 
                               try to autorename the file to avoid the conflict
    :return: Details about the copied folder
    :rtype: dict
    """
    try:
        if 'from_path' in params and 'to_path' in params:
            copy_folder_url = "https://api.dropboxapi.com/2/files/copy_v2"
            headers = {'Authorization': f'Bearer {access_token}',
                    'Content-Type': 'application/json'}
            response = requests.post(copy_folder_url, headers=headers, json=params)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing required data")
    except Exception as e:
        raise Exception(e)

def dropbox_move_folder(access_token,params):
    """
     Moves a  folder to a different location in the user's Dropbox

    :param str access_token: (str, required) Used for authentication.
    :param dict params: Filters the properties to be returned for each event.
    
        - :from_path: (str, Required) Path in the user's Dropbox to be moved.
        - :to_path: (str, Required) Path in the user's Dropbox that is the destination
        - :allow_ownership_transfer: (bool) Allow moves by owner even if it would result
                                      in an ownership transfer for the content being moved
        - :autorename: (bool) If there's a conflict, have the Dropbox server 
                               try to autorename the file to avoid the conflict
    :return: Details about the copied folder
    :rtype: dict
    """
    try:
        if 'from_path' in params and 'to_path' in params:
            move_folder_url = "https://api.dropboxapi.com/2/files/move_v2"
            headers = {'Authorization': f'Bearer {access_token}',
                    'Content-Type': 'application/json'}
            response = requests.post(move_folder_url, headers=headers, json=params)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing required data")
    except Exception as e:
        raise Exception(e)

def dropbox_delete_folder(access_token,params):
    """
     Deletes a folder at a given path with all its contents
    :param str access_token: (str, required) Used for authentication.
    :param dict params: Filters the properties to be returned for each event.
    
        - :path: (str, Required) Path in the user's Dropbox to delete.
    :return: Details about the deleted folder
    :rtype: dict
    """
    try:
        if 'path' in params:
            delete_folder_url = "https://api.dropboxapi.com/2/files/delete_v2"
            headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
            response = requests.post(delete_folder_url, headers=headers, json=params)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing folder path")
    except Exception as e:
        raise Exception(e)

def dropbox_copy_file(access_token,params):
    """
     Copies a file to a different location in the user's Dropbox

    :param str access_token: (str, required) Used for authentication.
    :param dict params: Filters the properties to be returned for each event.
    
        - :from_path: (str, Required) Path in the user's Dropbox to be copied or moved.
        - :to_path: (str, Required) Path in the user's Dropbox that is the destination
        - :allow_ownership_transfer: (bool) Allow moves by owner even if it would result
                                      in an ownership transfer for the content being moved
        - :autorename: (bool) If there's a conflict, have the Dropbox server 
                               try to autorename the file to avoid the conflict
    :return: Details about the copied file
    :rtype: dict
    """
    try:
        if 'from_path' in params and 'to_path' in params:
            copy_folder_url = "https://api.dropboxapi.com/2/files/copy_v2"
            headers = {'Authorization': f'Bearer {access_token}',
                    'Content-Type': 'application/json'}
            response = requests.post(copy_folder_url, headers=headers, json=params)
            if response.status_code == 200:
             return response.json()
            else:
             raise Exception(response.json())
        else:
            raise Exception("missing required data")
        
    except Exception as e:
        raise Exception(e)

def dropbox_move_file(access_token,params):
    """
     Moves a  file to a different location in the user's Dropbox

    :param str access_token: (str, required) Used for authentication.
    :param dict params: Filters the properties to be returned for each event.
    
        - :from_path: (str, Required) Path in the user's Dropbox to be moved.
        - :to_path: (str, Required) Path in the user's Dropbox that is the destination
        - :allow_ownership_transfer: (bool) Allow moves by owner even if it would result
                                      in an ownership transfer for the content being moved
        - :autorename: (bool) If there's a conflict, have the Dropbox server 
                               try to autorename the file to avoid the conflict
    :return: Details about the copied file
    :rtype: dict
    """
    try:
        if 'from_path' in params and 'to_path' in params:
            move_file_url = "https://api.dropboxapi.com/2/files/move_v2"
            headers = {'Authorization': f'Bearer {access_token}',
                    'Content-Type': 'application/json'}
            response = requests.post(move_file_url, headers=headers, json=params)
            if response.status_code == 200:
             return response.json()
            else:
             raise Exception(response.json())
        else:
            raise Exception("missing required data")
    except Exception as e:
        raise Exception(e)

def dropbox_delete_file(access_token,params):
    """
     Deletes a file at a given path.
    :param str access_token: (str, required) Used for authentication.
    :param dict params: Filters the properties to be returned for each event.
    
        - :path: (str, Required) Path in the user's Dropbox to delete.
    :return: Details about the deleted file
    :rtype: dict
    """
    try:
        if 'path' in params:
            delete_folder_url = "https://api.dropboxapi.com/2/files/delete_v2"
            headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
            response = requests.post(delete_folder_url, headers=headers, json=params)
            if response.status_code == 200:
             return response.json()
            else:
             raise Exception(response.json())
        else:
            raise Exception("missing file path")
    except Exception as e:
        raise Exception(e)