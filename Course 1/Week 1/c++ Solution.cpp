#include <iostream>
#include <string>

using namespace std;

string add(const string& num1, const string& num2) {
    int n1 = num1.length();
    int n2 = num2.length();
    int carry = 0;
    string result;

    // Perform addition digit by digit
    for (int i = n1 - 1, j = n2 - 1; i >= 0 || j >= 0 || carry > 0; --i, --j) {
        int sum = carry;
        if (i >= 0) {
            sum += (num1[i] - '0');
        }
        if (j >= 0) {
            sum += (num2[j] - '0');
        }
        carry = sum / 10;
        result = to_string(sum % 10) + result;
    }

    return result;
}

string subtract(const string& num1, const string& num2) {
    int n1 = num1.length();
    int n2 = num2.length();
    string result;

    int i = n1 - 1, j = n2 - 1;
    int borrow = 0;

    // Perform subtraction digit by digit
    while (i >= 0 || j >= 0) {
        int digit1 = (i >= 0) ? (num1[i] - '0') : 0;
        int digit2 = (j >= 0) ? (num2[j] - '0') : 0;

        int diff = digit1 - digit2 - borrow;

        if (diff < 0) {
            diff += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }

        result = to_string(diff) + result;

        i--;
        j--;
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

    // Calculate (a + b) * (c + d)
    string sum_ab = add(a, b);
    string sum_cd = add(c, d);
    string ad_bc = karatsubaMultiply(sum_ab, sum_cd);
    ad_bc = subtract(ad_bc, ac);
    ad_bc = subtract(ad_bc, bd);

    // Combine the results using the Karatsuba algorithm formula
    string result = add(add(ac + string(2 * half_len, '0'), ad_bc + string(half_len, '0')), bd);

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

// Output : 8539734222673567065463525913473929274390907708686253193095326904481864813177325434676245947323784349299707034369488855815665904