//コンパイラ最適化用
#pragma GCC optimize("Ofast")
//インクルード(アルファベット順)
#include<algorithm>//sort,二分探索,など
#include<bitset>//固定長bit集合
#include<cmath>//pow,logなど
#include<complex>//複素数
#include<deque>//両端アクセスのキュー
#include<functional>//sortのgreater
#include<iomanip>//setprecision(浮動小数点の出力の誤差)
#include<iostream>//入出力
#include<iterator>//集合演算(積集合,和集合,差集合など)
#include<map>//map(辞書)
#include<numeric>//iota(整数列の生成),gcdとlcm(c++17)
#include<queue>//キュー
#include<set>//集合
#include<stack>//スタック
#include<string>//文字列
#include<unordered_map>//イテレータあるけど順序保持しないmap
#include<unordered_set>//イテレータあるけど順序保持しないset
#include<utility>//pair
#include<vector>//可変長配列

using namespace std;
typedef long long ll;

//マクロ
//forループ関係
//引数は、(ループ内変数,動く範囲)か(ループ内変数,始めの数,終わりの数)、のどちらか
//Dがついてないものはループ変数は1ずつインクリメントされ、Dがついてるものはループ変数は1ずつデクリメントされる
#define REP(i,n) for(ll i=0;i<ll(n);i++)
#define REPD(i,n) for(ll i=n-1;i>=0;i--)
#define FOR(i,a,b) for(ll i=a;i<=ll(b);i++)
#define FORD(i,a,b) for(ll i=a;i>=ll(b);i--)
//xにはvectorなどのコンテナ
#define ALL(x) x.begin(),x.end() //sortなどの引数を省略したい
#define SIZE(x) ll(x.size()) //sizeをsize_tからllに直しておく
//定数
#define INF 1000000000000 //10^12:極めて大きい値,∞
#define MOD 1000000007 //10^9+7:合同式の法
#define MAXR 100000 //10^5:配列の最大のrange(素数列挙などで使用)
//略記
#define PB push_back //vectorヘの挿入
#define MP make_pair //pairのコンストラクタ
#define F first //pairの一つ目の要素
#define S second //pairの二つ目の要素
#define Umap unordered_map
#define Uset unordered_set



signed main(){
    ll n;cin>>n;
    char s[500000];cin>>s;
    //それぞれのアルファベットのインデックス
    vector<set<ll>> alph(26);
    vector<ll> a(n);
    REP(i,n){alph[ll(s[i]-'a')].insert(i);a[i]=ll(s[i]-'a');}
    ll q;cin>>q;
    vector<ll> ans;
    REP(_,q){
        ll x;cin>>x;
        if(x==1){
            //iを--し忘れていた
            ll i;char c;cin>>i>>c;i--;
            ll j=ll(c-'a');ll k=a[i];a[i]=j;
            //ここで永遠にバグらせた
            alph[k].erase(i);
            alph[j].insert(i);
        }else{
            ll ans=0;
            ll l,r;cin>>l>>r;l--;r--;
            REP(i,26){
                auto y=alph[i].lower_bound(l);
                if(y!=alph[i].end())if(*y<=r)ans++;
            }
            cout<<ans<<endl;
        }
    }
}