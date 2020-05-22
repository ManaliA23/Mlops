programfile = open('/root/mlops/Mlops/cnnmodel.py','r')
code = programfile.read()

if 'keras' or 'tensorflow' in code :
  if 'Conv2D' or 'Convolution' in code:
  print('kerasCNN')
  else:
  print('not kerasCNN')
else:
print('not deep learning')
    
