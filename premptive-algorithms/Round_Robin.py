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
        for i in range(len(AT)):
            mylst.append(
                {
                    "pid":pid[i],
                    "AT": AT[i],
                    "BT": BT[i],
                    "RT": BT[i],
                    "CT":0,
                    "TAT":0,
                    "WT":0
                }
            )
        mylst.sort(key=lambda x:x['AT'])
        ct = 0
        completed_processes = []
        process_index = 0
        ready_queue = deque()
        while len(completed_processes)<n:
            while process_index<n and mylst[process_index]['AT']<=ct:
                process_index+=1
                ready_queue.append(mylst[process_index])
                print(f"Ready Queue:{ready_queue[0]}")
            
            if ready_queue:
                cur_process = ready_queue.popleft()
                time_slice = min(TQ,cur_process['RT'])
                ct+=time_slice
                cur_process['RT']-=time_slice
            break










        for process in mylst:
            print(f"PID|||AT|||BT|||CT|||TAT|||WT")
            print(f"{process['pid']}|||||{process['AT']}||||{process['BT']}||||{process['CT']}|||||{process['TAT']}||||{process['WT']}")




obj = Round_Robin(pid = [1,2,3],AT = [4,0,2], BT = [3,6,8], TQ = 2)
obj.solve()