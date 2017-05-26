import os

chd = os.getcwd()
files = os.listdir(chd)

for file in files:
    name = os.path.splitext(file)[0]
    ext = os.path.splitext(file)[1]
    if ext == '.sdf':
        print(file, name, ext)
        cmd1 = "balloon -H --nconfs 1 --noGA --chargemodel SFKEEM -f C:\\Balloon\\MMFF94.mff --input-file "+str(file)+" -o mol2 "+name+".mol2"
        os.system(cmd1)
