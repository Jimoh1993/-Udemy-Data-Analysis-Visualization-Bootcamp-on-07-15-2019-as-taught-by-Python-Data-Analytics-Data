import numpy as np
arr = np.arange(10)
print arr

np.save('save_array', arr)
#new file is created called "save_array"

new_array = np.load('save_array.npy')
print new_array

#save multiple arrays
array_1 = np.arange(25)
array_2 = np.arange(30)

np.savez('saved_archive.npz', x=array_1, y=array_2)
load_archive = np.load('saved_archive.npz')
print load_archive['x']
print load_archive['y']

#savetext file
np.savetxt('notepadfile.txt', array_1, delimiter=',')

#loading of txt file
load_txt_file = np.loadtxt('notepadfile.txt',  delimiter=',')
print 'load_txt_file is'
print load_txt_file
