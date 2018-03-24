#include <cassert>
//#include "fibonacci.h"
#include <iostream>

using std::cin;
using std::cout;
// The following code calls a naive algorithm for computing a Fibonacci number.
//
// What to do:
// 1. Compile the following code and run it on an input "40" to check that it is slow.
//    You may also want to submit it to the grader to ensure that it gets the "time limit exceeded" message.
// 2. Implement the fibonacci_fast procedure.
// 3. Remove the line that prints the result of the naive algorithm, comment the lines reading the input,
//    uncomment the line with a call to test_solution, compile the program, and run it.
//    This will ensure that your efficient algorithm returns the same as the naive one for small values of n.
// 4. If test_solution() reveals a bug in your implementation, debug it, fix it, and repeat step 3.
// 5. Remove the call to test_solution, uncomment the line with a call to fibonacci_fast (and the lines reading the input),
//    and submit it to the grader.

uint64_t fibonacci_naive(int n) {
    if (n <= 1)
        return n;

    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2);
}

uint64_t fibonacci_fast(int n) {
    // write your code here
    if (n <=1) {
      return n;
    }
    else {
      uint64_t f = 1;
      uint64_t f1 = 1;  //delayed by 1 
      uint64_t f2 = 0;  //delayed by 2
      
      for(int i = 2; i < n; ++i) {
        f2 = f1; // shift back
        f1 = f;  // shift back
        f = f1 + f2; // sum of previous two values
      }
      return f;
    }
}


uint64_t fibonacci_fast_last_digit(int n) {
    // write your code here
    if (n <=1) {
      return n;
    }
    else {
      uint64_t f = 1;
      uint64_t f1 = 1;  //delayed by 1 
      uint64_t f2 = 0;  //delayed by 2
      
      for(int i = 2; i < n; ++i) {
        f2 = f1; // shift back
        f1 = f;  // shift back
        f = (f1 + f2) % 10; // sum of previous two values
      }
      return f;
    }
}

int main() {
    int n = 0;
    std::cin >> n;

    std::cout << fibonacci_fast_last_digit(n) << '\n';
    return 0;
}
