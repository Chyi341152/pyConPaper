#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import redis

redis.StrictRedis(host='localhost', port=6379, password='macintosh', db=0)
