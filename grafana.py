import requests
status=[200, 201, 202, 204, 206, 207, 208]
def grafana_create_dashboard(params,token,domain):
    try:
        if "title" in params["dashboard"] and token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/dashboards/db"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.post(GRAFANA_API_URL, headers=headers, json=data)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)

def grafana_get_dashboard(params,token,domain):
    try:
        if "uid" in params and token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/dashboards/uid/{data['uid']}"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.get(GRAFANA_API_URL, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)
    
def grafana_delete_dashboard(params,token,domain):
    try:
        if "uid" in params and token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/dashboards/uid/{data['uid']}"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.delete(GRAFANA_API_URL, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)

def grafana_get_many_dashboard(params,token,domain):
    try:
        if'type' in params and token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/search/"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.get(GRAFANA_API_URL, headers=headers,params=data)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)

def grafana_update_dashboard(params,token,domain):
    try:
        if "uid" in params["dashboard"] and token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/dashboards/db"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.post(GRAFANA_API_URL, headers=headers, json=data)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)
    
def grafana_create_team(params,token,domain):
    try:
        if "name" in params and token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/teams"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.post(GRAFANA_API_URL, headers=headers, json=data)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)
    
def grafana_delete_team(params,token,domain):
    try:
        if "teams_id" in params and token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/teams/{data['teams_id']}"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.delete(GRAFANA_API_URL, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)
    
def grafana_get_team(params,token,domain):
    try:
        if "teams_id" in params and token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/teams/{data['teams_id']}"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.get(GRAFANA_API_URL, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)
    
def grafana_get_many_team(params,token,domain):
    try:
        if token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value

            GRAFANA_API_URL = f"https://{domain}/api/teams/search"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.get(GRAFANA_API_URL, headers=headers, params=data)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(response.text)
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)
    
def grafana_update_team(params,token,domain):
    try:
        if "team_id" in params and token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/teams/{data['team_id']}"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.put(GRAFANA_API_URL, headers=headers, json=data)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)


def grafana_get_many_users(params,token,domain):
    try:
        if token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/org/users"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.get(GRAFANA_API_URL, headers=headers, params=data)
            if response.status_code in status:
                print(response.json())
                return response.json()
            else:
                raise Exception(response.text)
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)
    
def grafana_update_user(params,token,domain):
    try:
        if "user_id" in params and token:
            data = {}
            for key, value in params.items():
                if key=="user_id":
                    continue
                else:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/org/users/{params['user_id']}"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.patch(GRAFANA_API_URL, headers=headers, json=data)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)

def grafana_delete_user(params,token,domain):
    try:
        if "user_id" in params and token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/org/users/{data['user_id']}"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.delete(GRAFANA_API_URL, headers=headers, json=data)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)

def grafana_get_team_members(params,token,domain):
    try:
        if "team_id" in params and token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/teams/{data['team_id']}/members"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.get(GRAFANA_API_URL, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)
    
def grafana_delete_team_members(params,token,domain):
    try:
        if "team_id" in params and "user_id" in params and token:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            GRAFANA_API_URL = f"https://{domain}/api/teams/{data['team_id']}/members/{data['user_id']}"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }
            response = requests.delete(GRAFANA_API_URL, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception({response.text})
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(e)
    except Exception as e:
        raise Exception(e)
