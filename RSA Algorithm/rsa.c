#include <stdio.h>
#include <math.h>

void main()
{
    double ptext, ctext, t1, temp;
    double p, q, k, e, n, d, phi, pk;
    printf("enter the message(plaintext):");
    scanf("%lf", &ptext);
    printf("Enter the prime number(p):");
    scanf("%lf", &p);
    printf("Enter the prime number(q):");
    scanf("%lf", &q);
    printf("Enter private key value(e):");
    scanf("%lf", &e);

    n = p * q;
    phi = (p - 1) * (q - 1);
    for (k = 1; k <= 20; k++)
    {
        t1 = (phi * k) + 1;
        d = t1 / e;
        if (fmod(t1, e) == 0)
        {
            break;
        }
    }
    printf("Value of d=%lf", d);
    temp = pow(ptext, e);
    ctext = fmod(temp, n);
    printf("\nCipher text is: %lf", ctext);
    temp = pow(ctext, d);
    ptext = (int)temp % (int)n;
    printf("\nThe plain text is:%lf", ptext);
}
