import io
from jira import JIRA, JIRAError
import requests

def authenticate(email,api_token,server):
    response = requests.get(server)
    if response.status_code == 200:
        jira = JIRA(server=server,
                basic_auth=(email, api_token))
        return jira
    else:
        raise Exception('error: Auth Exception')
    
def jira_get_issues(params,email,api_token,server):
    try:
        if email and api_token and server and 'jql_str' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            jql_parts = []
            for key, value in params.items():
                if key=='jql_str':
                    jql_sub_parts = [f"{sub_key}={sub_value}" for sub_key, sub_value in value.items()]
                    jql_parts.append(' AND '.join(jql_sub_parts))
                elif value:
                    data[key] = value
            jql_query = ' AND '.join(jql_parts)
            issues = jira.search_issues(jql_query,**data)
            issue_list = []
            for issue in issues:
                issue_dict = issue.raw
                issue_list.append(issue_dict)
            return issue_list
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")
    
def jira_get_issue(params,email,api_token,server):
    try:
        if email and api_token and server and 'id' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            get_issue = jira.issue(**data)
            issue_dict = get_issue.raw
            return issue_dict
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")



def jira_create_issue(params,email,api_token,server):
    try:
        if email and api_token and server and 'project' in params and 'issuetype' in params and 'summary' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            new_issue = jira.create_issue(**data)
            return new_issue.raw
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")


def jira_delete_issue(params,email,api_token,server):
    try:
        if email and server and api_token and 'id' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            issue = jira.issue(data['id'])
            optional_params = {}
            for key, value in data.items():
                if key != 'id':
                    optional_params[key] = value
            issue.delete(**optional_params)
            return f"Issue : Deleted successfully."
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise Exception(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")

def jira_create_comment(params,email,api_token,server):
    try:
        if email and api_token and server and  'issue' in params and 'body' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            new_comment = jira.add_comment(**data)
            return new_comment.raw
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")

def jira_get_comments(params,email,api_token,server):
    try:
        if email and api_token and server and 'issue' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            get_comments = jira.comments(**data)
            comments_list = [comment.raw for comment in get_comments]
            return comments_list
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")

def jira_get_comment(params,email,api_token,server):
    try:
        if email and api_token and server and 'issue' in params and 'comment' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            get_comment = jira.comment(**data)
            return get_comment.raw
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")
    
def jira_delete_comment(params,email,api_token,server):
    try:
        if email and api_token and server and 'issue' in params and 'comment' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            get_comment = jira.comment(**data)
            get_comment.delete()
            return f"Comment : Deleted successfully."
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")
    
def jira_update_comment(params,email,api_token,server):
    try:
        if email and api_token and server and 'issue' in params and 'body' in params and 'comment' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            for key, value in params.items():
                if key=='issue' or key=='comment':
                    data[key] = value
            get_comment = jira.comment(**data)
            update_data={}
            for key, value in params.items():
                if key=='issue' or key=='comment':
                    continue
                else:
                    update_data[key] = value
            get_comment.update(**update_data)
            return f"Comment : Updated successfully."
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")
    

def jira_create_attachment(params,email,api_token,server):
    try:
        if email and api_token and server and 'issue' in params and ('attachment' in params or 'url' in params) and 'filename' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            if 'attachment' in data:
                attachment_data = {
                    'issue': data['issue'],
                    'filename': data['filename'],
                    'attachment': io.BytesIO(params['attachment']),
                }
                jira.add_attachment(**attachment_data)
                return "Attachment added successfully"
            elif 'url' in data:
                response = requests.get(data['url'])
                if response.status_code == 200:
                    file_content = response.content
                    attachment_data = {
                        'issue': data['issue'],
                        'filename': data['filename'],
                        'attachment': io.BytesIO(file_content),
                    }
                    jira.add_attachment(**attachment_data)
                return "Attachment added successfully"
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")

def jira_get_attachments(params,email,api_token,server):
    try:
        if email and server and api_token and 'id' in params:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            jira = authenticate(email,api_token,server)
            issue = jira.issue(data['id'])
            attachments = issue.fields.attachment 
            attachment_info = []
            for attachment in attachments:
                attachment_dict = attachment.raw
                attachment_info.append(attachment_dict)
            return attachment_info
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")

def jira_get_attachment(params,email,api_token,server):
    try:
        if email and server and api_token and 'id' in params:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            jira = authenticate(email,api_token,server)
            attachment = jira.attachment(data['id'])
            attachment_dict = attachment.raw
            return attachment_dict
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")
    
def jira_delete_attachment(params,email,api_token,server):
    try:
        if email and server and api_token and 'id' in params:
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            jira = authenticate(email,api_token,server)
            attachment = jira.delete_attachment(data['id'])
            if attachment:
                return "Attachment deleted successfully"
            else:
                raise Exception('Failed to delete')
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")

def jira_create_user(params,email,api_token,server):
    try:
        if email and server and api_token and 'username' in params and 'email' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            new_user = jira.add_user(**data)
            return "Success"
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")
    
def jira_get_users(params,email,api_token,server):
    try:
        if email and server and api_token and 'query' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            get_users = jira.search_users(**data)
            users_list = [user.raw for user in get_users]
            return users_list
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")
    
def jira_get_user(params,email,api_token,server):
    try:
        if email and server and api_token and 'id' in params:
            jira = authenticate(email,api_token,server)
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            get_users = jira.user(**data)
            return get_users.raw
        else:
            raise Exception('error: Missing input data')
    except JIRAError as http_error:
        raise JIRAError(f"error: {str(http_error)}")
    except Exception as e:
        raise Exception(f"error: {str(e)}")
    