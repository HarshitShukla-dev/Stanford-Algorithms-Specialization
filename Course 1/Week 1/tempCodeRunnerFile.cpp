#include <iostream>
#include <string>
using namespace std;

// Custom multiplication function for large numbers represented as strings
string multiply(const string& num1, const string& num2) {
    int n1 = num1.length();
    int n2 = num2.length();
    string result(n1 + n2, '0');

    for (int i = n1 - 1; i >= 0; --i) {
        int carry = 0;
        for (int j = n2 - 1; j >= 0; --j) {
            int sum = (num1[i] - '0') * (num2[j] - '0') + (result[i + j + 1] - '0') + carry;
            result[i + j + 1] = (sum % 10) + '0';
            carry = sum / 10;
        }
        result[i] += carry;
    }

    // Remove leading zeros
    size_t pos = result.find_first_not_of('0');
    if (pos != string::npos) {
        return result.substr(pos);
    }

    return "0";
}

string karatsubaMultiply(const string& num1, const string& num2) {
    int n1 = num1.length();
    int n2 = num2.length();

    // Base case: Single-digit multiplication
    if (n1 == 1 && n2 == 1) {
        int product = (num1[0] - '0') * (num2[0] - '0');
        return to_string(product);
    }

    // Make the length of both numbers equal by padding with leading zeros
    int max_len = max(n1, n2);
    string padded_num1 = string(max_len - n1, '0') + num1;
    string padded_num2 = string(max_len - n2, '0') + num2;

    int half_len = max_len / 2;

    // Split the numbers into two halves
    string a = padded_num1.substr(0, half_len);
    string b = padded_num1.substr(half_len);
    string c = padded_num2.substr(0, half_len);
    string d = padded_num2.substr(half_len);

    // Recursive calls for subproblems
    string ac = karatsubaMultiply(a, c);
    string bd = karatsubaMultiply(b, d);
    string ad_bc = multiply(karatsubaMultiply(a, d), karatsubaMultiply(b, c));

    // Combine the results using the Karatsuba algorithm formula
    string result = multiply(ac + string(2 * half_len, '0'), "1") +
                    multiply(ad_bc + string(half_len, '0'), "1") +
                    bd;
    
    // Remove leading zeros
    size_t pos = result.find_first_not_of('0');
    if (pos != string::npos) {
        return result.substr(pos);
    }

    return "0";
}

int main() {
    string numA = "3141592653589793238462643383279502884197169399375105820974944592";
    string numB = "2718281828459045235360287471352662497757247093699959574966967627";
    cout << karatsubaMultiply(numA, numB) << endl;
    return 0;
}
