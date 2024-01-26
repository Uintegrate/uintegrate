import time

from sshtunnel import open_tunnel

import mysql.connector
from mysql.connector import errorcode


def create_connection(credentials):
    try:
        if (
            "host" in credentials
            and "database" in credentials
            and "user" in credentials
            and "password" in credentials
            and "port" in credentials
        ):
            if not credentials.get("connection_timeout", None):
                credentials["connection_timeout"] = int(credentials.pop(
                    "connectionTimeout", None
                ))
            else: 
                credentials.pop("connectionTimeout", None)
            credentials["port"] = int(credentials.get("port", 3306))
            credentials["ssl_ca"] = credentials.pop("sslCa", None)
            credentials["ssl_cert"] = credentials.pop("sslCert", None)
            credentials["ssl_key"] = credentials.pop("sslKey", None)
            ignore_keys = [
                "sshEnabled",
                "sshHost",
                "sshPort",
                "sshMysqlPort",
                "sshUser",
                "sshAuthenticateWith",
                "sshPassword",
                "sshPrivateKey",
                "sshPassphrase",
                "Type",
            ]

            if credentials.get("sslEnabled", "False") == "True":
                ignore_keys.append("sslEnabled")
                credentials["ssl_disabled"] = False
                if not (
                    credentials.get("ssl_ca", None)
                    and credentials.get("ssl_cert", None)
                    and credentials.get("ssl_key", None)
                ):
                    raise Exception("Missing Input for SSL Connection!")
            else:
                ignore_keys.extend(["sslEnabled", "ssl_ca", "ssl_cert", "ssl_key"])

            if credentials.get("sshEnabled", False) == "True":
                sshHost = credentials.get("sshHost", None)
                sshPort = int(credentials.get("sshPort", 22))
                sshMysqlPort = int(credentials.get("sshMysqlPort", 3306))
                sshUser = credentials.get("sshUser", None)
                sshAuthenticateWith = credentials.get("sshAuthenticateWith", None)
                sshPassword = credentials.get("sshPassword", None)
                sshPrivateKey = credentials.get("sshPrivateKey", None)
                sshPassphrase = credentials.get("sshPassphrase", None)
                ignore_keys.append("port")
                config = {
                    key: value
                    for (key, value) in credentials.items()
                    if value
                    if key not in ignore_keys
                }
                if (
                    sshHost
                    and sshPort
                    and sshMysqlPort
                    and sshUser
                    and sshAuthenticateWith
                ):
                    ssh_config = {}
                    if sshAuthenticateWith == "Password":
                        if sshPassword:
                            ssh_config = {
                                "ssh_address_or_host": (sshHost, sshPort),
                                "ssh_username": sshUser,
                                "ssh_password": sshPassword,
                                "remote_bind_address": (config["host"], sshMysqlPort),
                            }
                        else:
                            raise Exception("Missing SSH Password")
                    elif sshAuthenticateWith == "Private Key":
                        if sshPrivateKey:
                            if sshPassphrase:
                                ssh_config = {
                                    "ssh_address_or_host": (sshHost, sshPort),
                                    "ssh_username": sshUser,
                                    "ssh_pkey": sshPrivateKey,
                                    "ssh_private_key_password": sshPassphrase,
                                    "remote_bind_address": (
                                        config["host"],
                                        sshMysqlPort,
                                    ),
                                }
                            else:
                                ssh_config = {
                                    "ssh_address_or_host": (sshHost, sshPort),
                                    "ssh_username": sshUser,
                                    "ssh_pkey": sshPrivateKey,
                                    "remote_bind_address": (
                                        config["host"],
                                        sshMysqlPort,
                                    ),
                                }
                        else:
                            raise Exception("Missing SSH Private Key")
                    else:
                        raise Exception("Wrong Value for SSH Authenticate with")
                else:
                    raise Exception("Missing Input for SSH Connection")

                attempt = 1
                attempts = 3
                delay = 2
                while attempt < attempts + 1:
                    with open_tunnel(**ssh_config) as tunnel:
                        try:
                            cnx = mysql.connector.MySQLConnection(
                                **config,
                                port=tunnel.local_bind_port,
                            )
                        except IOError as e:
                            if attempts is attempt:
                                raise Exception(f"Error creating connection: {e}")
                            time.sleep(delay**attempt)
                            attempt += 1
                        except mysql.connector.Error as err:
                            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                                raise Exception(
                                    "Something is wrong with your user name or password"
                                )
                            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                                raise Exception("Database does not exist")
                            else:
                                raise Exception(err)
                        else:
                            return cnx
            else:
                config = {
                    key: value
                    for (key, value) in credentials.items()
                    if value
                    if key not in ignore_keys
                }
                attempt = 1
                attempts = 3
                delay = 2
                while attempt < attempts + 1:
                    try:
                        cnx = mysql.connector.connect(**config)
                    except IOError as e:
                        if attempts is attempt:
                            raise Exception(f"Error creating connection: {e}")
                        time.sleep(delay**attempt)
                        attempt += 1
                    except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                            raise Exception(f"Something is wrong with your Credentials: {err}")
                        elif err.errno == errorcode.ER_BAD_DB_ERROR:
                            raise Exception("Database does not exist")
                        else:
                            raise Exception(err)
                    else:
                        return cnx
    except Exception as e:
        raise Exception(f"Error Creating Connection: {e}")


def operation_priority(query_priority):
    if query_priority == "low":
        priority = "LOW_PRIORITY "
    elif query_priority == "high":
        priority = "HIGH_PRIORITY "
    else:
        priority = ""
    return priority


def cnx_timeout_and_pool_size(credentials, connection_timeout, pool_size):
    if connection_timeout:
        credentials["connection_timeout"] = connection_timeout
    if pool_size:
        credentials["pool_size"] = pool_size
    return credentials


def raise_exception_or_rollback(choice, cnx, e, response, queries):
    if choice == "roll":
        try:
            cnx.rollback()
            response["Query_failed"] = "performed rollback due to a query's failure"
        except Exception as e:
            raise Exception(f"Database Error: {e} ///// queries: {queries}")
    elif choice == "raise":
        raise Exception(f"SQL Error: {e} ///// queries: {queries}")
    return response


def query_exec_info_insert(i, cnx, cursor, query, values):
    connection_info = {
        "connection_id": cnx.connection_id,
        "server_version": cnx.get_server_info(),
    }

    query_info = {
        "affected_rows": cursor.rowcount,
        "last_insert_id": cursor.lastrowid,
        "warnings": cursor.fetchwarnings(),
    }

    return {
        "query_index": i,
        "query": query,
        "values": values,
        "connection_info": connection_info,
        "query_info": query_info,
    }


def query_exec_info_update(i, cnx, cursor, query, values):
    connection_info = {
        "connection_id": cnx.connection_id,
        "server_version": cnx.get_server_info(),
    }

    query_info = {
        "affected_rows": cursor.rowcount,
        "warnings": cursor.fetchwarnings(),
    }

    return {
        "query_index": i,
        "query": query,
        "values": values,
        "connection_info": connection_info,
        "query_info": query_info,
    }


def query_exec_info_delete(i, cnx, cursor, query):
    connection_info = {
        "connection_id": cnx.connection_id,
        "server_version": cnx.get_server_info(),
    }

    query_info = {
        "affected_rows": cursor.rowcount,
        "warnings": cursor.fetchwarnings(),
    }

    return {
        "query_index": i,
        "query": query,
        "connection_info": connection_info,
        "query_info": query_info,
    }


def query_exec_info_delete_row(i, cnx, cursor, query, values):
    connection_info = {
        "connection_id": cnx.connection_id,
        "server_version": cnx.get_server_info(),
    }

    query_info = {
        "affected_rows": cursor.rowcount,
        "warnings": cursor.fetchwarnings(),
    }

    return {
        "query_index": i,
        "query": query,
        "values": values,
        "connection_info": connection_info,
        "query_info": query_info,
    }


def query_exec_info_select(i, cnx, cursor, *query_group):
    query = query_group[0]
    if len(query_group) > 1:
        values = query_group[1]
    else:
        values = []

    connection_info = {
        "connection_id": cnx.connection_id,
        "server_version": cnx.get_server_info(),
    }

    query_info = {
        "affected_rows": cursor.rowcount,
        "warnings": cursor.fetchwarnings(),
    }

    return {
        "query_index": i,
        "query": query,
        "conditions_values": values,
        "connection_info": connection_info,
        "query_info": query_info,
    }


def query_exec_info_execute_sql(i, cnx, cursor, *query_group):
    query = query_group[0]
    if len(query_group) > 1:
        values = query_group[1]
    else:
        values = []

    connection_info = {
        "connection_id": cnx.connection_id,
        "server_version": cnx.get_server_info(),
    }

    query_info = {
        "affected_rows": cursor.rowcount,
        "last_insert_id": cursor.lastrowid,
        "warnings": cursor.fetchwarnings(),
    }

    return {
        "query_index": i,
        "query": query,
        "values": values,
        "connection_info": connection_info,
        "query_info": query_info,
    }


def query_exec_info(
    operation,
    *args,
):
    if operation == "insert":
        return query_exec_info_insert(*args)
    elif operation == "update":
        return query_exec_info_update(*args)
    elif operation == "delete":
        return query_exec_info_delete(*args)
    elif operation == "delete_row":
        return query_exec_info_delete_row(*args)
    elif operation == "select":
        return query_exec_info_select(*args)
    elif operation == "execute_sql":
        return query_exec_info_execute_sql(*args)

    else:
        raise Exception(f"Wrong operation: {operation}")


def execute_queries(
    cnx,
    cursor,
    response,
    queries,
    query_batching,
    skip_on_conflict,
    operation,
    output_details,
):
    choice = "raise"
    query_execution_info = {}

    try:
        if query_batching == "transaction":
            cnx.start_transaction()
            for i, query in enumerate(queries):
                cursor.execute(*query)
                if output_details:
                    query_execution_info[i] = query_exec_info(
                        operation, i, cnx, cursor, *query
                    )
            choice = "roll"

        else:
            for i, query in enumerate(queries):
                cursor.execute(*query)
                if output_details:
                    query_execution_info[i] = query_exec_info(
                        operation, i, cnx, cursor, *query
                    )

        cnx.commit()

    except mysql.connector.errors.IntegrityError as e:
        if "1062" in str(e) and skip_on_conflict:
            response["notes"] = "Skipped insertion due to conflict."
        else:
            response = raise_exception_or_rollback(choice, cnx, e, response, queries)
    except Exception as e:
        response = raise_exception_or_rollback(choice, cnx, e, response, queries)

    if output_details:
        response["query_execution_information"] = query_execution_info

    return (response, cnx, cursor)


def return_operator(condition_operator):
    operator = ""
    if condition_operator == "equal":
        operator = " ="
    elif condition_operator == "not equal":
        operator = " <>"
    elif condition_operator == "like":
        operator = " LIKE"
    elif condition_operator == "greater than":
        operator = " >"
    elif condition_operator == "less than":
        operator = " <"
    elif condition_operator == "greater than or equal to":
        operator = " >="
    elif condition_operator == "less than or equal to":
        operator = " <="
    elif condition_operator == "is null":
        operator = " IS NULL"
    else:
        raise Exception("Operator not included")
    return operator


def condition_group_creator(combine_conditions, conditions):
    combining_conditions = ""
    values = []
    condition_group = ""

    if combine_conditions == "and":
        combining_conditions = " AND "
    elif combine_conditions == "or":
        combining_conditions = " OR "
    else:
        raise Exception("Wrong Combine Conditions value")

    for i, condition in enumerate(conditions):
        operator = return_operator(condition.get("operator"))
        combine = ""
        value_representaion = " %" + "s"
        if i != 0:
            combine = combining_conditions

        if operator == " IS NULL":
            value_representaion = ""
        else:
            value = condition.get("value", None)
            values.append(value)

        combination_part = (
            combine + condition.get("column") + operator + value_representaion
        )

        condition_group += combination_part
    return (condition_group, values)


def mysql_insert(credentials, params):
    try:
        response = {"result": "Operation Performed Successfully"}
        connection_timeout = params.get("connection_timeout", None)
        pool_size = params.get("pool_size", None)
        replace_empty_with_null = params.get("replace_empty_with_null", False)
        skip_on_conflict = params.get("skip_on_conflict", False)
        output_details = params.get("output_details", False)
        query_batching = params.get("query_batching", None)
        insert_rows = params.get("insert_rows", None)
        priority_input = params.get("priority", None)
        table = params.get("table", None)

        credentials = cnx_timeout_and_pool_size(
            credentials, connection_timeout, pool_size
        )

        if table and insert_rows:
            insert_queries = []

            priority = operation_priority(priority_input)

            for row in insert_rows:
                columns = []
                variables = []
                values = []
                for column, value in row.items():
                    columns.append(column)
                    variables.append("%" + "s")
                    if replace_empty_with_null and value == "":
                        values.append(None)
                    else:
                        values.append(value)
                insert_query = (
                    "INSERT "
                    + priority
                    + "INTO "
                    + table
                    + " ("
                    + ", ".join(columns)
                    + ") VALUES ("
                    + ", ".join(variables)
                    + ");"
                )
                insert_queries.append((insert_query, tuple(values)))

            cnx = create_connection(credentials)
            cursor = cnx.cursor()

            response, cnx, cursor = execute_queries(
                cnx,
                cursor,
                response,
                insert_queries,
                query_batching,
                skip_on_conflict,
                "insert",
                output_details,
            )

            cursor.close()
            cnx.close()

            return response
        else:
            raise Exception("Missing Input Data")
    except Exception as e:
        raise Exception(f"Error Inserting Data: {e}")


def mysql_update(credentials, params):
    try:
        response = {"result": "Operation Performed Successfully"}
        connection_timeout = params.get("connection_timeout", None)
        pool_size = params.get("pool_size", None)
        replace_empty_with_null = params.get("replace_empty_with_null", False)
        output_details = params.get("output_details", False)
        query_batching = params.get("query_batching", None)
        update_row = params.get("update_row", None)
        column_match = params.get("column_match", None)
        value_match = params.get("value_match", None)
        table = params.get("table", None)

        credentials = cnx_timeout_and_pool_size(
            credentials, connection_timeout, pool_size
        )

        if table and update_row and column_match and value_match:
            update_query = []
            columns = []
            values = []
            for column, value in update_row.items():
                columns.append(column)
                if replace_empty_with_null and value == "":
                    values.append(None)
                else:
                    values.append(value)

            join_var = " = %" + "s, "
            query = (
                "UPDATE "
                + table
                + " SET "
                + join_var.join(columns)
                + " = %"
                + "s "
                + " WHERE "
                + column_match
                + " = %"
                + "s;"
            )
            values.append(value_match)
            update_query.append((query, tuple(values)))

            cnx = create_connection(credentials)
            cursor = cnx.cursor()

            response, cnx, cursor = execute_queries(
                cnx,
                cursor,
                response,
                update_query,
                query_batching,
                False,
                "update",
                output_details,
            )

            cursor.close()
            cnx.close()

            return response
        else:
            raise Exception("Missing Input Data")

    except Exception as e:
        raise Exception(f"Error Updating Data: {e}")


def mysql_delete(credentials, params):
    try:
        response = {"result": "Operation Performed Successfully"}
        table = params.get("table", None)
        connection_timeout = params.get("connection_timeout", None)
        pool_size = params.get("pool_size", None)
        output_details = params.get("output_details", False)
        query_batching = params.get("query_batching", None)
        command = params.get("command", None)
        conditions = params.get("conditions", {})
        combine_conditions = params.get("combine_conditions", "")

        credentials = cnx_timeout_and_pool_size(
            credentials, connection_timeout, pool_size
        )

        if table and command:
            query = ""
            operation_type = "delete"
            delete_query = []

            if command == "truncate":
                query = f"TRUNCATE TABLE {table};"
                delete_query = [(query,)]
            elif command == "drop":
                query = f"DROP TABLE {table};"
                delete_query = [(query,)]
            elif command == "delete":
                if combine_conditions and conditions:
                    operation_type = "delete_row"
                    condition_group, values = condition_group_creator(
                        combine_conditions, conditions
                    )
                    query = "DELETE FROM " + table + " WHERE " + condition_group + ";"
                    delete_query = [(query, tuple(values))]
                elif not conditions:
                    query = f"DELETE FROM {table};"
                    delete_query = [(query,)]
                else:
                    raise Exception("Missing Input Data")
            else:
                raise Exception("Missing Input Data")

            cnx = create_connection(credentials)
            cursor = cnx.cursor()

            response, cnx, cursor = execute_queries(
                cnx,
                cursor,
                response,
                delete_query,
                query_batching,
                False,
                operation_type,
                output_details,
            )

            cursor.close()
            cnx.close()

            return response
        else:
            raise Exception("Missing Input Data")
    except Exception as e:
        raise Exception(f"Error Deleting Data: {e}")


def mysql_select(credentials, params):
    try:
        response = {"result": "Operation Performed Successfully"}
        table = params.get("table", None)
        connection_timeout = params.get("connection_timeout", None)
        pool_size = params.get("pool_size", None)
        output_details = params.get("output_details", False)
        query_batching = params.get("query_batching", None)
        conditions = params.get("conditions", {})
        combine_conditions = params.get("combine_conditions", "")
        return_all = params.get("return_all", False)
        return_limit = params.get("return_limit", None)
        sort_rules = params.get("sort_rules", {})
        output_columns = params.get("output_columns", [])
        select_distinct = params.get("select_distinct", False)

        credentials = cnx_timeout_and_pool_size(
            credentials, connection_timeout, pool_size
        )

        if table:
            query = ""
            condition_group_section = ""
            return_limit_section = ""
            sort_rules_section = ""
            select_distinct_value = ""
            columns_to_output = " * "
            select_query = []
            values = []
            operation_type = "select"

            if not return_all and int(return_limit):
                return_limit_section = f" LIMIT {int(return_limit)}"

            if combine_conditions and conditions:
                condition_group, values = condition_group_creator(
                    combine_conditions, conditions
                )
                condition_group_section = " WHERE " + condition_group

            if select_distinct:
                select_distinct_value = " DISTINCT"

            if output_columns:
                columns_to_output = " " + ", ".join(output_columns) + " "

            if sort_rules:
                sort_rule_part = ""

                for i, sort_rule in enumerate(sort_rules):
                    comma = ", "
                    if i == 0:
                        comma = ""
                    column = sort_rule.get("column", None)
                    direction = sort_rule.get("direction", None)
                    sort_dir = ""
                    if column and direction:
                        if direction == "asc":
                            sort_dir = "ASC"
                        elif direction == "desc":
                            sort_dir = "DESC"
                        else:
                            raise Exception("Missing Input Data")
                        sort_rule_part += comma + column + " " + sort_dir
                    else:
                        raise Exception("Missing Input Data")
                sort_rules_section = " ORDER BY " + sort_rule_part

            query = (
                "SELECT"
                + select_distinct_value
                + columns_to_output
                + "FROM "
                + table
                + condition_group_section
                + sort_rules_section
                + return_limit_section
                + ";"
            )
            if values:
                select_query = [(query, tuple(values))]
            else:
                select_query = [(query,)]

            cnx = create_connection(credentials)
            cursor = cnx.cursor(dictionary=True, buffered=True)

            response, cnx, cursor = execute_queries(
                cnx,
                cursor,
                response,
                select_query,
                query_batching,
                False,
                operation_type,
                output_details,
            )

            response["result_rows"] = cursor.fetchall()

            cursor.close()
            cnx.close()

            return response
        else:
            raise Exception("Missing Input Data")
    except Exception as e:
        raise Exception(f"Error Selecting Data: {e}")


def mysql_execute_sql(credentials, params):
    try:
        response = {"result": "Operation Performed Successfully"}
        connection_timeout = params.get("connection_timeout", None)
        pool_size = params.get("pool_size", None)
        replace_empty_with_null = params.get("replace_empty_with_null", False)
        output_details = params.get("output_details", False)
        query_batching = params.get("query_batching", None)
        queries_with_values = params.get("queries_with_values", [])
        operation_type = "execute_sql"

        credentials = cnx_timeout_and_pool_size(
            credentials, connection_timeout, pool_size
        )
        if queries_with_values:
            queries_to_execute = []

            for query_with_values in queries_with_values:
                query = query_with_values.get("query", "")
                query_values = query_with_values.get("values", [])
                if not query:
                    raise Exception("Missing Query in Input Data")
                if query_values:
                    if replace_empty_with_null:
                        values = []
                        for value in query_values:
                            if value == "":
                                values.append(None)
                            else:
                                values.append(value)
                    else:
                        values = query_with_values["values"]
                    queries_to_execute.append((query, tuple(values)))
                else:
                    queries_to_execute.append((query,))

            cnx = create_connection(credentials)
            cursor = cnx.cursor(dictionary=True, buffered=True)

            choice = "raise"
            query_execution_info = {}

            result_rows = []

            try:
                if query_batching == "transaction":
                    cnx.start_transaction()
                    for i, query in enumerate(queries_to_execute):
                        cursor.execute(*query)

                        if cursor.with_rows:
                            result_rows.append(cursor.fetchall())

                        if output_details:
                            query_execution_info[i] = query_exec_info(
                                operation_type, i, cnx, cursor, *query
                            )
                    choice = "roll"
                else:
                    for i, query in enumerate(queries_to_execute):
                        cursor.execute(*query)

                        if cursor.with_rows:
                            result_rows.append(cursor.fetchall())

                        if output_details:
                            query_execution_info[i] = query_exec_info(
                                operation_type, i, cnx, cursor, *query
                            )

                cnx.commit()

            except mysql.connector.errors.IntegrityError as e:
                response = raise_exception_or_rollback(
                    choice, cnx, e, response, queries_to_execute
                )
            except Exception as e:
                response = raise_exception_or_rollback(
                    choice, cnx, e, response, queries_to_execute
                )

            if output_details:
                response["query_execution_information"] = query_execution_info

            response["result_rows"] = result_rows

            cursor.close()
            cnx.close()

            return response
        else:
            raise Exception("Missing Input Data")
    except Exception as e:
        raise Exception(f"Error Executing SQL Query: {e}")