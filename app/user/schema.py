def userEntity(user) -> dict:
    return{
        "id": str(user["_id"]),
        "email": user["email"],
        "name": user["name"],
    }
    