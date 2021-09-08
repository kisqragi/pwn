#include<stdio.h>
#include<unistd.h>
void main(void) {
    setvbuf(stdout, NULL, _IONBF, 0);
jail:
    read(0,stdout,0x300);
    puts("back to jail");
    goto jail;
}
