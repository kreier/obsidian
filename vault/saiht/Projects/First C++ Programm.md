---
date: 2000-11-01
---
I had my website [[saiht.de]] since the end of 1999. When I started studying physics in 2000 I used the opportunity to also learn object oriented programming with C++. And I documented my first program on saiht.de: https://saiht.de/legacy/physik/program/Integralberechnung.cc
## Integralberechnung
It is written in German, and maybe not very elegant. But I was happy for my first try!
```cpp
// mein erstes C++ Programm

#include <iostream>
#include <math.h>

using namespace std;

int main()
{
  int i = 0 , anzahl = 0;  
  float summe = 0;

  cout << "\n Berechnen der Näherung des Integrals f(x)=sin(x) zwischen 0 und pi" << endl;
  cout << "\n Anzahl der zu berechnenden Istwerte: ";
  cin  >> anzahl;
  if (anzahl < 2) anzahl = 2; 
  for( i = 0 ; i < anzahl ; i++)
  {
    summe = summe + sin ( M_PI / ( 2 * anzahl ) + ( M_PI * i ) / anzahl );
  }
  summe = summe / anzahl * M_PI;
  cout << "\n Die Näherung nach " << anzahl << " Berechnungen beträgt: " << summe << endl;
  cout << "\n";
}
```
And a few more programs were to follow. By the end of my study I had moved to Java with [[ar65view]].