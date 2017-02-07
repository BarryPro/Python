# -*- coding:utf-8 -*-

import dbm

# Open existing file.
db = dbm.open('websites','w')#打开持久文件

# Add another item.
db['www.wrox.com'] = 'Wrox home page'

# Verify the previous item remains.
if db['www.python.org'] != None:
    print('Found www.python.org')
else:
    print('Error: Missing item')

# Iterate over the keys. May be slow.
# May use a lot of memory
for key in db.keys():
    print('Key =',key,'value=',db[key])

del db['www.wrox.com']
print("After deleting www.wrox.com,we have:")

for key in db.keys():
    print('key=',key,'value=',db[key])

# Close and save to disk
db.close()
