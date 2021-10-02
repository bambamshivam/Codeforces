#include <bits/stdc++.h>
using namespace std;
int d[401][401];
char s[401];
int cost(int i1,int j1,int i2,int j2){
	return d[i2][j2]-d[i2][j1-1]-d[i1-1][j2]+d[i1-1][j1-1];
}
int main(){
	int t;
	cin>>t;
	for(int w=0;w<t;w++){
		int n,m;
		cin>>n>>m;
		for(int i=1;i<=n;i++){
			cin>>s;
			for(int j=1;j<=m;j++){
				d[i][j]=d[i-1][j]+d[i][j-1]-d[i-1][j-1]+(s[j-1]=='1');
			}
		}
		int h=1000000000;
		int m1=h;
		for(int i=1;i<=n;i++){
			for(int j=i+4;j<=n;j++){
				int p=h,c=h;
				for(int k=4;k<=m;k++){
					int i1=i,j1=k-3,i2=j,j2=k;
					int t1=cost(i1+1,j1+1,i2-1,j2-1);
					int a1=j2-j1-1-cost(i1,j1+1,i1,j2-1);
					int a2=i2-i1-1-cost(i1+1,j2,i2-1,j2);
					int a3=j2-j1-1-cost(i2,j1+1,i2,j2-1);
					int a4=i2-i1-1-cost(i1+1,j1,i2-1,j1);
					int s=t1+a1+a2+a3+a4;
					int b1=i2-i1-1-cost(i1+1,j2,i2-1,j2);
					int b2=cost(i1+1,j2,i2-1,j2);
					int b3=1-cost(i1,j2,i1,j2);
					int b4=1-cost(i2,j2,i2,j2);
					c=min(p+a2,s);
					m1=min(m1,c);
					p=c;
					p=p-b1+b2+b3+b4;
				}
			}
		}
		cout<<m1<<endl;
	}
}