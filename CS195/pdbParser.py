
outfile = open("dumb.txt","w")



outfile.write("20\n")
outfile.write("TRP_CAGE\n")

for line in open('1L2Y.pdb'):
    list = line.split()
    id = list[0]

    if id == "ENDMDL":
        break

    if id == 'ATOM':
        type = list[2]
        if type == 'CA':
            
            residue = list[3]
            type_of_chain = list[4]
            atom_count = int(list[5])
            position = list[6:9]

            if atom_count >= 0:
               
                if True: #type_of_chain not in visited:
                    #masses are in kilograms
                    if residue == 'ALA':
                        mass = 1.18026E-25

                    if residue == 'ARG':
                        mass = 2.59349E-25

                    if residue == 'ASN':
                        mass = 1.89469E-25

                    if residue == 'ASP':
                        mass = 1.91105E-25

                    if residue == 'CYS':
                        mass = 1.71262E-25

                    if residue == 'GLU':
                        mass = 2.14396E-25

                    if residue == 'GLN':
                        mass = 2.12761E-25

                    if residue == 'GLY':
                        mass = 9.47347E-26

                    if residue == 'HIS':
                        mass = 2.27723E-25

                    if residue == 'ILE':
                        mass = 1.87901E-25

                    if residue == 'LEU':
                        mass = 1.87901E-25

                    if residue == 'LYS':
                        mass = 2.12833E-25

                    if residue == 'MET':
                        mass = 2.17845E-25

                    if residue == 'PHE':
                        mass = 2.44387E-25

                    if residue == 'PRO':
                        mass = 1.61262E-25

                    if residue == 'SER':
                        mass = 1.44593E-25

                    if residue == 'THR':
                        mass = 1.67885E-25

                    if residue == 'TRP':
                        mass = 3.09207E-25

                    if residue == 'TYR':
                        mass = 2.70954E-25

                    if residue == 'VAL':
                        mass = 1.6461E-25


                    #print residue,mass,' '.join(position)
                    outfile.write(residue)
                    outfile.write("\t")
                    outfile.write(str(mass))
                    outfile.write("\t")
                    outfile.write('\t'.join(position))
                    outfile.write("\n")
















