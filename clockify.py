import requests

valid_status_code = [200, 201, 202, 204, 206, 207, 208]
###########################################################################
############# CLIENT  ###################################
def Clockify_create_client(params, api_token):
    try:
        if "name" in params and "workspace_id" in params:
            client = {}
            for key, value in params.items():
                client[key] = value
            url = f"https://api.clockify.me/api/workspaces/{params['workspace_id']}/clients"
            headers = {"X-Api-Key": api_token, "Content-Type": "application/json"}
            response = requests.post(url, headers=headers, json=client)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)
def Clockify_get_client(params, api_token):
    try:
        if "id" in params and "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/clients/{params['id']}"
            headers = {
               "X-Api-Key": api_token,
            }
            response = requests.get(api_url, headers=headers)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing input data")
    except Exception as error:
        raise Exception(error)
def Clockify_update_client(params, api_token):
    try:
        if "id" in params and "workspace_id" in params:
            client_id = params["id"]
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/clients/{client_id}"
            headers = {
                "X-Api-Key": api_token,
                "Content-Type": "application/json",
            }
            client = {}
            keys_to_skip = ["client_id"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    client[key] = value
            response = requests.put(api_url, headers=headers, json=client)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing input data")
    except Exception as error:
        raise Exception(error)
    
def Clockify_delete_client(params, api_token):
    try:
        if "id" in params and "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/clients/{params['id']}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.delete(api_url, headers=headers)
            if response.status_code in valid_status_code:
                return f"Deleted client with  ID: {params['id']}"
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing input data")
    except Exception as error:
        raise Exception(error)
    
def Clockify_get_all_clients(params, api_token):
    try:
        if "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/clients/"
            query_string = "&".join([f"{key}={value}" for key, value in params.items()])
            full_url = f"{api_url}?{query_string}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.get(full_url, headers=headers)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing workspace Id")
    except Exception as e:
        raise Exception(e)
############################ WORKSPACE AND USERS #########################################
def Clockify_get_all_users(params, api_token):
    try:
        if "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/users/"
            query_string = "&".join([f"{key}={value}" for key, value in params.items()])
            full_url = f"{api_url}?{query_string}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.get(full_url, headers=headers)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)
    
def Clockify_get_all_workspaces(api_token):
    api_url = f"https://api.clockify.me/api/v1/workspaces/"
    headers = {
        "X-Api-Key": api_token,
    }
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code in valid_status_code:
            return response.json()
        else:
            raise Exception(response.json())
    except Exception as error:
        raise Exception(error)
########################################################################################
############# PROJECT #######################################
def Clockify_create_project(params, api_token):
    try:
        if "name" in params and "workspace_id" in params:
            project = {}
            for key, value in params.items():
                project[key] = value
            url = f"https://api.clockify.me/api/workspaces/{params['workspace_id']}/projects"
            
            
            headers = {"X-Api-Key": api_token, "Content-Type": "application/json"}
            response = requests.post(url, headers=headers, json=project)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)
    
def Clockify_get_all_projects(params, api_token):
    try:
        if "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/projects/"
            query_string = "&".join([f"{key}={value}" for key, value in params.items()])
            full_url = f"{api_url}?{query_string}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.get(full_url, headers=headers)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)

def Clockify_get_project(params, api_token):
    try:
        if "id" in params and "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/projects/{params['id']}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.get(api_url, headers=headers)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing input data")
    except Exception as error:
        raise Exception(error)
    
def Clockify_update_project(params, api_token):
    try:
        if "id" in params and "workspace_id" in params:
            project_id = params["id"]
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/projects/{project_id}"
            headers = {
                "X-Api-Key": api_token,
                "Content-Type": "application/json",
            }
            project = {}
            keys_to_skip = ["project_id"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    project[key] = value
            response = requests.put(api_url, headers=headers, json=project)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing input data")
    except Exception as error:
        raise Exception(error)

def Clockify_delete_project(params, api_token):
    try:
        if "id" in params and "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/projects/{params['id']}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.delete(api_url, headers=headers)

            if response.status_code in valid_status_code:
                return f"Deleted project with  ID: {params['id']}"
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing input data")

    except Exception as error:
        raise Exception(error)
################ TAGS ##############################################################
def Clockify_create_tag(params, api_token):
    try:
        if "name" in params and "workspace_id" in params:
            tag = {}
            for key, value in params.items():
                tag[key] = value
            url = (
                f"https://api.clockify.me/api/workspaces/{params['workspace_id']}/tags"
            )
            headers = {"X-Api-Key": api_token, "Content-Type": "application/json"}
            response = requests.post(url, headers=headers, json=tag)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def Clockify_get_tag(params, api_token):
    try:
        if "id" in params and "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/tags/{params['id']}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.get(api_url, headers=headers)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def Clockify_get_all_tags(params, api_token):
    try:
        if "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/tags/"
            query_string = "&".join([f"{key}={value}" for key, value in params.items()])
            full_url = f"{api_url}?{query_string}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.get(full_url, headers=headers)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)

def Clockify_update_tag(params, api_token):
    try:
        if "id" in params and "workspace_id" in params:
            tag_id = params["id"]
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/tags/{tag_id}"
            headers = {
                "X-Api-Key": api_token,
                "Content-Type": "application/json",
            }
            tag = {}
            keys_to_skip = ["tag_id"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    tag[key] = value
            response = requests.put(api_url, headers=headers, json=tag)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing input data")
    except Exception as error:
        raise Exception(error)

def Clockify_delete_tag(params, api_token):
    try:
        if "id" in params and "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/tags/{params['id']}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.delete(api_url, headers=headers)
            if response.status_code in valid_status_code:
                return f"Deleted tag with  ID: {params['id']}"
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)
####################### TASKS ######################################
def Clockify_create_task(params, api_token):
    try:
        if "name" in params and "projectId" in params and "workspace_id" in params:
            task = {}
            keys_to_skip = ["projectId"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    task[key] = value
            url = f"https://api.clockify.me/api/workspaces/{params['workspace_id']}/projects/{params['projectId']}/tasks"
            headers = {"X-Api-Key": api_token, "Content-Type": "application/json"}
            response = requests.post(url, headers=headers, json=task)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def Clockify_get_task(params, api_token):
    try:
        if "id" in params and "projectId" in params and "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/projects/{params['projectId']}/tasks/{params['id']}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.get(api_url, headers=headers)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def Clockify_get_all_tasks(params, api_token):
    try:
        if "projectId" in params and "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/projects/{params['projectId']}/tasks/"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.get(api_url, headers=headers)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response)
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def Clockify_update_task(params, api_token):
    try:
        if "projectId" in params and "workspace_id" in params:
            task = {}
            keys_to_skip = ["projectId", "id"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    task[key] = value
            url = f"https://api.clockify.me/api/workspaces/{params['workspace_id']}/projects/{params['projectId']}/tasks/{params['id']}"
            headers = {"X-Api-Key": api_token, "Content-Type": "application/json"}
            response = requests.put(url, headers=headers, json=task)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def Clockify_delete_task(params, api_token):
    try:
        if "id" in params and "projectId" in params and "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/projects/{params['projectId']}/tasks/{params['id']}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.delete(api_url, headers=headers)
            if response.status_code in valid_status_code:
                return f"Deleted task with  ID: {params['id']}"
            else:
                raise Exception(response.json())
        raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)
################## TIME ENTRY ##################################################
def Clockify_create_time_entry(params, api_token):
    try:
        if "start" in params and "workspace_id" in params:
            time_entry = {}
            for key, value in params.items():
                time_entry[key] = value
            url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/time-entries/"
            headers = {"X-Api-Key": api_token, "Content-Type": "application/json"}
            response = requests.post(url, headers=headers, json=time_entry)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)
    
def Clockify_delete_time_entry(params, api_token):
    try:
        if "id" in params and "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/time-entries/{params['id']}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.delete(api_url, headers=headers)
            if response.status_code in valid_status_code:
                return f"Deleted time entry  with  ID: {params['id']}"
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def Clockify_update_time_entry(params, api_token):
    try:
        if "id" in params and "workspace_id" in params:
            time_entry = {}
            keys_to_skip = {"id"}
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    time_entry[key] = value
            url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/time-entries/{params['id']}"
            headers = {"X-Api-Key": api_token, "Content-Type": "application/json"}
            response = requests.put(url, headers=headers, json=time_entry)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def Clockify_get_time_entry(params, api_token):
    try:
        if "id" in params and "workspace_id" in params:
            api_url = f"https://api.clockify.me/api/v1/workspaces/{params['workspace_id']}/time-entries/{params['id']}"
            headers = {
                "X-Api-Key": api_token,
            }
            response = requests.get(api_url, headers=headers)
            if response.status_code in valid_status_code:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)
