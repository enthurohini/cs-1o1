import os

module_name = raw_input("Enter the module name:")
os.makedirs(module_name+'/root')
folder_list = ['asset','app','bin','changelog','config','db','docs','log','lib','public','samples','test','tmp']
file_list = ['.htaccess','version.txt','ti.php','index.php','README.md']
asset_list = ['css','img','js']
app_a_list = ['img','text_files','downloads']
new = 'C:/Python27/'+ module_name + '/root'
os.chdir(new)
print os.getcwd()
for i in folder_list:
         os.mkdir(i)

for i in file_list:
         f = open(i , 'w')

new1 = new+'/asset'
os.chdir(new1)
print os.getcwd()
for i in asset_list:
         os.mkdir(i)

new2 = new+'/app'
os.chdir(new2)
print os.getcwd()
os.mkdir('assets')

new3 = new2+'/assets'
os.chdir(new3)
print os.getcwd()
for i in app_a_list:
         os.mkdir(i)

new4 = new2 + '/folder1'
os.chdir(new4)
print os.getcwd()
os.makedirs('db/assets')
