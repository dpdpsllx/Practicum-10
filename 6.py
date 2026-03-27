def checkmessage(msg):
    if len(msg) < 160:
        return msg
    else:
        return msg[:160]

'''msg = input()
print(checkmessage(msg))'''
