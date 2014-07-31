import os

module_name = raw_input("Enter the module name:")
os.mkdir(module_name)
folder_list = ['asset','app','bin','changelog','config','db','docs','log','lib','public','samples','test','tmp']
file_list = ['.htaccess','version.txt','ti.php','index.php','README.md']
asset_list = ['css','img','js','other_file']
app_list = ['assets','folder_1','folder_2','folder_n']
app_a_list = ['img','text_files','downloads']
folder_file = ['config.php','folder_1.php','other_files']
folder = ['folder_1','folder_2','folder_n']

#new = module_name + '/root'
#os.chdir(new)
for i in folder_list:
         os.mkdir(module_name+'/'+i)

for i in file_list:
         f = open(i , 'w')

#new1 = new+'/'+'asset'
#os.chdir(new1)
for i in asset_list:
         os.mkdir(module_name+'/asset/'+i)

#new2 = new+'/'+'app'
#os.chdir(new2)
for i in app_list:
    os.mkdir(module_name+'/app/'+i)


#new3 = new2+'/assets'
#os.chdir(new3)
for i in app_a_list:
         os.mkdir(module_name+'/app/assets/'+i)

for i in folder:
    #new_path = new2 + '/' +i
    #os.chdir(new_path)
    os.mkdir(module_name+'/app/'+i+'/db')
    os.mkdir(module_name+'/app/'+i+'/assets')
    for n in folder_file:
        f = open(module_name+'/app/'+i+'/'+n , 'w')
    #new_path1 = new_path + '/db'
    #os.chdir(new_path1)
    f = open(module_name+'/app/'+i+'/db/access.php' , 'w')
    #new_path2 ='module_name/app/'+i+'assets/assets'
    #os.chdir(new_path2)
    for n in app_a_list:
         os.mkdir(module_name+'/app/'+i+'/assets/'+n)
print 'successfully, directory structure is formed'

