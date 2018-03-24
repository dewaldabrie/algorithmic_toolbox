#include <cxxtest/TestSuite.h>
#include <vector>
#include "fibonacci.h"

using std::vector;
using std::cin;
using std::cout;
 
class TestSpecificCases: public CxxTest::TestSuite
{
public:
    void test_specific_inputs(void) {
      const vector<int> input = {3, 10};
      const vector<uint64_t> output = {2, 5};
      
      auto in_iter = input.begin();
      auto out_iter = output.begin();
      
      cout << std::endl;
      while (1) {
        cout << "Checking whether fibonacci_fast(" << *in_iter << ") == " << *out_iter << std::endl;
        TS_ASSERT_EQUALS(fibonacci_fast_last_digit(*in_iter), *out_iter);
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
      for (int i = 0; i < 20; ++i) {
        TS_ASSERT_EQUALS(fibonacci_fast(i) % 10, fibonacci_fast_last_digit(i));
      }
    }
};
