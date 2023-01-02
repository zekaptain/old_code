//includes creating atoms with mass and temperature using probability function
//based on velocity intervals ranging 3 standard deviations with random angles
//converts spherical coordinates to cartesian coordinates for intial velocities

//Paige Diamond, Zeke Elkins, Shannon White, Kayla Huff, Tim Webber
// 10-30-2014

#include <cmath>
#include <math.h>
#include <iostream>
#include <stdlib.h>
#include <cstdlib> // needed for rand
#include <ctime>//neded for srand(time(0))
#include <fstream> //needed for files
#include <vector>
#include <cfloat>
#include <string>

#define N 50

using namespace std;

double massArray[20];

int main() {

  int numAminos;
  double massR;
  string throwingS;
  float throwingF;
  ifstream inFile;
  inFile.open("dumb.txt");

  ofstream outFile;
  outFile.open("testVel.txt");

  inFile >> numAminos;
  inFile >> throwingS;

  for (int i =0; i<numAminos; i++) {

    inFile >> throwingS;
    inFile >> massR;
    inFile >> throwingF;
    inFile >> throwingF;
    inFile >> throwingF;

    cout << massR << endl;

    massArray[i] = massR;

  }

  for (int q=0; q<numAminos; q++) {
    //double mass = 6.63352088E-27; //mass in kg for one atom (ARGON)
    double mass = massArray[q]; // mass of aminos
    float k = 1.3806488E-23; //m^2 kg s^-2 K^-1
    double temp = 298; //kelvin
    double pi = 3.14159;
    double avgVelocity = 0;
    double velocity[N],velX[N],velY[N],velZ[N],x[N],y[N],z[N],theta[N],phi[N];
    int atomIndexL = 0;
    double velIndex = 0;
    double width = 0;
    double mostProbVel = 0;
    int atomIndex=0;

   
    //Set range for possible values (0-2*average or +-3 standard deviations)

    avgVelocity = (sqrt(2*k*temp/mass))*(2/(sqrt(pi)));

    //cout<<"Average velocity" << avgVelocity<< endl;


    mostProbVel = sqrt (2*k*temp/mass);
    velIndex = mostProbVel;
    //most probable velocity is different than average velocity because the distribution is skewed. 
    //We want to start at the "top of the hill" so we always overestimate the boxes and don't 	  
    //run into rounding errors             


    /*for(atomIndex = 0; atomIndex <N; atomIndex++){
    if(atomIndex == 0){
                    
       width = pow(3, 1/3)/(pow((mass/(2*pi*k*temp)),1/2)*pow(N, 1/3)*pow(4*pi, 1/3));
    }*/


    //creates atoms left of the hill until the velocity is equal to zero

    for (atomIndexL=0; atomIndexL < N; atomIndexL++ ){
                  
      if (velIndex >= 0.0000){
    
               width = 1/((sqrt((mass/(2*pi*k*temp))*(mass/(2*pi*k*temp))*(mass/(2*pi*k*temp))))*(4*pi*(velIndex*velIndex))*(exp(-(mass*(velIndex*velIndex))/(2*k*temp)))*N);




                  x[atomIndex]= static_cast <double> (rand()) / static_cast <double> (RAND_MAX/500);
                  y[atomIndex] = static_cast <double> (rand()) / static_cast <double> (RAND_MAX/500);
                  z[atomIndex] = static_cast <double> (rand()) / static_cast <double> (RAND_MAX/500);
                  theta[atomIndex] = static_cast<double>(rand()) / static_cast<double>(RAND_MAX/(M_PI));
                  phi[atomIndex] = static_cast<double>(rand()) / static_cast<double>(RAND_MAX/(2*M_PI));


                  //Randomize Velocity within intvel, convert to cartesian coordinates

                  velocity[atomIndex]=velIndex - static_cast <double> (rand()) / static_cast <double> (RAND_MAX/width);
                  velX[atomIndex]=velocity[atomIndex]*sin(theta[atomIndex])*cos(phi[atomIndex]);
                  velY[atomIndex]=velocity[atomIndex]*sin(theta[atomIndex])*sin(phi[atomIndex]);
                  velZ[atomIndex]=velocity[atomIndex]*cos(theta[atomIndex]);

                  velIndex=velIndex-width; 

                  //Update index
                  cout << "width" << width << endl;
                  cout <<"Atom Index " << atomIndexL << endl;
                  cout << "Atom Velocity " << velocity[atomIndex] << endl;
                  cout<< velX[atomIndex] << " " << velY[atomIndex] << " " << velZ[atomIndex] << endl;

  		            atomIndex++;

      	}
      }

    velIndex = mostProbVel;

    //creates remaining atoms to the right of the most probable velocity

    for (; atomIndex<N; atomIndex++){
                    
               width = 1/((sqrt((mass/(2*pi*k*temp))*(mass/(2*pi*k*temp))*(mass/(2*pi*k*temp))))*(4*pi*(velIndex*velIndex))*(exp(-(mass*(velIndex*velIndex))/(2*k*temp)))*N);




               	x[atomIndex]= static_cast <double> (rand()) / static_cast <double> (RAND_MAX/500);
                  y[atomIndex] = static_cast <double> (rand()) / static_cast <double> (RAND_MAX/500);
                  z[atomIndex] = static_cast <double> (rand()) / static_cast <double> (RAND_MAX/500);
                  theta[atomIndex] = static_cast<double>(rand()) / static_cast<double>(RAND_MAX/(M_PI));
                  phi[atomIndex] = static_cast<double>(rand()) / static_cast<double>(RAND_MAX/(2*M_PI));


                  //Randomize Velocity within intvel, convert to cartesian coordinates

                  velocity[atomIndex]=velIndex +  static_cast <double> (rand()) / static_cast <double> (RAND_MAX/width);
                  velX[atomIndex]=velocity[atomIndex]*sin(theta[atomIndex])*cos(phi[atomIndex]);
                  velY[atomIndex]=velocity[atomIndex]*sin(theta[atomIndex])*sin(phi[atomIndex]);
                  velZ[atomIndex]=velocity[atomIndex]*cos(theta[atomIndex]);

                  velIndex=velIndex+width; 

                  //Update index
                  cout << "width" << width << endl;
                  cout <<"Atom Index " << atomIndex << endl;
                  cout << "Atom Velocity " << velocity[atomIndex] << endl;
                  cout<< velX[atomIndex] << " " << velY[atomIndex] << " " << velZ[atomIndex] << endl;
      }



    double avgCheck = 0;

    //check out average

    for(int j=0; j<atomIndex; j++){

         avgCheck = avgCheck + velocity [j];

    }

    avgCheck = avgCheck / atomIndex;

    //cout << "Average: " <<  avgCheck << endl; 

    double outputVelX = -1;
    double outputVelY = -1;
    double outputVelZ = -1;
    int random1 = (rand()) % 50; 
    int random2 = (rand()) % 50;
    int random3 = (rand()) % 50;

    outputVelX = velX[random1];
    outputVelY = velY[random2];
    outputVelZ = velZ[random3];

    outFile << outputVelX;
    outFile << "\t";
    outFile << outputVelY;
    outFile << "\t";
    outFile << outputVelZ;
    outFile << "\n";

}
  return 0;

}