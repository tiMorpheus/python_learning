

def ask_ok(prompt, retries=4, complaint='Yes or no, please'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes', 'yeah'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        if retries < 0:
            raise IOError('go away')
        print(complaint)


print(ask_ok("Do you really want to quit?"))