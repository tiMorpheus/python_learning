

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print()



parrot(1000)
parrot(action='VOOOOOM', voltage=1000000)
#parrot('a thousand', state='pushing up the daisies')
#parrot('a million', 'bereft of life', 'jump')