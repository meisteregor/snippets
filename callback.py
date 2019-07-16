# smysl v tom 4tob peredat' func kak arg i osus4estvit' vyzov v tele
file = """hi\nman"""


def foreach(common_arg, callback):
    smth_to_iter = common_arg.split('\n')
    for line in smth_to_iter:
        print(callback(line))


def capitalize(line):
    return line.capitalize()


foreach(file, capitalize)
