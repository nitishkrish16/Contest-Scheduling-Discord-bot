#include <iostream>
using namespace std;
int s(int n)
{
    if(n==0)
    {
        return 0;
    }
    else if(n==1)
    {
        return 1;
    }
    else if(n==2)
    {
        return -2;
    }
    else
    {
        return s(n-1)-s(n-2);
    }
}
int p(int n)
{
    if(n==0)
    {
        return 0;
    }
    else if(n==1)
    {
        return 1;
    }
    else if(n==2)
    {
        return -1;
    }
    else
    {
        return s(n)+p(n-1);
    }
}
int main()
{
    int stage;
    cout<<"\nEnter the stage for which you need position:- ";
    cin>>stage;
    int steps = s(stage);
    //cout<<steps;
    int position = p(stage);
    cout<<endl<<"POSITIION: "<<position;
    cout<<"\n\n\n";
}
