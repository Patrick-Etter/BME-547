def interface():
    print('my programs')
    print('options')
    print('1 - analyze HDL')
    print('2 - analyze LDL')
    print('9-quit')
    keep_running = True
    while keep_running:
        choice = input('enter choice: ')
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()
        elif choice == '3':
            cholesterol_driver()            


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

def LDL_input():
    val = input('enter LDL value: ')
    return int(val)    

def check_LDL(LDL_val):
    if LDL_val < 130:
        return 'normal'
    elif LDL_val <= 159:
        return 'borderline high'
    elif LDL_val <= 189:
        return 'high'
    else:
        return 'very high'

def output_LDL_result(LDL_val, characterization):
    print('the results for an LDL value of {} is {}'.format(LDL_val, characterization))

def LDL_driver():
    LDL_val = LDL_input()
    answer = check_LDL(LDL_val)
    output_LDL_result(LDL_val, answer)


def cholesterol_input():
    val = input('enter cholesterol value: ')
    return int(val)

def check_cholesterol(cholesterol_val):
    if cholesterol_val < 200:
        return 'normal'
    elif cholesterol_val <= 239:
        return 'borderline high'
    else:
        return 'high'

def output_cholesterol_result(cholesterol_val, characterization):
    print('the results for an cholesterol value of {} is {}'.format(cholesterol_val, characterization))

def cholesterol_driver():
    cholesterol_val = cholesterol_input()
    answer = check_cholesterol(cholesterol_val)
    output_cholesterol_result(cholesterol_val, answer)    

if __name__ == '__main__':
    interface()