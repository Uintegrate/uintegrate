import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError


def create_client_instance(API_KEY, SERVER_PREFIX):
    try:
        if API_KEY and SERVER_PREFIX:
            mailchimp = MailchimpMarketing.Client()
            mailchimp.set_config({"api_key": API_KEY, "server": SERVER_PREFIX})
            return mailchimp
        else:
            raise Exception("Please provide API Key and Server Prefix")
    except Exception as e:
        raise Exception(f"Error creating client instance: {e}")


def reply_upon_success(response):
    valid_status_code = [200, 201, 202, 204, 206, 207, 208]
    if response.status_code in valid_status_code:
        return {
            "result": "Operation Performed successfuly",
            "Status Code": response.status_code,
        }


def mailchimp_check_connection(API_KEY, SERVER_PREFIX):
    try:
        mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)
        try:
            response = mailchimp.ping.get()
        except ApiClientError as error:
            raise Exception(f"Mailchimp API error: {error.text}")
        else:
            return response
    except Exception as e:
        raise Exception(f"error checking connection: {e}")


#################################### Code goes Here #############################################

#################################### Members ####################################################


def mailchimp_create_member(API_KEY, SERVER_PREFIX, params):
    try:
        body = params.get("body", {})

        if "list_id" in params and "email_address" in body and "status" in body:
            data = {key: value for (key, value) in params.items() if value}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.lists.add_list_member(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error creating member: {e}")


def mailchimp_get_member(API_KEY, SERVER_PREFIX, params):
    try:
        if "list_id" in params and "subscriber_hash" in params:
            data = {key: value for (key, value) in params.items() if value}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.lists.get_list_member(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error getting member: {e}")


def mailchimp_get_list_members(API_KEY, SERVER_PREFIX, params):
    try:
        if "list_id" in params:
            data = {key: value for (key, value) in params.items() if value}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.lists.get_list_members_info(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error getting list members: {e}")


def mailchimp_update_member(API_KEY, SERVER_PREFIX, params):
    try:
        if "list_id" in params and "subscriber_hash" in params and "body" in params:
            data = {key: value for (key, value) in params.items() if value}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.lists.update_list_member(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error updating member: {e}")


def mailchimp_delete_member(API_KEY, SERVER_PREFIX, params):
    try:
        list_id = params.get("list_id", None)
        subscriber_hash = params.get("subscriber_hash", None)

        if list_id and subscriber_hash:
            data = {"list_id": list_id, "subscriber_hash": subscriber_hash}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.lists.delete_list_member_permanent(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return reply_upon_success(response)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error deleting member: {e}")


def mailchimp_archive_member(API_KEY, SERVER_PREFIX, params):
    try:
        list_id = params.get("list_id", None)
        subscriber_hash = params.get("subscriber_hash", None)

        if list_id and subscriber_hash:
            data = {"list_id": list_id, "subscriber_hash": subscriber_hash}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.lists.delete_list_member(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return reply_upon_success(response)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error Archiving member: {e}")


def mailchimp_add_note_to_member(API_KEY, SERVER_PREFIX, params):
    try:
        if "list_id" in params and "subscriber_hash" in params and "body" in params:
            data = {key: value for (key, value) in params.items() if value}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.lists.create_list_member_note(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error adding note to member: {e}")


############################################ Events #################################################


def mailchimp_add_member_event(API_KEY, SERVER_PREFIX, params):
    try:
        body = params.get("body", {})

        if "list_id" in params and "subscriber_hash" in params and "name" in body:
            data = {key: value for (key, value) in params.items() if value}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.lists.create_list_member_event(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return reply_upon_success(response)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error adding member's event: {e}")


def mailchimp_list_member_events(API_KEY, SERVER_PREFIX, params):
    try:
        if "list_id" in params and "subscriber_hash" in params:
            data = {key: value for (key, value) in params.items() if value}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.lists.get_list_member_events(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error listing member's events: {e}")


########################################## Tags ##################################################


def mailchimp_update_member_tags(API_KEY, SERVER_PREFIX, params):
    try:
        if (
            "list_id" in params
            and "subscriber_hash" in params
            and "tags" in params.get("body", {})
        ):
            data = {key: value for (key, value) in params.items() if value}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.lists.update_list_member_tags(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return reply_upon_success(response)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error updating member tags: {e}")


def mailchimp_list_member_tags(API_KEY, SERVER_PREFIX, params):
    try:
        if "list_id" in params and "subscriber_hash" in params:
            data = {key: value for (key, value) in params.items() if value}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.lists.get_list_member_tags(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error getting member tags: {e}")


def mailchimp_find_tags(API_KEY, SERVER_PREFIX, params):
    try:
        if "list_id" in params:
            data = {key: value for (key, value) in params.items() if value}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.lists.tag_search(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error finding tags: {e}")


######################################## Lists #####################################################


def mailchimp_get_many_lists(API_KEY, SERVER_PREFIX, params):
    try:
        data = {key: value for (key, value) in params.items() if value}

        mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

        try:
            response = mailchimp.lists.get_all_lists(**data)
        except ApiClientError as error:
            raise Exception(f"Mailchimp API error: {error.text}")
        else:
            return response
    except Exception as e:
        raise Exception(f"Error getting lists: {e}")


########################################### Campaigns ##############################################


def mailchimp_get_campaign(API_KEY, SERVER_PREFIX, params):
    try:
        if "campaign_id" in params:
            data = {key: value for (key, value) in params.items() if value}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.campaigns.get(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error getting campain: {e}")


def mailchimp_get_many_campaigns(API_KEY, SERVER_PREFIX, params):
    try:
        data = {key: value for (key, value) in params.items() if value}

        mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

        try:
            response = mailchimp.campaigns.list(**data)
        except ApiClientError as error:
            raise Exception(f"Mailchimp API error: {error.text}")
        else:
            return response
    except Exception as e:
        raise Exception(f"Error getting campains: {e}")


def mailchimp_send_campaign(API_KEY, SERVER_PREFIX, params):
    try:
        campaign_id = params.get("campaign_id", None)
        if campaign_id:
            data = {"campaign_id": campaign_id}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.campaigns.send(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return reply_upon_success(response)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error sending campain: {e}")


def mailchimp_resend_campaign(API_KEY, SERVER_PREFIX, params):
    try:
        campaign_id = params.get("campaign_id", None)
        if campaign_id:
            data = {"campaign_id": campaign_id}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.campaigns.create_resend(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error resending campain: {e}")


def mailchimp_replicate_campaign(API_KEY, SERVER_PREFIX, params):
    try:
        campaign_id = params.get("campaign_id", None)
        if campaign_id:
            data = {"campaign_id": campaign_id}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.campaigns.replicate(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error replicating campain: {e}")


def mailchimp_delete_campaign(API_KEY, SERVER_PREFIX, params):
    try:
        campaign_id = params.get("campaign_id", None)
        if campaign_id:
            data = {"campaign_id": campaign_id}

            mailchimp = create_client_instance(API_KEY, SERVER_PREFIX)

            try:
                response = mailchimp.campaigns.remove(**data)
            except ApiClientError as error:
                raise Exception(f"Mailchimp API error: {error.text}")
            else:
                return reply_upon_success(response)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(f"Error deleting campain: {e}")