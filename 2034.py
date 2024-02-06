from collections import OrderedDict
import heapq

class StockPrice(object):


    #for looking up dates
    def __init__(self):
        self.minheap = [] #the min price will be at the top
        self.maxheap = [] #we will push negative price so that max price will be at the top
        self.latest_time = -1 #the latest timestamp
        self.timestamps = {} #dictionary that keeps track of the 'actual' timestamp, price pair
        

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """

        self.timestamps[timestamp] = price #add or update price

        self.latest_time = max(self.latest_time, timestamp) #update latest time if necassary

        heapq.heappush(self.minheap, (price, timestamp)) #push to heaps
        heapq.heappush(self.maxheap, (-price, timestamp))


    def current(self):
        """
        :rtype: int
        """
        return self.timestamps[self.latest_time]

        

    def maximum(self):
        """
        :rtype: int
        """


        #iterate through heap until we find one that is accurate to the dict
        current_price, timestamp  = heapq.heappop(self.maxheap)

        while -current_price != self.timestamps[timestamp]: 
            current_price, timestamp = heapq.heappop(self.maxheap)

        heapq.heappush(self.maxheap, (current_price, timestamp))

        return -current_price

    def minimum(self):
        """
        :rtype: int
        """

        current_price, timestamp = heapq.heappop(self.minheap)

        while current_price != self.timestamps[timestamp]: 
            current_price, timestamp = heapq.heappop(self.minheap)

        heapq.heappush(self.minheap, (current_price, timestamp))


        return current_price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
    

stockPrice = StockPrice()
stockPrice.update(1, 10)# // Timestamps are [1] with corresponding prices [10].
print(stockPrice.price_data_minheap)
stockPrice.update(2, 5)#  // Timestamps are [1,2] with corresponding prices [10,5].
print(stockPrice.price_data_minheap)
stockPrice.current()#     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum()#     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3)#  // The previous timestamp 1 had the wrong price, so it is updated to 3.
print(stockPrice.price_data_minheap)
                        #  // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum()#     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2)#  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
print(stockPrice.price_data_minheap)
stockPrice.minimum()#     // return 2, the minimum price is 2 at timestamp 4.