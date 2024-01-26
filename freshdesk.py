import requests
def freshdesk_get_ticket(domain, ticket_id,params):
    try:
        url = f"https://{domain}.freshdesk.com/api/v2/tickets/{ticket_id}"
        if "user" in params and "pwd" in params:
            user = params["user"]
            pwd = params["pwd"]
            response = requests.get(url, auth=(user, pwd))
            if response.status_code == 200:
              return response.json()
            else:
             raise Exception(response.json())
    except Exception as e:
            raise Exception(e)

def freshdesk_get_all_tickets(domain,params):
    try:
        url = f"https://{domain}.freshdesk.com/api/v2/tickets"
        if "user" in params and "pwd" in params:
            user = params["user"]
            pwd = params["pwd"]
            query_string = ""
            keys_to_skip = ["user", "pwd"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    query_string += f"&{key}={value}"
            if query_string != "":
                url += f"?{query_string}"
            response = requests.get(url, auth=(user, pwd))
            if response.status_code == 200:
              return response.json()
            else:
             raise Exception(response.json())
        else:
            raise SyntaxError("Missing input data")
    except Exception as e:
            raise Exception(e)

def freshdesk_create_ticket(domain,params):
    try:
        url = f"https://{domain}.freshdesk.com/api/v2/tickets"
        allRequired = [
            "user",
            "pwd",
            "priority",
            "status",
            "source",
            "description",
            "subject",
        ]
        oneRequired = [
            "requester_id",
            "email",
            "facebook_id",
            "phone",
            "twitter_id",
            "unique_external_id",
        ]
        if all(item in params for item in allRequired) and any(
            item in params for item in oneRequired
        ):
            user = params["user"]
            pwd = params["pwd"]
            data = {"ticket": {}}
            keys_to_skip = ["user", "pwd"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    data["ticket"][key] = value
            response = requests.post(url, auth=(user, pwd), json=data)
            result = response.json()
            if response.status_code == 201:
             return response.json()
            else:
             raise Exception(response.json())
        else:
            raise SyntaxError("Missing input data")
    except Exception as e:
            raise Exception(e)

def freshdesk_delete_ticket(domain, ticket_id,params):
    try:
        url = f"https://{domain}.freshdesk.com/api/v2/tickets/{ticket_id}"
        if "user" in params and "pwd" in params:
            user = params["user"]
            pwd = params["pwd"]
            response = requests.delete(url, auth=(user, pwd))
            successStatus= [200,201,202,204,206,207,208]
            if response.status_code in successStatus:
                return {"Result": f"Deleted ticket ID: {ticket_id}"}
            else:
                raise Exception(
                    f"Failed to delete the ticket. Status code: {response.status_code}"
                )
        else:
            raise SyntaxError("Missing input data")
    except Exception as e:
            raise Exception(e)

def freshdesk_update_ticket(domain, ticket_id,params):
    try:
        url = f"https://{domain}.freshdesk.com/api/v2/tickets/{ticket_id}"
        if "user" in params and "pwd" in params:
            user = params["user"]
            pwd = params["pwd"]
            data = {"ticket": {}}
            keys_to_skip = ["user", "pwd"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    data["ticket"][key] = value
            response = requests.put(url, auth=(user, pwd), json=data)
            result = response.json()
            for item in result:
                if item == "errors" or item == "code" or item == "message":
                    raise Exception(result)
            return result
        else:
            raise SyntaxError("Missing input data")
    except Exception as e:
            raise Exception(e)
        
def freshdesk_get_contact(domain, contact_id,params):
    try:
        url = f"https://{domain}.freshdesk.com/api/v2/contacts/{contact_id}"
        if "user" in params and "pwd" in params:
            user = params["user"]
            pwd = params["pwd"]
            response = requests.get(url, auth=(user, pwd))
            result = response.json()
            for item in result:
                if item == "errors" or item == "code":
                    raise Exception(result)
            return result
        else:
            raise SyntaxError("Missing input data")
    except Exception as e:
            raise Exception(e)

def freshdesk_get_all_contacts(domain,params):
    try:
        url = f"https://{domain}.freshdesk.com/api/v2/contacts"
        if "user" in params and "pwd" in params:
            user = params["user"]
            pwd = params["pwd"]
            query_string = ""
            keys_to_skip = ["user", "pwd"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    query_string += f"&{key}={value}"

            if query_string != "":
                url += f"?{query_string}"
            response = requests.get(url, auth=(user, pwd))
            result = response.json()
            for item in result:
                if item == "errors" or item == "code":
                    raise Exception(result)
            return result
        else:
            raise SyntaxError("Missing input data")
    except Exception as e:
            raise Exception(e)

def freshdesk_create_contact(domain,params):
    try:
        url = f"https://{domain}.freshdesk.com/api/v2/contacts"
        if "user" in params and "pwd" in params and "email" in params:
            user = params["user"]
            pwd = params["pwd"]
            data = {}
            keys_to_skip = ["user", "pwd"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    data[key] = value
            response = requests.post(url, auth=(user, pwd), json=data)
            result = response.json()
            for item in result:
                if item == "errors" or item == "code":
                    raise Exception(result)
            return result
        else:
            raise SyntaxError("Missing input data")
    except Exception as e:
            raise Exception(e)

def freshdesk_delete_contact(domain, contact_id,params):
    try:
        url = f"https://{domain}.freshdesk.com/api/v2/contacts/{contact_id}"
        if "user" in params and "pwd" in params:
            user = params["user"]
            pwd = params["pwd"]
            response = requests.delete(url, auth=(user, pwd))
            successStatus= [200,201,202,204,206,207,208]
            if response.status_code in successStatus:
                return {"Result": f"Deleted contact ID: {contact_id}"}
            else:
                raise Exception(
                    f"Failed to delete the contact. Status code: {response.status_code}"
                )
    except Exception as e:
            raise Exception(e)

def freshdesk_update_contact(domain, contact_id,params):
    try:
        url = f"https://{domain}.freshdesk.com/api/v2/contacts/{contact_id}"
        if "user" in params and "pwd" in params:
            user = params["user"]
            pwd = params["pwd"]
            data = {}
            keys_to_skip = ["user", "pwd"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    data[key] = value
            response = requests.put(url, auth=(user, pwd), json=data)
            result = response.json()
            for item in result:
                if item == "errors" or item == "code" or item == "message":
                    raise Exception(result)
            return result
        else:
            raise SyntaxError("Missing input data")
    except Exception as e:
            raise Exception(e)
