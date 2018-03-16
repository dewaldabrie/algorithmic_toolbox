#include "max_pairwise_product.h"

long long MaxPairwiseProductNaive(const vector<long long>& numbers) {
  long long result = 0;
  int n = numbers.size();
  long long product = 0;
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

long long BetterMaxPairwiseProduct(const vector<long long>& numbers) {
  // find two largest numbers in vector
  long long largest = 0;
  long long second_largest = 0;
  for (auto num : numbers ){
    if (num > largest){
      largest = num;
    }
    else if (num > second_largest){
      second_largest = num;
    }
  }

  return largest * second_largest;
}

int main() {
    int n;
    cin >> n;
    vector<long long> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }

    long long result = BetterMaxPairwiseProduct(numbers);
    cout << result << "\n";
    return 0;
}
