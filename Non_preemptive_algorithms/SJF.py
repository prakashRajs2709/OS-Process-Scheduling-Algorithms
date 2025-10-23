from collections import deque


class SJF:
    def __init__(self,pid,AT,BT):
        self.pid = pid
        self.AT = AT
        self.BT = BT


    def solve(self):
        n = len(self.AT)
        mylst = []
        total_tat = total_wt = total_ret = 0
        for i in range(len(self.AT)):
            mylst.append(
                {
                    "pid":self.pid[i],
                    "AT": self.AT[i],
                    "BT": self.BT[i],
                    "RT": self.BT[i],
                    "CT":0,
                    "TAT":0,
                    "WT":0,
                    "ReT":0,
                    'is_Started':False,
                }
            )
        mylst.sort(key=lambda x:x['AT'])
        ct = 0
        completed_processes = []
        process_index = 0
        ready_queue = []
        while len(completed_processes)<n:
            while process_index<n and mylst[process_index]['AT']<=ct:
                ready_queue.append(mylst[process_index])
                process_index+=1

            if ready_queue:
                ready_queue.sort(key=lambda x:x['BT'])
                cur_process = ready_queue.pop(0)
            
                if not cur_process['is_Started']:
                    cur_process['ReT'] = ct - cur_process['AT']
                    cur_process['is_Started']=True
                    total_ret+=cur_process['ReT']
                
                ct+=cur_process['BT']

                cur_process['CT']=ct
                cur_process['TAT'] = cur_process['CT'] - cur_process['AT']
                cur_process['WT'] = cur_process['TAT'] - cur_process['BT']
                total_tat+=cur_process['TAT']
                total_wt+=cur_process['WT']

                completed_processes.append(cur_process)
            
            else:
                if process_index<n:
                    ct = mylst[process_index]['AT']
                else:
                    break
        avg_tat = total_tat / n
        avg_wt = total_wt / n
        avg_ret = total_ret / n
        mylst.sort(key=lambda x:x['pid'])
        print(f"PID|||AT|||BT|||CT|||TAT|||WT|||ReT")
        for process in mylst:
            print(f"{process['pid']}|||||{process['AT']}||||{process['BT']}||||{process['CT']}|||||{process['TAT']}||||{process['WT']}|||||{process['ReT']}")
        return f"Average Turn Around Time: {str(round(avg_tat,2))}, Average Waiting Time: {round(avg_wt,2)}, Average Response Time: {round(avg_ret,2)}"


# obj = SJF(pid=[1,2,3],AT=[0,2,4],BT=[6,8,3])
# print(obj.solve())

# obj = SJF(pid=[1,2,3,4],AT=[1,2,1,4],BT=[3,4,2,4])
# print(obj.solve())