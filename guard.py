from loguru import logger

def set_logger():
    pass

def guard():
    """
    fork of get_lock()
    v1.0
    purpose:
    avoid cron scripts collisions via multiple executions
    restrictions:
    works with linux OS only, requires right main func content ordering and global var declaration for
    improvements:
    compatibility with macOS
    future:
    transformation into decorator, separate module, packaging
    """
    name = sys.argv[0].split(os.sep)[-1]
    com = "ps aux | grep " + name + " | grep -i python | grep -v 'grep' | grep -v '/bin/sh' | awk -F ' ' '{ print $1 \" \" $2 \" \" $9 }'"
    p = subprocess.Popen([com], stdout=subprocess.PIPE, shell=True)
    res = p.communicate()[0]
    if isinstance(res, bytes):
        res = res.decode("utf-8")
    res2 = [str(x) for x in res.split('\n') if len(x) > 0]
    max_processes = 1
    if len(res2) > max_processes:
        logger.error('finishing redundant process, more than {} processes running: {}'.format(max_processes, pformat(res2)))
        sys.exit()

@logger.catch
def main():
    set_logger()
    guard()
    # main_logic()
