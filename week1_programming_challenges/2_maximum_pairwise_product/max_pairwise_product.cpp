#include <iostream>
#include <stdint.h>
#include "max_pairwise_product.h"

using std::cin;
using std::cout;
using std::vector;

int MaxPairwiseProductNaive(const vector<int>& numbers) {
  int result = 0;
  int n = numbers.size();
  int product = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = i + 1; j < n; ++j) {
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
