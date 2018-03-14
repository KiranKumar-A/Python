import pdb

print('Statement 1')
for i in range(5):
    print('Statement ' + str(i+2))

pdb.set_trace()
print('Statement 7')
pdb.pm()
