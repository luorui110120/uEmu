#include <stdio.h>
#include <string.h>
#include <stdlib.h>
 
unsigned char hexData[7] = {
    0x38, 0x35, 0x3C, 0x3C, 0x3F, 0x5A, 0x50 
};
 
unsigned char g_encode[] = {0x33, 0x31, 0x39, 0x33, 0x31, 0x39, 0x24, 0x35, 0x50};
char* xorstring(unsigned char* input, int size){
    int i = 0;
    char *pbuf = malloc(size);
    memset(pbuf, 0, size);
    for(i = 0; i < size; i++){
        pbuf[i] = input[i] ^ 0x50;
    }
    if(0 == strcmp("hello\n", pbuf)){
        printf("new decode buf:%d", strlen(pbuf));
    }
    return (char*) pbuf;
}
int main(){
    //char szbuf[] = "3293$P";
    printf("%s\n", xorstring(hexData, sizeof(hexData)));
    printf("%s\n", xorstring(g_encode, sizeof(g_encode)));
    //printf("%s\n", xorstring(szbuf, strlen(szbuf)));
    return 0;
}

