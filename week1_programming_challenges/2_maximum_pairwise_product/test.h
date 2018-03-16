#include <cxxtest/TestSuite.h>
// #include <vector>
// #include "max_pairwise_product.h"

// using std::vector;

 
class MyTestSuite1 : public CxxTest::TestSuite 
{
public:
   void testAddition( void )
   {
      TS_ASSERT( 1 + 1 > 1 );
      TS_ASSERT_EQUALS( 1 + 1, 2 );
   }
}; 

/*  
class MyTestSuite: public CxxTest::TestSuite
{
public:
    void test1(void)
    {
      vector<long long> input = {2, 90000, 100000}; 
      TS_ASSERT_EQUALS(BetterMaxPairwiseProduct2(input), 9000000000);
    }`:w

}*/
