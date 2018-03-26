#include <cxxtest/TestSuite.h>
#include <vector>
#include <tuple>
#include "lcm.h"

using std::vector;
using std::tuple;
using std::get;
using std::cin;
using std::cout;
 
class TestPrimeNumberFinder: public CxxTest::TestSuite {
public:
  void test_prime_finder (void) {
    vector<int> inputs {10, 20, 1999999999};
    vector<vector<int>> outputs = {
      {2, 5},
      {2, 2, 5},
      {31, 64516129}
    };
    auto in_iter = inputs.begin();
    auto out_iter = outputs.begin();

    while(in_iter < inputs.end()) {
      cout << "Checking answers for find_prime_factors(" << *in_iter << ")" << std::endl;
      TS_ASSERT_EQUALS(
          find_prime_factors(*in_iter), 
          *out_iter
      );
      ++in_iter;
      ++out_iter;
    }
  }

};



class TestSpecificCases: public CxxTest::TestSuite {
public:
    void test_specific_inputs(void) {
      const vector<tuple<int, int>> input = {
        tuple<int, int>(6, 8),
        tuple<int, int>(28851538, 1183019),
        tuple<int, int>(14159572, 63967072),
        tuple<int, int>(1999999999,2000000000)
      };
      const vector<long long> output = {
        24,
        1933053046,
        226436590403296,
        3999999998000000000
      };
      
      auto in_iter = input.begin();
      auto out_iter = output.begin();
      
      cout << std::endl;
      while (1) {
        cout << "Checking whether lcm(" << get<0>(*in_iter) << ", " << get<1>(*in_iter) << ") == " << *out_iter << std::endl;
        TS_ASSERT_EQUALS(lcm(get<0>(*in_iter), get<1>(*in_iter)), *out_iter);
        if (++in_iter == input.end()) {
          break;
        }
        ++out_iter;
      }
    }
};


class StressTest: public CxxTest::TestSuite {
  /*
   *  Generate random inputs and compare our target algorithm against a naive
   *  but hopefully correct implementation.
   */
  public:
    void test_stress(void) {
      for (int i = 0; i < 10; ++i) {
        int a = rand() % 2000;
        int b = rand() % 2000;
        cout << "Checking whether lcm(" << a << ", " << b << ") == " << "lcm_naive(" << a << ", " << b << ")" << std::endl;
        TS_ASSERT_EQUALS(lcm(a, b), lcm_naive(a, b));
      }
    }
};
