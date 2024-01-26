import requests
status=[200, 201, 202, 204, 206, 207, 208] 
def refresh_access_token(refresh_token,CLIENT_ID,CLIENT_SECRET):
    try:
        token_params = {
        'grant_type': 'refresh_token',
        'refresh_token':refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
        response = requests.post('https://zoom.us/oauth/token', data=token_params)
        return response.json()['access_token']
    except requests.exceptions.RequestException as e:
        raise(e)
    except Exception as e:
        raise Exception(e)

def zoom_create_meeting(params,access_token):
    try:
        if access_token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            url = 'https://api.zoom.us/v2/users/me/meetings'
            headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f'Meeting creation failed:{response.text}')
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise(e)
    except Exception as e:
        raise Exception(e) 

def zoom_get_meeting(params,access_token):
    try:
        if 'meetingId' in params and access_token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            url = f'https://api.zoom.us/v2/meetings/{data["meetingId"]}'
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json',
            }
            response = requests.get(url, headers=headers,params=data)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f'Meeting retrieval failed:{response.text}')
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)

    except Exception as e:
        raise Exception(e)

def zoom_list_meetings(params,access_token):
    try:
        if access_token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            url = 'https://api.zoom.us/v2/users/me/meetings'
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json',
            }
            response = requests.get(url, headers=headers,params=data)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f'Meeting listing failed:{response.text}')
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)
    
def zoom_update_meeting(params,access_token):
    try:
        if 'meeting_id' in params and access_token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            url = f'https://api.zoom.us/v2/meetings/{data["meeting_id"]}'
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json',
            }
            response = requests.patch(url, headers=headers, json=data)
            if response.status_code in status:
                return "Meeting updated successfully"
            else:
                raise Exception(f'Meeting update failed:{response.text}')
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)

def zoom_delete_meeting(params,access_token):
    try:
        if 'meeting_id' in params and access_token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            url = f'https://api.zoom.us/v2/meetings/{data["meeting_id"]}'
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json',
            }
            response = requests.delete(url, headers=headers,params=data)
            if response.status_code in status:
                return "Meeting deleted successfully"
            else:
                raise Exception(f'Meeting deletion failed:{response.text}')
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)