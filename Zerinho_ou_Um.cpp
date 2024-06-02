#include <bits/stdc++.h>
using namespace std;

int main() {
	int a, b, c; cin >> a >> b >> c;
	if(a==b and a==c){
		cout <<"*";
	}
	else if (a!=b and a!=c){
		cout << "A";
	}
	else if(b!=a and b!=c){
		cout << "B";
	}
	else{
		cout << "C";
	}
}
