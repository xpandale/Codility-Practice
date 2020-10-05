'''
https://www.testdome.com/questions/python/train-composition/40609?visibility=3&skillId=9&orderBy=Difficulty
A TrainComposition is built by attaching and detaching wagons from the left and the right sides, efficiently with respect to time used.

For example, if we start by attaching wagon 7 from the left followed by attaching wagon 13, again from the left, we get a composition of two wagons (13 and 7 from left to right). Now the first wagon that can be detached from the right is 7 and the first that can be detached from the left is 13.

Implement a TrainComposition that models this problem.
'''

class TrainComposition:
    
    def __init__(self):
        self.wagons = {}
        self.left   = 1
        self.right  = 0
    
    def attach_wagon_from_left(self, wagonId):
        self.left -= 1
        self.wagons[self.left] = wagonId
    
    def attach_wagon_from_right(self, wagonId):
        self.right += 1
        self.wagons[self.right] = wagonId 

    def detach_wagon_from_left(self):
        if self.left > self.right:
            return None
        else:
            _id = self.wagons[self.left]
            del self.wagons[self.left]
            self.left += 1
            return _id
    
    def detach_wagon_from_right(self):
        if self.right < self.left:
            return None
        else:
            _id = self.wagons[self.right]
            del self.wagons[self.right]
            self.right -= 1
            return _id

if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right()) # should print 7
    print(train.detach_wagon_from_left()) # should print 13
