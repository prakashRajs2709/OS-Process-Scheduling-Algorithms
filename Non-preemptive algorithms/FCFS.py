import math,statistics
class FCFS:
    def __init__(self,AT,BT):
        self.AT = AT
        self.BT = BT
    
    def solveforsameAT(self):
        ct = 0
        rem = tat = 0
        wt = 0
        for i in range(len(self.BT)):
            ct = ct + self.BT[i]
            tat = tat + (ct - self.AT[i])
            wt = wt + (tat - self.BT[i] - rem)
            rem = tat
        return f"Average Turn Around Time: {str(round(tat/len(self.AT),2))}, Average Waiting Time: {round(wt/len(self.BT),2)}"

    def solvefordifferentAT(self):
        mylst = []
        ct = 0
        rem = tat = 0
        wt = 0
        for i in range(len(self.AT)):
            mylst.append(
                {
                    'AT':self.AT[i],
                    'BT':self.BT[i]
                }
            )
        mylst.sort(key=lambda x:x['AT'])
        for i in range(len(self.BT)):
            ct = ct + mylst[i]['BT']
            tat = tat + (ct - mylst[i]['AT'])
            wt = wt + (tat - mylst[i]['BT'] - rem)
            rem = tat
        return f"Average Turn Around Time: {str(round(tat/len(self.AT),2))}, Average Waiting Time: {round(wt/len(self.BT),2)}"
        





# obj = FCFS(AT=[0,0,0],BT= [5,3,8])
# print(obj.solveforsameAT())
# obj = FCFS(AT=[2,0,4],BT= [5,3,4])
# print(obj.solvefordifferentAT())