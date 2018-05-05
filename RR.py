global clock_cycles
import operator
#''''''''''''''''''''''''''''''''''''''
#           PROCESS CLASS  
class process:
    
    #         INIT METHOD             #
    def ___init___(self,arrival_time=0,burst_time=0,tburst=0,finish_time=0,start_time=-1,wait_time=0,turnaround_t=0,io_t=0,io_w=0):

        self.arrival_time=arrival_time
        self.burst_time=burst_time
        self.tburst=tburst
        self.finish_time=finish_time
        self.start_time=start_time
        self.wait_time=wait_time
        self.turnaround_time=turnaround_t
        self.io_time=io_t
        self.io_wait=io_w
#''''''''''''''''''''''''''''''''''''''''
#'''''''''''''''''''''''''''''''''''''''
#       display 
def display(ready_queue):
    i=1
    print('\n\n\n\n\nPROCESSES  |   WAIT TIME   |   BUSRT TIME   |  ARRIVAL TIME  |  START TIME  |  FINISH TIME  |TURNAROUND TIME | I/O TIME  | I/O WAIT TIME')
    for p in ready_queue:
        print ('   p '+str(i)+'     '+'{:^15}'.format(p.wait_time)+'  '+'{:^15}'.format(p.burst_time)+'   '+'{:^15}'.format(p.arrival_time)+' '+'{:^15}'.format(p.start_time)+''+'{:^15}'.format(p.finish_time)+'{:^15}'.format(p.turnaround_time)+'{:^15}'.format(p.io_time)+'{:^15}'.format(p.io_wait))
        i+=1
#'''''''''''''''''''''''''''''''''''''''
#''''''''''''''''''''''''''''''''''''''
#          SORT QUEUE
def sort(ready_queue,f):
                 #SORTING QUEUE BY ARRIVAL TIME 
      ready_queue.sort(key=lambda x:x.arrival_time,reverse=f)

#''''''''''''''''''''''''''''''''''''''''

#''''''''''''''''''''''''''''''''''''''
#          INPUT QUEUE METHOD
def input_queue(ready_queue):
        total_no_of_process= input ('ENTER TOTAL NUMBER OF PROCESSES TO BE QUEUED : ')
       
        for i in range(0,total_no_of_process):
            a=input('ENTER PROCESS '+str(i+1)+' ARRIVAL TIME : ')
            b=input('ENTER PROCESS '+str(i+1)+' BURST TIME : ')
            c=input('ENTER TIME AFTER WHICH IT WILL GO FOR INPUT/OUTPUT : ')
            d=input('ENTER TIME FOR WHICH PROCESS WILL SATY FOR  INPUT/OUTPUT : ')

            print ("\n")
            p=process()
            p.arrival_time=a
            p.burst_time=b
            p.tburst=b
            p.io_time=c
            p.io_wait=d
           
            p.start_time=-1
            p.wait_time=0
            p.finish_time=0
            p.turnaround_time=0
            p.io_time=c
            p.io_wait=d
            ready_queue.append(p)

        import os
        os.system('cls')

#''''''''''''''''''''''''''''''''''''''
def same_arr_time_p(ready_queue,p_queue,t):
    flag1=True 
    while(flag1 and len(ready_queue)):        
                    p=ready_queue.pop()
                    if(p.arrival_time==t):
                        p_queue.insert(0,p)
                    else:
                        ready_queue.append(p)
                        flag1=False

#-------------------------------------------------------------------------------------------------------------------------------

ready_queue=[]               #READY QUEUE    
quantum_time=input('ENTER PROCESSER QUANTUM TIME : ')
input_queue(ready_queue)     #LOADING PROCESSES
sort(ready_queue,True)            #SORTING QUEUE BY ARRIVAL TIME 
clock_cycles=0   
p_queue=[]
executed_processes=[]
            #cpu ticks
RUNING_PROCESS=False
flag=True
wflag=True
check=True
sflag=True
while(len(ready_queue) or len(p_queue)):
    
    if(ready_queue):
    #---------------------------------------------------------------------------------------------------
        p=ready_queue.pop()
        #boundry
        if(p.arrival_time>clock_cycles and check):
            check=False
            while(p.arrival_time!=clock_cycles):
                clock_cycles+=1
            p_queue.insert(0,p)
            same_arr_time_p(ready_queue,p_queue,p.arrival_time)#inqueueing same arrival time processes
        #process doesn't arrive yet to queue in p_queue
        elif(p.arrival_time>clock_cycles and len(p_queue)==0):
              while(p.arrival_time!=clock_cycles):
                  clock_cycles+=1
              ready_queue.append(p)
        #p_queue enqueue
        else:
            p_queue.insert(0,p)
            same_arr_time_p(ready_queue,p_queue,p.arrival_time) #inqueueing same arrival time processes 
            t=len(ready_queue)-1
            if(ready_queue):
                while(ready_queue and t>-1 and ready_queue[t].arrival_time<=clock_cycles ):
                    p=ready_queue.pop()
                    p_queue.insert(0,p)
                    same_arr_time_p(ready_queue,p_queue,p.arrival_time) #inqueueing same arrival time processes
                    t-=1           
    #--------------------------------------------------------------------------------------------------------    
   
    if(ready_queue):
        #----------------------------------------------------------------------------------------------
        if(p_queue):
           
            runing_process=p_queue.pop()
            if(runing_process.tburst<=quantum_time and runing_process.tburst>0):
                if(sflag):
                    runing_process.start_time=clock_cycles
                    sflag=False
                clock_cycles+=runing_process.tburst
                runing_process.finish_time=clock_cycles
                runing_process.tburst=0
                flag=True
            elif(runing_process.tburst>quantum_time):
                if(sflag):
                    runing_process.start_time=clock_cycles
                    sflag=False
                runing_process.tburst-=quantum_time
                clock_cycles+=quantum_time
                p_queue.insert(0,runing_process)
            if(runing_process.tburst==0 and flag==True):
                runing_process.wait_time=clock_cycles - runing_process.arrival_time - runing_process.burst_time
                runing_process.turnaround_time=clock_cycles - runing_process.arrival_time
                executed_processes.append(runing_process)
                sflag=True           
                

    else:
        #-----------------------------------------------------------------------------------------------
        while(p_queue):

            runing_process=p_queue.pop()
            if(runing_process.tburst<=quantum_time and runing_process.tburst>0):
                if(sflag):
                    runing_process.start_time=clock_cycles
                    sflag=False
                clock_cycles+=runing_process.tburst
                runing_process.finish_time=clock_cycles
                runing_process.tburst=0
                flag=True
            elif(runing_process.tburst>quantum_time):
                if(sflag):
                    runing_process.start_time=clock_cycles
                    sflag=False
                runing_process.tburst-=quantum_time
                clock_cycles+=quantum_time
                p_queue.insert(0,runing_process)
            if(runing_process.tburst==0 and flag==True):
                runing_process.wait_time=clock_cycles - runing_process.arrival_time - runing_process.burst_time
                runing_process.turnaround_time=clock_cycles - runing_process.arrival_time
                executed_processes.append(runing_process)
                sflag=True           
       #---------------------------------------------------------------------------------------
display(executed_processes)
sum=0
sumt=0
for i in executed_processes:
    sum+=i.wait_time
    sumt+=i.turnaround_time
ave=sum/len(executed_processes)
avet=sumt/len(executed_processes)
print ('\n\n\nAVERAGE WAITING TIME : '+str(ave)) 
print ('\nAVERAGE TURNAROUND TIME : '+str(avet))

#---------------------------------------------------------------------------------------------------------------------- 
