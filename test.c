#include <stdio.h>

void multistore(long, long, long *);
long mult2(long, long);

int main()
{
   long d;
   multistore(2,3,&d);
   printf("2 * 3 -> %ld\n", d);
   return 0;


}

void multistore(long x, long y, long *dest)
{
   long t = mult2(x,y);
   *dest = t;

}

long mult2(long a, long b)
{
	long s = a*b;
        return s;

}
