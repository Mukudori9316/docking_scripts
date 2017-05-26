cd %~dp0
"C:\Program Files (x86)\MGLTools-1.5.6\python.exe" "C:\Program Files (x86)\MGLTools-1.5.6\Lib\site-packages\AutoDockTools\Utilities24\prepare_gpf4.py" -l ligand.pdbqt -r receptor.pdbqt -i reference.gpf -o grid_parameter.gpf
"C:\Program Files (x86)\MGLTools-1.5.6\python.exe" "C:\Program Files (x86)\MGLTools-1.5.6\Lib\site-packages\AutoDockTools\Utilities24\prepare_dpf4.py" -l ligand.pdbqt -r receptor.pdbqt -o docking_parameter.dpf
