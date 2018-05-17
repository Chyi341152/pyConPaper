#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# map, reduce
import functools


# map() 函数接受两个参数，一个函数，一个时序列，map将传入的函数依次作用到序列的每一个元素，并将结果作为新的list返回
print("map function list[1,2,3,4,5,6] %s"%(list(map(str, [1,2,3,4,5,6]))))

# reduce() 函数把一个函数作用在一个序列【x1,x2,x3】上，这个函数必须接受两个参数，reduce把结果继续和序列的下一个元素做累计计算
print("reduce function list[1,2,3,4,5,6] %s"%(functools.reduce(lambda x,y: x+y, [1,2,3,4,5,6])))

