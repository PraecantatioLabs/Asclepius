import subprocess
from os import listdir

# echo_cmd = ['echo', 'this', 'comes', 'from', 'echo']
# proc = subprocess.Popen(echo_cmd, stdout=subprocess.PIPE)
# output = proc.communicate()[0]
# print('Got stdout:', output)

print(listdir('./hospitals'))
for hospital in listdir('./hospitals'):
    command = ['python', './hospitals/' + hospital]
    hospital = hospital[:-2] + 'txt'
    with open('./hospitals/' + hospital, 'wb+') as w:
        proc = subprocess.Popen(command, stdout=w)
        proc.communicate()
        # print('Got stdout:', output)
        

