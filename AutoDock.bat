cd %~dp0
balloon -H --nconfs 1 --noGA --chargemodel SFKEEM -f D:\Balloon\MMFF94.mff --input-file ligand.sdf -o mol2 ligand.mol2
obabel -imol2 ligand.mol2 -omop -O ligand.mop -xk "PM7 XYZ MMOK EPS=78.3 NSPA=162"
mopac2016.exe ligand.mop
obabel -iout ligand.out -opdbqt -O ligand.pdbqt
vina.exe --config conf.txt --out out.pdbqt --log log.txt
