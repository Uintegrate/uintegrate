import requests

api_version = "2023-10"


def shopify_get_many_products(subdomain, api_key, api_password):
    try:
        base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/products.json"
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(base_url, auth=(
            api_key, api_password), headers=headers)
        if response:
            products_data = response.json()
            return products_data
        else:
            raise Exception(
                f"Failed to retrieve products. Status code: {response.status_code}. Response: {response.text}"
            )
    except Exception as error:
        raise Exception(str(error))


def shopify_get_product(subdomain, api_key, api_password, params):
    try:
        if "product_id" in params:
            product_id = params["product_id"]
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/products/{product_id}.json"
            headers = {
                'Content-Type': 'application/json',
            }
            response = requests.get(base_url, auth=(
                api_key, api_password), headers=headers)
            if response:
                product_data = response.json()
                return product_data
            else:
                raise Exception(
                    f"Failed to retrieve product {product_id}. Status code: {response.status_code}. Response: {response.text}"
                )
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_delete_product(subdomain, api_key, api_password, params):
    try:
        if "product_id" in params:
            product_id = params["product_id"]
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/products/{product_id}.json"
            headers = {
                'Content-Type': 'application/json',
            }

            response = requests.delete(base_url, auth=(
                api_key, api_password), headers=headers)
            if response:
                return {"message": "Product deleted successfully."}
            else:
                raise Exception(
                    f"Failed to delete product {product_id}. Status code: {response.status_code}. Response: {response.text}"
                )
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_create_product(subdomain, api_key, api_password, params):
    try:
        if "title" in params:
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/products.json"
            headers = {
                'Content-Type': 'application/json',
            }
            data = {
                "product": {}
            }
            for key, value in params.items():
                if value:
                    data["product"][key] = value

            response = requests.post(base_url, auth=(
                api_key, api_password), json=data, headers=headers)

            if response:
                product_data = response.json()
                return product_data
            else:
                raise Exception(
                    f"Failed to create the product. Status code: {response.status_code}. Response: {response.text}")
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_update_product(subdomain, api_key, api_password, params):
    try:
        if "id" in params:
            id = params["id"]
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/products/{id}.json"
            headers = {
                'Content-Type': 'application/json',
            }
            data = {
                "product": {
                }
            }
            for key, value in params.items():
                skip_keys = ["id"]
                if key in skip_keys:
                    continue
                if value:
                    data["product"][key] = value
            if data["product"]:
                response = requests.put(base_url, auth=(
                    api_key, api_password), json=data, headers=headers)

                if response:
                    product_data = response.json()
                    return product_data
                else:
                    raise Exception(
                        f"Failed to update the product. Status code: {response.status_code}. Response: {response.text}")
            else:
                raise Exception(
                    "At least one field must be updated")
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_update_variant_product(subdomain, api_key, api_password, params):
    try:
        if "product_id" in params and "variant_id" in params:
            product_id = params["product_id"]
            variant_id = params["variant_id"]
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/products/{product_id}/variants/{variant_id}.json"
            headers = {
                'Content-Type': 'application/json',
            }
            data = {
                "variant": {}
            }
            for key, value in params.items():
                skip_keys = ["product_id", "variant_id"]
                if key in skip_keys:
                    continue
                if value:
                    data["variant"][key] = value
            if data["variant"]:
                response = requests.put(base_url, auth=(
                    api_key, api_password), json=data, headers=headers)

                if response:
                    variant_product_data = response.json()
                    return variant_product_data
                else:
                    raise Exception(
                        f"Failed to update the product variant. Status code: {response.status_code}. Response: {response.text}")
            else:
                raise Exception(
                    "At least one field must be updated")
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_get_variant_products(subdomain, api_key, api_password, params):
    try:
        if "id" in params:
            id = params["id"]
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/products/{id}/variants.json"
            headers = {
                'Content-Type': 'application/json',
            }
            response = requests.get(base_url, auth=(
                api_key, api_password), headers=headers)
            if response:
                variant_product_data = response.json()
                return variant_product_data
            else:
                raise Exception(
                    f"Failed to retrieve variants for product {id}. Status code: {response.status_code}. Response: {response.text}"
                )
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_create_variant_product(subdomain, api_key, api_password, params):
    try:
        if "id" in params:
            id = params["id"]
            base_url = f"https://{subdomain}.myshopify.com/admin/api/2021-07/products/{id}/variants.json"
            headers = {
                'Content-Type': 'application/json',
            }
            data = {
                "variant": {}
            }
            for key, value in params.items():
                skip_keys = ["id"]
                if key in skip_keys:
                    continue
                if value:
                    data["variant"][key] = value
            response = requests.post(base_url, auth=(
                api_key, api_password), json=data, headers=headers)

            if response:
                variant_product_data = response.json()
                return variant_product_data
            else:
                raise Exception(
                    f"Failed to create the product. Status code: {response.status_code}. Response: {response.text}")
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_get_many_customers(subdomain, api_key, api_password):
    try:
        base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/customers.json"
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(base_url, auth=(
            api_key, api_password), headers=headers)
        if response:
            customers_data = response.json()
            return customers_data
        else:
            raise Exception(
                f"Failed to retrieve customers. Status code: {response.status_code}. Response: {response.text}"
            )
    except Exception as error:
        raise Exception(str(error))


def shopify_get_customer_by_id(subdomain, api_key, api_password, params):
    try:
        if "id" in params:
            id = params["id"]
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/customers/{id}.json"
            headers = {
                'Content-Type': 'application/json',
            }
            response = requests.get(base_url, auth=(
                api_key, api_password), headers=headers)
            if response:
                customer_data = response.json()
                return customer_data
            else:
                raise Exception(
                    f"Failed to retrieve customer. Status code: {response.status_code}. Response: {response.text}"
                )
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_create_customer(subdomain, api_key, api_password, params):
    try:
        if "email" in params and "phone" in params:
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/customers.json"
            headers = {
                'Content-Type': 'application/json',
            }
            data = {"customer": {}}
            for key, value in params.items():
                if value:
                    data["customer"][key] = value
            response = requests.post(base_url, auth=(
                api_key, api_password), json=data, headers=headers)
            if response:
                customer_data = response.json()
                return customer_data
            else:
                raise Exception(
                    f"Failed to create customer. Status code: {response.status_code}{response.text}"
                )
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_update_customer(subdomain, api_key, api_password, params):
    try:
        if "id" in params:
            id = params["id"]
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/customers/{id}.json"
            headers = {
                'Content-Type': 'application/json',
            }
            data = {"customer": {}}
            for key, value in params.items():
                skip_keys = ["id"]
                if key in skip_keys:
                    continue
                if value:
                    data["customer"][key] = value
            if data["customer"]:
                response = requests.put(base_url, auth=(
                    api_key, api_password), json=data, headers=headers)
                if response:
                    customer_data = response.json()
                    return customer_data
                else:
                    raise Exception(
                        f"Failed to update the customer. Status code: {response.status_code}. Response: {response.text}"
                    )
            else:
                raise Exception(
                    "At least one field must be updated")
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_get_many_orders(subdomain, api_key, api_password):
    try:
        base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/orders.json"
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(base_url, auth=(
            api_key, api_password), headers=headers)
        if response:
            orders_data = response.json()
            return orders_data
        else:
            raise Exception(
                f"Failed to retrieve orders. Status code: {response.status_code}. Response: {response.text}"
            )
    except Exception as error:
        raise Exception(str(error))


def shopify_get_order_by_id(subdomain, api_key, api_password, params):
    try:
        if "id" in params:
            id = params["id"]
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/orders/{id}.json"
            headers = {
                'Content-Type': 'application/json',
            }
            response = requests.get(base_url, auth=(
                api_key, api_password), headers=headers)
            if response:
                order_data = response.json()
                return order_data
            else:
                raise Exception(
                    f"Failed to retrieve order {id}. Status code: {response.status_code}. Response: {response.text}"
                )
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_delete_order(subdomain, api_key, api_password, params):
    try:
        if "id" in params:
            id = params["id"]
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/orders/{id}.json"
            headers = {
                'Content-Type': 'application/json',
            }
            response = requests.delete(base_url, auth=(
                api_key, api_password), headers=headers)
            if response:
                return {"message": "order deleted successfully."}
            else:
                raise Exception(
                    f"Failed to delete order {id}. Status code: {response.status_code}. Response: {response.text}"
                )
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_create_order(subdomain, api_key, api_password, params):
    try:
        if "line_items" in params:
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/orders.json"
            headers = {
                'Content-Type': 'application/json',
            }
            data = {
                "order": {}
            }
            for key, value in params.items():
                if value:
                    data["order"][key] = value
            response = requests.post(base_url, auth=(
                api_key, api_password), json=data, headers=headers)

            if response:
                order_data = response.json()
                return order_data
            else:
                raise Exception(
                    f"Failed to create the order. Status code: {response.status_code}. Response: {response.text}")
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_update_order(subdomain, api_key, api_password, params):
    try:
        if "id" in params:
            id = params["id"]
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/orders/{id}.json"
            headers = {
                'Content-Type': 'application/json',
            }
            data = {
                "order": {}
            }
            for key, value in params.items():
                skip_keys = ["id"]
                if key in skip_keys:
                    continue
                if value:
                    data["order"][key] = value
            if data["order"]:
                response = requests.put(base_url, auth=(
                    api_key, api_password), json=data, headers=headers)

                if response:
                    order_data = response.json()
                    return order_data
                else:
                    raise Exception(
                        f"Failed to update the order. Status code: {response.status_code}. Response: {response.text}")
            else:
                raise Exception(
                    "At least one field must be updated")
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_update_inventory_quantity(subdomain, api_key, api_password, params):
    try:
        if "inventory_item_id" in params and "available" in params and "location_id" in params:
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/inventory_levels/set.json"
            headers = {
                'Content-Type': 'application/json',
            }
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            if data:
                response = requests.post(base_url, auth=(
                    api_key, api_password), json=data, headers=headers)
                if response:
                    inventory_quantity_data = response.json()
                    return inventory_quantity_data
                else:
                    raise Exception(
                        f"Failed to update inventory quantity. Status code: {response.status_code}. Response: {response.text}")
            else:
                raise Exception(
                    "At least one field must be updated")
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))


def shopify_create_blog_articles(subdomain, api_key, api_password, params):
    try:
        if "blog_id" in params and "title" in params:
            blog_id = params["blog_id"]
            base_url = f"https://{subdomain}.myshopify.com/admin/api/{api_version}/blogs/{blog_id}/articles.json"
            headers = {
                'Content-Type': 'application/json',
            }
            data = {"article": {}}
            for key, value in params.items():
                if value:
                    data["article"][key] = value

            response = requests.post(base_url, auth=(
                api_key, api_password), json=data, headers=headers)

            if response:
                article = response.json()
                return article
            else:
                raise Exception(
                    f"Failed to create a new article. Status code: {response.status_code}. Response: {response.text}")
        else:
            raise Exception("missing parameters")
    except Exception as error:
        raise Exception(str(error))