#include <bits/stdc++.h>
using namespace std;
int l[1002][1002];
int m,n,k,b,a;
int main(){
	cin>>n>>m>>k;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>l[i][j];
		}
	}
	while(k-->0){
		cin>>b;a=0;b-=1;
		while(a<n){
			if(l[a][b]==2) a+=1;
			else{
				if(l[a][b]==1){
					b+=1;
					l[a][b-1]=2;
				}
				else{
					b-=1;
					l[a][b+1]=2;
				}
			}
		}
		cout<<b+1<<' ';
	}
}