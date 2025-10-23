class Round_Robin:
    def __init__(self,pid,AT,BT, TQ):
        self.pid = pid
        self.AT = AT
        self.BT = BT
        self.TQ = TQ
    
    def solve(self):
        pid = self.pid
        AT = self.AT
        BT = self.BT
        TQ = self.TQ
        n = len(AT)
        mylst = []
        for i in range(len(AT)):
            mylst.append(
                {
                    "pid":pid[i],
                    "AT": AT[i],
                    "BT": BT[i],
                    "CT":0,
                    "TAT":0,
                    "WT":0
                }
            )
        for process in mylst:
            print(f"PID|||AT|||BT|||CT|||TAT|||WT")
            print(f"{process['pid']}|||||{process['AT']}||||{process['BT']}||||{process['CT']}|||||{process['TAT']}||||{process['WT']}")




obj = Round_Robin(pid = [1,2,3],AT = [0,0,0], BT = [4,5,3], TQ = 2)
obj.solve()