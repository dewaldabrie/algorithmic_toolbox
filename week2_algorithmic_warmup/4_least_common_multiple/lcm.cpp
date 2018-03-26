#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;
using std::max;
using std::min;

bool DEBUG {false};

long long lcm_naive(int a, int b) {
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}


template<typename T>
vector<T> find_prime_factors(T a) {
  vector <T> prime_factors;
  T z {2};
  while (z <= a) {
    if (a % z == 0) {
      prime_factors.push_back(z);
      a /= z;
    }
    else {
      ++z;
    }
  }

  return prime_factors;
}

void cancel_common(vector<int>* a_primes, vector<int>* b_primes) {
  for (auto i = a_primes->begin(); i != a_primes->end(); ++i) {
    for (auto j = b_primes->begin(); j != b_primes->end(); ++j) {
      if (*i == *j) {
        a_primes->erase(i);
        b_primes->erase(j);
        --j;
        --i;
      }
    }
  }
}

long long lcm(int a, int b) {
  // prime number decomposition
  vector<int> a_primes = find_prime_factors(a);
  if (DEBUG) {
    cout << "A's primes are: ";
    for (auto i: a_primes)
      std::cout << i << ' ';
    cout << std::endl;
  }

  vector<int> b_primes = find_prime_factors(b);
  if (DEBUG) {
    cout << "B's primes are: ";
    for (auto i: b_primes)
      std::cout << i << ' ';
    cout << std::endl;
  }

  //cancel out primes
  // outer loop must iterate over longest vectpr
  if (a_primes.size() > b_primes.size()) {
    cancel_common(&b_primes, &a_primes);
  }
  else {
    cancel_common(&a_primes, &b_primes);
  }
  if (DEBUG) {
    cout << "A's primes after cancellation are: ";
    for (auto i: a_primes)
      std::cout << i << ' ';
    cout << std::endl;
  }
  
  // find product of one of the prime factors after cancellation
  long long product = 1;
  for (auto i = a_primes.begin(); i != a_primes.end(); ++i) {
    product *= (long long) *i;
  }
  if (DEBUG) {
  cout << "Product of A's cancelled primes is: " << product << std::endl;
  cout << "Answer is " << product << " * " << b << " = " << product*b << std::endl;
  }
  // answer is the prodoct of the cancelled primes 
  // of the one, multiplied by the beginning value of 
  // the other
  return product*(long long)b; 

}

//comment this out when running the tests
int main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm((int)a, (int)b) << std::endl;
  return 0;
}
