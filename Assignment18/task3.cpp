#include <iostream>
using namespace std;

long long factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() {
    int num;
    cout << "Enter a non-negative integer: ";
    cin >> num;

    if (num < 0) {
        cout << "Factorial for negative numbers is not possible!";
    } else {
        long long result = factorial(num);
        cout << "Factorial of " << num << " = " << result;
    }

    return 0;
}