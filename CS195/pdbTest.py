#test code for switching c++ atomVel file to python 
import math
import random

N = 100
k = 1.3806488E-23 #m^2 kg s^-2 K^-1
temp = 298 #kelvin
pi = 3.14159
avgVelocity = 0
velocity = [N]
velX = [N]
velY = [N]
velZ = [N]
x = [N]
y = [N]
z = [N]
theta = [N]
phi = [N]
atomIndexL = 0
velIndex = 0
width = 0
mostProbVel = 0
atomIndex=0


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


                    #add code for calculating velX, velY, velZ
                    avgVelocity = (math.sqrt(2*k*temp/mass))*(2/(math.sqrt(pi)))

                    mostProbVel = math.sqrt(2*k*temp/mass)
                    velIndex = mostProbVel


                    #for (atomIndexL=0; atomIndexL < N; atomIndexL++):
                    for i in range(N):
                
                        if velIndex >= 0.0000:
  
                            width = 1/((math.sqrt((mass/(2*pi*k*temp))*(mass/(2*pi*k*temp))*(mass/(2*pi*k*temp))))*(4*pi*(velIndex*velIndex))*(math.exp(-(mass*(velIndex*velIndex))/(2*k*temp)))*N)



                            #convert this to python language
                            #check if RAND_MAX is ok in python -- ask urness
                            #2147483647 is the highest rand number
                            #replaced RAND_MAX with random.randint(0,2147483647) b/c that num is highest rand num in GNU lib
                            x.append((long)(random.random()) / (long)(random.randint(0,2147483647)/500))
                            y.append((long)(random.random()) / (long)(random.randint(0,2147483647)/500))
                            z.append((long)(random.random()) / (long)(random.randint(0,2147483647)/500))
                            theta.append((long)(random.random()) / (long)(random.randint(0,2147483647)/(math.pi)))
                            phi.append((long)(random.random()) / (long)(random.randint(0,2147483647)/(2*math.pi)))


                            #Randomize Velocity within intvel, convert to cartesian coordinates

                            velocity.append(velIndex - (long)(random.random()) / (long)(random.randint(0,2147483647)/width))
                            velX.append((velocity[atomIndex]*math.sin(theta[atomIndex])*math.cos(phi[atomIndex])))
                            velY.append((velocity[atomIndex]*math.sin(theta[atomIndex])*math.sin(phi[atomIndex])))
                            velZ.append((velocity[atomIndex]*math.cos(theta[atomIndex])))

                            velIndex=velIndex-width

                            #Update index
                            atomIndex = atomIndex + 1

                        velIndex = mostProbVel

                    #creates remaining atoms to the right of the most probable velocity
                    #for (; atomIndex<N; atomIndex++):
                    for i in range(N):

                        #if velIndex >= 0.00000:
                          #  width = 1/((math.sqrt((mass/(2*pi*k*temp))*(mass/(2*pi*k*temp))*(mass/(2*pi*k*temp))))*(4*pi*(velIndex*velIndex))*(math.exp(-(mass*(velIndex*velIndex))/(2*k*temp)))*N)
                          

                        x.append((long)(random.random()) / (long)(random.randint(0,2147483647)/500))
                        y.append((long)(random.random()) / (long)(random.randint(0,2147483647)/500))
                        z.append((long)(random.random()) / (long)(random.randint(0,2147483647)/500))
                        theta.append((long)(random.random()) / (long)(random.randint(0,2147483647)/(math.pi)))
                        phi.append((long)(random.random()) / (long)(random.randint(0,2147483647)/(2*math.pi)))


                        #Randomize Velocity within intvel, convert to cartesian coordinates

                        velocity.append(velIndex - (long)(random.random()) / (long)(random.randint(0,2147483647)/width))
                        velX.append((velocity[atomIndex]*math.sin(theta[atomIndex])*math.cos(phi[atomIndex])))
                        velY.append((velocity[atomIndex]*math.sin(theta[atomIndex])*math.sin(phi[atomIndex])))
                        velZ.append((velocity[atomIndex]*math.cos(theta[atomIndex])))

                        velIndex=velIndex+width



                    #output a random velocity for x, y, z
                    outputVelX = velX[random.randint(0,N)] 
                    outputVelY = velY[random.randint(0,N)]
                    outputVelZ = velZ[random.randint(0,N)]

                    print outputVelX
                    print outputVelY
                    print outputVelZ
















