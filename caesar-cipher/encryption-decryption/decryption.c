#include <stdio.h>
#include <conio.h>
#include <string.h>
void main()
{
    char data[100] = "";
    char encrypt[100] = "";
    int key;
    printf("Enter data to encrypt: ");
    gets(data);
    printf("Enter key: ");
    scanf("%d", &key);
    for (int i = 0; i < strlen(data); i++)
    {
        if (data[i] == ' ')
            encrypt[i] = ' ';
        else
        {
            encrypt[i] = data[i] - key;
            if ((encrypt[i] < 'A' && encrypt[i] > 'z') || (encrypt[i] < 'a'))
                encrypt[i] = data[i] + 26 - key;
        }
    }
    printf("Encrypted Data: ");
    puts(encrypt);
}