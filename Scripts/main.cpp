#include <iostream>
#include <Ising.h>

using namespace std;

int main()
{
   Ising Is = Ising(2);
   Is.T = 1.0;
   Is.TotalEnergy(1);
   cout << "total energy: " << Is.E_tot << " J" << endl;

   Is.Metropolis(10);
   cout << "total energy now: " << Is.E_tot << " J" << endl;
   cout << "avg: " << Is.avg << " J" << endl;
   return 0; 
}