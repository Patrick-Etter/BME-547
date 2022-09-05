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

def HDL_driver():
    HDL_val = HDL_input()
    answer = check_HDL(HDL_val)
    output_HDL_result(HDL_val, answer)


def output_HDL_result(HDL_val, characterization):
    print('the results for an HDL value of {} is {}'.format(HDL_val, characterization))



interface()