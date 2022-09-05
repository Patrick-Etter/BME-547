def interface():
    print('my programs')
    print('options')
    print('9-quit')
    keep_running = True
    while keep_running:
        choice = input('enter choice: ')
        if choice == '9':
            return


def HDL_input():
    val = input('enter HDL value: ')
    return int(val)

def check_HDL(HDL_val):
    if HDL_val >= 60:
        return 'normal'
    elif 40 <= HDL_val < 60:
        return 'borderline low'
    else:
        return 'low'


interface()