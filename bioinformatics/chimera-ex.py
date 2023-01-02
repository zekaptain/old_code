template = chimera.openModels.open('121P.pdb')

for r in template[0].residues:
    if r.id.chainId == 'A':
        print r.type, r.id
