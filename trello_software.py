from trello import TrelloClient
from datetime import datetime


def convertDateTime(dateString):
    date_string = dateString
    date_format = "%Y-%m-%dT%H:%M"
    # Convert string to datetime object
    date_time = datetime.strptime(date_string, date_format)
    return date_time

def convertdateToString(date):
    if type(date) == str:
        return date
    date_format = "%Y-%m-%dT%H:%M"
    date_string = date.strftime(date_format)
    return date_string

def createClient(api_key, api_secret, token):
    return TrelloClient(api_key=api_key, api_secret=api_secret, token=token)


############################################# BOARDS #############################################


def jsonify_board(board):
    return {
        "board_id": board.id,
        "board_name": board.name,
        "board_url": board.url,
        "board_description": board.description,
        "board_closed": board.closed,
    }


def trello_create_board(access_token, params):
    try:
        if (
            "board_name" in params
            and params["board_name"] != None
            and params["board_name"] != ""
        ):
            board_name = params["board_name"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            optional_args = {}
            description = None
            if "optional_args" in params:
                optional_args = params["optional_args"]
            if 'description' in optional_args:
                description = optional_args.pop("description")
            board = client.add_board(board_name, **optional_args)
            if description != None and description != "":
                board.set_description(description)
            return jsonify_board(board)
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_get_board(access_token, params):
    try:
        if (
            "board_id" in params
            and params["board_id"] != None
            and params["board_id"] != ""
        ):
            board_id = params["board_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            board = client.get_board(board_id=board_id)
            return jsonify_board(board)
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_delete_board(access_token, params):
    try:
        if (
            "board_id" in params
            and params["board_id"] != None
            and params["board_id"] != ""
        ):
            board_id = params["board_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            board = client.get_board(board_id=board_id)
            board.delete()
            return "Board deleted Successfully"
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_update_board(access_token, params):
    try:
        if (
            "board_id" in params
            and params["board_id"] != None
            and params["board_id"] != ""
        ):
            board_id = params["board_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            board = client.get_board(board_id=board_id)
            if (
                "board_name" in params
                and params["board_name"] != None
                and params["board_name"] != ""
            ):
                board_name = params["board_name"]
                board.set_name(board_name)
            if (
                "description" in params
                and params["description"] != None
                and params["description"] != ""
            ):
                description = params["description"]
                board.set_description(description)
            if (
                "closed" in params
                and params["closed"] != None
                and params["closed"] != ""
            ):
                closed = params["closed"]
                if closed:
                    board.close()
                else:
                    board.open()
            if (
                "organization_id" in params
                and params["organization_id"] != None
                and params["organization_id"] != ""
            ):
                organization_id = params["organization_id"]
                organization = client.get_organization(organization_id=organization_id)
                board.set_organization(organization)
            return jsonify_board(board)
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_get_boards(access_token, params):
    try:
        client = createClient(
            access_token["api_key"],
            access_token["api_secret"],
            access_token["token"],
        )
        boards = client.list_boards()
        boards_list = []
        for board in boards:
            boards_list.append(jsonify_board(board))
        return boards_list
    except Exception as e:
        raise Exception(e)


def trello_close_board(access_token, params):
    try:
        if (
            "board_id" in params
            and params["board_id"] != None
            and params["board_id"] != ""
        ):
            board_id = params["board_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            board = client.get_board(board_id=board_id)
            board.close()
            return "Board closed Successfully"
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_open_board(access_token, params):
    try:
        if (
            "board_id" in params
            and params["board_id"] != None
            and params["board_id"] != ""
        ):
            board_id = params["board_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            board = client.get_board(board_id=board_id)
            board.open()
            return "Board opened Successfully"
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


############################################# LISTS #############################################


def jsonify_list(trello_list):
    return {
        "list_id": trello_list.id,
        "list_name": trello_list.name,
        "list_closed": trello_list.closed,
        "list_pos": trello_list.pos,
    }


def jsonify_card(card):
    return {
        "card_id": card.id,
        "card_name": card.name,
        "card_description": card.description,
        "card_closed": card.closed,
        "card_due_date": convertdateToString(card.due_date),
        "card_url": card.short_url,
        "board_id": card.board_id,
        "list_id": card.list_id,
    }


def trello_create_list(access_token, params):
    try:
        if (
            "board_id" in params
            and params["board_id"] != None
            and params["board_id"] != ""
        ):
            board_id = params["board_id"]
            if (
                "list_name" in params
                and params["list_name"] != None
                and params["list_name"] != ""
            ):
                list_name = params["list_name"]
                client = createClient(
                    access_token["api_key"],
                    access_token["api_secret"],
                    access_token["token"],
                )
                if "pos" in params and params["pos"] != None and params["pos"] != "":
                    pos = params["pos"]
                else:
                    pos = "bottom"
                board = client.get_board(board_id=board_id)
                trello_list = board.add_list(list_name, pos=pos)
                return jsonify_list(trello_list)
            else:
                raise Exception("Missing Input data")
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_get_list(access_token, params):
    try:
        if (
            "list_id" in params
            and params["list_id"] != None
            and params["list_id"] != ""
        ):
            list_id = params["list_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            trello_list = client.get_list(list_id=list_id)
            return jsonify_list(trello_list)
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_get_list_cards(access_token, params):
    try:
        if (
            "list_id" in params
            and params["list_id"] != None
            and params["list_id"] != ""
        ):
            list_id = params["list_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            trello_list = client.get_list(list_id=list_id)
            cards = trello_list.list_cards()
            cards_list = []
            for card in cards:
                cards_list.append(jsonify_card(card))
            return cards_list
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_update_list(access_token, params):
    try:
        if (
            "list_id" in params
            and params["list_id"] != None
            and params["list_id"] != ""
        ):
            list_id = params["list_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            trello_list = client.get_list(list_id=list_id)
            if (
                "list_name" in params
                and params["list_name"] != None
                and params["list_name"] != ""
            ):
                list_name = params["list_name"]
                trello_list.set_name(list_name)
            if (
                "board_id" in params
                and params["board_id"] != None
                and params["board_id"] != ""
            ):
                board_id = params["board_id"]
                board = client.get_board(board_id=board_id)
                trello_list.move_to_board(board)
            if (
                "list_pos" in params
                and params["list_pos"] != None
                and params["list_pos"] != ""
            ):
                list_pos = params["list_pos"]
                trello_list.set_pos(list_pos)
            if (
                "closed" in params
                and params["closed"] != None
                and params["closed"] != ""
            ):
                closed = params["closed"]
                if closed:
                    trello_list.close()
                else:
                    trello_list.open()
            if (
                "subscribe" in params
                and params["subscribe"] != None
                and params["subscribe"] != ""
            ):
                subscribe = params["subscribe"]
                if subscribe:
                    trello_list.subscribe()
                else:
                    trello_list.unsubscribe()

            return jsonify_list(trello_list)
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_get_lists(access_token, params):
    try:
        if (
            "board_id" in params
            and params["board_id"] != None
            and params["board_id"] != ""
        ):
            board_id = params["board_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            board = client.get_board(board_id=board_id)
            lists = board.list_lists()
            lists_list = []
            for trello_list in lists:
                lists_list.append(jsonify_list(trello_list))
            return lists_list
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_archive_list(access_token, params):
    try:
        if (
            "list_id" in params
            and params["list_id"] != None
            and params["list_id"] != ""
        ):
            list_id = params["list_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            trello_list = client.get_list(list_id=list_id)
            trello_list.close()
            return "List archived Successfully"
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_unarchive_list(access_token, params):
    try:
        if (
            "list_id" in params
            and params["list_id"] != None
            and params["list_id"] != ""
        ):
            list_id = params["list_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            trello_list = client.get_list(list_id=list_id)
            trello_list.open()
            return "List unarchived Successfully"
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


############################################# CARDS #############################################


def trello_create_card(access_token, params):
    try:
        if (
            "list_id" in params
            and params["list_id"] != None
            and params["list_id"] != ""
        ):
            list_id = params["list_id"]
            if (
                "card_name" in params
                and params["card_name"] != None
                and params["card_name"] != ""
            ):
                card_name = params["card_name"]
                client = createClient(
                    access_token["api_key"],
                    access_token["api_secret"],
                    access_token["token"],
                )
                optional_args = {}
                description = None
                due_date = None
                if "optional_args" in params:
                    optional_args = params["optional_args"]
                trello_list = client.get_list(list_id=list_id)
                card = trello_list.add_card(card_name)
                if 'description' in optional_args:
                    description = optional_args.pop("description")
                if description != None and description != "":
                    card.set_description(description)
                if 'due_date' in optional_args:
                    due_date = optional_args.pop("due_date")
                if due_date != None and due_date != "":
                    due_date = convertDateTime(due_date)
                    card.set_due(due_date)
                return jsonify_card(card)
            else:
                raise Exception("Missing Input data")
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_get_card(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
        ):
            card_id = params["card_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            return jsonify_card(card)
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_delete_card(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
        ):
            card_id = params["card_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            card.delete()
            return "Card deleted Successfully"
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_archive_card(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
        ):
            card_id = params["card_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            card.set_closed(True)
            return "Card archived Successfully"
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_unarchive_card(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
        ):
            card_id = params["card_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            card.set_closed(False)
            return "Card unarchived Successfully"
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_update_card(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
        ):
            card_id = params["card_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            if (
                "card_name" in params
                and params["card_name"] != None
                and params["card_name"] != ""
            ):
                card_name = params["card_name"]
                card.set_name(card_name)
            if (
                "description" in params
                and params["description"] != None
                and params["description"] != ""
            ):
                description = params["description"]
                card.set_description(description)
            if (
                "card_pos" in params
                and params["card_pos"] != None
                and params["card_pos"] != ""
            ):
                card_pos = params["card_pos"]
                card.set_pos(card_pos)
            if (
                "due_date" in params
                and params["due_date"] != None
                and params["due_date"] != ""
            ):
                due_date = params["due_date"]
                due_date = convertDateTime(due_date)
                card.set_due(due_date)
            if (
                "closed" in params
                and params["closed"] != None
                and params["closed"] != ""
            ):
                closed = params["closed"]
                if closed:
                    card.set_closed(True)
                else:
                    card.set_closed(False)
            if (
                "subscribe" in params
                and params["subscribe"] != None
                and params["subscribe"] != ""
            ):
                subscribe = params["subscribe"]
                if subscribe:
                    card.subscribe()
            return jsonify_card(card)
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_assign_member_to_card(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
            and "member_id" in params
            and params["member_id"] != None
            and params["member_id"] != ""
        ):
            card_id = params["card_id"]
            member_id = params["member_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id)
            card.assign(member_id)
            return "Member assigned Successfully"
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


############################################# CARDS COMMENTS #############################################


def trello_create_card_comment(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
        ):
            card_id = params["card_id"]
            if (
                "comment" in params
                and params["comment"] != None
                and params["comment"] != ""
            ):
                comment = params["comment"]
                client = createClient(
                    access_token["api_key"],
                    access_token["api_secret"],
                    access_token["token"],
                )
                card = client.get_card(card_id=card_id)
                comment = card.comment(comment)
                return comment
            else:
                raise Exception("Missing Input data")
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_delete_comment(access_token, params):
    try:
        if (
            "comment_id" in params
            and params["comment_id"] != None
            and params["comment_id"] != ""
            and "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
        ):
            card_id = params["card_id"]
            comment_id = params["comment_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            
            card = client.get_card(card_id)
            comments = card.get_comments()
            comment_to_delete = None
            for comment in comments:
                if comment["id"] == comment_id:
                    comment_to_delete = comment
                    break
            if comment_to_delete:
                card.delete_comment(comment_to_delete)
                return "Comment deleted Successfully"
            else:
                raise Exception("Comment not found")
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_update_card_comment(access_token, params):
    try:
        if (
            "comment_id" in params
            and params["comment_id"] != None
            and params["comment_id"] != ""
            and "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
        ):
            card_id = params["card_id"]
            comment_id = params["comment_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            if (
                "comment_text" in params
                and params["comment_text"] != None
                and params["comment_text"] != ""
            ):
                comment_text = params["comment_text"]
                card = client.get_card(card_id)
                card.update_comment(comment_id, comment_text)
                return "Comment updated Successfully"
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


############################################# CARDS ATTACHMENTS #############################################


def jsonify_attachment(attachment):
    return {
        "attachment_id": attachment.id,
        "attachment_name": attachment.name,
        "attachment_url": attachment.url,
        "attachment_date": attachment.date,
        "attachment_mimetype": attachment.mimetype,
        "attachment_date": attachment.date,
        "attachment_mimeType": attachment.mimetype,
        "attachment_member_id": attachment.member_id,
    }


def trello_create_card_attachment(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
        ):
            card_id = params["card_id"]
            if (
                "attachment" in params
                and params["attachment"] != None
                and params["attachment"] != ""
            ):
                attachment = params["attachment"]
                client = createClient(
                    access_token["api_key"],
                    access_token["api_secret"],
                    access_token["token"],
                )
                card = client.get_card(card_id=card_id)
                attachment_toReturn = None
                if attachment["type"] == "url":
                    attachment_toReturn = card.attach(url=attachment["value"], name=attachment["name"])
                elif attachment["type"] == "file":
                    attachment_toReturn = card.attach(file=attachment["value"], name=attachment["name"])
                if attachment_toReturn:
                    return attachment_toReturn
            else:
                raise Exception("Missing Input data")
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_get_card_attachments(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
        ):
            card_id = params["card_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            attachments = card.attachments
            return attachments
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_get_card_attachment(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
            and "attachment_id" in params
            and params["attachment_id"] != None
            and params["attachment_id"] != ""
        ):
            card_id = params["card_id"]
            attachment_id = params["attachment_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            attachments = card.attachments
            attachment_to_return = None
            for attachment in attachments:
                if attachment["id"] == attachment_id:
                    attachment_to_return = attachment
                    break
            if attachment_to_return:
                return attachment_to_return
            else:
                raise Exception("Attachment not found")
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_delete_card_attachment(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
            and "attachment_id" in params
            and params["attachment_id"] != None
            and params["attachment_id"] != ""
        ):
            card_id = params["card_id"]
            attachment_id = params["attachment_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            card.remove_attachment(attachment_id=attachment_id)
            return "Attachment deleted Successfully"
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


############################################# CARDS CHECKLISTS #############################################


def jsonify_checklist(checklist):
    return {
        "checklist_id": checklist.id,
        "checklist_name": checklist.name,
        "checklist_items": checklist.items,
        "checklist_card_id": checklist.trello_card,
    }


def trello_create_checklist(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
        ):
            card_id = params["card_id"]
            if (
                "checklist_name" in params
                and params["checklist_name"] != None
                and params["checklist_name"] != ""
                and "checklist_items" in params
                and params["checklist_items"] != None
                and params["checklist_items"] != ""
            ):
                checklist_name = params["checklist_name"]
                checklist_items = params["checklist_items"]
                client = createClient(
                    access_token["api_key"],
                    access_token["api_secret"],
                    access_token["token"],
                )
                card = client.get_card(card_id=card_id)
                checklist = card.add_checklist(checklist_name, checklist_items)
                return jsonify_checklist(checklist)
            else:
                raise Exception("Missing Input data")
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_delete_card_checklist(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
            and "checklist_id" in params
            and params["checklist_id"] != None
            and params["checklist_id"] != ""
        ):
            card_id = params["card_id"]
            checklist_id = params["checklist_id"]
            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            checklists = card.checklists
            for checklist in checklists:
                if checklist.id == checklist_id:
                    checklist_to_delete = checklist
                    break
            checklist_to_delete.delete()
            return "Checklist deleted Successfully"
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_delete_checklist_items(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
            and "checklist_id" in params
            and params["checklist_id"] != None
            and params["checklist_id"] != ""
        ):
            card_id = params["card_id"]
            checklist_id = params["checklist_id"]

            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            checklists = card.checklists

            for checklist in checklists:
                if checklist.id == checklist_id:
                    checklist_to_update = checklist
                    break

            while len(checklist_to_update.items) > 0:
                checklist_to_update.delete_checklist_item(checklist_to_update.items[0])
            return jsonify_checklist(checklist_to_update)
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_get_card_checklists(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
        ):
            card_id = params["card_id"]

            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            checklists = card.checklists
            checklists_list = []
            for checklist in checklists:
                checklists_list.append(jsonify_checklist(checklist))
            return checklists_list
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_get_card_checklist(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
            and "checklist_id" in params
            and params["checklist_id"] != None
            and params["checklist_id"] != ""
        ):
            card_id = params["card_id"]
            checklist_id = params["checklist_id"]

            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            checklists = card.checklists
            checklist_to_return = None
            for checklist in checklists:
                if checklist.id == checklist_id:
                    checklist_to_return = checklist
                    break
            if checklist_to_return:
                return jsonify_checklist(checklist_to_return)
            else:
                raise Exception("Checklist not found")
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)


def trello_get_checklist_items(access_token, params):
    try:
        if (
            "card_id" in params
            and params["card_id"] != None
            and params["card_id"] != ""
            and "checklist_id" in params
            and params["checklist_id"] != None
            and params["checklist_id"] != ""
        ):
            card_id = params["card_id"]
            checklist_id = params["checklist_id"]

            client = createClient(
                access_token["api_key"],
                access_token["api_secret"],
                access_token["token"],
            )
            card = client.get_card(card_id=card_id)
            checklists = card.checklists
            checklist_to_return = None
            for checklist in checklists:
                if checklist.id == checklist_id:
                    checklist_to_return = checklist
                    break
            if checklist_to_return:
                return checklist_to_return.items
            else:
                raise Exception("Checklist not found")
        else:
            raise Exception("Missing Input data")
    except Exception as e:
        raise Exception(e)