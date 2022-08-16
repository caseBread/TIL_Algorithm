#include<bits/stdc++.h>
#define ll long long
using namespace std;

int n, k;
vector<int> s(100001);
vector<int> arr(100001);
int maxx;
int temp;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}
	s[1] = arr[1];
	for (int i = 2; i <= n; i++) {
		s[i] = s[i - 1] + arr[i];
	}
	for (int i = 1; i <= n - k + 1; i++) {
		temp = s[i + k - 1] - s[i - 1];
		if (i == 1)
			maxx = temp;
		else 
			maxx = max(maxx, temp);
	}
	cout << maxx;
}