from github import Github


def login_token(access_token):
    github_service = Github(access_token)
    return github_service


def handle_auth(credentials):
    if "access_token" in credentials:
        github_service = login_token(access_token=credentials["access_token"])
    else:
        raise Exception("Invalid Credentials")
    return github_service


def convertdateToString(date):
    if type(date) == str:
        return date
    date_format = "%Y-%m-%dT%H:%M"
    date_string = date.strftime(date_format)
    return date_string


def jsonify_repo(repo):
    return {
        "id": repo.id,
        "name": repo.name,
        "full_name": repo.full_name,
        "owner": repo.owner.login,
        "description": repo.description,
        "private": repo.private,
        "size": repo.size,
        "url": repo.url,
        "html_url": repo.html_url,
        "created_at": convertdateToString(repo.created_at),
        "updated_at": convertdateToString(repo.updated_at),
        "pushed_at": convertdateToString(repo.pushed_at),
    }


def jsonify_isssue(issue):
    return {
        "id": issue.id,
        "title": issue.title,
        "body": issue.body,
        "locked": issue.locked,
        "url": issue.url,
        "html_url": issue.html_url,
        "created_at": convertdateToString(issue.created_at),
        "updated_at": convertdateToString(issue.updated_at),
        "number": issue.number,
    }


def jsonify_release(release):
    return {
        "id": release.id,
        "tag_name": release.tag_name,
        "name": release.title,
        "body": release.body,
        "url": release.url,
        "html_url": release.html_url,
        "created_at": convertdateToString(release.created_at),
    }


def jsonify_file(file):
    return {
        "name": file.name,
        "path": file.path,
        "sha": file.sha,
        "url": file.url,
        "html_url": file.html_url,
        "type": file.type,
        "content": file.content,
        "encoding": file.encoding,
        "size": file.size,
        "decoded_content": file.decoded_content.decode("utf-8"),
    }



def github_get_user_repos(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "username" in params
            and params["username"] is not None
            and params["username"] != ""
        ):
            user = github_service.get_user(params["username"])
            repos = user.get_repos()
            return [jsonify_repo(repo) for repo in repos]
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


# def github_get_top_referrers(credentials, params):
#     try:
#         github_service = handle_auth(credentials)
#         if "owner" in params and params["owner"] is not None and params["owner"] != "" and 'repo_name' in params and params["repo_name"] is not None and params["repo_name"] != "":
#             owner = github_service.get_user(params["owner"])
#             repo = owner.get_repo(params["repo_name"])
#             referrers = repo.get_top_referrers()
#             return [referrer for referrer in referrers]
#         else:
#             raise Exception("Missing input data")
#     except Exception as e:
#         raise Exception(e)


def github_get_repo_license(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            license = repo.get_license()
            return license.__dict__
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_get_repo_issues(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            issues = repo.get_issues()
            return [jsonify_isssue(issue=issue) for issue in issues]
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_get_repo(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            return jsonify_repo(repo)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_create_repo_release(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
            and "tag_name" in params
            and params["tag_name"] is not None
            and params["tag_name"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            args = {}
            if (
                "additionals" in params
                and params["additionals"] is not None
                and params["additionals"] != {}
            ):
                args = params["additionals"]
            release = repo.create_git_release(tag=params["tag_name"], **args)
            return jsonify_release(release)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_get_repo_releases(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            releases = repo.get_releases()
            return [jsonify_release(release=release) for release in releases]
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_get_release(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
            and "tag_name" in params
            and params["tag_name"] is not None
            and params["tag_name"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            release = repo.get_release(params["tag_name"])
            return jsonify_release(release)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_update_release(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
            and "tag_name" in params
            and params["tag_name"] is not None
            and params["tag_name"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            release = repo.get_release(params["tag_name"])
            args = {}
            if (
                "additionals" in params
                and params["additionals"] is not None
                and params["additionals"] != {}
            ):
                args = params["additionals"]
            release = release.update_release(**args)
            return jsonify_release(release)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def gihtub_delete_release(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
            and "tag_name" in params
            and params["tag_name"] is not None
            and params["tag_name"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            release = repo.get_release(params["tag_name"])
            release.delete_release()
            return "Release deleted successfully"
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_get_organization_repos(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "organization" in params
            and params["organization"] is not None
            and params["organization"] != ""
        ):
            organization = github_service.get_organization(params["organization"])
            repos = organization.get_repos()
            return [jsonify_repo(repo) for repo in repos]
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_create_issue(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
            and "title" in params
            and params["title"] is not None
            and params["title"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            title = params["title"]
            args = {}
            if (
                "additionals" in params
                and params["additionals"] is not None
                and params["additionals"] != {}
            ):
                args = params["additionals"]
            issue = repo.create_issue(title=title, **args)
            return jsonify_isssue(issue)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_get_issue(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
            and "issue_number" in params
            and params["issue_number"] is not None
            and params["issue_number"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            issue = repo.get_issue(params["issue_number"])
            return jsonify_isssue(issue)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_create_issue_comment(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
            and "issue_number" in params
            and params["issue_number"] is not None
            and params["issue_number"] != ""
            and "body" in params
            and params["body"] is not None
            and params["body"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            issue = repo.get_issue(params["issue_number"])
            comment = issue.create_comment(params["body"])
            return jsonify_isssue(issue)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_edit_issue(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
            and "issue_number" in params
            and params["issue_number"] is not None
            and params["issue_number"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            issue = repo.get_issue(params["issue_number"])
            args = {}
            if (
                "additionals" in params
                and params["additionals"] is not None
                and params["additionals"] != {}
            ):
                args = params["additionals"]
            issue.edit(**args)
            return jsonify_isssue(issue)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_list_file(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "path" in params
            and params["path"] is not None
            and params["path"] != ""
            and "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            content = repo.get_contents(params["path"])
            return jsonify_file(content)
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_create_file(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "path" in params
            and params["path"] is not None
            and params["path"] != ""
            and "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
            and "message" in params
            and params["message"] is not None
            and params["message"] != ""
            and "content" in params
            and params["content"] is not None
            and params["content"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            content = repo.create_file(
                params["path"], params["message"], params["content"]
            )
            return jsonify_file(content["content"])
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_delete_file(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "path" in params
            and params["path"] is not None
            and params["path"] != ""
            and "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
            and "message" in params
            and params["message"] is not None
            and params["message"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            content = repo.get_contents(params["path"])
            repo.delete_file(params["path"], params["message"], content.sha)
            return "File deleted successfully"
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)


def github_edit_file(credentials, params):
    try:
        github_service = handle_auth(credentials)
        if (
            "path" in params
            and params["path"] is not None
            and params["path"] != ""
            and "owner" in params
            and params["owner"] is not None
            and params["owner"] != ""
            and "repo_name" in params
            and params["repo_name"] is not None
            and params["repo_name"] != ""
            and "message" in params
            and params["message"] is not None
            and params["message"] != ""
            and "content" in params
            and params["content"] is not None
            and params["content"] != ""
        ):
            owner = github_service.get_user(params["owner"])
            repo = owner.get_repo(params["repo_name"])
            content = repo.get_contents(params["path"])
            repo.update_file(
                params["path"], params["message"], params["content"], content.sha
            )
            return "File updated successfully"
        else:
            raise Exception("Missing input data")
    except Exception as e:
        raise Exception(e)
