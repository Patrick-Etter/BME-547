

def create_patient_entry(patient_first_name, patient_last_name, patient_id, patient_age):

    new_patient = {'First Name':patient_first_name, 'Last Name':patient_last_name, 'ID':patient_id, 'Age':patient_age, 'Tests':[]}

    return new_patient


def get_full_name(patient):
    return patient['First Name'] + ' ' + patient['Last Name']


def database_lister(database_list):
    
    for patient in database_list.values():
        print('Name: {}  ID No.: {}  Age: {}'.format(get_full_name(patient), patient['ID'], patient['Age']))


def ID_patient_matcher(database_list, ID):
  
    try:
        matching_patient = database_list[ID]
    except:
        matching_patient = 'No patient found'
    return matching_patient


def test_result_adder(database_list, ID_no, test_name, test_value):

    patient = ID_patient_matcher(database_list, ID_no)
    patient['Tests'].append( (test_name, test_value) )

    
def adult_or_minor(patient):
    if patient['Age'] >= 18:
        return 'adult'
    else:
        return 'minor'


def main():
    db = {}
    db[1] = create_patient_entry("Ann", "Ables", 1, 30)
    db[2] = create_patient_entry('Bob', 'Boyles', 2, 24)
    db[3] = create_patient_entry('Chris', 'Chou', 3, 25)
    test_result_adder(db, 3, 'HDL', 100)
    database_lister(db)
    print(ID_patient_matcher(db, 3))
    # print('Patient {} is a {}'.format(get_full_name(db[2]), adult_or_minor(db[2])))


if __name__ == '__main__':
    main()


