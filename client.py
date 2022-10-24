

import requests

# r = requests.get('http://127.0.0.1:5000/info')
# print(r.status_code)
# print(r.text)
'''
out_data = {'name': 'Patrick Etter',
            'hdl_value': 15}
r = requests.post('http://127.0.0.1:5000/hdl_check', json=out_data)
print(r.status_code)
print(r.text)
'''
'''
out_data = {'a': 5, 'b': 12}
r = requests.post('http://127.0.0.1:5000/add_numbers', json=out_data)
print(r.status_code)
print(r.text)

'''
r = requests.get('http://127.0.0.1:5000/add/2/7')
print(r.status_code)
print(r.text)