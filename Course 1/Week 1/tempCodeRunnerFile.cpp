#include <iostream>
#include <cmath>
#include <string>
using namespace std;

// Custom integer exponentiation function
long long int_pow(long long base, int exp) {
    long long result = 1;
    while (exp > 0) {
        if (exp & 1) {  // If exp is odd
            result *= base;
        }
        base *= base;
        exp >>= 1;
    }
    return result;
}

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
    long long a = num1 / int_pow(10LL, half_n1);  // Use LL suffix here
    long long b = num1 % int_pow(10LL, half_n1);  // Use LL suffix here
    long long c = num2 / int_pow(10LL, half_n2);  // Use LL suffix here
    long long d = num2 % int_pow(10LL, half_n2);  // Use LL suffix here

    // Recursive calls for subproblems
    long long ac = karatsubaMultiply(a, c);
    long long bd = karatsubaMultiply(b, d);
    long long ad_bc = karatsubaMultiply(a + b, c + d) - ac - bd;

    // Combine the results using the Karatsuba algorithm formula
    return ac * int_pow(10LL, half_n1 * 2) + ad_bc * int_pow(10LL, half_n1) + bd;  // Use LL suffix here
}

int main() {
    long long numA = 3141592653589793238LL;  // Use LL suffix here
    numA = numA * 1000000000000000000LL + 4197169399375105820974944592LL;  // Use LL suffix here
    long long numB = 2718281828459045235LL;  // Use LL suffix here
    numB = numB * 1000000000000000000LL + 247093699959574966967627LL;  // Use LL suffix here
    cout << karatsubaMultiply(numA, numB) << endl;
    return 0;
}
