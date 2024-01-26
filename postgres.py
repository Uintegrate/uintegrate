import psycopg2

def create_connection(creds):
    con = psycopg2.connect(
        host=creds["host"],
        database=creds["database"],
        user=creds["user"],
        password=creds["password"],
        port="5432",
    )
    return con


def postgres_create_table(creds, params):
    try:
        con = create_connection(creds)
        cursor = con.cursor()
        if (
            "table_name" in params
            and params["table_name"]
            and params["table_name"] != ""
            and "fields" in params
            and params["fields"]
            and params["fields"] != {}
        ):
            table_name = params["table_name"]
            fields = params["fields"]
            string_fields = ""
            for field in fields.keys():
                string_fields += f"{field} {fields[field]}, "
            string_fields = string_fields[:-2]
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({string_fields})"
            cursor.execute(query)
            con.commit()
            cursor.close()
            con.close()
            return "Table created successfully"
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def postgres_insert_row(creds, params):
    try:
        con = create_connection(creds)
        cursor = con.cursor()
        if (
            "table_name" in params
            and params["table_name"]
            and params["table_name"] != ""
            and "data" in params
            and params["data"]
            and params["data"] != {}
        ):
            table_name = params["table_name"]
            data = params["data"]
            string_fields = ""
            string_values = ""
            for field in data.keys():
                string_fields += f"{field}, "
                string_values += f"'{data[field]}', "
            string_fields = string_fields[:-2]
            string_values = string_values[:-2]
            query = (
                f"INSERT INTO {table_name} ({string_fields}) VALUES ({string_values})"
            )
            cursor.execute(query)
            con.commit()
            cursor.close()
            con.close()
            return "Row inserted successfully"
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def postgres_update_row(creds, params):
    try:
        con = create_connection(creds)
        cursor = con.cursor()
        if (
            "table_name" in params
            and params["table_name"]
            and params["table_name"] != ""
            and "data" in params
            and params["data"]
            and params["data"] != {}
            and "conditions" in params
            and params["conditions"]
            and params["conditions"] != {}
        ):
            table_name = params["table_name"]
            data = params["data"]
            conditions = params["conditions"]
            condition_type = conditions["type"]
            condition_string = "WHERE "
            if condition_type == "AND":
                for condition in conditions["conditions"]:
                    condition_string += f"{condition} AND "
                condition_string = condition_string[:-4]
            elif condition_type == "OR":
                for condition in conditions["conditions"]:
                    condition_string += f"{condition} OR "
                condition_string = condition_string[:-3]
            elif condition_type == "custom":
                condition_string += conditions["conditions"]
            else:
                raise Exception("Invalid condition type")
            string_fields = ""
            for field in data.keys():
                string_fields += f"{field} = '{data[field]}', "
            string_fields = string_fields[:-2]
            query = f"UPDATE {table_name} SET {string_fields} {condition_string}"
            cursor.execute(query)
            con.commit()
            cursor.close()
            con.close()
            return "Row updated successfully"
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def postgres_delete_row(creds, params):
    try:
        con = create_connection(creds)
        cursor = con.cursor()
        if (
            "table_name" in params
            and params["table_name"]
            and params["table_name"] != ""
        ):
            table_name = params["table_name"]
            conditions = None
            condition_string = ""
            if (
                "conditions" in params
                and params["conditions"]
                and params["conditions"] != {}
            ):
                conditions = params["conditions"]
                condition_type = conditions["type"]
                condition_string = "WHERE "
                if condition_type == "AND":
                    for condition in conditions["conditions"]:
                        condition_string += f"{condition} AND "
                    condition_string = condition_string[:-4]
                elif condition_type == "OR":
                    for condition in conditions["conditions"]:
                        condition_string += f"{condition} OR "
                    condition_string = condition_string[:-3]
                elif condition_type == "custom":
                    condition_string += conditions["conditions"]
                else:
                    raise Exception("Invalid condition type")

            query = f"DELETE FROM {table_name} {condition_string}"
            cursor.execute(query)
            con.commit()
            cursor.close()
            con.close()
            return "Row deleted successfully"
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def postgres_delete_table(creds, params):
    try:
        con = create_connection(creds)
        cursor = con.cursor()
        if (
            "table_name" in params
            and params["table_name"]
            and params["table_name"] != ""
            and "type" in params
            and params["type"]
            and params["type"] != ""
        ):
            table_name = params["table_name"]
            delete_type = params["type"]
            if delete_type == "clear":
                query = f"Delete from {table_name}"
            elif delete_type == "drop":
                query = f"DROP TABLE {table_name}"
            else:
                raise Exception("Invalid delete type")
            cursor.execute(query)
            con.commit()
            cursor.close()
            con.close()
            return f"Table {delete_type}ed successfully"
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def postgres_execute_custom_query(creds, params):
    try:
        con = create_connection(creds)
        cursor = con.cursor()
        if "query" in params and params["query"] and params["query"] != "":
            query = params["query"]
            cursor.execute(query)
            try:
                result = cursor.fetchall()
                con.commit()
                cursor.close()
                con.close()
                return result
            except:
                con.commit()
                cursor.close()
                con.close()
                return "Query executed successfully"
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def postgres_select_row(creds, params):
    try:
        con = create_connection(creds)
        cursor = con.cursor()
        count = None
        if (
            "table_name" in params
            and params["table_name"]
            and params["table_name"] != ""
        ):
            if "count" in params and params["count"] and params["count"] != 0:
                count = params["count"]
            table_name = params["table_name"]
            # data = params["data"]
            conditions = None
            condition_string = ""
            if (
                "conditions" in params
                and params["conditions"]
                and params["conditions"] != {}
            ):
                conditions = params["conditions"]
                condition_type = conditions["type"]
                condition_string = "WHERE "
                if condition_type == "AND":
                    for condition in conditions["conditions"]:
                        condition_string += f"{condition} AND "
                    condition_string = condition_string[:-4]
                elif condition_type == "OR":
                    for condition in conditions["conditions"]:
                        condition_string += f"{condition} OR "
                    condition_string = condition_string[:-3]
                elif condition_type == "custom":
                    condition_string += conditions["conditions"]
                else:
                    raise Exception("Invalid condition type")

            query = f"SELECT * FROM {table_name} {condition_string}"
            if count:
                query += f" LIMIT {count}"
            cursor.execute(query)
            result = cursor.fetchall()
            con.commit()
            cursor.close()
            con.close()
            return result
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)