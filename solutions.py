def count_values(lis):
    unique_lis = [None]*len(lis)
    unique_count = 0

    #Store unique values in a list
    for i in range(len(lis)):
        unique = True
        for j in range(len(lis)):
            if lis[i] == unique_lis[j]:
                unique = False

        if unique == True:
            unique_lis[unique_count] = lis[i]
            unique_count+=1

    #Counts instances of unique values in given list
    for i in range(unique_count):
        count = 0
        for j in range(len(lis)):
            if lis[j] == unique_lis[i]:
                count+=1

        print(str(unique_lis[i]) + ": " + str(count))

print("Test count_values:")
count_values(["a","a","b","c"])


class ValueCounter:

    def __init__(self):
        self.unique = []
        self.count_unique = 0
    
    def set_items(self,lis):

        self.unique = [None]*2*len(lis)

        #Store unique values in a list
        for i in range(len(lis)):
            unique_val = True
            for j in range(len(lis)):
                if lis[i] == self.unique[j]:
                    unique_val = False

            if unique_val == True:
                self.unique[self.count_unique] = lis[i]
                self.count_unique+=1

        for i in range(self.count_unique):
            count_each = 0
            for j in range(len(lis)):
                if lis[j] == self.unique[i]:
                    count_each+=1
            self.unique[self.count_unique+i] = count_each

    def print_count(self):
        for i in range(self.count_unique):
            value = self.unique[i]
            count = self.unique[self.count_unique+i]

            print(str(value) + ": " + str(count))
        pass

#Test
print("Test ValueCounter:")
value_counter = ValueCounter()
value_counter.set_items(["a","b","a","d","c","d","c","c","f","b","a","a"])
value_counter.print_count()






