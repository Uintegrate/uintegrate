import requests
import base64


######################    Generate Access Token      ######################

def salesforce_refresh_access_token(client_id, client_secret, refresh_token):
    try:
        url = f"https://login.salesforce.com/services/oauth2/token?grant_type=refresh_token&client_id={client_id}&client_secret={client_secret}&refresh_token={refresh_token}"
        response = requests.post(url)
        response_json = response.json()
        if "access_token" in response_json:
            return response_json["access_token"]
        else:
            return {"access_token": "Invalid access_token"}

    except Exception as error:
        raise Exception(error)
    
    
###########################################################################

# User Actions


def salesforce_get_user(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/User/"
        if "id" in params:
            access_token = token
            user_id = params["id"]
            url += f"{user_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_list_users(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/query?q="
        access_token = token
        query = "SELECT Id, name, Email FROM User"
        conditions = ""
        for key, value in params.items():
            if key == "fields":
                query = f"SELECT {value} FROM User"

            if key == "conditions":
                conditions = " AND ".join(value)
                conditions = " WHERE " + conditions

        url += query + conditions
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


###########################################################################

# Task Actions


def salesforce_get_task(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Task/"
        if "id" in params:
            access_token = token
            task_id = params["id"]
            url += f"{task_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_get_task_summary(domain, token):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Task"
        access_token = token
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_list_tasks(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/query?q="

        access_token = token
        query = "SELECT Id, Subject, Status, Priority FROM Task"
        conditions = ""
        for key, value in params.items():
            if key == "fields":
                query = f"SELECT {value} FROM Task"

            if key == "conditions":
                conditions = " AND ".join(value)
                conditions = " WHERE " + conditions

        url += query + conditions

        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_create_task(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Task"
        if "status" in params:
            access_token = token
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_update_task(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Task/"
        if "id" in params:
            access_token = token
            task_id = params["id"]
            url += f"{task_id}"
            data = {}
            for key, value in params.items():
                if key == "id":
                    continue
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.patch(url, headers=headers, json=data)
            if response.status_code == 204:
                return {"Result": f"Updated Task ID: {task_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)
    

def salesforce_delete_task(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Task/"
        if "id" in params:
            access_token = token
            task_id = params["id"]
            url += f"{task_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            if response.status_code == 204:
                return {"Result": f"Deleted Task ID: {task_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


###########################################################################

# Opportunity Actions


def salesforce_get_opportunity(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Opportunity/"
        if "id" in params:
            access_token = token
            opportunity_id = params["id"]
            url += f"{opportunity_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_get_opportunity_summary(domain, token):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Opportunity"
        access_token = token
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_list_opportunities(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/query?q="
        access_token = token
        query = "SELECT Id, AccountId, Amount, Probability, Type FROM Opportunity"
        conditions = ""
        for key, value in params.items():
            if key == "fields":
                query = f"SELECT {value} FROM Opportunity"

            if key == "conditions":
                conditions = " AND ".join(value)
                conditions = " WHERE " + conditions

        url += query + conditions

        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_create_opportunity(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Opportunity"
        if "name" in params and "stageName" in params and "closeDate" in params:
            access_token = token
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_update_opportunity(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Opportunity/"
        if "id" in params:
            access_token = token
            opportunity_id = params["id"]
            url += f"{opportunity_id}"
            data = {}
            for key, value in params.items():
                if key == "id":
                    continue
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.patch(url, headers=headers, json=data)
            if response.status_code == 204:
                return {"Result": f"Updated Opportunity ID: {opportunity_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_delete_opportunity(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Opportunity/"
        if "id" in params:
            access_token = token
            opportunity_id = params["id"]
            url += f"{opportunity_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            if response.status_code == 204:
                return {"Result": f"Deleted Opportunity ID: {opportunity_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


###########################################################################

# Lead Actions


def salesforce_get_lead(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Lead/"
        if "id" in params:
            access_token = token
            lead_id = params["id"]
            url += f"{lead_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_get_lead_summary(domain, token):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Lead"
        access_token = token
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_list_leads(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/query?q="
        access_token = token
        query = "SELECT Id, Company, FirstName, LastName, Street, PostalCode, City, Email, Status FROM Lead"
        conditions = ""
        for key, value in params.items():
            if key == "fields":
                query = f"SELECT {value} FROM lead"

            if key == "conditions":
                conditions = " AND ".join(value)
                conditions = " WHERE " + conditions

        url += query + conditions

        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_create_lead(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Lead"
        if "company" in params and "lastName" in params:
            access_token = token
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_update_lead(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Lead/"
        if "id" in params:
            access_token = token
            lead_id = params["id"]
            url += f"{lead_id}"
            data = {}
            for key, value in params.items():
                if key == "id":
                    continue
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.patch(url, headers=headers, json=data)
            if response.status_code == 204:
                return {"Result": f"Updated Lead ID: {lead_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_delete_lead(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Lead/"
        if "id" in params:
            access_token = token
            lead_id = params["id"]
            url += f"{lead_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            if response.status_code == 204:
                return {"Result": f"Deleted Lead ID: {lead_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_add_lead_to_campaign(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/CampaignMember"
        if "leadId" in params and "campaignId" in params:
            access_token = token
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


###########################################################################

# Contact Actions


def salesforce_get_contact(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Contact/"
        if "id" in params:
            access_token = token
            contact_id = params["id"]
            url += f"{contact_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_get_contact_summary(domain, token):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Contact"
        access_token = token
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_list_contacts(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/query?q="
        access_token = token
        query = "SELECT Id, FirstName, LastName, Email FROM Contact"
        conditions = ""
        for key, value in params.items():
            if key == "fields":
                query = f"SELECT {value} FROM Contact"

            if key == "conditions":
                conditions = " AND ".join(value)
                conditions = " WHERE " + conditions

        url += query + conditions

        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_create_contact(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Contact"
        if "lastName" in params:
            access_token = token
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_update_contact(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Contact/"
        if "id" in params:
            access_token = token
            contact_id = params["id"]
            url += f"{contact_id}"
            data = {}
            for key, value in params.items():
                if key == "id":
                    continue
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.patch(url, headers=headers, json=data)
            if response.status_code == 204:
                return {"Result": f"Updated Contact ID: {contact_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_delete_contact(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Contact/"
        if "id" in params:
            access_token = token
            contact_id = params["id"]
            url += f"{contact_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            if response.status_code == 204:
                return {"Result": f"Deleted Contact ID: {contact_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_add_contact_to_campaign(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/CampaignMember"
        if "contactId" in params and "campaignId" in params:
            access_token = token
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


###########################################################################

# Case Actions


def salesforce_get_case(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Case/"
        if "id" in params:
            access_token = token
            case_id = params["id"]
            url += f"{case_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_get_case_summary(domain, token):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Case"
        access_token = token
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_list_cases(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/query?q="
        access_token = token
        query = (
            "SELECT Id, AccountId, ContactId, Priority, Status, Subject, Type FROM Case"
        )
        conditions = ""
        for key, value in params.items():
            if key == "fields":
                query = f"SELECT {value} FROM Case"

            if key == "conditions":
                conditions = " AND ".join(value)
                conditions = " WHERE " + conditions

        url += query + conditions

        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_create_case(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Case"
        if "type" in params:
            access_token = token
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_update_case(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Case/"
        if "id" in params:
            access_token = token
            case_id = params["id"]
            url += f"{case_id}"
            data = {}
            for key, value in params.items():
                if key == "id":
                    continue
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.patch(url, headers=headers, json=data)
            if response.status_code == 204:
                return {"Result": f"Updated Case ID: {case_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_delete_case(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Case/"
        if "id" in params:
            access_token = token
            case_id = params["id"]
            url += f"{case_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            if response.status_code == 204:
                return {"Result": f"Deleted Case ID: {case_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_add_comment_to_case(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/CaseComment"
        if "parentId" in params:
            access_token = token
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


###########################################################################

# Account Actions


def salesforce_get_account(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Account/"
        if "id" in params:
            access_token = token
            account_id = params["id"]
            url += f"{account_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_get_account_summary(domain, token):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Account"
        access_token = token
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_list_accounts(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/query?q="
        access_token = token
        query = "SELECT Id, Name, Type FROM Account"
        conditions = ""
        for key, value in params.items():
            if key == "fields":
                query = f"SELECT {value} FROM Account"

            if key == "conditions":
                conditions = " AND ".join(value)
                conditions = " WHERE " + conditions

        url += query + conditions

        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_create_account(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Account"
        if "name" in params:
            access_token = token
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_update_account(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Account/"
        if "id" in params:
            access_token = token
            account_id = params["id"]
            url += f"{account_id}"
            data = {}
            for key, value in params.items():
                if key == "id":
                    continue
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.patch(url, headers=headers, json=data)
            if response.status_code == 204:
                return {"Result": f"Updated Account ID: {account_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_delete_account(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Account/"
        if "id" in params:
            access_token = token
            account_id = params["id"]
            url += f"{account_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            if response.status_code == 204:
                return {"Result": f"Deleted Account ID: {account_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


###########################################################################

# Custom Object Actions


def salesforce_get_custom_object(domain, token, params):
    try:
        url = (
            f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/"
        )
        if "customObjectName" in params and "id" in params:
            access_token = token
            custom_object_name = params["customObjectName"]
            record_id = params["id"]
            url += f"{custom_object_name}/{record_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_list_custom_objects(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/query?q="
        if "customObjectName" in params:
            access_token = token
            custom_object_name = params["customObjectName"]
            query = "Select id FROM " + custom_object_name
            conditions = ""

            for key, value in params.items():
                if key == "customObjectName":
                    continue
                if key == "fields":
                    query = f"SELECT {value} FROM " + custom_object_name

                if key == "conditions":
                    conditions = " AND ".join(value)
                    conditions = " WHERE " + conditions

            url += query + conditions

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_create_custom_object(domain, token, params):
    try:
        url = (
            f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/"
        )
        if "customObjectName" in params and "name" in params:
            access_token = token
            custom_object_name = params["customObjectName"]
            url += f"{custom_object_name}"

            data = {}
            for key, value in params.items():
                if key == "customObjectName":
                    continue
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_update_custom_object(domain, token, params):
    try:
        url = (
            f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/"
        )
        if "customObjectName" in params and "id" in params:
            access_token = token
            custom_object_name = params["customObjectName"]
            record_id = params["id"]
            url += f"{custom_object_name}/{record_id}"
            data = {}
            keys_to_skip = ["id", "customObjectName"]
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.patch(url, headers=headers, json=data)
            if response.status_code == 204:
                return {"Result": f"Updated Custom Object ID: {record_id} From {custom_object_name}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_delete_custom_object(domain, token, params):
    try:
        url = (
            f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/"
        )
        if "customObjectName" in params and "id" in params:
            access_token = token
            custom_object_name = params["customObjectName"]
            record_id = params["id"]
            url += f"{custom_object_name}/{record_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            if response.status_code == 204:
                return {"Result": f"Deleted Custom Object ID: {record_id} From {custom_object_name}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


###########################################################################

# Search Action


def salesforce_search_records(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/query?q="
        if "query" in params:
            access_token = token
            query = params["query"]
            url += query
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


###########################################################################

# Attachment Actions


def salesforce_get_attachment(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Attachment/"
        if "id" in params:
            access_token = token
            attachment_id = params["id"]
            url += f"{attachment_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_get_attachment_summary(domain, token):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Attachment"

        access_token = token
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_list_attachments(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/query?q="

        access_token = token
        query = "SELECT Id, Name FROM Attachment"
        conditions = ""
        for key, value in params.items():
            if key == "fields":
                query = f"SELECT {value} FROM Attachment"

            if key == "conditions":
                conditions = " AND ".join(value)
                conditions = " WHERE " + conditions

        url += query + conditions

        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_create_attachment(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Attachment"
        if (
            "name" in params
            and "parentId" in params
            and ("binary" in params or "url" in params)
        ):
            access_token = token

            binary_data = None
            if params.get("binary"):
                binary_data = params["binary"]

            file_path = None
            if params.get("url"):
                file_path = params["url"]

            keys_to_skip = ["binary", "url"]
            data = {}
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    data[key] = value

            if file_path is not None:
                myFile = requests.get(file_path)
                if myFile.status_code == 200:
                    binary_data = myFile.content
                else:
                    raise Exception(
                        f"Failed to fetch the file. Status code: {myFile.status_code}"
                    )

            base64_data = base64.b64encode(binary_data.encode()).decode("utf-8")
            data["body"] = base64_data

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_update_attachment(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Attachment/"
        if "id" in params:
            access_token = token
            attachment_id = params["id"]
            url += f"{attachment_id}"

            data = {}
            for key, value in params.items():
                if key == "id":
                    continue
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.patch(url, headers=headers, json=data)
            if response.status_code == 204:
                return {"Result": f"Updated Attachment ID: {attachment_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


def salesforce_delete_attachment(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Attachment/"
        if "id" in params:
            access_token = token
            attachment_id = params["id"]
            url += f"{attachment_id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            if response.status_code == 204:
                return {"Result": f"Deleted Attachment ID: {attachment_id}"}
            else:
                if response.content:
                    result = response.json()
                    if type(result) == list:
                        for item in result[0]:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
                    else:
                        for item in result:
                            if item == "errorCode":
                                raise Exception(result)
                        return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


###########################################################################

# Flow Actions


def salesforce_list_flows(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/actions/custom/flow"
        access_token = token
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        result = response.json()
        if type(result) == list:
            for item in result[0]:
                if item == "errorCode":
                    raise Exception(result)
            return result
        else:
            for item in result:
                if item == "errorCode":
                    raise Exception(result)
            return result

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


###########################################################################

# Add Notes to Opportunity OR Lead OR Contact OR Account


def salesforce_add_note_to_record(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/Note"
        if "parentId" in params and "title" in params:
            access_token = token
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)


###########################################################################

# Document Action


def salesforce_upload_document(domain, token, params):
    try:
        url = f"https://{domain}.my.salesforce.com/services/data/v58.0/sobjects/ContentVersion"
        if (
            "title" in params
            and "pathOnClient" in params
            and ("binary" in params or "url" in params)
        ):
            access_token = token

            binary_data = None
            if params.get("binary"):
                binary_data = params["binary"]

            file_path = None
            if params.get("url"):
                file_path = params["url"]

            keys_to_skip = ["binary", "url"]
            data = {}
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    data[key] = value

            if file_path is not None:
                myFile = requests.get(file_path)
                if myFile.status_code == 200:
                    binary_data = myFile.content
                else:
                    raise Exception(
                        f"Failed to fetch the file. Status code: {myFile.status_code}"
                    )

            base64_data = base64.b64encode(binary_data.encode()).decode("utf-8")
            data["versionData"] = base64_data

            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if type(result) == list:
                for item in result[0]:
                    if item == "errorCode":
                        raise Exception(result)
                return result
            else:
                for item in result:
                    if item == "errorCode":
                        raise Exception(result)
                return result
        else:
            raise Exception("Missing input data")

    except Exception as error:
        if "Expecting value" in str(error):
            raise Exception("Invalid Domain")
        else:
            raise Exception(error)