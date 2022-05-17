#include<bits/stdc++.h>

using namespace std;

//typedef long long long long;
#define inf 1e18
#define mod 1000000007
#define pb push_back

void dfs(long long r, long long m, long long* dp, long long* c, long long* a, bool &cyc,vector<long long>* adj){
    c[r] = 1;
    dp[r] = 0;
    for(long long i=0; i<adj[r].size(); i++){
        long long j = adj[r][i];
        if(a[j]>m)continue;
        if(c[j]==1)cyc=true;
        else if(c[j] ==0)dfs(j,m,dp,c,a,cyc,adj);
        dp[r]=max(dp[r],dp[j]+1);
    }
    c[r]=2;
}


int main(int argc, char const *argv[])
{
    long long n,m1,k;
    cin >> n >> m1 >> k;

    long long a[n];
    vector<long long> adj[n];
    for(long long i=0; i<n; i++){
        long long ai;
        cin>>ai;
        a[i] = ai;
    }
    k-=1;

    for(long long i=0; i<m1; i++) {
        long long u,v;
        cin >> u >> v;

        adj[u-1].push_back(v-1);
    }

    long long l=0; 
    long long r = 10000000000;
    long long ans = -1;

    while(l<=r){

        long long m = (l+r)/2;
        bool cyc = false;
        long long dp[n];
        long long c[n];
        memset(dp,-1,sizeof(dp));
        memset(c,0,sizeof(dp));

        for(long long i=0; i<n; i++){
            if(a[i]<=m)dfs(i,m,dp,c,a,cyc,adj);
        }
        long long mk = -1;
        for(long long i=0; i<n; i++){
            mk = max(dp[i],mk);
        }
        if(cyc or mk>=k){
            ans = m;
            r=m-1;
        }
        else{
            l=m+1;
        }
    }
    cout << ans<< endl;
    return 0;
}