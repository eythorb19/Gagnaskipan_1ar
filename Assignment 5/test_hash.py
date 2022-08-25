from ass5_hash import HashMap
from ass5_hash import Bucket, ItemExistsException, NotFoundException
import random
from ass5_hash import MyHashableKey
import string
from random import Random

START_LIST_SIZE = 3
END_LIST_SIZE = 20

RANDOM_GENERATIONS = 10000

RANDOM_NUMBER_START_RANGE = 1
RANDOM_NUMBER_END_RANGE = 10000

RANDOM_STRING_SIZE_RANGE_START = 1
RANDOM_STRING_SIZE_RANGE_END = 15

def check():
    maxarr = []
    minarr = []
    for r in range(3,20):
        test_list = [0]*r
        for i in range(RANDOM_GENERATIONS):
            randstr = ""
            for x in range(random.randint(RANDOM_STRING_SIZE_RANGE_START, RANDOM_STRING_SIZE_RANGE_END)):
                rand_number = random.randint(65,126)
                randstr+=str(chr(rand_number))
            
            rand_hash_nr = random.randint(RANDOM_NUMBER_START_RANGE,RANDOM_NUMBER_END_RANGE)
            key = MyHashableKey(rand_hash_nr, randstr)
            hash_key = hash(key)%r
            print(hash_key)
            test_list[hash_key]+=1
        print(test_list)

        maxim_ratio = max(test_list)/(RANDOM_GENERATIONS/r)
        maxarr.append(maxim_ratio)
        minim_ratio = min(test_list)/(RANDOM_GENERATIONS/r)
        minarr.append(minim_ratio)

    x = sum(maxarr)/len(maxarr)
    y = sum(minarr)/len(minarr)
    print('average max ratio:'+str(x))
    print('average min ratio:'+str(y))
    z = ((x-1 + 1-y)/2)*100
    print("average deviation from 100% even distribution: "+str(z)+"%")

check()