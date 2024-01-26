from pyairtable import Api, retry_strategy


def create_api_instance(ACCESS_TOKEN):
    try:
        if ACCESS_TOKEN:
            api = Api(ACCESS_TOKEN, retry_strategy=retry_strategy(total=10))
            return api
        else:
            raise Exception("Please provide access token")
    except Exception as e:
        raise Exception(
            f"failed to create api instance using the provided token with error: {e}"
        )


def create_table_instance(ACCESS_TOKEN, base_id, table_id):
    try:
        if ACCESS_TOKEN and base_id and table_id:
            api = create_api_instance(ACCESS_TOKEN)
            table = api.table(base_id, table_id)
            return table
        else:
            raise Exception("Missing required input data")
    except Exception as e:
        raise Exception(
            f"failed to create table instance using the provided data with error: {e}"
        )


########################## here comes the code ####################################


########################## records ####################################


def airtable_list_records(ACCESS_TOKEN, params):
    try:
        base_id = params.get("base_id", None)
        table_id = params.get("table_id", None)

        table = create_table_instance(ACCESS_TOKEN, base_id, table_id)

        ignore_keys = ["base_id", "table_id"]
        data = {
            key: value
            for (key, value) in params.items()
            if value
            if key not in ignore_keys
        }

        response = table.all(**data)
        return response
    except Exception as e:
        raise Exception({e})


def airtable_create_record(ACCESS_TOKEN, params):
    try:
        if "fields" in params:
            base_id = params.get("base_id", None)
            table_id = params.get("table_id", None)

            table = create_table_instance(ACCESS_TOKEN, base_id, table_id)

            ignore_keys = ["base_id", "table_id"]
            data = {
                key: value
                for (key, value) in params.items()
                if value
                if key not in ignore_keys
            }

            response = table.create(**data)
            return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception({e})


def airtable_batch_create_records(ACCESS_TOKEN, params):
    try:
        if params.get("records", None):
            base_id = params.get("base_id", None)
            table_id = params.get("table_id", None)

            table = create_table_instance(ACCESS_TOKEN, base_id, table_id)

            ignore_keys = ["base_id", "table_id"]
            data = {
                key: value
                for (key, value) in params.items()
                if value
                if key not in ignore_keys
            }

            response = table.batch_create(**data)
            return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception({e})


def airtable_update_record(ACCESS_TOKEN, params):
    try:
        if "fields" in params and "record_id" in params:
            base_id = params.get("base_id", None)
            table_id = params.get("table_id", None)

            table = create_table_instance(ACCESS_TOKEN, base_id, table_id)

            ignore_keys = ["base_id", "table_id"]
            data = {
                key: value
                for (key, value) in params.items()
                if value
                if key not in ignore_keys
            }

            response = table.update(**data)
            return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception({e})


def airtable_batch_update_records(ACCESS_TOKEN, params):
    try:
        cond = True
        if "records" in params:
            for record in params["records"]:
                if not ("id" in record and "fields" in record):
                    cond = False

        if cond:
            base_id = params.get("base_id", None)
            table_id = params.get("table_id", None)

            table = create_table_instance(ACCESS_TOKEN, base_id, table_id)

            ignore_keys = ["base_id", "table_id"]
            data = {
                key: value
                for (key, value) in params.items()
                if value
                if key not in ignore_keys
            }

            response = table.batch_update(**data)
            return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception({e})


def airtable_batch_update_or_create_records(ACCESS_TOKEN, params):
    try:
        cond_field = True
        if "records" in params:
            for record in params["records"]:
                if "fields" not in record:
                    cond_field = False


        if cond_field and "key_fields" in params:
            base_id = params.get("base_id", None)
            table_id = params.get("table_id", None)

            table = create_table_instance(ACCESS_TOKEN, base_id, table_id)

            ignore_keys = ["base_id", "table_id"]
            data = {
                key: value
                for (key, value) in params.items()
                if value
                if key not in ignore_keys
            }

            response = table.batch_upsert(**data)
            return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception({e})


def airtable_delete_record(ACCESS_TOKEN, params):
    try:
        record_id = params.get("record_id", None)
        if record_id:
            base_id = params.get("base_id", None)
            table_id = params.get("table_id", None)

            table = create_table_instance(ACCESS_TOKEN, base_id, table_id)

            data = {"record_id": record_id}

            response = table.delete(**data)
            return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception({e})


def airtable_batch_delete_records(ACCESS_TOKEN, params):
    try:
        record_ids = params.get("record_ids", [])
        if record_ids:
            base_id = params.get("base_id", None)
            table_id = params.get("table_id", None)

            table = create_table_instance(ACCESS_TOKEN, base_id, table_id)

            data = {"record_ids": record_ids}

            response = table.batch_delete(**data)
            return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception({e})


def airtable_get_record(ACCESS_TOKEN, params):
    try:
        record_id = params.get("record_id", None)
        if record_id:
            base_id = params.get("base_id", None)
            table_id = params.get("table_id", None)

            table = create_table_instance(ACCESS_TOKEN, base_id, table_id)

            ignore_keys = ["base_id", "table_id"]
            data = {
                key: value
                for (key, value) in params.items()
                if value
                if key not in ignore_keys
            }

            response = table.get(**data)
            return response
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception({e})