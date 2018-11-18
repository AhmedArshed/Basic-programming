#include <iostream>
#include <stdlib.h> 
using namespace std;


//////// START OF MARKER FOR fib

long long fib(int a) {
  if (a<=1) { return a; }
  long long sum =0;
  long long h1=1;
  long long h2=1;
  for( int i=1;  i<a;  i++) {

  sum = h1+h2;
  h1=h2;
  h2=sum;
  
}
return h1;
}
//////// END OF MARKER 



//////// DO NOT MODIFY CODE BEYOND THIS LINE

int main(int argc, char* argv[]) {
    cout << (fib(atoi(argv[1]))) <<endl;
    return 0;
}
