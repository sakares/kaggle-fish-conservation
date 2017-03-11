import subprocess
import time
import os
import re

def findThisProcess( process_name ):
  ps     = subprocess.Popen("ps -eaf | grep "+process_name, shell=True, stdout=subprocess.PIPE)
  output = ps.stdout.read()
  ps.stdout.close()
  ps.wait()

  return output

# This is the function you can use  
def isThisRunning( process_name ):
  output = findThisProcess( process_name )

  if re.search('path/of/process'+process_name, output) is None:
    return False
  else:
    return True



while(True):
  if(isThisRunning('preditct-fish') == False):
    print("Not running")
    bc = 'python predict-fish.py'
    pcs = subprocess.Popen(bc.split(), stdout=subprocess.PIPE)
    output, error = pcs.communicate()
    print(output)
    print('Started TF')

