#include <iostream>
#include <string>
using namespace std;

long long karatsubaMultiply(long long num1, long long num2) {
    // Convert numbers to strings to find their lengths
    int n1 = to_string(num1).length();
    int n2 = to_string(num2).length();

    // Base case: Single-digit multiplication
    if (min(n1, n2) == 1) {
        return num1 * num2;
    }

    // Split the numbers into two halves
    int half_n1 = n1 / 2;
    int half_n2 = n2 / 2;
    long long a = num1 / pow(10, half_n1);
    long long b = num1 % (long long)pow(10, half_n1);
    long long c = num2 / pow(10, half_n2);
    long long d = num2 % (long long)pow(10, half_n2);

    // Recursive calls for subproblems
    long long ac = karatsubaMultiply(a, c);
    long long bd = karatsubaMultiply(b, d);
    long long ad_bc = karatsubaMultiply(a + b, c + d) - ac - bd;

    // Combine the results using the Karatsuba algorithm formula
    return ac * (long long)pow(10, half_n1 * 2) + ad_bc * (long long)pow(10, half_n1) + bd;
}

int main() {
    long long numA = 3141592653589793238462643383279502884197169399375105820974944592;
    long long numB = 2718281828459045235360287471352662497757247093699959574966967627;
    cout << karatsubaMultiply(numA, numB) << endl;
    return 0;
}
