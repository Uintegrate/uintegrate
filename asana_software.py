import asana
from asana.rest import ApiException
import json


def asana_get_many_project(accessToken,params):
    try:
        if "workspace" in params:
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            projects_api_instance = asana.ProjectsApi(api_client)
            opts = {"opt_fields": "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,offset,owner,path,permalink_url,project_brief,public,start_on,team,team.name,uri,workspace,workspace.name", }
            for key, value in params.items():
                if value:
                    opts[key] = value
            api_response = projects_api_instance.get_projects(opts)
            projects = list(api_response)
            return projects
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_get_project(accessToken,params):
    try:
        if "project_gid" in params:
            project_gid = params["project_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            projects_api_instance = asana.ProjectsApi(api_client)
            opts = {
                "opt_fields": "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,project_brief,public,start_on,team,team.name,workspace,workspace.name",
            }
            project = projects_api_instance.get_project(project_gid, opts)
            if project:
                return project
            else:
                raise Exception("Failed to fetches projects.")
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_create_project(accessToken,params):
    try:
        if "name" in params and "workspace" in params and "team" in params:
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            projects_api_instance = asana.ProjectsApi(api_client)
            body_data = {}
            for key, value in params.items():
                body_data[key] = value
            body = {"data": body_data}
            opts = {
                "opt_fields": "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,project_brief,public,start_on,team,team.name,workspace,workspace.name",
            }
            response = projects_api_instance.create_project(body, opts)
            return response
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_update_project(accessToken,params):
    try:
        if "project_gid" in params and "workspace" in params:
            project_gid = params["project_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            projects_api_instance = asana.ProjectsApi(api_client)
            body_data = {}
            for key, value in params.items():
                skip_keys = ["project_gid"]
                if key in skip_keys:
                    continue
                if value:
                    body_data[key] = value
            body = {"data": body_data}
            opts = {
                "opt_fields": "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,project_brief,public,start_on,team,team.name,workspace,workspace.name",
            }
            response = projects_api_instance.update_project(
                body, project_gid, opts)
            return response
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_delete_project(accessToken,params):
    try:
        if "project_gid" in params:
            project_gid = params["project_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            projects_api_instance = asana.ProjectsApi(api_client)
            projects_api_instance.delete_project(project_gid)
            return {"message": f"Deleted project with ID {project_gid}"}
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_create_project_from_template(accessToken,params):
    try:
        if "project_template_gid" in params and "name" in params:
            project_template_gid = params["project_template_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            project_templates_api_instance = asana.ProjectTemplatesApi(
                api_client)
            body_data = {
                "public": False,
            }
            for key, value in params.items():
                skip_keys = ["project_template_gid"]
                if key in skip_keys:
                    continue
                if value:
                    body_data[key] = value
            opts = {
                "body": {"data": body_data},
                "opt_fields": "new_project,new_project.name,new_project_template,new_project_template.name,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,resource_subtype,status",
            }
            api_response = project_templates_api_instance.instantiate_project(
                project_template_gid, opts)
            return api_response
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_create_task(accessToken,params):
    try:
        if "name" in params and "workspace" in params:
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            tasks_api_instance = asana.TasksApi(api_client)
            body_data = {}
            for key, value in params.items():
                if value:
                    body_data[key] = value
            body = {"data": body_data}
            opts = {
                "opt_fields": "actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,parent,parent.created_by,parent.name,parent.resource_subtype,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,workspace,workspace.name",
            }
            api_response = tasks_api_instance.create_task(body, opts)
            return api_response
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_get_task(accessToken,params):
    try:
        if "task_gid" in params:
            task_gid = params["task_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            tasks_api_instance = asana.TasksApi(api_client)
            opts = {
                "opt_fields": "actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,parent,parent.created_by,parent.name,parent.resource_subtype,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,workspace,workspace.name",
            }
            api_response = tasks_api_instance.get_task(task_gid, opts)
            return api_response
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_get_many_task(accessToken,params):
    try:
        configuration = asana.Configuration()
        configuration.access_token = accessToken
        api_client = asana.ApiClient(configuration)
        tasks_api_instance = asana.TasksApi(api_client)
        opts = {"opt_fields": "actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name", }
        for key, value in params.items():
            if value:
                opts[key] = value
        api_response = tasks_api_instance.get_tasks(opts)
        tasks = list(api_response)
        return tasks
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_update_task(accessToken,params):
    try:
        if "task_gid" in params:
            task_gid = params["task_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            tasks_api_instance = asana.TasksApi(api_client)
            body_data = {}
            for key, value in params.items():
                skip_keys = ["task_gid"]
                if key in skip_keys:
                    continue
                if value:
                    body_data[key] = value
            body = {"data": body_data}
            opts = {
                "opt_fields": "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,project_brief,public,start_on,team,team.name,workspace,workspace.name",
            }
            api_response = tasks_api_instance.update_task(body, task_gid, opts)
            return api_response
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_delete_task(accessToken,params):
    try:
        if "task_gid" in params:
            task_gid = params["task_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            tasks_api_instance = asana.TasksApi(api_client)
            tasks_api_instance.delete_task(task_gid)
            return {"message": f"Deleted project with ID {task_gid}"}
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_search_task(accessToken,params):
    try:
        if "workspace_gid" in params:
            workspace_gid = params["workspace_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            tasks_api_instance = asana.TasksApi(api_client)
            opts = {
                "opt_fields": "actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,parent,parent.created_by,parent.name,parent.resource_subtype,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,workspace,workspace.name",
                "completed": False
            }
            for key, value in params.items():
                skip_keys = ["workspace_gid"]
                if key in skip_keys:
                    continue
                if value:
                    opts[key] = value
            api_response = tasks_api_instance.search_tasks_for_workspace(
                workspace_gid, opts)
            tasks = list(api_response)
            return tasks
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_duplicate_task(accessToken,params):
    try:
        if "task_gid" in params and "name" in params:
            task_gid = params["task_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            tasks_api_instance = asana.TasksApi(api_client)
            body_data = {}
            for key, value in params.items():
                if value:
                    body_data[key] = value
            body = {"data": body_data}
            opts = {
                "opt_fields": "new_project,new_project.name,new_project_template,new_project_template.name,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,resource_subtype,status",
            }
            api_response = tasks_api_instance.duplicate_task(
                body, task_gid, opts)
            return api_response
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_upload_file_task(accessToken,params):
    try:
        if "parent" in params and "url" in params and "name" in params:
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            attachments_api_instance = asana.AttachmentsApi(api_client)
            opts = {
                "resource_subtype": "external",
                "opt_fields": "connected_to_app,created_at,download_url,host,name,parent,parent.created_by,parent.name,parent.resource_subtype,permanent_url,resource_subtype,size,view_url",
            }
            for key, value in params.items():
                if value:
                    opts[key] = value
            api_response = attachments_api_instance.create_attachment_for_object(
                opts)
            return api_response
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_get_user(accessToken,params):
    try:
        if "user_gid" in params:
            user_gid = params["user_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            users_api_instance = asana.UsersApi(api_client)
            opts = {
                "opt_fields": "email,name,photo,photo.image_1024x1024,photo.image_128x128,photo.image_21x21,photo.image_27x27,photo.image_36x36,photo.image_60x60,workspaces,workspaces.name",
            }
            api_response = users_api_instance.get_user(user_gid, opts)
            return api_response
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_get_many_user(accessToken,params):
    try:
        if "workspace_gid" in params:
            workspace_gid = params["workspace_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            users_api_instance = asana.UsersApi(api_client)
            opts = {}
            api_response = users_api_instance.get_users_for_workspace(
                workspace_gid, opts)
            users = list(api_response)
            return users
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_create_section_project(accessToken,params):
    try:
        if "project_gid" in params and "name" in params:
            project_gid = params["project_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            sections_api_instance = asana.SectionsApi(api_client)
            body_data = {}
            for key, value in params.items():
                skip_keys = ["project_gid"]
                if key in skip_keys:
                    continue
                if value:
                    body_data[key] = value
            opts = {
                "body": {"data": body_data},
                "opt_fields": "created_at,name,project,project.name,projects,projects.name",
            }
            api_response = sections_api_instance.create_section_for_project(
                project_gid, opts)
            return api_response
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_get_section_project(accessToken,params):
    try:
        if "project_gid" in params:
            project_gid = params["project_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            sections_api_instance = asana.SectionsApi(api_client)
            opts = {
                "opt_fields": "created_at,name,offset,path,project,project.name,projects,projects.name,uri",
            }
            api_response = sections_api_instance.get_sections_for_project(
                project_gid, opts)
            sections = list(api_response)
            return sections
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_move_task_to_section(accessToken,params):
    try:
        if "section_gid" in params and "task" in params:
            section_gid = params["section_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            sections_api_instance = asana.SectionsApi(api_client)
            body_data = {}
            for key, value in params.items():
                skip_keys = ["section_gid"]
                if key in skip_keys:
                    continue
                if value:
                    body_data[key] = value
            opts = {
                "body": {"data": body_data},
            }
            sections_api_instance.add_task_for_section(section_gid, opts)
            return {"message": f"Successfully Moved the task"}
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_add_project_for_task(accessToken,params):
    try:
        if "task_gid" in params and "project" in params:
            insert_after = params.get("insert_after")
            insert_before = params.get("insert_before")
            section = params.get("section")
            provided_params = [param for param in (
                insert_after, insert_before, section) if param is not None]
            if len(provided_params) < 1 or len(provided_params) == 1:
                task_gid = params["task_gid"]
                configuration = asana.Configuration()
                configuration.access_token = accessToken
                api_client = asana.ApiClient(configuration)
                tasks_api_instance = asana.TasksApi(api_client)
                body_data = {}
                for key, value in params.items():
                    skip_keys = ["task_gid"]
                    if key in skip_keys:
                        continue
                    if value:
                        body_data[key] = value
                body = {"data": body_data}
                tasks_api_instance.add_project_for_task(body, task_gid)
                return {"message": f"Successfully added the specified project to the task."}
            else:
                raise Exception(
                    "You can specify at most one of insert_after, insert_before, or section.")
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_remove_project_for_task(accessToken,params):
    try:
        if "task_gid" in params and "project" in params:
            task_gid = params["task_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            tasks_api_instance = asana.TasksApi(api_client)
            body_data = {}
            for key, value in params.items():
                skip_keys = ["task_gid"]
                if key in skip_keys:
                    continue
                if value:
                    body_data[key] = value
            body = {"data": body_data}
            tasks_api_instance.remove_project_for_task(body, task_gid)
            return {"message": f"Successfully removed the specified project from the task."}
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_get_tasks_for_project(accessToken,params):
    try:
        if "project_gid" in params:
            project_gid = params["project_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            tasks_api_instance = asana.TasksApi(api_client)
            opts = {
                "opt_fields": "actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,followers,followers.name,html_notes,liked,likes,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name",
            }
            for key, value in params.items():
                skip_keys = ["project_gid"]
                if key in skip_keys:
                    continue
                if value:
                    opts[key] = value
            api_response = tasks_api_instance.get_tasks_for_project(
                project_gid, opts)
            tasks = list(api_response)
            return tasks
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_create_subtask(accessToken,params):
    try:
        if "task_gid" in params and "name" in params:
            task_gid = params["task_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            tasks_api_instance = asana.TasksApi(api_client)
            body_data = {}
            for key, value in params.items():
                skip_keys = ["task_gid"]
                if key in skip_keys:
                    continue
                if value:
                    body_data[key] = value
            body = {"data": body_data}
            opts = {
                "opt_fields": "actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,parent,parent.created_by,parent.name,parent.resource_subtype,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,workspace,workspace.name",
            }
            api_response = tasks_api_instance.create_subtask_for_task(
                body, task_gid, opts)
            return api_response
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_get_many_subtask(accessToken,params):
    try:
        if "task_gid" in params:
            task_gid = params["task_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            tasks_api_instance = asana.TasksApi(api_client)
            opts = {
                "opt_fields": "actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name",
            }
            api_response = tasks_api_instance.get_subtasks_for_task(
                task_gid, opts)
            subtasks = list(api_response)
            return subtasks
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_add_task_comment(accessToken,params):
    try:
        if "task_gid" in params:
            if "text" in params or "html_text" in params:
                task_gid = params["task_gid"]
                configuration = asana.Configuration()
                configuration.access_token = accessToken
                api_client = asana.ApiClient(configuration)
                stories_api_instance = asana.StoriesApi(api_client)
                body_data = {}
                for key, value in params.items():
                    skip_keys = ["task_gid"]
                    if key in skip_keys:
                        continue
                    if value:
                        body_data[key] = value
                body = {"data": body_data}
                opts = {
                    "opt_fields": "assignee,assignee.name,created_at,created_by,created_by.name,custom_field,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.is_formula_field,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.resource_subtype,custom_field.text_value,custom_field.type,dependency,dependency.created_by,dependency.name,dependency.resource_subtype,duplicate_of,duplicate_of.created_by,duplicate_of.name,duplicate_of.resource_subtype,duplicated_from,duplicated_from.created_by,duplicated_from.name,duplicated_from.resource_subtype,follower,follower.name,hearted,hearts,hearts.user,hearts.user.name,html_text,is_editable,is_edited,is_pinned,liked,likes,likes.user,likes.user.name,new_approval_status,new_date_value,new_dates,new_dates.due_at,new_dates.due_on,new_dates.start_on,new_enum_value,new_enum_value.color,new_enum_value.enabled,new_enum_value.name,new_multi_enum_values,new_multi_enum_values.color,new_multi_enum_values.enabled,new_multi_enum_values.name,new_name,new_number_value,new_people_value,new_people_value.name,new_resource_subtype,new_section,new_section.name,new_text_value,num_hearts,num_likes,old_approval_status,old_date_value,old_dates,old_dates.due_at,old_dates.due_on,old_dates.start_on,old_enum_value,old_enum_value.color,old_enum_value.enabled,old_enum_value.name,old_multi_enum_values,old_multi_enum_values.color,old_multi_enum_values.enabled,old_multi_enum_values.name,old_name,old_number_value,old_people_value,old_people_value.name,old_resource_subtype,old_section,old_section.name,old_text_value,previews,previews.fallback,previews.footer,previews.header,previews.header_link,previews.html_text,previews.text,previews.title,previews.title_link,project,project.name,resource_subtype,source,sticker_name,story,story.created_at,story.created_by,story.created_by.name,story.resource_subtype,story.text,tag,tag.name,target,target.created_by,target.name,target.resource_subtype,task,task.created_by,task.name,task.resource_subtype,text,type",
                }
                api_response = stories_api_instance.create_story_for_task(
                    body, task_gid, opts)
                return api_response
            else:
                raise Exception(
                    "Must specify either text or html_text of comment")
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))


def asana_remove_task_comment(accessToken,params):
    try:
        if "story_gid" in params:
            story_gid = params["story_gid"]
            configuration = asana.Configuration()
            configuration.access_token = accessToken
            api_client = asana.ApiClient(configuration)
            stories_api_instance = asana.StoriesApi(api_client)
            stories_api_instance.delete_story(story_gid)
            return {"message": f"Successfully deleted the specified story."}
        else:
            raise Exception("Missing Input Data")
    except ApiException as e:
        raise Exception(json.loads(e.body))