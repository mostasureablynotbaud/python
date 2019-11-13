


testsubs = [['e', '3']]




def encodemsg(message,subsututions):
    for s in subsututions:
        old = s[0]
        new = s[1]
        converted = message.replace(old,new)
    return converted


message = input('Encode your message:')
convertedtxt = encodemsg(message, testsubs)
print(message)
print(convertedtxt)
