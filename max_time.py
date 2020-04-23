#!/usr/bin/python3


def max_time(time):
    time = time.replace(':', '')
    output = ""
    if time[0] == "?":
        if time[1] == "?" or int(time[1]) > 3:
            output += "2"
        else:
            output += "1"
    if time[1] == "?":
        if output[0] == "2":
            output += "3"
        else:
            output += "9"
    if time[2] == "?":

        output += "5"
    else:
        output += time[2]
    if time[3] == "?":
        output += "9"
    else:
        output += time[3]

    return output[0:2] + ":" + output[2:]


print(max_time("??:4?"))
