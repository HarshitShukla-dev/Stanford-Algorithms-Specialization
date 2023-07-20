#include <iostream>

using namespace std;

// Function to multiply two 64-digit integers using the Karatsuba algorithm
__int128 karatsuba_multiplication(__int128 x, __int128 y)
{
    // If the numbers are small, just use the naive multiplication algorithm
    if (x < 1000000000000000000 || y < 1000000000000000000)
    {
        return x * y;
    }

    // Divide the numbers into two halves
    __int128 x1 = x / 1000000000000000000;
    __int128 x2 = x % 1000000000000000000;
    __int128 y1 = y / 1000000000000000000;
    __int128 y2 = y % 1000000000000000000;

    // Calculate the products of the four sub-products
    __int128 a = karatsuba_multiplication(x1, y1);
    __int128 b = karatsuba_multiplication(x2, y2);
    __int128 c = karatsuba_multiplication(x1 + x2, y1 + y2);
    __int128 d = c - a - b;

    // Return the product of the two numbers
    return a * 1000000000000000000 + d * 1000000000000 + b;
}

int main()
{
    // Test cases
    __int128 x = 3141592653589793238462643383279502884197169399375105820974944592;
    __int128 y = 2718281828459045235360287471352662497757247093699959574966967627;
    __int128 expected_result = 82809993815966864968449855465452963451693827871762562303537280302639309781455903689785063331441134771596896079399266490085334554;
    __int128 actual_result = karatsuba_multiplication(x, y);

    // Check if the results are equal
    if (actual_result == expected_result)
    {
        cout << "The Karatsuba algorithm works correctly!" << endl;
        cout << actual_result << endl;
    }
    else
    {
        cout << "The Karatsuba algorithm does not work correctly!" << endl;
    }

    return 0;
}
