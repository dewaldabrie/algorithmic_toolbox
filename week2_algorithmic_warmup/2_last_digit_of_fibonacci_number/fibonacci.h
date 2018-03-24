/*************************************************************************************//**
 *  @file       fibonacci.h
 *
 *  @brief      Brief description of fibonacci.h
 *
 *  @date       2018-03-21 20:29
 *         
 **************************************************************************************/


#ifndef FIBONACCI_H
#define FIBONACCI_H

#include <stdint.h>

uint64_t fibonacci_naive(int n);
uint64_t fibonacci_fast(int n);
uint64_t fibonacci_fast_last_digit(int n);


#endif /* !FIBONACCI_H */

