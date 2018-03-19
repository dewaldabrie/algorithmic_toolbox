#! /bin/bash
#
# runtests.sh
# Copyright (C) 2018 dewald <dewald@anticipation>
#
# Distributed under terms of the MIT license.
#

cxxtestgen --error-printer -o runner.cpp test.h
g++ -o runner -I/usr/include/cxxtest --std=c++14 runner.cpp max_pairwise_product.cpp
./runner
