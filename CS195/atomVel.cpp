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

int main() {

  double mass = .0005;
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
  string throwingS;
  float throwingF; 
  int numAminos;

  ifstream infile;
  infile.open("dumb.txt");

  ofstream outfile;
  outfile.open("trpVel.txt");

  //outfile << "output test";

  infile >> numAminos;
  infile >> throwingS;
  for (int i = 0; i<numAminos; i++) {
    infile >> throwingS;
    infile >> mass;
    infile >> throwingF;
    infile >> throwingF;
    infile >> throwingF;
  
    cout << mass << endl;

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
              width = 1/((sqrt((mass/(2*pi*k*temp))*(mass/(2*pi*k*temp))*(mass/(2*pi*k*temp))))*(4*pi*(velIndex*velIndex))*(exp(-(mass*(velIndex*velIndex))/(2*k*temp)))*N);



                  x[atomIndexL]= static_cast <double> (rand()) / static_cast <double> (RAND_MAX/500);
                  y[atomIndexL] = static_cast <double> (rand()) / static_cast <double> (RAND_MAX/500);
                  z[atomIndexL] = static_cast <double> (rand()) / static_cast <double> (RAND_MAX/500);
                  theta[atomIndexL] = static_cast<double>(rand()) / static_cast<double>(RAND_MAX/(M_PI));
                  phi[atomIndexL] = static_cast<double>(rand()) / static_cast<double>(RAND_MAX/(2*M_PI));


                  //Randomize Velocity within intvel, convert to cartesian coordinates

                  velocity[atomIndexL]=velIndex - static_cast <double> (rand()) / static_cast <double> (RAND_MAX/width);
                  velX[atomIndexL]=velocity[atomIndexL]*sin(theta[atomIndexL])*cos(phi[atomIndexL]);
                  velY[atomIndexL]=velocity[atomIndexL]*sin(theta[atomIndexL])*sin(phi[atomIndexL]);
                  velZ[atomIndexL]=velocity[atomIndexL]*cos(theta[atomIndexL]);

                  velIndex=velIndex-width; 

                  //Update index
                  //cout << "width" << width << endl;
                  //cout <<"Atom Index " << atomIndexL << endl;
                  //outfile << velX[atomIndex] << "\t" << velY[atomIndex] << "\t" << velZ[atomIndex] << endl;

                atomIndexL++;

      	}
      }

    velIndex = mostProbVel;

    //creates remaining atoms to the right of the most probable velocity

    for (; atomIndex<N; atomIndex++){
                    
               width = 1/((sqrt((mass/(2*pi*k*temp))*(mass/(2*pi*k*temp))*(mass/(2*pi*k*temp))))*(4*pi*(velIndex*velIndex))*(exp(-(mass*(velIndex*velIndex))/(2*k*temp)))*N);

               cout << width << endl;


               	x[atomIndex]= static_cast <double> (rand()) / static_cast <double> (RAND_MAX/500);
                //cout << x[atomIndex] << endl;
                y[atomIndex] = static_cast <double> (rand()) / static_cast <double> (RAND_MAX/500);

                z[atomIndex] = static_cast <double> (rand()) / static_cast <double> (RAND_MAX/500);
                theta[atomIndex] = static_cast<double>(rand()) / static_cast<double>(RAND_MAX/(M_PI));
                phi[atomIndex] = static_cast<double>(rand()) / static_cast<double>(RAND_MAX/(2*M_PI));


                  //Randomize Velocity within intvel, convert to cartesian coordinates

                  velocity[atomIndex]=velIndex +  static_cast <double> (rand()) / static_cast <double> (RAND_MAX/width);
                  //cout << velocity[atomIndex] << endl;
                  velX[atomIndex]=velocity[atomIndex]*sin(theta[atomIndex])*cos(phi[atomIndex]);
                  velY[atomIndex]=velocity[atomIndex]*sin(theta[atomIndex])*sin(phi[atomIndex]);
                  velZ[atomIndex]=velocity[atomIndex]*cos(theta[atomIndex]);

                  velIndex=velIndex+width; 

                  //Update index
                  //cout << "width" << width << endl;
                  //cout <<"Atom Index " << atomIndex << endl;
                  //cout << "Atom Velocity " << velocity[atomIndex] << endl;
                  //cout<< velX[atomIndex] << " " << velY[atomIndex] << " " << velZ[atomIndex] << endl;
                  


           

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

    outfile << outputVelX;
    outfile << "\t";
    outfile << outputVelY;
    outfile << "\t";
    outfile << outputVelZ;
    outfile << "\n";

}

    infile.close();
    outfile.close();

  return 0;

}