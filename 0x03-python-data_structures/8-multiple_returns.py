#!/usr/bin/python3
def multiple_returns(sentence):
    sent_length = len(sentence)

    if (sent_length == 0):
        nw_tuple = (sent_length, None)
    else:
        nw_tuple = (sent_length, sentence[0])

    return (nw_tuple)
