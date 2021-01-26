def path_expander(expanduser_):
    def function_body_receiver(function_body):
        def func_arg_rec(function_arg):
            return function_body(expanduser_(function_arg)) if "~" in function_arg else function_body(function_arg)

        return func_arg_rec

    return function_body_receiver


@path_expander(os.path.expanduser)
def take_input(path):
    cmd = 'grep -r "cluster::realm" {}'.format(path)
    raw = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    p = raw.stdout.readlines()
    n = list(map(lambda s: s.decode().strip().replace(',', '').replace('  ', ' ').replace('"', ''), p))
    delim = ': '
    o = [{'filepath': _.split(delim)[0], 'j_key': _.split(delim)[1], 'realm_old': _.split(delim)[2]} for _ in n]
    return o
