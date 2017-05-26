import os

chd = os.getcwd()
files = os.listdir(chd)

for file in files:
    name = os.path.splitext(file)[0]
    ext = os.path.splitext(file)[1]
    if ext == '.pdb':
        print(file, name, ext)
        cmd1 = "'C:\Program_Files_(x86)\MGLTools-1.5.6\python.exe' 'C:\Program_Files_(x86)\MGLTools-1.5.6\Lib\site-packages\AutoDockTools\Utilities24\prepare_ligand4.py' -l "+file+" -o "+name+".pdbqt"
        os.system(cmd1)
