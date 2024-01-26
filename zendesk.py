import requests
import base64
import json 


###########################################################################

# Ticket Actions

def zendesk_create_ticket(params,api_token,base_url,email):
    try:
            if 'description' in params['ticket']:
                ticket = {}
                for key, value in params.items():
                    ticket[key] = value
                
               
                auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
                url =f"https://{base_url}.zendesk.com/api/v2/tickets" 
                headers = {
                    "Authorization": auth_header,
                    "Content-Type": "application/json"
                }

                response = requests.post(url,headers=headers,data=json.dumps(ticket))
                res=response.json()
                if "error" in res:
                    raise Exception(res)
                else:
                    return response.json()
                
                
            else:
                raise Exception("Missing input data")   
   
    except Exception as error:
        raise Exception(error)
    



def zendesk_get_ticket(params,api_token,base_url,email):

    try:
        if 'id' in params:

         auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
         url = f"https://{base_url}.zendesk.com/api/v2/tickets/{params['id']}" 
       
         headers = {
            "Authorization": auth_header,
            "Content-Type": "application/json"
            }
         response = requests.get(url, headers=headers)
         res=response.json()
         if "error" in res:
             raise Exception(res)
         else:
             return response.json()
       
        else:
         raise Exception("missing ticket id")
      

    except Exception as e:
        raise Exception(e)




def zendesk_get_all_tickets(params,api_token,base_url,email):
      try:
       url = f'https://{base_url}.zendesk.com/api/v2/search?query=type:ticket'
       if params['status']:
            url += f'+status:{params["status"]}'
       if params['sort_by']:
            url += f'&sort_by:{params["sort_by"]}'
       if params['sort_order']:
            url += f'&sort_order:{params["sort_order"]}'
       auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
       headers = {
                "Authorization": auth_header,
                "Content-Type": "application/json"
            } 
       response = requests.get(url,headers=headers,params=params)
       if "error" in response:
             raise Exception(response)
       else:
             return response.json()
      except Exception as e:
        raise Exception(e)


def zendesk_update_ticket(params,api_token,base_url,email):
    try:
        
        if "ticket_id" in params:
            ticket_id=params['ticket_id']
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            url = f"https://{base_url}.zendesk.com/api/v2/tickets/{ticket_id}" 
            headers = {
                "Authorization": auth_header,
                "Content-Type": "application/json"
            }
            
            ticket = {}
            keys_to_skip = ["ticket_id"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                  ticket[key] = value
                    
            response = requests.put(url,headers=headers,data=json.dumps(ticket))
            res=response.json()
            if "error" in res:
             raise Exception(res)
            else:
             return response.json()
           
        else:
            raise Exception("Missing input data")

    except Exception as e:
        raise Exception(e)
    


def zendesk_delete_ticket(params,api_token,base_url,email):
    try:
         
          if 'id' in params:
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            url = f"https://{base_url}.zendesk.com/api/v2/tickets/{params['id']}" 
            headers = {
                    "Authorization": auth_header,
                    "Content-Type": "application/json"
                }
            requests.delete(url,headers=headers)
            return f"Deleted ticket ID: {params['id']}"
          else:
            raise Exception("missing ticket id")
 

    except Exception as e:
        raise Exception(e)



def zendesk_recover_ticket(params,api_token,base_url,email):
    try:
        if 'id' in params:
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
             
            url=f"https://{base_url}.zendesk.com/api/v2/suspended_tickets/{params['id']}/recover"
            headers = {
                    "Authorization": auth_header,
                    "Content-Type": "application/json"
                }
            response=requests.put(url,headers=headers)
            res=response.json()
            if "error" in res:
             raise Exception(res)
            else:
             return response.json()
           
        else:
            raise Exception("missing ticket id")

    except Exception as e:
        raise Exception(e)



###########################################################################

# User Actions


def zendesk_create_user(params,api_token,base_url,email):
    try:
        
        if "name" in params["user"] and len(params["user"]["name"]) >= 1:
          
            new_user = {}
           
            for key, value in params.items():
                if value:
                  new_user[key] = value


            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            url = f"https://{base_url}.zendesk.com/api/v2/users" 
            headers = {
            "Authorization": auth_header,
            "Content-Type": "application/json"
        }
            response = requests.post(url, headers=headers, json=new_user)
            res=response.json()
            if "error" in res:
             raise Exception(res)
            else:
             return response.json()

        else:
            raise Exception("Name must be at least one character long.")

    except Exception as e:
        raise Exception(e)




def zendesk_get_user(params,api_token,base_url,email):
    try:

        if 'id' in params:
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            url = f"https://{base_url}.zendesk.com/api/v2/users/{params['id']}" 
            headers = {
                    "Authorization": auth_header,
                    "Content-Type": "application/json"
                }
            response = requests.get(url,headers=headers)
            res=response.json()
            if "error" in res:
             raise Exception(res)
            else:
             return response.json()
        else:
            raise Exception("missing user id")
        
    except Exception as e:
        raise Exception(e)



def zendesk_get_all_users(params,api_token,base_url,email):
    try:
        url = f"https://{base_url}.zendesk.com/api/v2/users" 
        query_string = '&'.join([f'{key}={value}' for key, value in params.items()])
        full_url = f"{url}?{query_string}"
        auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
       
        headers = {
                "Authorization": auth_header,
                "Content-Type": "application/json"
            } 
        response = requests.get(full_url,headers=headers)
        res=response.json()
        if "error" in res:
             raise Exception(res)
        else:
             return response.json()
        
    except Exception as e:
        raise Exception(e)



def zendesk_delete_user(params,api_token,base_url,email):
    try:
        if 'id' in params:
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            url = f"https://{base_url}.zendesk.com/api/v2/users/{params['id']}" 
            headers = {
                    "Authorization": auth_header,
                    "Content-Type": "application/json"
                } 
        
            requests.delete(url,headers=headers)
            return f"Deleted user ID: {params['id']}"
        else:
            raise Exception("missing user id ")
       
    

    except Exception as e:
        raise Exception(e)



def zendesk_update_user(params,api_token,base_url,email):
  try:
        
        if "id" in params:
            user_id=params['id']
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            url = f"https://{base_url}.zendesk.com/api/v2/users/{user_id}" 
            headers = {
                "Authorization": auth_header,
                "Content-Type": "application/json"
            }
            
            updated= {}
            keys_to_skip = ["id"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                  updated[key] = value
                    
            response = requests.put(url,headers=headers,data=json.dumps(updated))
            res=response.json()
            if "error" in res:
             raise Exception(res)
            else:
             return response.json()
        else:
            raise Exception("Error : Missing input data")

  except Exception as e:
        raise Exception(e)
    



def zendesk_get_user_org(params,api_token,base_url,email):
    try:
        if 'id' in params:
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            headers = {
                    "Authorization": auth_header,
                    "Content-Type": "application/json"
                }
            url = f"https://{base_url}.zendesk.com/api/v2/users/{params['id']}/organizations" 
        
            response = requests.get(url,headers=headers)
            res=response.json()
            if "error" in res:
             raise Exception(res)
            else:
             return response.json()
        else: 
            raise Exception(" Error : missing user id")
       

    except Exception as e:
        raise Exception(e)



def zendesk_get_data_related_to_user(params,api_token,base_url,email):
    try:
        if 'id' in params:
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            headers = {
                    "Authorization": auth_header,
                    "Content-Type": "application/json"
                }
            url = f"https://{base_url}.zendesk.com/api/v2/users/{params['id']}/related" 
            
            response = requests.get(url,headers=headers)
            res=response.json()
            if "error" in res:
             raise Exception(res)
            else:
             return response.json()
        else:
            raise Exception(" Error : missing user id")

    except Exception as e:
        raise Exception(e)


def zendesk_search_users(params,api_token,base_url,email):
    try:
        auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
        headers = {
                "Authorization": auth_header,
                "Content-Type": "application/json"
            }
        url = f"https://{base_url}.zendesk.com/api/v2/users/search" 
        
        if "external_id" in params:
            external_id = params["external_id"]
            url += f"?external_id={external_id}"

        if "query" in params:
           query = params["query"]
           if "external_id" in params:
                 url += f"&query={query}"
           else:
                  url += f"?query={query}"
        response = requests.get(url,headers=headers)
        res=response.json()
        if "error" in res:
             raise Exception(res)
        else:
             return response.json()
     
    except Exception as e:
        raise Exception(e)
    



###########################################################################

# Organization Actions

def zendesk_get_organization(params,api_token,base_url,email):
    try:
        if 'id' in params:
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            headers = {
                    "Authorization": auth_header,
                    "Content-Type": "application/json"
                }
            url = f"https://{base_url}.zendesk.com/api/v2/organizations/{params['id']}" 
        
            response = requests.get(url,headers=headers)
            if 'error' in response.json():
              raise Exception(response.json())
            else:
              return  response.json()
        else:
            raise Exception("Error : missing organization ID")
       
        
    except Exception as e:
        raise Exception(e)
    



def zendesk_get_all_organizations(api_token,base_url,email):
    try:
        auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
        headers = {
                "Authorization": auth_header,
                "Content-Type": "application/json"
            }
        url = f"https://{base_url}.zendesk.com/api/v2/organizations/" 
      
        response = requests.get(url,headers=headers)
        res=response.json()
        if "error" in res:
             raise Exception(res)
        else:
             return response.json()
      
    except Exception as e:
        raise Exception(e)
    


def zendesk_create_org(params,api_token,base_url,email):
    try:
            if "name" in params['organization']:
             org = {}
             for key, value in params.items():
                 org[key] = value
            
           
             auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
             url = f"https://{base_url}.zendesk.com/api/v2/organizations/"  
             headers = {
                "Authorization": auth_header,
                "Content-Type": "application/json"
             }

             response = requests.post(url,headers=headers,data=json.dumps(org))
             res=response.json()
             if "error" in res:
              raise Exception(res)
             else:
               return response.json()
            else:
              
              raise Exception("Missing input data")

        
    except Exception as error:
        raise Exception(error)




def zendesk_update_org(params,api_token,base_url,email):
  try:
        
        if "id" in params:
            org_id=params['id']
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            url = f"https://{base_url}.zendesk.com/api/v2/organizations/{org_id}" 
            headers = {
                "Authorization": auth_header,
                "Content-Type": "application/json"
            }
            
            updated= {}
            keys_to_skip = ["id"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                  updated[key] = value
                    
            response = requests.put(url,headers=headers,data=json.dumps(updated))
            res=response.json()
            if "error" in res:
             raise Exception(res)
            else:
             return response.json()
        else:
            raise Exception("Missing input data")

  except Exception as e:
        raise Exception(e)


    
def zendesk_delete_org(params,api_token,base_url,email):

    try:
        if 'id' in params:
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            headers = {
                    "Authorization": auth_header,
                    "Content-Type": "application/json"
                }
            url = f"https://{base_url}.zendesk.com/api/v2/organizations/{params['id']}" 
            
                
            requests.delete(url,headers=headers)
            return f"Deleted organization ID: {params['id']}"
        else :
            raise Exception("Error : missing organization ID")
     
    except Exception as e:
        raise Exception(e)
    




def zendesk_get_data_related_to_org(params,api_token,base_url,email):
   
    try:
        if 'id' in params:
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            headers = {
                    "Authorization": auth_header,
                    "Content-Type": "application/json"
                }
            url = f"https://{base_url}.zendesk.com/api/v2/organizations/{params['id']}/related" 
            
            response = requests.get(url,headers=headers)
            res=response.json()
            if "error" in res:
             raise Exception(res)
            else:
             return response.json()
        else:
            raise Exception("Error : missing organization ID")

    except Exception as e:
        raise Exception(e)


def zendesk_count_organizations(api_token,base_url,email):
    try:
        auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
        headers = {
                "Authorization": auth_header,
                "Content-Type": "application/json"
            }

        url = f"https://{base_url}.zendesk.com/api/v2/organizations/count" 
       
        response = requests.get(url,headers=headers)
        res=response.json()
        if "error" in res:
             raise Exception(res)
        else:
             return response.json()
        

    except Exception as e:
        raise Exception(e)


###########################################################################

# Ticket Field Actions


def zendesk_get_ticket_field(params,api_token,base_url,email):
    try:
        if 'id' in params:
            auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
            headers = {
                    "Authorization": auth_header,
                    "Content-Type": "application/json"
                }
            url = f"https://{base_url}.zendesk.com/api/v2/ticket_fields/{params['id']}" 
        
            response = requests.get(url,headers=headers)
            res=response.json()
            if "error" in res:
             raise Exception(res)
            else:
             return response.json()
        else:
            raise Exception("Error : missing Ticket ID")
        

    except Exception as e:
        raise Exception(e)
    



def zendesk_get_all_ticket_fields(api_token,base_url,email):
    try:
        auth_header = f"Basic {base64.b64encode(f'{email}/token:{api_token}'.encode()).decode()}"
        headers = {
                "Authorization": auth_header,
                "Content-Type": "application/json"
            }
        url = f"https://{base_url}.zendesk.com/api/v2/ticket_fields/" 
       
        response = requests.get(url,headers=headers)
        res=response.json()
        if "error" in res:
             raise Exception(res)
        else:
             return response.json()
        

    except Exception as e:
        raise Exception(f"error: {str(e)}")
    
