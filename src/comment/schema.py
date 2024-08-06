def commentEntity(comment) -> dict:
    return {
        "id": str(comment["_id"]),
        "content": comment["content"],
        "show_id": str(comment["show_id"]),
        "user_id": str(comment["user_id"]),
        "date_created": comment["date_created"],
        "username": comment["username"],
        "reply_count": comment["reply_count"],
    }