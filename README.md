# cmpe273-assignment3
This is the LRU cache and Bloom filter implementation of distributed cache system


## Question to the determination of **k(hashes)** and  *m* bits values 
n -> number of items to be store
p -> false positive probability
k -> number of hashes appliy
m -> number of bits in the filter

The probabability equations for Bloom Filter:
 m = -(n * log(p)) / log (1 / log(2)^2 )
 p = (1- exp(-k/(m/n))^k
Let's say that we want the false positive to be around 0.01 then we have
m = roughly around 9,585,000  and k = 7 (i have clacualte this 7 is the best
for 0.01 false positive with m = roughly around 9,585,000 so the side of 24 size of a bitarray would meet this requirement of 1 million items 
To sum up, it depends on how the designer makes trade off between the false positive rate and bit array size and hashes. 
## Runtime setup for midterm execution and your test_bloom_filter.py file
  Since your midterm and text inputs are different
  * To run your test env: please uncomment the the code indicate under
    is_memeber() under bloom_filter.py file  
