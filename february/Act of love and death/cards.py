import json

class Card:
    def __init__(self, index = None, name = None):
        f = open("Act of love and death\cards.json")
        self.data = json.load(f)['cards']
        f.close()
        
        if index is not None and index < len(self.data):
            self.index = index
        else:
            if name is None:
                raise ValueError("Card name is required")
            for i in range(len(self.data)):
                if self.data[i]["name"] == name:
                    self.index = i
        self.data = self.data[self.index]
    
    def print_card(self):
        for i in self.data:
            print(i + ":", self.data[i])

test = Card(0)
print(test.data)
test.print_card()