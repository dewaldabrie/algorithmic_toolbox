#include <iostream>
#include <stdint.h>
#include "max_pairwise_product.h"

using std::cin;
using std::cout;
using std::vector;

uint64_t MaxPairwiseProductNaive(vector<uint64_t>& numbers) {
  uint64_t result = 0;
  uint64_t n = numbers.size();
  uint64_t product = 0;
  for (uint64_t i = 0; i < n; ++i) {
    for (uint64_t j = i + 1; j < n; ++j) {
      product = numbers[i] * numbers[j];
      if (product > result) {
        result = product;
      }
    }
  }
  return result;
}

uint64_t BetterMaxPairwiseProduct(const vector<uint64_t>& numbers) {
  // find two largest numbers in vector
  uint64_t largest = 0;
  uint64_t second_largest = 0;
  for (auto num : numbers ){
    if (num > largest){
      second_largest = largest;
      largest = num;
    }
    else if (num > second_largest){
      second_largest = num;
    }
  }

  return largest * second_largest;
}

/*  
int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }

    int result = BetterMaxPairwiseProduct(numbers);
    cout << result << "\n";
    return 0;
}
*/
