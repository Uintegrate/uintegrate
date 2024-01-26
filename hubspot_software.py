from hubspot import HubSpot
import logging
import requests
################## AUTHENTICATION ######################################################################################
def refresh_access_token(client_id1,client_secret1,refresh_token1):
    api_client = HubSpot()
    try:
        tokens = api_client.auth.oauth.tokens_api.create(
            grant_type='refresh_token',
            client_id=client_id1,
            client_secret=client_secret1,
            refresh_token=refresh_token1
        )
        return tokens.access_token
    except requests.exceptions.RequestException as e:
        raise Exception(f"RequestException: {e}")
############# CONTACTS ####################################################################################
def hubspot_get_all_contacts(access_token,params):
    try:
        if 'limit' in params:
         limit=params['limit']
         url = f"https://api.hubapi.com/crm/v3/objects/contacts?limit={limit}"
        else:
         url="https://api.hubapi.com/crm/v3/objects/contacts"
        properties = params.get('properties', [])
        if isinstance(properties, list):
            properties_str = ','.join([f'{prop}' for prop in properties])
            url += f"&properties={properties_str}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get(url=url,headers=headers)
        result=response.json()
        if response.status_code==200:
              return result  
        else:
                raise Exception(result)
    except Exception as e:
        raise Exception(e)
def hubspot_get_contact(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/contacts/{params['id']}"
          properties = params.get('properties', [])
          if isinstance(properties, list):
                properties_str = '&'.join([f'properties={prop}' for prop in properties])
                url += f"?{properties_str}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          contact = requests.get(url=url,headers=headers)
          if contact.status_code == 404:
                raise Exception("invalid input data")
          else:
                return contact.json() 
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)
            
def hubspot_create_contact(access_token,params):
    try:
        if 'email'in params['properties']:
            contact = {}
            for key, value in params.items():
                contact[key] = value
            headers = {
                        'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                        }
            url = "https://api.hubapi.com/crm/v3/objects/contacts"
            response = requests.post(url=url,json=contact,headers=headers)
            result=response.json()
            if response.status_code==201:
               return result  
            else:
                raise Exception(result)
        else:
            raise Exception("missing contact email")
    except Exception as e:
        raise Exception(e)   
    
def hubspot_update_contact(access_token,params):
    try:
        if 'id' in params:
            contact = {}
            key_to_skip=['id']
            for key, value in params.items():
                if key in key_to_skip:
                    continue
                contact[key] = value
            headers = {
                        'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                        }
            url = f"https://api.hubapi.com/crm/v3/objects/contacts/{params['id']}"
            response = requests.patch(url=url,json=contact,headers=headers)
            result=response.json()
            if response.status_code==200:
               return result  
            else:
                raise Exception(result)
        else:
            raise Exception("Missing contact Id ")
    except Exception as e:
        raise Exception(e)  
    
def hubspot_delete_contact(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/contacts/{params['id']}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          requests.delete(url,headers=headers)
          return f"contact of id {params['id']} successfully deleted"  
    except Exception as e:
        raise Exception(e)
####################################### COMPANIES ######################################
def hubspot_create_company(access_token,params):
    try:
        if 'domain' in params['properties']:
            company = {}
            for key,value in params.items():
                company[key] = value
            headers = {
                        'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                        }
            url = "https://api.hubapi.com/crm/v3/objects/companies"
            response = requests.post(url=url,json=company,headers=headers)
            result=response.json()
            if response.status_code==201:
                return result  
            else:
                    raise Exception(result)
        else:
            raise Exception("missing company domain")
    except Exception as e:
        raise Exception(e)   

def hubspot_update_company(access_token,params):
    try:
        if 'id' in params:
            company = {}
            keys_to_skip=['id']
            for key, value in params.items():
                if key in keys_to_skip:
                        continue
                if value:
                    company[key] = value
            headers = {
                        'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                        }
            url = f"https://api.hubapi.com/crm/v3/objects/companies/{params['id']}"
            response = requests.patch(url=url,json=company,headers=headers)
            result=response.json()
            if response.status_code==200:
               return result  
            else:
                raise Exception(result)
        else:
            raise Exception("Missing company Id ")
    except Exception as e:
        raise Exception(e)  

def hubspot_get_company(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/companies/{params['id']}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          response = requests.get(url, headers=headers)
          if response.status_code == 404:
                raise Exception("invalid input data")
          else:
                return response.json() 
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)
    
def hubspot_get_all_companies(access_token,params):
  try: 
        if 'limit' in params:
          limit= params['limit']  
          url = f"https://api.hubapi.com/crm/v3/objects/companies?limit={limit}"
        else:
          url="https://api.hubapi.com/crm/v3/objects/companies/"
        properties = params.get('properties', [])
        if isinstance(properties, list):
                properties_str = '&'.join([f'properties={prop}' for prop in properties])
                url += f"&{properties_str}"
        headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
        response = requests.get(url=url, headers=headers)
        result=response.json()
        if response.status_code==200:
               return result
        else:
                raise Exception(result)
  except Exception as e:
        raise Exception(e)

def hubspot_delete_company(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/companies/{params['id']}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          requests.delete(url,headers=headers)
          return f"company of id {params['id']} successfully deleted"
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)
##################### TICKETS ##############################################
def  hubspot_create_ticket(access_token,params):
    try:   
          if 'hs_pipeline_stage' in params['properties']:
            ticket = {}
            for key, value in params.items():
                ticket[key] = value
            headers = {
                        'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                        }
            url = "https://api.hubapi.com/crm/v3/objects/tickets"
            response = requests.post(url=url,json=ticket,headers=headers)
            result=response.json()
            if response.status_code==201:
               return result  
            else:
                raise Exception(result)
          else:
              raise Exception("missing pipeline stage")
    
    except Exception as e:
        raise Exception(e)
        
def  hubspot_update_ticket(access_token,params):
    try:
          if 'id' in params:
            ticket = {}
            key_to_skip=['id']
            for key, value in params.items():
                if key in key_to_skip:
                    continue
                else:
                    ticket[key] = value
            headers = {
                        'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                        }
            url = f"https://api.hubapi.com/crm/v3/objects/tickets/{params['id']}"
            response = requests.patch(url=url,json=ticket,headers=headers)
            result=response.json()
            if response.status_code==200:
               return result  
            else:
                raise Exception(result)
          else:
              raise Exception("missing ticket id")
    
    except Exception as e:
        raise Exception(e) 
     
def hubspot_get_ticket(access_token,params):
    try:
        if 'id' in params:
            url = f"https://api.hubapi.com/crm/v3/objects/tickets/{params['id']}"
            properties = params.get('properties', [])
            if isinstance(properties, list):
                properties_str = '&'.join([f'properties={prop}' for prop in properties])
                url += f"?{properties_str}"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access_token}'
            }
            response = requests.get(url=url, headers=headers)
            if response.status_code == 404:
                raise Exception("invalid input data")
            else:
                return response.json() 
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)
    
def hubspot_get_all_tickets(access_token,params):
  try: 
         if 'limit' in params:
          limit= params['limit']  
          url = f"https://api.hubapi.com/crm/v3/objects/tickets?limit={limit}"
         else:
          url="https://api.hubapi.com/crm/v3/objects/tickets/"
         properties = params.get('properties', [])
         if isinstance(properties, list):
                properties_str = '&'.join([f'properties={prop}' for prop in properties])
                url+= f"&{properties_str}"
         headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
         
         response = requests.get(url=url, headers=headers)
         result=response.json()
         if response.status_code==200:
               return result  
         else:
                raise Exception(result)
  except Exception as e:
        raise Exception(e)
        
def hubspot_delete_ticket(access_token,params):
    try:
        if 'id' in params:
            url = f"https://api.hubapi.com/crm/v3/objects/tickets/{params['id']}"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access_token}'
            }
            requests.delete(url,headers=headers)
            return f"ticket of id {params['id']} successfully deleted"
        else:
            raise Exception("Missing ticket ID")
    except Exception as e:
        raise Exception(e)
 ############################### Deals ##################################################################################
def hubspot_create_deal(access_token,params):
    try:
        if 'dealname' in params['properties']:
            deal = {}
            for key, value in params.items():
                deal[key] = value
            headers = {
                        'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                        }
            url = "https://api.hubapi.com/crm/v3/objects/deals"
            response = requests.post(url=url,json=deal,headers=headers)
            result=response.json()
            if response.status_code==201:
               return result  
            else:
                raise Exception(result)
        else:
            raise Exception("missing deal name")
    except Exception as e:
        raise Exception(e)  

def hubspot_update_deal(access_token,params):
    try:
        if 'id' in params:
            deal = {}
            keys_to_skip=['id']
            for key, value in params.items():
                if key in keys_to_skip:
                        continue
                if value:
                    deal[key] = value
            headers = {
                        'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                        }
            url = f"https://api.hubapi.com/crm/v3/objects/deals/{params['id']}"
            response = requests.patch(url=url,json=deal,headers=headers)
            result=response.json()
            if response.status_code==200:
               return result  
            else:
                raise Exception(result)
        else:
            raise Exception("Missing deal Id ")
    except Exception as e:
        raise Exception(e) 

def hubspot_get_deal(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/deals/{params['id']}"
          properties = params.get('properties', [])
          if isinstance(properties, list):
                properties_str = '&'.join([f'properties={prop}' for prop in properties])
                url += f"?{properties_str}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          response = requests.get(url=url,headers=headers)
          if response.status_code == 404:
                raise Exception("invalid input data")
          else:
                return response.json() 
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)    

def hubspot_get_many_deals(access_token,params):
  try: 
         if 'limit' in params:
          limit= params['limit']  
          url = f"https://api.hubapi.com/crm/v3/objects/deals?limit={limit}"
         else:
          url="https://api.hubapi.com/crm/v3/objects/deals/"
         properties = params.get('properties', [])
         if isinstance(properties, list):
                properties_str = '&'.join([f'properties={prop}' for prop in properties])
                url += f"&{properties_str}"
         headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
         response = requests.get(url=url,headers=headers)
         result=response.json()
         if response.status_code==200:
               return result  
         else:
                raise Exception(result)
  except Exception as e:
        raise Exception(e)
            
def hubspot_delete_deal(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/deals/{params['id']}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          requests.delete(url,headers=headers)
          return f"deal of id {params['id']} successfully deleted"
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)
##################### ENGAGEMENTS ########################################################################################
########## CALLS ################################
def hubspot_create_call(access_token,params):
    try:
        if 'hs_timestamp' in params['properties']:
            call = {}
            for key, value in params.items():
                call[key] = value
            headers = {
                        'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                        }
            url = "https://api.hubapi.com/crm/v3/objects/calls"
            response = requests.post(url=url,json=call,headers=headers)
            result=response.json()
            if response.status_code==201:
               return result  
            else:
                raise Exception(result)
        else:
            raise Exception("missing call timestamp")
    except Exception as e:
        raise Exception(e)
      
def hubspot_get_call(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/calls/{params['id']}"
          properties = params.get('properties', [])
          if isinstance(properties, list):
                properties_str = '&'.join([f'properties={prop}' for prop in properties])
                url += f"?{properties_str}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          response = requests.get(url=url,headers=headers)
          if response.status_code == 404:
                raise Exception("invalid input data")
          else:
                return response.json() 
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)
    
def hubspot_get_many_calls(access_token,params):
  try:   
         if 'limit' in params:
          limit= params['limit']  
          url = f"https://api.hubapi.com/crm/v3/objects/calls?limit={limit}"
         else:
          url="https://api.hubapi.com/crm/v3/objects/calls"
         properties = params.get('properties', [])
         if isinstance(properties, list):
                properties_str = ','.join([f'{prop}' for prop in properties])
                url += f"&properties={properties_str}"
         headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
         response = requests.get(url=url,headers=headers)
         result=response.json()
         if response.status_code==200:
               return result  
         else:
                raise Exception(result)
  except Exception as e:
        raise Exception(e)
        
def hubspot_delete_call(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/calls/{params['id']}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          requests.delete(url,headers=headers)
          return f"call of id {params['id']} successfully deleted"
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)
########## Email  ####################################################################################
def hubspot_create_email(access_token,params):
    try:
        if 'hs_timestamp' in params['properties']:
            email = {}
            for key, value in params.items():
                email[key] = value
                
            headers = {
                        'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                        }
            url = "https://api.hubapi.com/crm/v3/objects/emails"
            response = requests.post(url=url,json=email,headers=headers)
            result=response.json()
            if response.status_code==201:
               return result  
            else:
                raise Exception(result)
        else:
            raise Exception("missing email timestamp")
    except Exception as e:
        raise Exception(e) 

    
def hubspot_get_email(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/emails/{params['id']}"
          properties = params.get('properties', [])
          if isinstance(properties, list):
                properties_str = '&'.join([f'properties={prop}' for prop in properties])
                url += f"?{properties_str}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          response = requests.get(url=url,headers=headers)
          if response.status_code == 404:
                raise Exception("invalid input data")
          else:
                return response.json() 
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e) 
    
def hubspot_get_many_emails(access_token,params):
  try:   
         if 'limit' in params:
          limit= params['limit']  
          url = f"https://api.hubapi.com/crm/v3/objects/emails?limit={limit}"
         else:
          url="https://api.hubapi.com/crm/v3/objects/emails"
         properties = params.get('properties', [])
         if isinstance(properties, list):
                properties_str = ','.join([f'{prop}' for prop in properties])
                url += f"&properties={properties_str}"
         headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
         response = requests.get(url=url, headers=headers)
         result=response.json()
         if response.status_code==200:
               return result  
         else:
                raise Exception(result)
  except Exception as e:
        raise Exception(e)
        
def hubspot_delete_email(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/emails/{params['id']}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          requests.delete(url,headers=headers)
          return f"email of id {params['id']} successfully deleted"
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)

################### TASKS #########################################################
def hubspot_create_task(access_token,params):
    try:
        if 'hs_timestamp' in params['properties']:
            task = {}
            for key, value in params.items():
                task[key] = value
            headers = {
                        'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                        }
            url = "https://api.hubapi.com/crm/v3/objects/tasks"
            response = requests.post(url=url,json=task,headers=headers)
            result=response.json()
            if response.status_code==201:
               return result  
            else:
                raise Exception(result)
        else:
            raise Exception("missing task timestamp")
    except Exception as e:
        raise Exception(e)
 
    
def hubspot_get_task(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/tasks/{params['id']}"
          properties = params.get('properties', [])
          if isinstance(properties, list):
                properties_str = '&'.join([f'properties={prop}' for prop in properties])
                url += f"?{properties_str}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          response = requests.get(url=url,headers=headers)
          if response.status_code == 404:
                raise Exception("invalid input data")
          else:
                return response.json() 
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e) 
    
def hubspot_get_many_tasks(access_token,params):
  try:   
         if 'limit' in params:
          limit= params['limit']  
          url = f"https://api.hubapi.com/crm/v3/objects/tasks?limit={limit}"
         else:
          url="https://api.hubapi.com/crm/v3/objects/tasks"
         properties = params.get('properties', [])
         if isinstance(properties, list):
                properties_str = ','.join([f'{prop}' for prop in properties])
                url += f"&properties={properties_str}"
                logging.warning(url)
         headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
         response = requests.get(url=url, headers=headers)
         result=response.json()
         if response.status_code==200:
               return result  
         else:
                raise Exception(result)
  except Exception as e:
        raise Exception(e)
        
def hubspot_delete_task(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/tasks/{params['id']}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          requests.delete(url,headers=headers)
          return f"task of id {params['id']} successfully deleted"
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)
    
################### MEETINGS #########################################################
def hubspot_create_meeting(access_token,params):
    try:
        if 'hs_timestamp' in params['properties']:
            meeting = {}
            for key, value in params.items():
                meeting[key] = value
            headers = {
                        'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                        }
            url = "https://api.hubapi.com/crm/v3/objects/meetings"
            response = requests.post(url=url,json=meeting,headers=headers)
            result=response.json()
            if response.status_code==201:
               return result  
            else:
                raise Exception(result)
        else:
            raise Exception("missing meeting timestamp")
    except Exception as e:
        raise Exception(e) 
    
def hubspot_get_meeting(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/meetings/{params['id']}"
          properties = params.get('properties', [])
          if isinstance(properties, list):
                properties_str = '&'.join([f'properties={prop}' for prop in properties])
                url += f"?{properties_str}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          response = requests.get(url=url,headers=headers)
          if response.status_code == 404:
                raise Exception("invalid input data")
          else:
                return response.json() 
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)   
    
def hubspot_get_many_meetings(access_token,params):
  try:   
         if 'limit' in params:
          limit= params['limit']  
          url = f"https://api.hubapi.com/crm/v3/objects/meetings?limit={limit}"
         else:
          url="https://api.hubapi.com/crm/v3/objects/meetings"
         properties = params.get('properties', [])
         if isinstance(properties, list):
                properties_str = ','.join([f'{prop}' for prop in properties])
                url += f"&properties={properties_str}"
         headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
         response = requests.get(url=url, headers=headers)
         result=response.json()
         if response.status_code==200:
               return result  
         else:
                raise Exception(result)
  except Exception as e:
        raise Exception(e)
        
def hubspot_delete_meeting(access_token,params):
    try:
        if 'id' in params:
          url = f"https://api.hubapi.com/crm/v3/objects/meetings/{params['id']}"
          headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {access_token}'
          }
          requests.delete(url,headers=headers)
          return f"meeting of id {params['id']} successfully deleted"
        else:
            raise Exception("missing input data")
    except Exception as e:
        raise Exception(e)
################# CONTACT LIST ######################################################################################## 
def hubspot_add_to_list(access_token,params):
    try:
        if 'record' in params:
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access_token}'
            }
            url = f"https://api.hubapi.com/crm/v3/lists/{params['list_id']}/memberships/add"
            response = requests.put(url=url,json=params['record'],headers=headers)
            result=response.json()
            if response.status_code==200:
             return result  
            else:
             raise Exception(result)
        else:
            raise Exception("missing record id")
    except Exception as e:
        raise Exception(e)
    
def hubspot_remove_from_list(access_token,params):
    try:
        if 'record' in params:
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {access_token}'
            }
            url = f"https://api.hubapi.com/crm/v3/lists/{params['list_id']}/memberships/remove"
            logging.warning(params['record'])
            response = requests.put(url=url,json=params['record'],headers=headers)
            result=response.json()
            if response.status_code==200:
             return result  
            else:
             raise Exception(result)
        else:
            raise Exception("missing record id")
    except Exception as e:
        raise Exception(e)