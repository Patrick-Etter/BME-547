

'''

Database format

[{
'name': <string>,
'id': <integer>,
'blood_type': <string>,
'test_name': <string>,
'test_result': <string>
}]

'''

db = []

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def server_on():
    return 'DB server is on'


def add_patient(patient_name, patient_id, blood_type):
    new_patient = {'name': patient_name,
                   'id': patient_id,
                   'blood_type': blood_type,
                   'test_name': [],
                   'test_results': []}
    db.append(new_patient)


def init_server():
    add_patient('Ann Ables', 1, 'A+')
    add_patient('Bob Boyles', 2, 'B+')
    # initialize logging


@app.route('/new_patient', methods=['POST'])
def add_new_patient_to_server():
    '''
    Receive data from POST request
    Call other functions to do all the work
    Return information
    '''
    in_data = request.get_json()
    message, status_code = add_new_patient_worker(in_data)
    return message, status_code


def add_new_patient_worker(in_data):
    result = validate_new_patient_info(in_data)
    if result is not True:
        return result, 400
    add_patient(in_data['name'],
                in_data['id'],
                in_data['blood_type'])
    return 'Patient successfully added', 200


def validate_new_patient_info(in_data):
    if type(in_data) is not dict:
        return 'POST data was not a dictionary'
    expected_keys = ['name', 'id', 'blood_type']
    for key in expected_keys:
        if key not in in_data:
            return 'Key {} is missing from POST data'.format(key)
    expected_types = [str, int, str]
    for key, ex_type in zip(expected_keys, expected_types):
        if type(in_data[key]) is not ex_type:
            return 'Key {} has the wrong data type'.format(key)
    return True




def add_test_to_patient(patient_id, test_name, test_result):
    for patient in db:
        if patient['id'] == patient_id:
            patient['test_name'].append(test_name)
            patient['test_results'].append(test_result)
            print(patient)



@app.route('/add_test', methods=['POST'])
def add_test_to_server():
    in_data = request.get_json()
    message, status_code = add_test_worker(in_data)
    return message, status_code


def add_test_worker(in_data):
    result = add_test_validate_data(in_data)
    if result is not True:
        return result, 400
    add_test_to_patient(in_data['id'],
                        in_data['test_name'],
                        in_data['test_result'])
    return 'Test successfully added', 200

def add_test_validate_data(in_data):
    if type(in_data) is not dict:
        return 'POST data was not a dictionary'
    expected_keys = ['id', 'test_name', 'test_result']
    for key in expected_keys:
        if key not in in_data:
            return 'Key {} is missing from POST data'.format(key)
    expected_types = [int, str, int]
    for key, ex_type in zip(expected_keys, expected_types):
        if type(in_data[key]) is not ex_type:
            return 'Key {} has the wrong data type'.format(key)
    return True    




if __name__ == '__main__':
    init_server()
    app.run()