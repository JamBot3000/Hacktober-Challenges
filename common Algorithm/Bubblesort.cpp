#include <iostream>
#define size 10

using namespace std;

int main(int argc, char const *argv[])
{   int n;
    cout<<"No. of Elements\n";
    cin>>n;
    
    int a[n];

    cout<<"Enter Elements:\n";
    for (int i = 0; i < n; i++)
    {
        cin>>a[i];
    }
    
    for (int i = 0; i < n; i++)
    {
        for (int i = 0; i < n-1; i++)
        {
            if(a[i]>a[i+1]) swap(a[i],a[i+1]);
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout<<a[i]<<" ";
    }
    
    
    return 0;
}
