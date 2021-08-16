#include <bits/stdc++.h>
using namespace std;
int main(){
	int n,b,a,s;
	cin>>n>>b>>a;
	int i;
	int ma=a;
	for(i=0;i<n;i++){
		cin>>s;
		if(b==0 && a==0){
			break;
		}
		if(s==1){
			if(b>0 && a!=ma){
				b-=1;
				a+=1;
			}
			else
			a-=1;
		}
		else{
			if(a>0)
			a-=1;
			else
			b-=1;
		}
	}
	cout<<i;
	return 0;
}