import requests
 
######################     Generate Access Token      ######################

def zohoCRM_refresh_access_token(client_id, client_secret, refresh_token):
    try:
        url = f"https://accounts.zoho.com/oauth/v2/token?refresh_token={refresh_token}&client_id={client_id}&client_secret={client_secret}&grant_type=refresh_token"
        response = requests.post(url)
        response_json = response.json()
        if "access_token" in response_json:
            return response_json["access_token"]
        else:
            raise Exception({"access_token": "Invalid access_token"})

    except Exception as error:
        raise Exception(error)
   
###########################################################################################################################
# Contact Actions


def zohoCRM_list_contacts(access_token, params):
    try:
        url = f"https://www.zohoapis.com/crm/v5/Contacts?"
        fields = "Owner,$currency_symbol,$field_states,Last_Activity_Time,$state,$process_flow,$locked_for_me,id,Created_Time,$editable,Created_By,$zia_owner_assignment,Description,$review_process,Record_Image,Modified_By,$review,Phone,Account_Name,Modified_Time,$orchestration,$in_merge,Locked__s,Tag,Fax,$approval_state"

        for key, value in params.items():
            if key == "fields":
                fields = value
                continue
            if value:
                url += f"&{key}={value}"

        url += f"&fields={fields}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 204:
            return {"Result": "No Contacts Yet!"}
        response_json = response.json()
        if "code" in response_json:
            if response_json["code"] == "UNABLE_TO_PARSE_DATA_TYPE":
                raise Exception("One of the parameters is in wrong format")
            else:
               raise Exception(response_json)
        return {"Contacts": response_json["data"]}

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_get_contact(access_token, params):
    try:
        if "contact_id" in params and params["contact_id"]:
            id = params["contact_id"]
            url = f"https://www.zohoapis.com/crm/v5/Contacts/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return {"Contact": response_json["data"]}

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_delete_contact(access_token, params):
    try:
        if "contact_id" in params and params["contact_id"]:
            id = params["contact_id"]
            url = f"https://www.zohoapis.com/crm/v5/Contacts/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_create_contact(access_token, params):
    try:
        if "Last_Name" in params and params["Last_Name"]:
            url = f"https://www.zohoapis.com/crm/v5/Contacts"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_update_contact(access_token, params):
    try:
        if "contact_id" in params and params["contact_id"]:
            id = params["contact_id"]
            url = f"https://www.zohoapis.com/crm/v5/Contacts/{id}"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.put(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


###########################################################################################################################
# Account Actions


def zohoCRM_list_accounts(access_token, params):
    try:
        url = f"https://www.zohoapis.com/crm/v5/Accounts?"
        fields = "Owner,$currency_symbol,$field_states,Account_Type,SIC_Code,Last_Activity_Time,Industry,Account_Site,$state,$process_flow,Billing_Country,$locked_for_me,$approval,Billing_Street,Created_Time,$wizard_connection_path,$editable,Billing_Code,Shipping_City,Shipping_Country,Shipping_Code,Billing_City,Created_By,$zia_owner_assignment,Annual_Revenue,Shipping_Street,Ownership,Description,Rating,Shipping_State,$review_process,Website,Employees,Record_Image,Modified_By,$review,Phone,Account_Name,$zia_visions,Account_Number,Ticker_Symbol,Modified_Time,$orchestration,Parent_Account,$in_merge,Locked__s,Billing_State,Tag,Fax,$approval_state"

        for key, value in params.items():
            if key == "fields":
                fields = value
                continue
            if value:
                url += f"&{key}={value}"

        url += f"&fields={fields}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 204:
            return {"Result": "No Accounts Yet!"}
        response_json = response.json()
        if "code" in response_json:
            if response_json["code"] == "UNABLE_TO_PARSE_DATA_TYPE":
                raise Exception("One of the parameters is in wrong format")
            else:
               raise Exception(response_json)
        return {"Accounts": response_json["data"]}

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_get_account(access_token, params):
    try:
        if "account_id" in params and params["account_id"]:
            id = params["account_id"]
            url = f"https://www.zohoapis.com/crm/v5/Accounts/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return {"Account": response_json["data"]}

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_delete_account(access_token, params):
    try:
        if "account_id" in params and params["account_id"]:
            id = params["account_id"]
            url = f"https://www.zohoapis.com/crm/v5/Accounts/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_create_account(access_token, params):
    try:
        if "Account_Name" in params and params["Account_Name"]:
            url = f"https://www.zohoapis.com/crm/v5/Accounts"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_update_account(access_token, params):
    try:
        if "account_id" in params and params["account_id"]:
            id = params["account_id"]
            url = f"https://www.zohoapis.com/crm/v5/Accounts/{id}"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.put(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


###########################################################################################################################
# Deal Actions


def zohoCRM_list_deals(access_token, params):
    try:
        url = f"https://www.zohoapis.com/crm/v5/Deals?"
        fields = "Owner,Description,$currency_symbol,Campaign_Source,$field_states,$review_process,Closing_Date,Reason_For_Loss__s,Last_Activity_Time,Modified_By,$review,Lead_Conversion_Time,$state,$process_flow,Deal_Name,Expected_Revenue,Overall_Sales_Duration,Stage,$locked_for_me,Account_Name,$zia_visions,$approval,Modified_Time,Created_Time,Amount,Next_Step,Probability,$wizard_connection_path,$editable,$orchestration,Contact_Name,Sales_Cycle_Duration,Type,$in_merge,Locked__s,Lead_Source,Created_By,Tag,$zia_owner_assignment,$approval_state,$pathfinder"

        for key, value in params.items():
            if key == "fields":
                fields = value
                continue
            if value:
                url += f"&{key}={value}"

        url += f"&fields={fields}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 204:
            return {"Result": "No Deals Yet!"}
        response_json = response.json()
        if "code" in response_json:
            if response_json["code"] == "UNABLE_TO_PARSE_DATA_TYPE":
                raise Exception("One of the parameters is in wrong format")
            else:
               raise Exception(response_json)
        return {"Deals": response_json["data"]}

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_get_deal(access_token, params):
    try:
        if "deal_id" in params and params["deal_id"]:
            id = params["deal_id"]
            url = f"https://www.zohoapis.com/crm/v5/Deals/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return {"Deal": response_json["data"]}

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_delete_deal(access_token, params):
    try:
        if "deal_id" in params and params["deal_id"]:
            id = params["deal_id"]
            url = f"https://www.zohoapis.com/crm/v5/Deals/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_create_deal(access_token, params):
    try:
        if "Deal_Name" in params and params["Deal_Name"] and "Stage" in params and params["Stage"]:
            url = f"https://www.zohoapis.com/crm/v5/Deals"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_update_deal(access_token, params):
    try:
        if "deal_id" in params and params["deal_id"]:
            id = params["deal_id"]
            url = f"https://www.zohoapis.com/crm/v5/Deals/{id}"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.put(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


###########################################################################################################################
# Lead Actions


def zohoCRM_list_leads(access_token, params):
    try:
        url = f"https://www.zohoapis.com/crm/v5/Leads?"
        fields = "Owner,Company,Email,$currency_symbol,$field_states,Last_Activity_Time,Industry,$state,Unsubscribed_Mode,Street,Zip_Code,$approval,Created_Time,$editable,City,No_of_Employees,Converted__s,Converted_Date_Time,Converted_Account,State,Country,Created_By,Annual_Revenue,Secondary_Email,Description,Rating,Website,Twitter,Salutation,First_Name,Full_Name,Lead_Status,Record_Image,Modified_By,Converted_Deal,$review,Lead_Conversion_Time,Skype_ID,Phone,Email_Opt_Out,Designation,Modified_Time,Unsubscribed_Time,Converted_Contact,Mobile,Last_Name,Locked__s,Lead_Source,Tag,Fax"

        for key, value in params.items():
            if key == "fields":
                fields = value
                continue
            if value:
                url += f"&{key}={value}"

        url += f"&fields={fields}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 204:
            return {"Result": "No Leads Yet!"}
        response_json = response.json()
        if "code" in response_json:
            if response_json["code"] == "UNABLE_TO_PARSE_DATA_TYPE":
                raise Exception("One of the parameters is in wrong format")
            else:
               raise Exception(response_json)
        return {"Leads": response_json["data"]}

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_get_lead(access_token, params):
    try:
        if "lead_id" in params and params["lead_id"]:
            id = params["lead_id"]
            url = f"https://www.zohoapis.com/crm/v5/Leads/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return {"Lead": response_json["data"]}

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_delete_lead(access_token, params):
    try:
        if "lead_id" in params and params["lead_id"]:
            id = params["lead_id"]
            url = f"https://www.zohoapis.com/crm/v5/Leads/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_create_lead(access_token, params):
    try:
        if "Last_Name" in params and params["Last_Name"] and "Company" in params and params["Company"]:
            url = f"https://www.zohoapis.com/crm/v5/Leads"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_update_lead(access_token, params):
    try:
        if "lead_id" in params and params["lead_id"]:
            id = params["lead_id"]
            url = f"https://www.zohoapis.com/crm/v5/Leads/{id}"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.put(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


###########################################################################################################################
# Product Actions


def zohoCRM_list_products(access_token, params):
    try:
        url = f"https://www.zohoapis.com/crm/v5/Products?"
        fields = "Product_Category,Qty_in_Demand,Owner,Description,Vendor_Name,Sales_Start_Date,Tax,Product_Active,Record_Image,Modified_By,Product_Code,Manufacturer,Support_Expiry_Date,$approval,Modified_Time,Created_Time,Commission_Rate,Product_Name,Handler,Support_Start_Date,Usage_Unit,Qty_Ordered,Qty_in_Stock,Created_By,Tag,Sales_End_Date,Unit_Price,Taxable,Reorder_Level,$currency_symbol,$review_process,$sharing_permission,$state,$approval_state"

        for key, value in params.items():
            if key == "fields":
                fields = value
                continue
            if value:
                url += f"&{key}={value}"

        url += f"&fields={fields}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 204:
            return {"Result": "No Products Yet!"}
        response_json = response.json()
        if "code" in response_json:
            if response_json["code"] == "UNABLE_TO_PARSE_DATA_TYPE":
                raise Exception("One of the parameters is in wrong format")
            else:
               raise Exception(response_json)
        return {"Products": response_json["data"]}

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_get_product(access_token, params):
    try:
        if "product_id" in params and params["product_id"]:
            id = params["product_id"]
            url = f"https://www.zohoapis.com/crm/v5/Products/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return {"Product": response_json["data"]}

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_delete_product(access_token, params):
    try:
        if "product_id" in params and params["product_id"]:
            id = params["product_id"]
            url = f"https://www.zohoapis.com/crm/v5/Products/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_create_product(access_token, params):
    try:
        if "Product_Name" in params and params["Product_Name"]:
            url = f"https://www.zohoapis.com/crm/v5/Products"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_update_product(access_token, params):
    try:
        if "product_id" in params and params["product_id"]:
            id = params["product_id"]
            url = f"https://www.zohoapis.com/crm/v5/Products/{id}"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.put(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


###########################################################################################################################
# Purchase Order Actions


def zohoCRM_list_purchase_orders(access_token, params):
    try:
        url = f"https://www.zohoapis.com/crm/v5/Purchase_Orders?"
        fields = "Owner,Tax,PO_Date,Billing_Country,Carrier,Status,Grand_Total,$approval,PO_Number,Billing_Street,Adjustment,Created_Time,Billing_Code,Tracking_Number,Excise_Duty,Shipping_City,Shipping_Country,Shipping_Code,Billing_City,Requisition_No,Created_By,Shipping_Street,Description,Discount,Vendor_Name,Shipping_State,Modified_By,Purchase_Items,Sales_Commission,Modified_Time,Due_Date,Terms_and_Conditions,Sub_Total,Subject,Contact_Name,Locked__s,Billing_State,Tag"

        for key, value in params.items():
            if key == "fields":
                fields = value
                continue
            if value:
                url += f"&{key}={value}"

        url += f"&fields={fields}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 204:
            return {"Result": "No Purchase Orders Yet!"}
        response_json = response.json()
        if "code" in response_json:
            if response_json["code"] == "UNABLE_TO_PARSE_DATA_TYPE":
                raise Exception("One of the parameters is in wrong format")
            else:
               raise Exception(response_json)
        return {"Purchase Orders": response_json["data"]}

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_get_purchase_order(access_token, params):
    try:
        if "purchase_order_id" in params and params["purchase_order_id"]:
            id = params["purchase_order_id"]
            url = f"https://www.zohoapis.com/crm/v5/Purchase_Orders/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return {"Purchase Order": response_json["data"]}

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_delete_purchase_order(access_token, params):
    try:
        if "purchase_order_id" in params and params["purchase_order_id"]:
            id = params["purchase_order_id"]
            url = f"https://www.zohoapis.com/crm/v5/Purchase_Orders/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_create_purchase_order(access_token, params):
    try:
        if "Subject" in params and params["Subject"] and "Vendor_Name" in params and params["Vendor_Name"] and "Purchase_Items" in params and params["Purchase_Items"]:
            url = f"https://www.zohoapis.com/crm/v5/Purchase_Orders"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_update_purchase_order(access_token, params):
    try:
        if "purchase_order_id" in params and params["purchase_order_id"]:
            id = params["purchase_order_id"]
            url = f"https://www.zohoapis.com/crm/v5/Purchase_Orders/{id}"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.put(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


###########################################################################################################################
# Quote Actions


def zohoCRM_list_quotes(access_token, params):
    try:
        url = f"https://www.zohoapis.com/crm/v5/Quotes?"
        fields = "Owner,Tax,Deal_Name,Billing_Country,Carrier,Grand_Total,Billing_Street,Adjustment,Created_Time,Billing_Code,Shipping_City,Shipping_Country,Shipping_Code,Billing_City,Quote_Number,Created_By,Shipping_Street,Description,Discount,Shipping_State,Modified_By,Valid_Till,Team,Account_Name,Quote_Stage,Modified_Time,Terms_and_Conditions,Sub_Total,Subject,Contact_Name,Locked__s,Billing_State,Tag"

        for key, value in params.items():
            if key == "fields":
                fields = value
                continue
            if value:
                url += f"&{key}={value}"

        url += f"&fields={fields}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 204:
            return {"Result": "No Quotes Yet!"}
        response_json = response.json()
        if "code" in response_json:
            if response_json["code"] == "UNABLE_TO_PARSE_DATA_TYPE":
                raise Exception("One of the parameters is in wrong format")
            else:
               raise Exception(response_json)
        return {"Quotes": response_json["data"]}

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_get_quote(access_token, params):
    try:
        if "quote_id" in params and params["quote_id"]:
            id = params["quote_id"]
            url = f"https://www.zohoapis.com/crm/v5/Quotes/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return {"Quote": response_json["data"]}

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_delete_quote(access_token, params):
    try:
        if "quote_id" in params and params["quote_id"]:
            id = params["quote_id"]
            url = f"https://www.zohoapis.com/crm/v5/Quotes/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_create_quote(access_token, params):
    try:
        if "Subject" in params and params["Subject"] and "Quoted_Items" in params and params["Quoted_Items"]:
            url = f"https://www.zohoapis.com/crm/v5/Quotes"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_update_quote(access_token, params):
    try:
        if "quote_id" in params and params["quote_id"]:
            id = params["quote_id"]
            url = f"https://www.zohoapis.com/crm/v5/Quotes/{id}"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.put(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


###########################################################################################################################
# Sales Order Actions


def zohoCRM_list_sales_orders(access_token, params):
    try:
        url = f"https://www.zohoapis.com/crm/v5/Sales_Orders?"
        fields = "Owner,Customer_No,Tax,Deal_Name,Billing_Country,Carrier,Quote_Name,Status,Grand_Total,Billing_Street,Adjustment,Created_Time,Billing_Code,Excise_Duty,Shipping_City,Shipping_Country,Shipping_Code,Billing_City,Purchase_Order,Created_By,Shipping_Street,Description,Discount,Shipping_State,Modified_By,Account_Name,Sales_Commission,Modified_Time,Due_Date,Terms_and_Conditions,Sub_Total,Subject,Contact_Name,SO_Number,Locked__s,Billing_State,Tag,Pending"

        for key, value in params.items():
            if key == "fields":
                fields = value
                continue
            if value:
                url += f"&{key}={value}"

        url += f"&fields={fields}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 204:
            return {"Result": "No Sales Orders Yet!"}
        response_json = response.json()
        if "code" in response_json:
            if response_json["code"] == "UNABLE_TO_PARSE_DATA_TYPE":
                raise Exception("One of the parameters is in wrong format")
            else:
               raise Exception(response_json)
        return {"Sales Orders": response_json["data"]}

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_get_sales_order(access_token, params):
    try:
        if "sales_order_id" in params and params["sales_order_id"]:
            id = params["sales_order_id"]
            url = f"https://www.zohoapis.com/crm/v5/Sales_Orders/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return {"Sales Order": response_json["data"]}

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_delete_sales_order(access_token, params):
    try:
        if "sales_order_id" in params and params["sales_order_id"]:
            id = params["sales_order_id"]
            url = f"https://www.zohoapis.com/crm/v5/Sales_Orders/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_create_sales_order(access_token, params):
    try:
        if "Subject" in params and params["Subject"] and "Ordered_Items" in params and params["Ordered_Items"]:
            url = f"https://www.zohoapis.com/crm/v5/Sales_Orders"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_update_sales_order(access_token, params):
    try:
        if "sales_order_id" in params and params["sales_order_id"]:
            id = params["sales_order_id"]
            url = f"https://www.zohoapis.com/crm/v5/Sales_Orders/{id}"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.put(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


###########################################################################################################################
# Vendor Actions


def zohoCRM_list_vendors(access_token, params):
    try:
        url = f"https://www.zohoapis.com/crm/v5/Vendors?"
        fields = "Owner,Email,Category,Description,Vendor_Name,Website,Record_Image,Modified_By,Phone,Street,Zip_Code,Modified_Time,Created_Time,City,State,GL_Account,Locked__s,Country,Created_By,Tag"

        for key, value in params.items():
            if key == "fields":
                fields = value
                continue
            if value:
                url += f"&{key}={value}"

        url += f"&fields={fields}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 204:
            return {"Result": "No Vendors Yet!"}
        response_json = response.json()
        if "code" in response_json:
            if response_json["code"] == "UNABLE_TO_PARSE_DATA_TYPE":
                raise Exception("One of the parameters is in wrong format")
            else:
               raise Exception(response_json)
        return {"Vendors": response_json["data"]}

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_get_vendor(access_token, params):
    try:
        if "vendor_id" in params and params["vendor_id"]:
            id = params["vendor_id"]
            url = f"https://www.zohoapis.com/crm/v5/Vendors/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return {"Vendor": response_json["data"]}

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_delete_vendor(access_token, params):
    try:
        if "vendor_id" in params and params["vendor_id"]:
            id = params["vendor_id"]
            url = f"https://www.zohoapis.com/crm/v5/Vendors/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_create_vendor(access_token, params):
    try:
        if "Vendor_Name" in params and params["Vendor_Name"]:
            url = f"https://www.zohoapis.com/crm/v5/Vendors"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_update_vendor(access_token, params):
    try:
        if "vendor_id" in params and params["vendor_id"]:
            id = params["vendor_id"]
            url = f"https://www.zohoapis.com/crm/v5/Vendors/{id}"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.put(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


###########################################################################################################################
# Invoice Actions


def zohoCRM_list_invoices(access_token, params):
    try:
        url = f"https://www.zohoapis.com/crm/v5/Invoices?"
        fields = "Owner,Tax,Billing_Country,Status,Grand_Total,Billing_Street,Adjustment,Created_Time,Billing_Code,Excise_Duty,Shipping_City,Shipping_Country,Shipping_Code,Billing_City,Purchase_Order,Created_By,Shipping_Street,Description,Discount,Shipping_State,Invoice_Date,Modified_By,Account_Name,Sales_Order,Deal_Name__s,Sales_Commission,Modified_Time,Due_Date,Terms_and_Conditions,Sub_Total,Invoice_Number,Subject,Contact_Name,Locked__s,Billing_State,Tag"

        for key, value in params.items():
            if key == "fields":
                fields = value
                continue
            if value:
                url += f"&{key}={value}"

        url += f"&fields={fields}"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 204:
            return {"Result": "No Invoices Yet!"}
        response_json = response.json()
        if "code" in response_json:
            if response_json["code"] == "UNABLE_TO_PARSE_DATA_TYPE":
                raise Exception("One of the parameters is in wrong format")
            else:
               raise Exception(response_json)
        return {"Invoices": response_json["data"]}

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_get_invoice(access_token, params):
    try:
        if "invoice_id" in params and params["invoice_id"]:
            id = params["invoice_id"]
            url = f"https://www.zohoapis.com/crm/v5/Invoices/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return {"Invoice": response_json["data"]}

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_delete_invoice(access_token, params):
    try:
        if "invoice_id" in params and params["invoice_id"]:
            id = params["invoice_id"]
            url = f"https://www.zohoapis.com/crm/v5/Invoices/{id}"
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.delete(url, headers=headers)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("ID Not Found")
        else:
            raise Exception(e)


def zohoCRM_create_invoice(access_token, params):
    try:
        if "Subject" in params and params["Subject"] and "Invoiced_Items" in params and params["Invoiced_Items"]:
            url = f"https://www.zohoapis.com/crm/v5/Invoices"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.post(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)


def zohoCRM_update_invoice(access_token, params):
    try:
        if "invoice_id" in params and params["invoice_id"]:
            id = params["invoice_id"]
            url = f"https://www.zohoapis.com/crm/v5/Invoices/{id}"
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            paylod = {"data": [data]}
            headers = {"Authorization": f"Bearer {access_token}"}
            response = requests.put(url, headers=headers, json=paylod)
            response_json = response.json()
            if "code" in response_json and response_json["code"] != 0:
                raise Exception(response_json)
            if response_json["data"] and "code" in response_json["data"][0] and response_json["data"][0]["code"] != "SUCCESS":
                raise Exception(response_json)
            return response_json

        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        if "Expecting value" in str(e):
            raise Exception("Invalid Base URL")
        else:
            raise Exception(e)