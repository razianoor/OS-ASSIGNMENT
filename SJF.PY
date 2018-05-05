
global clock_cycles
import operator




#''''''''''''''''''''''''''''''''''''''
#           PROCESS CLASS  
class process:
    
    #         INIT METHOD             #
    def ___init___(self,arrival_time=0,burst_time=0,tburst=0,finish_time=0,start_time=-1,wait_time=0,turnaround_t=0):

        self.arrival_time=arrival_time
        self.burst_time=burst_time
        self.tburst=tburst
        self.finish_time=finish_time
        self.start_time=start_time
        self.wait_time=wait_time
        self.turnaround_time=turnaround_t
#''''''''''''''''''''''''''''''''''''''''


#'''''''''''''''''''''''''''''''''''''''
#       display 

def display(ready_queue):
    i=1
    
    print('\n\n\n\n\nPROCESSES  |   WAIT TIME   |   BUSRT TIME   |  ARRIVAL TIME  |  START TIME  |  FINISH TIME  |TURNAROUND TIME ')
    for p in ready_queue:
        print ('   p '+str(i)+'     '+'{:^15}'.format(p.wait_time)+'  '+'{:^15}'.format(p.burst_time)+'   '+'{:^15}'.format(p.arrival_time)+' '+'{:^15}'.format(p.start_time)+''+'{:^15}'.format(p.finish_time)+'{:^15}'.format(p.finish_time))
        i+=1
    
#'''''''''''''''''''''''''''''''''''''''

#''''''''''''''''''''''''''''''''''''''
#          SORT QUEUE
def sort(ready_queue,f):
                 #SORTING QUEUE BY ARRIVAL TIME 
      ready_queue.sort(key=lambda x:x.arrival_time,reverse=f)

#''''''''''''''''''''''''''''''''''''''''
#          SORTING---->BURST TIME
def bsort(ready_queue,f):
      
      ready_queue.sort(key=lambda x:x.burst_time,reverse=f)





#''''''''''''''''''''''''''''''''''''''
#          INPUT QUEUE METHOD
def input_queue(ready_queue):
        total_no_of_process= input ('ENTER TOTAL NUMBER OF PROCESSES TO BE QUEUED : ')
        for i in range(0,total_no_of_process):
            a=input('ENTER PROCESS '+str(i+1)+' ARRIVAL TIME : ')
            b=input('ENTER PROCESS '+str(i+1)+' BURST TIME : ')
            print ("\n")
            p=process()
            p.arrival_time=a
            p.burst_time=b
            p.tburst=b
            p.start_time=-1
            p.wait_time=0
            p.finish_time=0
            p.turnaround_time=0
            ready_queue.append(p)

        import os
        os.system('cls')

#''''''''''''''''''''''''''''''''''''''
def same_arr_time_p(ready_queue,p_queue,t):
    flag=True 
    while(flag and len(ready_queue)):        
                    p=ready_queue.pop()
                    if(p.arrival_time==t):
                        p_queue.append(p)
                    else:
                        ready_queue.append(p)
                        flag=False


#-------------------------------------------------------------------------------------------------------------------------------
ready_queue=[]               #READY QUEUE    
input_queue(ready_queue)     #LOADING PROCESSES
sort(ready_queue,True)            #SORTING QUEUE BY ARRIVAL TIME 
clock_cycles=0               #cpu ticks

p_queue=[]
executed_processes=[]

wflag=True
check=True

while(len(ready_queue) or len(p_queue)):
    
    if(len(ready_queue)):
    #---------------------------------------------------------------------------------------------------
        p=ready_queue.pop()
        #boundry
        if(p.arrival_time>clock_cycles and check):
            check=False
            while(p.arrival_time!=clock_cycles):
                clock_cycles+=1
            p_queue.append(p)
            same_arr_time_p(ready_queue,p_queue,p.arrival_time)#inqueueing same arrival time processes
           
        #process doesn't arrive yet to queue in p_queue
        elif(p.arrival_time>clock_cycles):
            ready_queue.append(p)
        #p_queue enqueue
        else:

            p_queue.append(p)
            same_arr_time_p(ready_queue,p_queue,p.arrival_time) #inqueueing same arrival time processes
            t=len(p_queue)-1
            if(len(ready_queue)):
                while(ready_queue[t].arrival_time<=clock_cycles and len(ready_queue)):
                    p=ready_queue.pop()
                    p_queue.append(p)
                    same_arr_time_p(ready_queue,p_queue,p.arrival_time) #inqueueing same arrival time processes
                    t-=1           
    #--------------------------------------------------------------------------------------------------------    
    #(min(ready_queue,key=lambda x: x.burst_time)

    bsort(p_queue,True)            #SORTING QUEUE BY BURST TIME #sort array in desc order on busrt time
    if(len(ready_queue)):
        #----------------------------------------------------------------------------------------------

        runing_process=p_queue.pop()

        
        while(runing_process.tburst > 0):

            #if(ready_queue[i].arrival_time>clock_cycles):
            #    clock_cycles+=1
                if(runing_process.start_time==-1):
                    runing_process.start_time=clock_cycles
                clock_cycles +=1
                runing_process.tburst-=1


                if(runing_process.tburst==0):
                    runing_process.finish_time=clock_cycles            
        if wflag:
            runing_process.wait_time=0
            wflag=False
        else:
            runing_process.wait_time=runing_process.start_time - runing_process.arrival_time #wait time
            runing_process.turnaround_time=runing_process.finish_time-runing_process.arrival_time  #turnaround time
       
        executed_processes.append(runing_process)

        #-----------------------------------------------------------------------------------------------
    else:
        #-----------------------------------------------------------------------------------------------
        while(p_queue):
            
            runing_process=p_queue.pop()

            while(runing_process.tburst > 0):

            #if(ready_queue[i].arrival_time>clock_cycles):
            #    clock_cycles+=1
                if(runing_process.start_time==-1):
                    runing_process.start_time=clock_cycles
                clock_cycles +=1
                runing_process.tburst-=1


                if(runing_process.tburst==0):
                    runing_process.finish_time=clock_cycles            
            if wflag:
                runing_process.wait_time=0
                wflag=False
            else:
                runing_process.wait_time=runing_process.start_time - runing_process.arrival_time #wait time
                runing_process.turnaround_time=runing_process.finish_time-runing_process.arrival_time  #turnaround time
       
            executed_processes.append(runing_process)

       #-----------------------------------------------------------------------------------------------
 

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

#-------------------------------------------_--------------------------------------------------------------
