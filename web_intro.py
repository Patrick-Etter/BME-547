import requests
'''
r = requests.get('https://api.github.com/repos/dward2/BME547/branches')
print(r)
print(type(r))
# print(r.text)

if r.status_code == 200:
    answer = r.json()
    print(type(answer))

    for branch in answer:
        print(branch['name'])
'''
'''
output_info = {'name': 'Patrick Etter',
               'net_id': 'pe43',
               'e-mail': 'patrick.etter@duke.edu'}

r = requests.post('http://vcm-21170.vm.duke.edu:5000/student',
                  json=output_info)
print(r)
print(r.text)

r = requests.get('http://vcm-21170.vm.duke.edu:5000/list')
print(r.text)
'''

my_message = {"user": 'chase', "message": 'hello'}
r = requests.post('http://vcm-21170.vm.duke.edu:5001/add_message',
                  json=my_message)

r = requests.get('http://vcm-21170.vm.duke.edu:5001/get_messages/patrick')
print(r.text)