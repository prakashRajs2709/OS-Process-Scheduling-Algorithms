class Round_Robin:
    def __init__(self,AT,BT, TQ):
        self.AT = AT
        self.BT = BT
        self.TQ = TQ
    
    def solve(self):
        AT = self.AT
        BT = self.BT
        TQ = self.TQ
        n = len(AT)
        mylst = []
        for i in range(len(AT)):
            mylst.append(
                {
                    "processindex":i+1,
                    "AT": AT[i],
                    "BT": BT[i],
                    "CT":0,
                    "TAT":0,
                    "WT":0
                }
            )
        for process in mylst:
            process['BT']-=TQ
            print(process['BT'], process['CT'])




obj = Round_Robin(AT = [0,0,0], BT = [4,5,3], TQ = 2)
obj.solve()