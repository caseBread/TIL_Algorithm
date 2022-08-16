//BOJ 1450
#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll n, c;
vector<int> t1;
vector<int> t2;
vector<int> a1;
vector<int> a2;

void sol(vector<int>& t, vector<int>& a, ll now, ll g) {
	if (now == t.size()) {
		if (g <= c) a.push_back(g);
	}
	else {
		now++;
		sol(t, a, now, g);
		g += t[now-1];
		sol(t, a, now, g);

	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	ll x;
	cin >> n >> c;
	for (ll i = 0; i < n/2; i++) {
		cin >> x;
		t1.push_back(x);
	}
	sol(t1, a1, 0, 0);
	for (ll i = n / 2; i < n; i++) {
		cin >> x;
		t2.push_back(x);
	}
	sol(t2, a2, 0, 0);
	sort(a1.begin(), a1.end());
	sort(a2.begin(), a2.end());
	ll j = a2.size() - 1;
	ll ans = 0;
	for (ll i = 0; i < a1.size(); i++) {
		while (j >= 0 && a1[i] + a2[j] > c) j--;
		ans += j + 1;
	}
	cout << ans;

}