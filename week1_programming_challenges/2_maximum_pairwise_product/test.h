#include <cxxtest/TestSuite.h>
#include <vector>
#include "max_pairwise_product.h"

using std::vector;
using std::cin;
using std::cout;
 
class TestCornerCases: public CxxTest::TestSuite
{
public:
    void test_large_inputs(void) {
      const vector<uint64_t> input = {(uint64_t)2, (uint64_t)90000, (uint64_t)100000}; 
      TS_ASSERT_EQUALS(BetterMaxPairwiseProduct(input), (uint64_t)9000000000);
    }
};


class StressTest: public CxxTest::TestSuite {
  /*
   *  Generate random inputs and compare our target algorithm against a naive
   *  but hopefully correct implementation.
   */
  public:
    void test_stress(void) {
      while (true) {
        int n = rand() % 10 + 2;
        cout << n << "\n";
        vector<uint64_t> a;
        for (int i = 0; i < n; ++i) {
          a.push_back((uint64_t)rand() % 100000);
        }
        for (int i = 0; i < n; ++i) {
          cout << a[i] << ' ';
        }
        cout << "\n";
        uint64_t res1 = BetterMaxPairwiseProduct(a);
        uint64_t res2 = MaxPairwiseProductNaive(a);
        if (res1 != res2) {
          cout << "Wrong answer: " << res1 << ' ' << res2 << "\n";
          break;
        } 
        else {
          cout << "OK\n";
        }
      }
    }
};


class StressTest_: public CxxTest::TestSuite {
  /*
   *  Generate random inputs and compare our target algorithm against a naive
   *  but hopefully correct implementation.
   */
  public:
    void test_stress(void) {
      while (true) {
        int n = rand() % 10 + 2;
        cout << n << "\n";
        vector<uint64_t> a;
        for (int i = 0; i < n; ++i) {
          a.push_back((uint64_t)rand() % 100000);
        }
        for (int i = 0; i < n; ++i) {
          cout << a[i] << ' ';
        }
        cout << "\n";
        uint64_t res1 = BetterMaxPairwiseProduct(a);
        uint64_t res2 = MaxPairwiseProductNaive(a);
        if (res1 != res2) {
          cout << "Wrong answer: " << res1 << ' ' << res2 << "\n";
          break;
        } 
        else {
          cout << "OK\n";
        }
      }
    }
};
