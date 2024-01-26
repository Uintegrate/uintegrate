import requests


status=[200, 201, 202, 204, 206, 207, 208]

def wordpress_create_post(params,base_url,token):
    try:
        if 'title' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/posts"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(api_url, json=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to create a new post.")
        else:
            raise Exception('Missing parameters.')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")
    
def wordpress_get_post(params,base_url,token):
    try:
        if 'post_id' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            
            api_url = f"{base_url}/wp-json/wp/v2/posts/{params2['post_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.get(api_url, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to retrieve the post.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")
    

def wordpress_get_posts(params,base_url,token):
    try:
        if token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/posts"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.get(api_url, headers=headers)
            if response.status_code in status:
                posts_data = response.json()
                return posts_data
            else:
                raise Exception(f"Failed to retrieve posts.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")

    
def wordpress_update_post(params,base_url,token):
    try:
        if 'post_id' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/posts/{params2['post_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(api_url, json=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to update the post.")
        else:
            raise Exception('Missing parameters')   
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_delete_post(params,base_url,token):
    try:
        if 'post_id' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/posts/{params2['post_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.delete(api_url, headers=headers)
            if response.status_code in status:
                return 'Post deleted successfully.'
            else:
                raise Exception(f"Failed to delete the post.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordress_get_users(params,base_url,token):
    try:
        if token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/users"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.get(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to retrieve users.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")

    
def wordpress_get_user(params,base_url,token):
    try:
        if 'user_id' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/posts/{params2['user_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.get(api_url, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to retrieve user.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_update_user(params,base_url,token):
    try:
        if 'user_id'in params and token and base_url:

            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/users/{params2['user_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.put(api_url, json=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to update user.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_create_user(params,base_url,token):
    try:
        if token and 'username' in params and 'email' in params and 'password' in params and base_url :
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/users"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }

            response = requests.post(api_url, json=params2 , headers=headers)

            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to create user.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_delete_user(params,base_url,token):
    try:
        if 'user_id' in params and 'reassign' in params and token and base_url:    
            params2 = {'force':True,}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/users/{params2['user_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
            }
            response = requests.delete(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return 'User deleted successfully'
            elif response.status_code == 404:
                raise Exception('User not found')
            else:
                raise Exception(f"Failed to delete user.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")

    
def wordpress_create_categorie(params,base_url,token):
    try:
        if 'name' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/categories"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json',
            }
            response = requests.post(api_url, json=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to create category.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")

    
def wordpress_get_categories(params,base_url,token):
    try:    
        if token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/categories"
            headers = {
                'Authorization': f'Bearer {token}',
            }
            response = requests.get(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to fetch categories.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_get_categorie(params,base_url,token):
    try:
        if token and 'categorie_id' in params and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/categories/{params2['categorie_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
            }
            response = requests.get(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to fetch categorie.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_update_categorie(params,base_url,token):
    try:
        if token and 'categorie_id' in params and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/categories/{params2['categorie_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
            }
            response = requests.put(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to update categorie.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_delete_categorie(params,base_url,token):
    try:
        if token and 'categorie_id' in params and base_url:
                params2 = {'force':True,}
                for key, value in params.items():
                    if value:
                        params2[key] = value
                api_url = f"{base_url}/wp-json/wp/v2/categories/{params2['categorie_id']}"
                headers = {
                    'Authorization': f'Bearer {token}',
                }
                response = requests.delete(api_url,params=params2, headers=headers)
                if response.status_code in status:
                    return 'Deleted Successfully'
                else:
                    raise Exception(f"Failed to delete categorie.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_get_tags(params,base_url,token):
    try:
        if token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/tags"
            headers = {
                'Authorization': f'Bearer {token}',
            }
            response = requests.get(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to fetch tags.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")

    
def wordpress_create_tag(params,base_url,token):
    try:
        if 'name'in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/tags"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json',
            }
            response = requests.post(api_url, json=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to create tag.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_get_tag(params,base_url,token):
    try:
        if token and 'tag_id' in params and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/tags/{params2['tag_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
            }
            response = requests.get(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to fetch tag.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")

    
def wordpress_update_tag(params,base_url,token):
    try:
        if token and 'tag_id'in params and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/tags/{params2['tag_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
            }
            response = requests.put(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to update tag.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_delete_tag(params,base_url,token):
    try:
        if token and 'tag_id' in params and base_url:
                params2 = {'force':True,}
                for key, value in params.items():
                    if value:
                        params2[key] = value
                api_url = f"{base_url}/wp-json/wp/v2/tags/{params2['tag_id']}"
                headers = {
                    'Authorization': f'Bearer {token}',
                }
                response = requests.delete(api_url,params=params2, headers=headers)
                if response.status_code in status:
                    return 'Deleted Successfully'
                else:
                    raise Exception(f"Failed to delete tag.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_create_page(params,base_url,token):
    try:
        if 'title' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/pages"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json',
            }
            response = requests.post(api_url, json=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to create page.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")

    
def wordpress_get_page(params,base_url,token):
    try:
        if 'page_id' in params and token and base_url:

            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/pages/{params2['page_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.get(api_url, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception (f"Failed to retrieve the page.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_get_pages(params,base_url,token):
    try:
        if token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/pages"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.get(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to retrieve pages.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_update_page(params,base_url,token):
    try:
        if 'page_id' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/pages/{params2['page_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(api_url, json=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to update the page.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_delete_page(params,base_url,token):
    try:
        if 'page_id' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/pages/{params2['page_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.delete(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return 'Page deleted successfully.'
            else:
                raise Exception(f"Failed to delete the page.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")

    

def wordpress_create_comment(params,base_url,token):
    try:
        if 'post' in params and 'content' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/comments"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json',
            }
            response = requests.post(api_url, json=params2, headers=headers)

            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to create comment.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")


def wordpress_get_comments(params,base_url,token):
    try:
        if token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/comments"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.get(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to retrieve comments.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")

    
def wordpress_get_comment(params,base_url,token):
    try:
        if 'comment_id' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/comments/{params2['comment_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.get(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to retrieve comment.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")

    
def wordpress_update_comment(params,base_url,token):
    try:
        if 'comment_id' in params and 'content' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/comments/{params2['comment_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.post(api_url, json=params2, headers=headers)
            if response.status_code in status:
                return response.json()
            else:
                raise Exception(f"Failed to update the cmnt.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")

    
def wordpress_delete_comment(params,base_url,token):
    try:
        if 'comment_id' in params and token and base_url:
            params2 = {}
            for key, value in params.items():
                if value:
                    params2[key] = value
            api_url = f"{base_url}/wp-json/wp/v2/comments/{params2['comment_id']}"
            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            response = requests.delete(api_url,params=params2, headers=headers)
            if response.status_code in status:
                return 'Comment deleted successfully.'
            else:
                raise Exception(f"Failed to delete comment.")
        else:
            raise Exception('Missing parameters')
    except requests.exceptions.RequestException as e:
        raise Exception(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")

    