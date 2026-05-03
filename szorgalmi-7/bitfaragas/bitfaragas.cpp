#include<iostream>
#include<vector>
#include<algorithm>
#include<cctype>
#include<string>
using namespace std;
#define u cout
#define n cin>>
#define f for
#define k if
#define L return
#define _ <<
using s=string;using t=int;using r=vector<t>;using h=char;
t p(s&e){
s i;f(h c:e)k(isalpha(c))i+=tolower(c);
t l=0,R=i.length()-1;
if(i.empty()){u _ "Ures.\n";L 1;}
f(;l<R;){k(i[l]!=i[R]){u _ "Nem egyezik: " _ i[l] _ " != " _ i[R] _ "\n";L 0;}l++;R--;}
L 1;}
void q(r&a){
u _ "Rendez: ";f(t i=0;i<(t)a.size();i++)u _ a[i] _ " ";u _ "\n";
t sw=1,j=0;
f(;sw;){sw=0;j++;u _ "Iteracio #" _ j _ "\n";
f(t i=0;i<(t)a.size()-1;++i){
u _ "arr[" _ i _ "]=" _ a[i] _ " vs arr[" _ i+1 _ "]=" _ a[i+1] _ "\n";
k(a[i]>a[i+1]){u _ "Csere!\n";swap(a[i],a[i+1]);sw=1;}
else u _ "OK\n";}
u _ "Allapot: ";f(t i=0;i<(t)a.size();i++)u _ a[i] _ " ";u _ "\n";
k(!sw)u _ "Rendezett.\n";}
}
t main(){
s T;u _ "Szo: ";getline(cin,T);
u _ (p(T)?"Palindrom.\n":"Nem palindrom.\n");
r R;t E;u _ "Menny szam: ";n E;u _ "Szamok:\n";
f(t i=0;i<E;++i){t N;u _ i+1 _ ". : ";n N;R.push_back(N);}
q(R);u _ "Eredmeny: ";f(t i=0;i<(t)R.size();i++)u _ R[i] _ " ";u _ "\n";}
