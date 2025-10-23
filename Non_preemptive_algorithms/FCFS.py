import math,statistics
class FCFS:
    def __init__(self,pid,AT,BT):
        self.pid = pid
        self.AT = AT
        self.BT = BT
    
    def solveforsameAT(self):
        ct = 0
        tat = wt = 0
        total_tat = total_wt  = 0
        print(f"PID|||AT|||BT|||CT|||TAT|||WT")
        for i in range(len(self.BT)):
            ct = ct + self.BT[i]
            tat = (ct - self.AT[i])
            wt = (tat - self.BT[i])
            total_tat+=tat
            total_wt+=wt
            print(f"{self.pid[i]}|||||{self.AT[i]}|||||{self.BT[i]}||||{ct}||||{tat}|||||{wt}")

        return f"Average Turn Around Time: {str(round(total_tat/len(self.AT),2))}, Average Waiting Time: {round(total_wt/len(self.BT),2)}"

    def solve(self):
        mylst = []
        st = 0
        pct = 0
        total_tat = total_wt = total_ret=0
        for i in range(len(self.AT)):
            mylst.append(
                {
                    'pid':self.pid[i],
                    'AT':self.AT[i],
                    'BT':self.BT[i],
                    'first_start_time':-1,
                    'CT':0,
                    'TAT':0,
                    'WT':0,
                    'ReT':0
                }
            )
        mylst.sort(key=lambda x:x['AT'])
        print(f"PID|||AT|||BT|||CT|||TAT|||WT")
        for i in range(len(self.BT)):
            process = mylst[i]
            st = max(pct,process['AT'])
            process['first_start_time']=st
            ct = st + process['BT']
            process['CT'] = ct
            pct = ct
            tat = (ct - process['AT'])
            process['TAT'] = tat
            wt = (tat - process['BT'])
            process['WT'] = wt
            ret = process['first_start_time'] - process['AT']
            process['ReT'] = ret
            total_tat+=tat
            total_wt+=wt
            total_ret+=ret
            print(
            f"{process['pid']}|||||{process['AT']}||||{process['BT']}||||"
            f"{st}|||{ct}||||{tat}|||||{wt}||||{ret}"
        )
        return f"Average Turn Around Time: {str(round(total_tat/len(self.AT),2))}, Average Waiting Time: {round(total_wt/len(self.BT),2)}, Average Response Time: {str(round(total_ret/len(self.AT),2))}"
        





# obj = FCFS(pid=[1,2,3],AT=[0,0,0],BT= [5,3,8])
# print(obj.solve())
# obj = FCFS(pid=[1,2,3],AT=[2,0,4],BT= [5,3,4])
# print(obj.solve())
obj = FCFS(pid=[1,2,3],AT=[5,3,0],BT= [3,1,2])
print(obj.solve())