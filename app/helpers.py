def sanitize(username, fullname, password):
    u = username[0]
    f = fullname[0]
    p = password[0]

    if (u is '') or (f is '') or (p is ''):
        return False
