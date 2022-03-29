//turn off ASLR
//echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
//turn off DEP
//gcc -fno-stack-protector -z execstack program.c -o program
#include <stdio.h>
#include <string.h>
void secret(){
printf("You have accessed the secret function!!\n");
}
int main(int argc, char *argv[])
{
char buf[512];
strcpy(buf, argv[1]);
printf("%s",buf);
return(0);
}
