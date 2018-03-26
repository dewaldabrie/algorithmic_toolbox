#! /bin/bash
#
# runtests.sh
# Copyright (C) 2018 dewald <dewald@anticipation>
#
# Distributed under terms of the MIT license.
#
rm -f runner
rm -f runner.cpp
cxxtestgen --error-printer -o runner.cpp test.h
g++ -o runner -I/usr/include/cxxtest --std=c++14 runner.cpp lcm.cpp
./runner
