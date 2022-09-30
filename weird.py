#!/bin/python

import math
import os
import random
import re
import sys



num= input()
if num%2!=0:
    print("Weird")
else:
    if num>=2 and num<=5:
        print("Not Weird")
    elif num>5 and num<=20:
        print("Weird")
    else :
        print("Not Weird")
