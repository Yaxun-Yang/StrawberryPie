def authorization_token(user_list, token):
    for u in user_list:
        if token == u.token:
            return u
    return None
