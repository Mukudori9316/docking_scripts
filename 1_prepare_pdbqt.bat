cd %~dp0
"C:\Program Files (x86)\MGLTools-1.5.6\python.exe" "C:\Program Files (x86)\MGLTools-1.5.6\Lib\site-packages\AutoDockTools\Utilities24\prepare_ligand4.py" -l ligand.pdb -o ligand.pdbqt
"C:\Program Files (x86)\MGLTools-1.5.6\python.exe" "C:\Program Files (x86)\MGLTools-1.5.6\Lib\site-packages\AutoDockTools\Utilities24\prepare_receptor4.py" -r receptor.pdb -o receptor.pdbqt -A 'hydrogens'
