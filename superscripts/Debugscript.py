import os
import subprocess
print('Name of script')
name=input('')

try:
    os.popen(name+'.py').read()
    print('next')
    subprocess.check_output(['python', name+'.py']) 
except Exception as ex:
    print(ex)
    input('')
