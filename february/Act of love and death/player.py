class Player:
    def __init__(self):
        self.deck = []
        self.origin = None
        #stats
        self.hp = 100
        self.stun = 0
        self.distance = 1
        #equipment
        self.left_hand = None       #slot for weapon
        self.right_hand = None      #slot for weapon
        self.mind = None            #slot for hacking device
        self.head = None            #slot for headgear
        self.chest = None           #slot for chestpiece
        self.legs = None            #slot for pants
        