#include<iostream>
#include<vector>
#include<cstdlib>
#include<ctime>
using namespace std;

void generate(vector<int> &A, int n = 10, int max = 50)
{
    for (int i = 0; i < n; i++)
    {
        A.push_back(rand()%(max+1));
    }
    
}

void print_vector(vector<int> &A)
{
    for (int x: A)
        cout<<x<<"\t";
    cout<<endl;
}

void merge(vector<int> &A, int lb, int mid, int ub)
{
    int i = lb, j = mid+1, k = 0;
    vector<int>temp;
    while(i <= mid && j <= ub)
    {
        if (A[i] < A[j])
        {
            temp.push_back(A[i]);
            i++;
        }
        else
        {
            temp.push_back(A[j]);
            j++;
        }        
    }
    while(i <= mid)
    {
        temp.push_back(A[i]);
        i++;
    }
    while(j <= ub)
    {
        temp.push_back(A[j]);
        j++;
    }
    for(int x = lb;x<=ub;x++)
        A[x] = temp[k++];
}

void split(vector<int> &A, int lb, int ub)
{
    if(lb<ub)
    {
        int mid = (lb + ub) / 2;
        split(A, lb, mid);
        split(A, mid+1, ub);
        merge(A, lb, mid, ub);
    }
}

int main()
{
    srand(time(NULL));
    vector<int> A;
    int n, max;
    //cin>>n>>max;
    generate(A);
    cout<<"Original Array:\n\n";
    print_vector(A);
    split(A, 0, A.size()-1);
    cout<<"Sorted Array:\n\n";
    print_vector(A);
    return 0;
}
