testmsg = 'somethingsafewthings'
testsub = [['e','3']]


def encodemsg(message, subsututions):
    for s in subsututions:
        old = s[0]
        new = s[1]
        converted = message.replace(old,new)

    return converted
    
convertedtxt = encodemsg(testmsg, testsub)
print(testmsg)
print(convertedtxt)
