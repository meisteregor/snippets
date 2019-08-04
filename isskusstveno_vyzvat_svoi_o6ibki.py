class Error(Exception):
    pass


class MyError(Error):
    pass


def head(filename, count):
    output = []
    try:
        with open(filename) as f:
            n = 0
            for substring in f.readlines():
                if n == count:
                    break
                n += 1
                output.append(substring)
    except IOError:
        raise MyError("MyIOE")
    return output


print(head("non_existing_file.txt", 3))