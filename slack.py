from slack_sdk import WebClient
import logging
import json
import requests


# Message Actions

def slack_send_message(params):
    try:
        if "token" in params and "channel" in params and ("text" in params or "blocks" in params or "attachments" in params):
            token = params["token"]
            client = WebClient(token=token)
            keys_to_skip=["token"]
            data = {}
            for key, value in params.items():
                if key in keys_to_skip:
                    continue
                if value:
                    data[key] = value
                
            response = client.chat_postMessage(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "channel" : response["channel"],
                "ts": response["ts"],
                "message": response["message"],
                "response_json":result
            }
            
            return response_json
            
        else:
            raise SyntaxError("Missing input data")

    except Exception as error:
        raise SyntaxError(error)


def slack_update_message(params):
    try:
        if "token" in params and "channel" in params and "ts" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.chat_update(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "channel" : response["channel"],
                "ts": response["ts"],
                "message": response["message"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_delete_message(params):
    try:
        if "token" in params and "channel" in params and "ts" in params:
            token = params["token"]
            channel_id = params["channel"]
            client = WebClient(token=token)
            logger = logging.getLogger(__name__)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.chat_delete(**data)
            return {"Result" : f"The message has been deleted from this channel ID: {channel_id}"}
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_get_permalink(params):
    try:
        if "token" in params and "channel" in params and "message_ts" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.chat_getPermalink(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "channel" : response["channel"],
                "permalink": response["permalink"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


#############################################################################################################################


# Channel Actions


def slack_get_channel(params):
    try:
        if "token" in params and "channel" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.conversations_info(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "channel" : response["channel"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_get_many_channels(params):
    try:
        if "token" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.conversations_list(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "channels" : response["channels"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_create_channel(params):
    try:
        if "token" in params and "name" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.conversations_create(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "channel" : response["channel"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_archive_conversation(params):
    try:
        if "token" in params and "channel" in params:
            token = params["token"]
            channel_id = params["channel"]
            client = WebClient(token=token)
            client.conversations_archive(channel=channel_id)
            return {"Result" : f"The channel has been archived successfully, channel ID: {channel_id}"}
        
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_unarchive_conversation(params):
    try:
        if "token" in params and "channel" in params:
            token = params["token"]
            channel_id = params["channel"]
            client = WebClient(token=token)
            client.conversations_unarchive(channel=channel_id)
            return {"Result" : f"The channel has been unarchived successfully, channel ID: {channel_id}"}
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_rename_conversation(params):
    try:
        if "token" in params and "channel" in params and "name" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.conversations_rename(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "channel" : response["channel"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_get_members(params):
    try:
        if "token" in params and "channel" in params:
            token = params["token"]
            channel_id = params["channel"]
            client = WebClient(token=token)
            response = client.conversations_members(channel=channel_id)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "members" : response["members"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_leave_conversation(params):
    try:
        if "token" in params and "channel" in params:
            token = params["token"]
            channel_id = params["channel"]
            client = WebClient(token=token)
            client.conversations_leave(channel=channel_id)
            return {"Result" : f"You are leaved this channel: {channel_id}"}
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_join_conversation(params):
    try:
        if "token" in params and "channel" in params:
            token = params["token"]
            channel_id = params["channel"]
            client = WebClient(token=token)
            response = client.conversations_join(channel=channel_id)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "channel" : response["channel"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_invite_users(params):
    try:
        if "token" in params and "channel" in params and "users" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.conversations_invite(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "channel" : response["channel"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


#############################################################################################################################


# User Actions


def slack_get_user(params):
    try:
        if "token" in params and "user" in params:
            token = params["token"]
            user_id = params["user"]
            client = WebClient(token=token)
            response = client.users_info(user=user_id)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "user" : response["user"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_get_many_users(params):
    try:
        if "token" in params:
            token = params["token"]
            client = WebClient(token=token)
            response = client.users_list()
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "members" : response["members"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_get_user_status(params):
    try:
        if "token" in params and "user" in params:
            token = params["token"]
            user_id = params["user"]
            client = WebClient(token=token)
            response = client.users_getPresence(user=user_id)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "presence" : response["presence"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


#############################################################################################################################

# File Actions


def slack_get_file(params):
    try:
        if "token" in params and "file" in params:
            token = params["token"]
            file_id = params["file"]
            client = WebClient(token=token)
            response = client.files_info(file=file_id)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "content": response["content"],
                "file" : response["file"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)
    

def slack_get_many_files(params):
    try:
        if "token" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.files_list(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "files" : response["files"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_upload_file(params):
    try:
        if "token" in params and "channel" in params and "filename" in params and ("url" in params or "binary" in params or "content" in params):
            token = params["token"]

            file_path = None
            if params.get("url"):
                file_path = params["url"]

            binary_data = None
            if params.get("binary"):
                binary_data = params["binary"].encode('utf-8')

            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token" or key == "url" or key == "binary":
                    continue
                if value:
                    data[key] = value

            if file_path is not None:
                myFile = requests.get(file_path)
                if myFile.status_code == 200:
                    data["file"] = myFile.content
                else:
                    raise Exception(f"Failed to fetch the file. Status code: {myFile.status_code}")

            if binary_data is not None:
                data["file"] = binary_data

            response = client.files_upload_v2(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "file" : response["file"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


#############################################################################################################################

# User Group Actions


def slack_get_userGroups(params):
    try:
        if "token" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.usergroups_list(**data)  
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "usergroups" : response["usergroups"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_create_userGroup(params):
    try:
        if "token" in params and "name" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.usergroups_create(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "usergroup" : response["usergroup"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_update_userGroup(params):
    try:
        if "token" in params and "usergroup" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.usergroups_update(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "usergroup" : response["usergroup"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_enable_userGroup(params):
    try:
        if "token" in params and "usergroup" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.usergroups_enable(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "usergroup" : response["usergroup"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)


def slack_disable_userGroup(params):
    try:
        if "token" in params and "usergroup" in params:
            token = params["token"]
            client = WebClient(token=token)
            data = {}
            for key, value in params.items():
                if key == "token":
                    continue
                if value:
                    data[key] = value
            response = client.usergroups_disable(**data)
            result = json.loads(json.dumps(response, default=str))
            response_json = {
                "usergroup" : response["usergroup"],
                "response_json":result
            }
            
            return response_json
        else:
            raise SyntaxError("Missing input data")

    except Exception as e:
        raise SyntaxError(e)