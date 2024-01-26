import requests
import base64

def bamboohr_get_report(api_key, domain,params):
    try:
        if "id" in params and "format" in params:
            base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
            api_key = f"{api_key}:"
            encoded_api_key = base64.b64encode(api_key.encode()).decode()
            endpoint = params["id"]
            data = {}
            for key, value in params.items():
                skip_keys = ["id", "format"]
                if key in skip_keys:
                    continue
                if value:
                    data[key] = value
            report_format = params["format"]
            content_type = ""
            if report_format == "pdf" or report_format == "json":
                content_type = f"application/{report_format}"
            elif report_format == "xls":
                content_type = "application/vnd.ms-excel"
            elif report_format == "csv" or report_format == "xml":
                content_type = f"text/{report_format}"
            headers = {
                "Authorization": f"Basic {encoded_api_key}",
                "Accept": content_type,
            }
            response = requests.get(
                base_url + f"reports/{endpoint}",
                json=data,
                headers=headers,
            )
            if response:
                if report_format == "json":
                    report_data = response.json()
                else:
                    report_data = response.text
                return report_data
            else:
                raise Exception(
                    {"error": f"Failed to retrieve report. Status code: {response.status_code}{response.text}"})
        else:
            raise Exception({"error": "missing parameters"})
    except Exception as error:
        raise Exception(str(error))

def bamboohr_create_employee(api_key, domain, params):
    try:
        if "firstName" in params and "lastName" in params:
            base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
            api_key = f"{api_key}:"
            encoded_api_key = base64.b64encode(api_key.encode()).decode()
            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value
            headers = {
                "content-type": "application/json",
                "Authorization": f"Basic {encoded_api_key}",
            }
            response = requests.post(
                base_url + "employees/", json=data, headers=headers
            )
            if response.status_code == 201:
                data = response.headers["Location"]
                parts = data.split("/")
                id = parts[-1]
                return {"id": id}
            else:
                raise Exception(
                    {"error": f"Failed to create employee. Status code: {response.status_code}{response.text}"}
                )
        else:
            raise Exception({"error": "missing parameters"})
    except Exception as error:
        raise Exception(str(error))

def bamboohr_get_employee_by_id(api_key, domain, params):
    try:
        if "id" in params:
            base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
            api_key = f"{api_key}:"
            encoded_api_key = base64.b64encode(api_key.encode()).decode()
            endpoint = params["id"]
            data = {}
            for key, value in params.items():
                skip_keys = ["id"]
                if key in skip_keys:
                    continue
                if value:
                    data[key] = value
            headers = {
                "Accept": "application/json",
                "Authorization": f"Basic {encoded_api_key}",
            }
            response = requests.get(
                base_url + "employees/" + endpoint + "/",
                params=data,
                headers=headers,
            )

            if response.status_code == 200:
                employee_data = response.json()
                return employee_data
            else:
                raise Exception(
                    {"error": f"Failed to get employee. Status code: {response.status_code}{response.text}"})
        else:
            raise Exception({"error": "missing parameters"})
    except Exception as error:
        raise Exception(str(error))

def bamboohr_get_employee_directory(api_key, domain):
    try:

        base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
        api_key = f"{api_key}:"
        encoded_api_key = base64.b64encode(api_key.encode()).decode()
        headers = {
            "Accept": "application/json",
            "Authorization": f"Basic {encoded_api_key}",
        }
        response = requests.get(
            base_url + "employees/directory",
            headers=headers,
        )

        if response.status_code == 200:
            employee_data = response.json()
            return employee_data
        else:
            raise Exception(
                {"error": f"Request failed with status code: {response.status_code}   {response.text}"})

    except Exception as error:
        raise Exception(str(error))

def bamboohr_update_employee(api_key, domain, params):
    try:
        if "id" in params:
            base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
            api_key = f"{api_key}:"
            encoded_api_key = base64.b64encode(api_key.encode()).decode()
            endpoint = params["id"]
            data = {}
            headers = {
                "content-type": "application/json",
                "Authorization": f"Basic {encoded_api_key}",
            }
            for key, value in params.items():
                skip_keys = ["id"]
                if key in skip_keys:
                    continue
                if value:
                    data[key] = value
            if data:
                response = requests.post(
                    base_url + "employees/" + endpoint + "/", json=data, headers=headers
                )
                if response.status_code == 200:
                    return {"message": "Employee information has been successfully updated"}
                else:
                    raise Exception(
                        {"error": f"Unable to update employee. Status code {response.status_code} {response.text}"})
            else:
                raise Exception(
                    {"error": "At least one field must be updated"})
        else:
            raise Exception({"error": "missing parameters"})
    except Exception as error:
        raise Exception(str(error))

def bamboohr_get_employee_file(api_key, domain, params):
    try:
        if "id" in params:
            base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
            api_key = f"{api_key}:"
            encoded_api_key = base64.b64encode(api_key.encode()).decode()
            headers = {
                "Accept": "application/json",
                "Authorization": f"Basic {encoded_api_key}",
            }
            id = params["id"]
            response = requests.get(
                base_url + f"employees/{id}/files/view/",
                headers=headers,
            )
            if response.status_code == 200:
                file_data = response.json()
                return file_data
            else:
                raise Exception(
                    {"error":  f"Request failed with status code: {response.status_code}  {response.text}"})
        else:
            raise Exception({"error": "missing parameters"})
    except Exception as error:
        raise Exception(str(error))

def bamboohr_delete_employee_file(api_key, domain, params):
    try:
        if "id" in params and "fileId" in params:
            base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
            api_key = f"{api_key}:"
            encoded_api_key = base64.b64encode(api_key.encode()).decode()

            headers = {
                "Authorization": f"Basic {encoded_api_key}",
            }
            id = params["id"]
            fileId = params["fileId"]
            response = requests.delete(
                base_url + f"employees/{id}/files/{fileId}",
                headers=headers,
            )

            if response.status_code == 200:
                return {"message": "File deleted successfully"}
            else:
                raise Exception(
                    {"error": f"Request failed with status code: {response.status_code}   {response.text}"})
        else:
            raise Exception({"error": "missing parameters"})
    except Exception as error:
        raise Exception(str(error))

def bamboohr_update_employee_file(api_key, domain, params):
    try:
        if "id" in params and "fileId" in params:
            base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
            api_key = f"{api_key}:"
            encoded_api_key = base64.b64encode(api_key.encode()).decode()
            data = {}
            for key, value in params.items():
                skip_keys = ["id", "fileId"]
                if key in skip_keys:
                    continue
                if value:
                    data[key] = value
            headers = {
                "content-type": "application/json",
                "Authorization": f"Basic {encoded_api_key}",
            }
            id = params["id"]
            fileId = params["fileId"]
            response = requests.post(
                base_url + f"employees/{id}/files/{fileId}", json=data, headers=headers
            )
            if response.status_code == 200:
                return {"message": "File details updated successfully"}
            else:
                raise Exception({"error": f"Request failed with status code: {response.status_code}   {response.text}"}
                                )
        else:
            raise Exception({"error": "missing parameters"})
    except Exception as error:
        raise Exception(str(error))

def bamboohr_upload_employee_file(api_key, domain, params):
    try:
        if ("category" in params
                and "fileName" in params
                and "id" in params
                ):
            base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
            api_key = f"{api_key}:"
            encoded_api_key = base64.b64encode(api_key.encode()).decode()

            data = {}
            for key, value in params.items():
                if value:
                    data[key] = value

            headers = {
                "Authorization": f"Basic {encoded_api_key}",
            }
            if "binary_data" in params:
                file_content = params["binary_data"]
                files = {
                    "file": (
                        params["fileName"],
                        file_content,
                    )
                }
            elif "file_url" in params:
                file_url = params["file_url"]
                response = requests.get(file_url)
                file_content = response.content
                files = {
                    "file": (
                        params["fileName"],
                        file_content,
                    )
                }
            else:
                raise Exception({"error": "Invalid file data provided."})
            id = params["id"]
            response = requests.post(
                base_url + f"employees/{id}/files",
                headers=headers,
                data=data,
                files=files,
            )
            if response.status_code == 201:
                return {"message": "File uploaded successfully."}
            else:
                raise Exception({"error": f"Error uploading file. Status code: {response.status_code}, Response: {response.text}"}
                                )
        else:
            raise Exception({"error": "missing parameters"})
    except Exception as error:
        raise Exception(str(error))

def bamboohr_view_company_files(api_key, domain):
    try:
        base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"

        api_key = f"{api_key}:"
        encoded_api_key = base64.b64encode(api_key.encode()).decode()
        headers = {
            "Authorization": f"Basic {encoded_api_key}",
            "Accept": "application/json",
        }
        response = requests.get(base_url + f"files/view/", headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(
                {"error":  f"Request failed with status code: {response.status_code}  {response.text}"})

    except Exception as error:
        raise Exception(str(error))

def bamboohr_delete_company_file(api_key, domain, params):
    try:
        if "fileId" in params:
            base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
            api_key = f"{api_key}:"
            encoded_api_key = base64.b64encode(api_key.encode()).decode()

            headers = {
                "Authorization": f"Basic {encoded_api_key}",
            }
            fileId = params["fileId"]
            response = requests.delete(
                base_url + f"/files/{fileId}",
                headers=headers,
            )

            if response.status_code == 200:
                return {"message": "File deleted successfully"}
            else:
                raise Exception({"error": f"Request failed with status code: {response.status_code}   {response.text}"}
                                )
        else:
            raise Exception({"error": "missing parameters"})

    except Exception as error:
        raise Exception(str(error))

def bamboohr_update_company_file(api_key, domain, params):
    try:
        if "fileId" in params:
            base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
            api_key = f"{api_key}:"
            encoded_api_key = base64.b64encode(api_key.encode()).decode()
            data = {}
            for key, value in params.items():
                skip_keys = ["fileId"]
                if key in skip_keys:
                    continue
                if value:
                    data[key] = value
            headers = {
                "content-type": "application/json",
                "Authorization": f"Basic {encoded_api_key}",
            }
            fileId = params["fileId"]
            response = requests.post(
                base_url + f"files/{fileId}", json=data, headers=headers
            )
            if response.status_code == 200:
                return {"message": "File details updated successfully"}
            else:
                raise Exception({"error":   f"Request failed with status code: {response.status_code} {response.text}"}
                                )
        else:
            raise Exception({"error": "missing parameters"})
    except Exception as error:
        raise Exception(str(error))

def bamboohr_upload_company_file(api_key, domain, params):
    try:
        if "category" in params and "fileName" in params:
            base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
            api_key = f"{api_key}:"
            encoded_api_key = base64.b64encode(api_key.encode()).decode()
            data = {}
            for key, value in params.items():

                if value:
                    data[key] = value
            headers = {
                "Authorization": f"Basic {encoded_api_key}",
            }
            if "binary_data" in params:
                file_content = params["binary_data"]
                files = {
                    "file": (
                        params["fileName"],
                        file_content,
                    )
                }
            elif "file_url" in params:
                file_url = params["file_url"]
                response = requests.get(file_url)
                file_content = response.content
                files = {
                    "file": (
                        params["fileName"],
                        file_content,
                    )
                }
            else:
                raise Exception({"error": "Invalid file data provided."})
            response = requests.post(
                base_url + f"files", headers=headers, data=data, files=files
            )
            if response.status_code == 201:
                return {"message": "File uploaded successfully."}
            else:
                raise Exception({"error": f"Error uploading file. Status code: {response.status_code}, Response: {response.text}"}
                                )
        else:
            raise Exception({"error": "missing parameters"})
    except Exception as error:
        raise Exception(str(error))

def bamboohr_get_whos_out(api_key, domain, params):
    try:
        base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
        api_key = f"{api_key}:"
        encoded_api_key = base64.b64encode(api_key.encode()).decode()
        data = {}
        for key, value in params.items():

            if value:
                data[key] = value
        headers = {
            "Accept": "application/json",
            "Authorization": f"Basic {encoded_api_key}",
        }
        response = requests.get(
            base_url + "time_off/whos_out/",
            params=data,
            headers=headers,
        )

        if response.status_code == 200:
            whos_out_data = response.json()
            return whos_out_data
        else:
            raise Exception(
                {"error": f"Failed to fetch 'Who's Out' data. Status code: {response.status_code} {response.text}"})
    except Exception as error:
        raise Exception(str(error))

def bamboohr_respond_to_timeoff_request(api_key, domain, params):
    try:
        if "requestId" in params and "status" in params:
            base_url = f"https://api.bamboohr.com/api/gateway.php/{domain}/v1/"
            api_key = f"{api_key}:"
            encoded_api_key = base64.b64encode(api_key.encode()).decode()
            data = {}
            for key, value in params.items():
                skip_keys = ["requestId"]
                if key in skip_keys:
                    continue
                if value:
                    data[key] = value
            headers = {
                "Accept": "application/json",
                "Authorization": f"Basic {encoded_api_key}",
            }
            requestId = params["requestId"]
            response = requests.put(
                base_url + f"time_off/requests/{requestId}/status",
                json=data,
                headers=headers,
            )
            if response.status_code == 200:
                return {"message": "Successfully responded to the time-off request"}
            else:
                raise Exception({"error": f"Failed to fetch time-off requests. Status code: {response.status_code}{response.text}"})
        else:
            raise Exception({"error": "missing parameters"})
    except Exception as error:
        raise Exception(str(error))
