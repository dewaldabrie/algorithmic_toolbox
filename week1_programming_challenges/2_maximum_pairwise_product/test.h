#include <cxxtest/TestSuite.h>
#include <vector>
#include "max_pairwise_product.h"

using std::vector;

 
class MyTestSuite3: public CxxTest::TestSuite
{
public:
    void test1(void)
    {
      const vector<uint64_t> input = {(uint64_t)2, (uint64_t)90000, (uint64_t)100000}; 
      TS_ASSERT_EQUALS(BetterMaxPairwiseProduct(input), (uint64_t)9000000000);
    }
};
