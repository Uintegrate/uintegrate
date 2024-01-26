import requests
########################### User Actions ###########################################################
def notion_get_many_users(integration_token,params):
    if 'page_size' in params:
      limit= params['page_size']
      url = f"https://api.notion.com/v1/users?page_size={limit}"
    else:
      url = f"https://api.notion.com/v1/users"
    headers = {
        "Authorization": f"Bearer {integration_token}",
        "Notion-Version": "2022-06-28",  
         "Content-Type": "application/json"  
    }
    try:
        response = requests.get(url, headers=headers)  
        if response.status_code==200:
         data = response.json()
         return data["results"]
        else:
           raise Exception(response.json())    
    except Exception as error:
        raise Exception(error)

def notion_get_user(integration_token,params):
    try:
     if 'user_id' in params:
       url = f"https://api.notion.com/v1/users/{params['user_id']}"
       headers = {
        "Authorization": f"Bearer {integration_token}",
        "Notion-Version": "2022-06-28",  
         "Content-Type": "application/json"  
       }
       response = requests.get(url, headers=headers)
       if response.status_code==200:
         data = response.json()
         return data
       else:
           raise Exception(response.json())
     else:
          raise Exception("missing user id")
    except Exception as error:
        raise Exception(error)
      
########### DATABASES ################################################################
def notion_get_database(integration_token,params):
    try: 
     if 'database_id' in params:
       url = f"https://api.notion.com/v1/databases/{params['database_id']}"
       headers = {
        "Authorization": f"Bearer {integration_token}",
        "Notion-Version": "2022-06-28",  
         "Content-Type": "application/json"  
       }
       response = requests.get(url, headers=headers)
       if response.status_code==200:
         data = response.json()
         return data
       else:
           raise Exception(response.json())
     else:
          raise Exception("missing database id")
    except Exception as error:
        raise Exception(error)

def notion_get_many_databases(integration_token,params):
    if 'page_size' in params:
      limit= params['page_size']
      url = f"https://api.notion.com/v1/databases?page_size={limit}"
    else:
      url = f"https://api.notion.com/v1/databases"
    headers = {
        "Authorization": f"Bearer {integration_token}",
        "Notion-Version": "2021-05-13",  
         "Content-Type": "application/json"  
    }
    try:
        response = requests.get(url, headers=headers)  
        if response.status_code==200:
         data = response.json()
         return data
        else:
           raise Exception(response.json())    
    except Exception as error:
        raise Exception(error)

def notion_search_database(integration_token,params):
    try:
     if 'database_id' in params:
       url = f"https://api.notion.com/v1/databases/{params['database_id']}/query"
       headers = {
        "Authorization": f"Bearer {integration_token}",
        "Notion-Version": "2022-06-28",  
         "Content-Type": "application/json"  
       }
       response = requests.post(url, headers=headers)
       if response.status_code==200:
         data = response.json()
         return data
       else:
           raise Exception(response.json())
     else:
          raise Exception("missing database id")
    except Exception as error:
        raise Exception(error)

########################## PAGES #########################################################
def notion_create_page(integration_token,params): 
    try: 
      if 'parent' in params and 'properties' in params:
        notion_api_url = "https://api.notion.com/v1/pages"
        headers = {
            "Authorization": f"Bearer {integration_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2021-05-13", 
            }
        response = requests.post(notion_api_url, headers=headers, json=params)
        if response.status_code == 200:
          return response.json()
        else:
          raise Exception(response.json())
      else:
        raise Exception("missing required parameters")
    except Exception as error:
         raise Exception(error)

def notion_get_page(integration_token,params):
    try:
     if 'page_id' in params:
       url = f"https://api.notion.com/v1/pages/{params['page_id']}"
       headers = {
        "Authorization": f"Bearer {integration_token}",
        "Notion-Version": "2022-06-28",  
         "Content-Type": "application/json"  
       }
       response = requests.get(url, headers=headers)
       if response.status_code==200:
         data = response.json()
         return data
       else:
           raise Exception(response.json())
     else:
          raise Exception("missing page id")
    except Exception as error:
        raise Exception(error)

def notion_archive_page(integration_token,params):
 try:
    if 'page_id' in params and 'archived' in params:
            notion_api_url = f"https://api.notion.com/v1/pages/{params['page_id']}"
            headers = {
                "Authorization": f"Bearer {integration_token}",
                "Content-Type": "application/json",
                "Notion-Version": "2021-05-13", 
                }
            to_archive={}
            to_archive['archived']=params['archived']
            response = requests.patch(notion_api_url, headers=headers, json=to_archive)
            if response.status_code == 200:
             return response.json()
            else:
             raise Exception(response.json())
    else:
       raise Exception("missing page id")
 except Exception as error:
         raise Exception(error)
       
############ BLOCKS #######################################################################
def notion_get_block(integration_token,params):
    try:
     if 'block_id' in params:        
       url = f"https://api.notion.com/v1/blocks/{params['block_id']}"
       headers = {
        "Authorization": f"Bearer {integration_token}",
        "Notion-Version": "2022-06-28",  
         "Content-Type": "application/json"  
       }
       response = requests.get(url, headers=headers)
       if response.status_code==200:
         data = response.json()
         return data
       else:
           raise Exception(response.json())
     else:
          raise Exception("missing block id")
    except Exception as error:
        raise Exception(error)
      
def notion_get_many_child_blocks(integration_token,params):
    try:
        if 'block_id' in params:
            if 'page_size' in params:
                 notion_api_url = f"https://api.notion.com/v1/blocks/{params['block_id']}/children?page_size={params['page_size']}"
            else:
                notion_api_url = f"https://api.notion.com/v1/blocks/{params['block_id']}/children"
            headers = {
             "Authorization": f"Bearer {integration_token}",
             "Notion-Version": "2021-05-13",  
             }
            response = requests.get(notion_api_url, headers=headers)
            if response.status_code == 200:
             return response.json()
            else:
             raise Exception(response.json())
        else:
            raise Exception("missing block Id")
    
    except Exception as error:
        raise Exception(error)

def notion_append_child_blocks(integration_token,params):
    try:
        if 'block_id' in params and 'children' in params:
            notion_api_url = f"https://api.notion.com/v1/blocks/{params['block_id']}/children"
            headers = {
                "Authorization": f"Bearer {integration_token}",
                "Notion-Version": "2022-06-28",
                "Content-Type": "application/json",  # Specify content type as JSON
            }
            to_append={}
            to_append['children']=params['children']
            response = requests.patch(notion_api_url, headers=headers, json=to_append)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(response.json())
        else:
            raise Exception("missing required input")
    except Exception as error:
            raise Exception(error)
