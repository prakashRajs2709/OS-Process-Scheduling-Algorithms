import math,statistics
class FCFS:
    def __init__(self,AT,BT):
        self.AT = AT
        self.BT = BT
    
    def solveforsameAT(self):
        ct = 0
        tat = wt = 0
        total_tat = total_wt = 0
        for i in range(len(self.BT)):
            ct = ct + self.BT[i]
            tat = (ct - self.AT[i])
            wt = (tat - self.BT[i])
            total_tat+=tat
            total_wt+=wt
            print(f"AT: {self.AT[i]}, BT: {self.BT[i]}, CT: {ct}, TAT: {tat}, WT: {wt}")

        return f"Same : Average Turn Around Time: {str(round(total_tat/len(self.AT),2))}, Average Waiting Time: {round(total_wt/len(self.BT),2)}"

    def solvefordifferentAT(self):
        mylst = []
        ct = 0
        tat = 0
        wt = 0
        st = 0
        pct = 0
        total_tat = total_wt = 0
        for i in range(len(self.AT)):
            mylst.append(
                {
                    'AT':self.AT[i],
                    'BT':self.BT[i]
                }
            )
        mylst.sort(key=lambda x:x['AT'])
        for i in range(len(self.BT)):
            st = max(pct,mylst[i]['AT'])
            ct = st + mylst[i]['BT']
            pct = ct
            tat = (ct - mylst[i]['AT'])
            wt = (tat - mylst[i]['BT'])
            total_tat+=tat
            total_wt+=wt
            print(f"AT: {mylst[i]['AT']}, BT: {mylst[i]['BT']}, CT: {ct}, TAT: {tat}, WT: {wt}")
        return f" Different: Average Turn Around Time: {str(round(total_tat/len(self.AT),2))}, Average Waiting Time: {round(total_wt/len(self.BT),2)}"
        





# obj = FCFS(AT=[0,0,0],BT= [5,3,8])
# print(obj.solveforsameAT())
# obj = FCFS(AT=[0,0,0],BT= [5,3,8])
# print(obj.solvefordifferentAT())
# obj = FCFS(AT=[2,0,4],BT= [5,3,4])
# print(obj.solvefordifferentAT())
# obj = FCFS(AT=[5,3,0],BT= [3,1,2])
# print(obj.solvefordifferentAT())