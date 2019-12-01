class Item:
    def __init__(self,ID,weight,benefit):
        self.ID=ID
        self.weight=weight
        self.benefit=benefit
        self.value=float(weight)/float(benefit)

class Knapsack:
    def __init__(self,max_weight):
        self.current_weight=0
        self.max_weight=max_weight
        self.items=[]

    def add_item(self,item):
        self.current_weight+=item.weight
        self.items.append(item)

    def print_items(self):
        

def main():
    max_weight=int(input("Enter the maximum weight"))
    k=Knapsack(max_weight)
    
if(__name__=="__main__"):
    main()
        
