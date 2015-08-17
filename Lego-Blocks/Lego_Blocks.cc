#include <iostream>
#include <vector>
#include <math.h>
 
using namespace std;
 
#define MOD 1000000007
 
unsigned long long power(unsigned long long num, int p) {
 
  if(p == 0) return 1;
  if(p == 1) return num;
 
  unsigned long long number = num;
  for(int i=2;i<=p;i++) {
    num *= number;
    num %= MOD;
  }
  return num;
}
 
int main() {
 
  int N, M;
 
  vector<long long> T(1001);
  vector<long long> S(1001);
  vector<long long> P(1001);
 
  T[0] = T[1] = 1;
  T[2] = 2;
  T[3] = 4;
  T[4] = 8;
 
  P[0] = P[1] = 1;
 
  for(int i=5;i<=1000;i++)
    T[i] = (T[i-1] + T[i-2] + T[i-3] + T[i-4])%MOD;
 
  S[0] = 1;
  S[1] = 1;
 
  long long sum;
  int Tt;
  cin >> Tt;
 
  for(int t=0;t<Tt;t++) {
    cin >> N >> M;
 
    for(int i=0;i<=M;i++)
      P[i] = (long long)power(T[i],N);
 
    for(int i=2;i<=M;i++) {
      sum = 0;
      for(int j=1;j<i;j++) {
	sum += (S[j]*P[i-j])%MOD;
	sum %= MOD;
      }
      S[i] = (P[i] - sum);
      S[i] = S[i]%MOD;
    }
    while(S[M] < 0)
      S[M] += MOD;
    cout << S[M] << endl;
  }
 
}
