import xmlrpc.client

def odoo_create_contact(url, db, username, apiPassword, params):
    try:
        if "name" in params:
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "res.partner"
                data = {}
                for key, value in params.items():
                    if value:
                        data[key] = value
                id = models.execute_kw(db, uid, apiPassword, model, "create", [data])
                return {"id": id}
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_contact_by_id(url, db, username, apiPassword, params):
    try:
        if "contact_id" in params:
            id = params.get("contact_id")
            fields = params.get("fields", [])
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "res.partner"
                data = models.execute_kw(db, uid, apiPassword, model, "read", [int(id)], {"fields": fields})
                if data:
                    return {"Contact": data}
                else:
                    raise Exception("Not found")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_many_contact(url, db, username, apiPassword, params):
    try:
        limit = params.get("limit")
        fields = params.get("fields", [])
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        uid = common.authenticate(db, username, apiPassword, {})
        if uid:
            models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
            model = "res.partner"
            ids = models.execute_kw(db, uid, apiPassword, model, "search", [[]])
            data = models.execute_kw(db, uid, apiPassword, model, "read", [ids], {"fields": fields})
            return {"Contacts": data[:limit]}
        else:
            raise Exception("Authentication failed. Please check your credentials.")
    except Exception as error:
        raise Exception(error)

def odoo_delete_contact(url, db, username, apiPassword, params):
    try:
        if "contact_id" in params:
            id = params.get("contact_id")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(
                    f"{url}/xmlrpc/2/object")
                model = "res.partner"
                if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                    models.execute_kw(db, uid, apiPassword, model, "unlink", [[id]])
                    return {"message": "Deleted successfully"}
                else:
                    raise Exception("ID not found or could not be deleted.")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_update_contact(url, db, username, apiPassword, params):
    try:
        if "contact_id" in params:
            id = params["contact_id"]
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "res.partner"
                data = {}
                for key, value in params.items():
                    skip_keys = ["contact_id"]
                    if key in skip_keys:
                        continue
                    if value:
                        data[key] = value
                if data:
                    if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                        models.execute_kw(db, uid, apiPassword, model, "write", [[int(id)], data])
                        return {"message": "Updated successfully"}
                    else:
                        raise Exception("Not found")
                else:
                    raise Exception("Please specify at least one field to update")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_create_user(url, db, username, apiPassword, params):
    try:
        if "name" in params and "login" in params:
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "res.users"
                data = {}
                for key, value in params.items():
                    if value:
                        data[key] = value
                id = models.execute_kw(db, uid, apiPassword, model, "create", [data])
                return {"id": id}
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_user_by_id(url, db, username, apiPassword, params):
    try:
        if "user_id" in params:
            id = params.get("user_id")
            fields = params.get("fields", [])
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "res.users"
                data = models.execute_kw(db, uid, apiPassword, model, "read", [int(id)], {"fields": fields})
                if data:
                    return {"User": data}
                else:
                    raise Exception("Not found")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_many_users(url, db, username, apiPassword, params):
    try:
        limit = params.get("limit")
        fields = params.get("fields", [])
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        uid = common.authenticate(db, username, apiPassword, {})
        if uid:
            models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
            model = "res.users"
            ids = models.execute_kw(
                db, uid, apiPassword, model, "search", [[]])
            data = models.execute_kw(
                db, uid, apiPassword, model, "read", [ids], {"fields": fields})
            return {"Users": data[:limit]}
        else:
            raise Exception("Authentication failed. Please check your credentials.")
    except Exception as error:
        raise Exception(error)

def odoo_delete_user(url, db, username, apiPassword, params):
    try:
        if "user_id" in params:
            id = params.get("user_id")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "res.users"
                if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                    models.execute_kw(db, uid, apiPassword, model, "unlink", [[id]])
                    return {"message": "Deleted successfully"}
                else:
                    raise Exception("ID not found or could not be deleted.")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_update_user(url, db, username, apiPassword, params):
    try:
        if "user_id" in params:
            id = params["user_id"]
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(
                    f"{url}/xmlrpc/2/object")
                model = "res.users"
                data = {}
                for key, value in params.items():
                    skip_keys = ["user_id"]
                    if key in skip_keys:
                        continue
                    if value:
                        data[key] = value
                if data:
                    if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                        models.execute_kw(db, uid, apiPassword, model, "write", [[int(id)], data])
                        return {"message": "Updated successfully"}
                    else:
                        raise Exception("Not found")
                else:
                    raise Exception("Please specify at least one field to update")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_create_opportunity(url, db, username, apiPassword, params):
    try:
        if "name" in params:
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "crm.lead"
                data = {}
                for key, value in params.items():
                    if value:
                        data[key] = value
                id = models.execute_kw(db, uid, apiPassword, model, "create", [data])
                return {"id": id}
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_opportunity_by_id(url, db, username, apiPassword, params):
    try:
        if "opportunity_id" in params:
            id = params.get("opportunity_id")
            fields = params.get("fields", [])
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "crm.lead"
                data = models.execute_kw(db, uid, apiPassword, model, "read", [int(id)], {"fields": fields})
                if data:
                    return {"Opportunity": data}
                else:
                    raise Exception("Not found")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_many_opportunity(url, db, username, apiPassword, params):
    try:
        limit = params.get("limit")
        fields = params.get("fields", [])
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        uid = common.authenticate(db, username, apiPassword, {})
        if uid:
            models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
            model = "crm.lead"
            ids = models.execute_kw(db, uid, apiPassword, model, "search", [[]])
            data = models.execute_kw(db, uid, apiPassword, model, "read", [ids], {"fields": fields})
            return {"Opportunities": data[:limit]}
        else:
            raise Exception("Authentication failed. Please check your credentials.")
    except Exception as error:
        raise Exception(error)

def odoo_delete_opportunity(url, db, username, apiPassword, params):
    try:
        if "opportunity_id" in params:
            id = params.get("opportunity_id")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(
                    f"{url}/xmlrpc/2/object")
                model = "crm.lead"
                if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                    models.execute_kw(db, uid, apiPassword, model, "unlink", [[id]])
                    return {"message": "Deleted successfully"}
                else:
                    raise Exception("ID not found or could not be deleted.")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_update_opportunity(url, db, username, apiPassword, params):
    try:
        if "opportunity_id" in params:
            id = params["opportunity_id"]
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(
                    f"{url}/xmlrpc/2/object")
                model = "crm.lead"
                data = {}
                for key, value in params.items():
                    skip_keys = ["opportunity_id"]
                    if key in skip_keys:
                        continue
                    if value:
                        data[key] = value
                if data:
                    if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                        models.execute_kw(db, uid, apiPassword, model, "write", [[int(id)], data])
                        return {"message": "Updated successfully"}
                    else:
                        raise Exception("Not found")
                else:
                    raise Exception("Please specify at least one field to update")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_create_sales_team(url, db, username, apiPassword, params):
    try:
        if "name" in params:
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "crm.team"
                data = {}
                for key, value in params.items():
                    if value:
                        data[key] = value
                id = models.execute_kw(db, uid, apiPassword, model, "create", [data])
                return {"id": id}
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_sales_team_by_id(url, db, username, apiPassword, params):
    try:
        if "sales_team_id" in params:
            id = params.get("sales_team_id")
            fields = params.get("fields", [])
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "crm.team"
                data = models.execute_kw(db, uid, apiPassword, model, "read", [int(id)], {"fields": fields})
                if data:
                    return {"SalesTeam": data}
                else:
                    raise Exception("Not found")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_many_sales_team(url, db, username, apiPassword, params):
    try:
        limit = params.get("limit")
        fields = params.get("fields", [])
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        uid = common.authenticate(db, username, apiPassword, {})
        if uid:
            models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
            model = "crm.team"
            ids = models.execute_kw(db, uid, apiPassword, model, "search", [[]])
            data = models.execute_kw(db, uid, apiPassword, model, "read", [ids], {"fields": fields})
            return {"SalesTeams": data[:limit]}
        else:
            raise Exception(
                {"error": "Authentication failed. Please check your credentials."})
    except Exception as error:
        raise Exception(error)

def odoo_delete_sales_team(url, db, username, apiPassword, params):
    try:
        if "sales_team_id" in params:
            id = params.get("sales_team_id")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "crm.team"
                if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                    models.execute_kw(db, uid, apiPassword, model, "unlink", [[id]])
                    return {"message": "Deleted successfully"}
                else:
                    raise Exception("ID not found or could not be deleted.")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_update_sales_team(url, db, username, apiPassword, params):
    try:
        if "sales_team_id" in params:
            id = params["sales_team_id"]
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "crm.team"
                data = {}
                for key, value in params.items():
                    skip_keys = ["sales_team_id"]
                    if key in skip_keys:
                        continue
                    if value:
                        data[key] = value
                if data:
                    if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                        models.execute_kw(db, uid, apiPassword, model, "write", [[int(id)], data])
                        return {"message": "Updated successfully"}
                    else:
                        raise Exception("Not found")
                else:
                    raise Exception("Please specify at least one field to update")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_create_sales_team_member(url, db, username, apiPassword, params):
    try:
        if "crm_team_id" in params and "user_id" in params:
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "crm.team.member"
                data = {}
                for key, value in params.items():
                    if value:
                        data[key] = value
                id = models.execute_kw(db, uid, apiPassword, model, "create", [data])
                return {"id": id}
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_sales_team_member_by_id(url, db, username, apiPassword, params):
    try:
        if "crm_team_id" in params:
            id = params.get("crm_team_id")
            fields = params.get("fields", [])
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "crm.team.member"
                data = models.execute_kw(db, uid, apiPassword, model, "read", [int(id)], {"fields": fields})
                if data:
                    return {"SalesTeamMember": data}
                else:
                    raise Exception("Not found")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_many_sales_team_member(url, db, username, apiPassword, params):
    try:
        limit = params.get("limit")
        fields = params.get("fields", [])
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        uid = common.authenticate(db, username, apiPassword, {})
        if uid:
            models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
            model = "crm.team.member"
            ids = models.execute_kw(db, uid, apiPassword, model, "search", [[]])
            data = models.execute_kw(db, uid, apiPassword, model, "read", [ids], {"fields": fields})
            return {"SalesTeamMembers": data[:limit]}
        else:
            raise Exception("Authentication failed. Please check your credentials.")
    except Exception as error:
        raise Exception(error)

def odoo_delete_sales_team_member(url, db, username, apiPassword, params):
    try:
        if "crm_team_id" in params:
            id = params.get("crm_team_id")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(
                    f"{url}/xmlrpc/2/object")
                model = "crm.team.member"
                if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                    models.execute_kw(db, uid, apiPassword, model, "unlink", [[id]])
                    return {"message": "Deleted successfully"}
                else:
                    raise Exception("ID not found or could not be deleted.")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_many_sale_orders(url, db, username, apiPassword, params):
    try:
        limit = params.get("limit")
        fields = params.get("fields", [])
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        uid = common.authenticate(db, username, apiPassword, {})
        if uid:
            models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
            model = "sale.order"
            ids = models.execute_kw(db, uid, apiPassword, model, "search", [[]])
            data = models.execute_kw(db, uid, apiPassword, model, "read", [ids], {"fields": fields})
            return {"SalesOrders": data[:limit]}
        else:
            raise Exception("Authentication failed. Please check your credentials.")
    except Exception as error:
        raise Exception(error)

def odoo_create_sale_order(url, db, username, apiPassword,params):
    try:
        if "partner_id" in params and "user_id" in params:
            order_lines_data=params.get("order_lines_data")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "sale.order"
                order_lines = [(0, 0, {
                    'product_id': line['product_id'],
                    'product_uom_qty': line['product_uom_qty'],
                }) for line in order_lines_data]  
                data = {
                    "partner_shipping_id": params["partner_id"],
                    "partner_invoice_id" : params["partner_id"],
                    "order_line":order_lines
                }
                for key, value in params.items():
                    skip_keys = ["order_lines_data"]
                    if key in skip_keys:
                        continue
                    if value:
                        data[key] = value
                id = models.execute_kw(db, uid, apiPassword, model, "create", [data])
                return {"id": id}
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

   
def odoo_update_sale_order(url, db, username, apiPassword,params):
    try:
        if "order_id" in params:
            id = params["order_id"]
            order_lines_data=params.get("order_lines_data",[])
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            data={}
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "sale.order"
                if (order_lines_data):
                    order_lines = [(0, 0, {
                        'product_id': line['product_id'],
                        'product_uom_qty': line['product_uom_qty'],
                    }) for line in order_lines_data] 
                    data = {
                        "order_line":order_lines
                    }
                for key, value in params.items():
                    skip_keys = ["order_id","order_lines_data"]
                    if key in skip_keys:
                        continue
                    if value:
                        data[key] = value
                if data:
                    if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                        models.execute_kw(db, uid, apiPassword, model, "write", [[int(id)], data])
                        return {"message": "Updated successfully"}
                    else:
                        raise Exception("Not found")
                else:
                    raise Exception("Please specify at least one field to update")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)


def odoo_delete_sale_order(url, db, username, apiPassword,params):
    try:
        if "order_id" in params:
            id = params.get("order_id")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(
                    f"{url}/xmlrpc/2/object")
                model = "sale.order"
                if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                    models.execute_kw(db, uid, apiPassword, model, "unlink", [[id]])
                    return {"message": "Deleted successfully"}
                else:
                    raise Exception("ID not found or could not be deleted.")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_sale_order_by_id(url, db, username, apiPassword, params):
    try:
        if "order_id" in params:
            id = params.get("order_id")
            fields = params.get("fields", [])
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "sale.order"
                data = models.execute_kw(db, uid, apiPassword, model, "read", [int(id)], {"fields": fields})
                if data:
                    return {"SalesOrder": data}
                else:
                    raise Exception("Not found")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_many_company(url, db, username, apiPassword, params):
    try:
        limit = params.get("limit")
        fields = params.get("fields", [])
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        uid = common.authenticate(db, username, apiPassword, {})
        if uid:
            models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
            model = "res.company"
            ids = models.execute_kw(db, uid, apiPassword, model, "search", [[]])
            data = models.execute_kw(db, uid, apiPassword, model, "read", [ids], {"fields": fields})
            return {"Companies": data[:limit]}
        else:
            raise Exception("Authentication failed. Please check your credentials.")
    except Exception as error:
        raise Exception(error)

def odoo_create_company(url, db, username, apiPassword,params):
    try:
        if "name" in params:
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "res.company"
                data = {}
                for key, value in params.items():
                    if value:
                        data[key] = value
                id = models.execute_kw(db, uid, apiPassword, model, "create", [data])
                return {"id": id}
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_company_by_id(url, db, username, apiPassword, params):
    try:
        if "company_id" in params:
            id = params.get("company_id")
            fields = params.get("fields", [])
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "res.company"
                data = models.execute_kw(db, uid, apiPassword, model, "read", [int(id)], {"fields": fields})
                if data:
                    return {"Company": data}
                else:
                    raise Exception("Not found")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_update_company(url, db, username, apiPassword, params):
    try:
        if "company_id" in params:
            id = params["company_id"]
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(
                    f"{url}/xmlrpc/2/object")
                model = "res.company"
                data = {}
                for key, value in params.items():
                    skip_keys = ["company_id"]
                    if key in skip_keys:
                        continue
                    if value:
                        data[key] = value
                if data:
                    if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                        models.execute_kw(db, uid, apiPassword, model, "write", [[int(id)], data])
                        return {"message": "Updated successfully"}
                    else:
                        raise Exception("Not found")
                else:
                    raise Exception("Please specify at least one field to update")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_many_product(url, db, username, apiPassword, params):
    try:
        limit = params.get("limit")
        fields = params.get("fields", [])
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        uid = common.authenticate(db, username, apiPassword, {})
        if uid:
            models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
            model = "product.template"
            ids = models.execute_kw(db, uid, apiPassword, model, "search", [[]])
            data = models.execute_kw(db, uid, apiPassword, model, "read", [ids], {"fields": fields})
            return {"Products": data[:limit]}
        else:
            raise Exception("Authentication failed. Please check your credentials.")
    except Exception as error:
        raise Exception(error)

def odoo_create_product(url, db, username, apiPassword,params):
    try:
        if "name" in params:
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "product.template"
                data = {}
                for key, value in params.items():
                    if value:
                        data[key] = value
                id = models.execute_kw(db, uid, apiPassword, model, "create", [data])
                return {"id": id}
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_product_by_id(url, db, username, apiPassword, params):
    try:
        if "product_id" in params:
            id = params.get("product_id")
            fields = params.get("fields", [])
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "product.template"
                data = models.execute_kw(db, uid, apiPassword, model, "read", [int(id)], {"fields": fields})
                if data:
                    return {"Product": data}
                else:
                    raise Exception("Not found")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_delete_product(url, db, username, apiPassword, params):
    try:
        if "product_id" in params:
            id = params.get("product_id")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "product.template"
                if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                    models.execute_kw(db, uid, apiPassword, model, "unlink", [[id]])
                    return {"message": "Deleted successfully"}
                else:
                    raise Exception("ID not found or could not be deleted.")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_update_product(url, db, username, apiPassword,params):
    try:
        if "product_id" in params:
            id = params["product_id"]
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(
                    f"{url}/xmlrpc/2/object")
                model = "product.template"
                data = {}
                for key, value in params.items():
                    skip_keys = ["product_id"]
                    if key in skip_keys:
                        continue
                    if value:
                        data[key] = value
                if data:
                    if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                        models.execute_kw(db, uid, apiPassword, model, "write", [[int(id)], data])
                        return {"message": "Updated successfully"}
                    else:
                        raise Exception("Not found")
                else:
                    raise Exception("Please specify at least one field to update")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_many_product_category(url, db, username, apiPassword, params):
    try:
        limit = params.get("limit")
        fields = params.get("fields", [])
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        uid = common.authenticate(db, username, apiPassword, {})
        if uid:
            models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
            model = "product.category"
            ids = models.execute_kw(db, uid, apiPassword, model, "search", [[]])
            data = models.execute_kw(db, uid, apiPassword, model, "read", [ids], {"fields": fields})
            return {"Categories": data[:limit]}
        else:
            raise Exception("Authentication failed. Please check your credentials.")
    except Exception as error:
        raise Exception(error)

def odoo_create_product_category(url, db, username, apiPassword, params):
    try:
        if "name" in params:
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "product.category"
                data = {}
                for key, value in params.items():
                    if value:
                        data[key] = value
                id = models.execute_kw(db, uid, apiPassword, model, "create", [data])
                return {"id": id}
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_product_category_by_id(url, db, username, apiPassword, params):
    try:
        if "category_id" in params:
            id = params.get("category_id")
            fields = params.get("fields", [])
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "product.category"
                data = models.execute_kw(db, uid, apiPassword, model, "read", [int(id)], {"fields": fields})
                if data:
                    return {"Category": data}
                else:
                    raise Exception("Not found")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_update_product_category(url, db, username, apiPassword, params):
    try:
        if "category_id" in params:
            id = params["category_id"]
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "product.category"
                data = {}
                for key, value in params.items():
                    skip_keys = ["category_id"]
                    if key in skip_keys:
                        continue
                    if value:
                        data[key] = value
                if data:
                    if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                        models.execute_kw(db, uid, apiPassword, model, "write", [[int(id)], data])
                        return {"message": "Updated successfully"}
                    else:
                        raise Exception("Not found")
                else:
                    raise Exception("Please specify at least one field to update")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_delete_product_category(url, db, username, apiPassword, params):
    try:
        if "category_id" in params:
            id = params.get("category_id")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                model = "product.category"
                if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                    models.execute_kw(db, uid, apiPassword, model, "unlink", [[id]])
                    return {"message": "Deleted successfully"}
                else:
                    raise Exception("ID not found or could not be deleted.")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_get_many_CustomResource(url, db, username, apiPassword,params):
    try:
        model = params.get("model")
        limit = params.get("limit")
        fields = params.get("fields", [])
        common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
        uid = common.authenticate(db, username, apiPassword, {})
        if uid:
            models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
            ids = models.execute_kw(db, uid, apiPassword, model, "search", [[]])
            data = models.execute_kw(db, uid, apiPassword, model, "read", [ids], {"fields": fields})
            return data[:limit]
        else:
            raise Exception("Authentication failed. Please check your credentials.")
    except Exception as error:
        raise Exception(error)

def odoo_create_CustomResource(url, db, username, apiPassword,params):
    try:
        if "model" in params:
            model = params.get("model")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                data = {}
                for key, value in params.items():
                    skip_keys = ["model"]
                    if key in skip_keys:
                        continue
                    if value:
                        data[key] = value
                id = models.execute_kw(db, uid, apiPassword, model, "create", [data])
                return {"id": id}
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)
    
def odoo_get_CustomResource_by_id(url, db, username, apiPassword, params):
    try:
        if "customResource_id" in params and "model" in params:
            id = params.get("customResource_id")
            fields = params.get("fields", [])
            model = params.get("model")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                data = models.execute_kw(db, uid, apiPassword, model, "read", [int(id)], {"fields": fields})
                if data:
                    return data
                else:
                    raise Exception("Not found")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_update_CustomResource(url, db, username, apiPassword, params):
    try:
        if "customResource_id" in params and "model" in params:
            id = params["customResource_id"]
            model = params.get("model")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                data = {}
                for key, value in params.items():
                    skip_keys = ["customResource_id","model"]
                    if key in skip_keys:
                        continue
                    if value:
                        data[key] = value
                if data:
                    if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                        models.execute_kw(db, uid, apiPassword, model, "write", [[int(id)], data])
                        return {"message": "Updated successfully"}
                    else:
                        raise Exception("Not found")
                else:
                    raise Exception("Please specify at least one field to update")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)

def odoo_delete_CustomResource(url, db, username, apiPassword, params):
    try:
        if "customResource_id" in params and "model" in params:
            id = params.get("customResource_id")
            model = params.get("model")
            common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
            uid = common.authenticate(db, username, apiPassword, {})
            if uid:
                models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
                if models.execute_kw(db, uid, apiPassword, model, "search", [[("id", "=", int(id))]]):
                    models.execute_kw(db, uid, apiPassword, model, "unlink", [[id]])
                    return {"message": "Deleted successfully"}
                else:
                    raise Exception("ID not found or could not be deleted.")
            else:
                raise Exception("Authentication failed. Please check your credentials.")
        else:
            raise Exception("Missing input data")
    except Exception as error:
        raise Exception(error)