from collections import deque
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
        total_tat = total_wt = total_ret = 0
        for i in range(len(AT)):
            mylst.append(
                {
                    "pid":pid[i],
                    "AT": AT[i],
                    "BT": BT[i],
                    "RT": BT[i],
                    "first_start_time": -1,
                    "CT":0,
                    "TAT":0,
                    "WT":0,
                    "ReT":0,
                }
            )
        mylst.sort(key=lambda x:x['AT'])
        ct = 0
        completed_processes = []
        process_index = 0
        ready_queue = deque()
        while len(completed_processes)<n:
            while process_index<n and mylst[process_index]['AT']<=ct:
                ready_queue.append(mylst[process_index])
                process_index+=1
            
            if ready_queue:
                cur_process = ready_queue.popleft()
                if cur_process['first_start_time']==-1:
                    cur_process['first_start_time']=ct
                time_slice = min(TQ,cur_process['RT'])
                ct+=time_slice
                cur_process['RT']-=time_slice

                while process_index<n and mylst[process_index]['AT']<=ct:
                    ready_queue.append(mylst[process_index])
                    process_index+=1
                
                if cur_process['RT']==0:
                    cur_process['CT']=ct
                    completed_processes.append(cur_process)
                else:
                    ready_queue.append(cur_process)
            
            else:
                if process_index<n:
                    ct = mylst[process_index]['AT']
        for process in completed_processes:
            process['TAT'] = process['CT'] - process['AT']
            process['WT'] = process['TAT'] - process['BT']
            process['ReT'] = process['first_start_time'] - process['AT']
            total_tat+=process['TAT']
            total_wt+=process['WT']
            total_ret+=process['ReT']
        
        print(f"PID|||AT|||BT|||CT|||TAT|||WT|||ReT")
        for process in mylst:
            print(f"{process['pid']}|||||{process['AT']}||||{process['BT']}||||{process['CT']}|||||{process['TAT']}||||{process['WT']}|||||{process['ReT']}")
        return f"Average Turn Around Time: {str(round(total_tat/len(self.AT),2))}, Average Waiting Time: {round(total_wt/len(self.BT),2)}, Average Response Time: {round(total_ret/len(self.BT),2)}"




# obj = Round_Robin(pid = [1,2,3],AT = [0,4,5], BT = [5,2,4], TQ = 2)
# print(obj.solve())

# obj = Round_Robin(pid = [1,2,3,4,5],AT = [0,1,2,3,4], BT = [5,3,1,2,3], TQ = 2)
# print(obj.solve())

# obj = Round_Robin(pid = [1,2,3,4],AT = [0,1,2,4], BT = [5,4,2,1], TQ = 2)
# print(obj.solve())

obj = Round_Robin(pid = [1,2,3,4,5,6],AT = [0,1,2,3,4,6], BT = [4,5,2,1,6,3], TQ = 2)
print(obj.solve())