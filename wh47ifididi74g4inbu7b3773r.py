subs = [['a','4'], ['e','3'], ['l','1'], ['o','0'], ['t','7']]


def msg_encoder(message, subsitutions):
    for s in subsitutions:
        old = s[0]
        new = s[1]
        message = message.replace(old, new)
        print('converted text ='+message)
    print('Leaving msg_encoder')

    return message

message = input('Encode your message: ')
converted_txt = msg_encoder(message, subs)
print('Your message was this :'+message)
print('Encoded into :'+converted_txt)
