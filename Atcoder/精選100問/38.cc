//Codeforcesで128bit整数を使いたいとき
//→__int128_tを使う&GNU C++17 (64)で提出する
//デバッグ用オプション：-fsanitize=undefined,address

//コンパイラ最適化
#pragma GCC optimize("Ofast")

//インクルードなど
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

//イテレーション
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
#define FORA(i,I) for(const auto& i:I)
//x:コンテナ
#define ALL(x) x.begin(),x.end() 
#define SIZE(x) ll(x.size()) 
//定数
#define INF32 2147483647 //2.147483647×10^{9}:32bit整数のinf
#define INF64 9223372036854775807 //9.223372036854775807×10^{18}:64bit整数のinf
#define MOD 1000000007 //問題による
#define MAXR 1000000 //10^6:前計算の配列の範囲
//略記
#define PB push_back 
#define MP make_pair
#define F first
#define S second

//aをbで割る時の繰上げ,繰り下げ
ll myceil(ll a,ll b){return (a+(b-1))/b;}
ll myfloor(ll a,ll b){return a/b;}

signed main(){
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード
    //ios::sync_with_stdio(false);
    //cin.tie(nullptr);
    ll q;cin>>q;
    REP(_,q){
        string x,y;cin>>x>>y;
        ll n,m;n=SIZE(x);m=SIZE(y);
        vector<vector<ll>> dp(n+1,vector<ll>(m+1,0));
        FOR(i,1,n){
            FOR(j,1,m){
                if(x[i-1]==y[j-1]){
                    dp[i][j]=max({dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+1});
                }else{
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        cout<<dp[n][m]<<endl;
    }
}