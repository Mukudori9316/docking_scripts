#!/usr/bin/env python
import os
from pypdb import get_pdb_file

print(os.getcwd())
def md4vina(
    dirname,
    pdb_id,
    ):
    os.chdir("c:/AutoDock/Projects")
    os.mkdir("./"+dirname)
    os.chdir("./"+dirname)
    cd = os.getcwd()
    config_txt = open(cd+'\\conf.txt', "w", encoding="utf-8")
    arg = "receptor = \nligand = \nout = \ncenter_x = \ncenter_y = \ncenter_z = \nsize_x = \nsize_y = \nsize_z = \nexaustiveness = 16\n"
    config_txt.write(arg)
    config_txt.close()
    pdb_pdb = open(cd+'\\{}.pdb'.format(pdb_id), "w", encoding="utf-8")
    pfile = get_pdb_file(pdb_id, filetype='pdb', compression=False)
    pdb_pdb.write(pfile)
    pdb_pdb.close()
    bat_file = open(cd+'\\Dock.bat', "w", encoding="utf-8")
    command = "something"
    bat_file.write(command)
    bat_file.close()
    return

dname = input(u"プロジェクト名を入力して下さい：")
pdbid = input(u"PDB idを入力して下さい：")
md4vina(dname, pdbid)
