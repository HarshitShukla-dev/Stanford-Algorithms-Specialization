#include <iostream>
#include <sstream>

using namespace std;

int main() {
  __int128 x = 3141592653589793238462643383279502884197169399375105820974944592;
  __int128 y = 2718281828459045235360287471352662497757247093699959574966967627;
  __int128 expected_result = 82809993815966864968449855465452963451693827871762562303537280302639309781455903689785063331441134771596896079399266490085334554;

  // Create an ostringstream object to store the value of x
  ostringstream oss;
  oss << x;

  // Get the string from the ostringstream object
  string str = oss.str();

  // Print the string to the console
  cout << str << endl;

  return 0;
}
