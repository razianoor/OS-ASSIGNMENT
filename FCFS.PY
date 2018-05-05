global clock_cycles
import operator



#''''''''''''''''''''''''''''''''''''''
#           PROCESS CLASS  
class process:
    
    #         INIT METHOD             #
    def ___init___(self,arrival_time=0,burst_time=0,tburst=0,finish_time=0,start_time=-1,turnaround_time=0,wait_time=0):

        self.arrival_time=arrival_time
        self.burst_time=burst_time
        self.tburst=tburst
        self.finish_time=finish_time
        self.start_time=start_time
        self.turnaround_time=turnaround_time
        self.wait_time=wait_time

#''''''''''''''''''''''''''''''''''''''''
    
#'''''''''''''''''''''''''''''''''''''''
#       display 

def display(ready_queue):
    i=1
    
    print('\n\n\n\n\nPROCESSES  |   WAIT TIME   |  TURNAROUND TIME  |   BUSRT TIME   |  ARRIVAL TIME  |  START TIME  |  FINISH TIME')
    for p in ready_queue:
        print ('   p '+str(i)+'     '+'{:^15}'.format(p.wait_time)+'   '+'{:^15}'.format(p.turnaround_time)+'  '+'{:^15}'.format(p.burst_time)+'   '+'{:^15}'.format(p.arrival_time)+'\t'+'{:^15}'.format(p.start_time)+'\t'+'{:^15}'.format(p.finish_time))
        i+=1
   
#'''''''''''''''''''''''''''''''''''''''


#'''''''''''''''''''''''''''''''''''''''
#       TURNAROUND TIME
def calculate_turnaround_time(ready_queue):
    for i in ready_queue:
        ready_queue[i].turnaround_time=ready_queue[i].finish_time-ready_queue[i].arrival_time
   
#'''''''''''''''''''''''''''''''''''''''


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


#''''''''''''''''''''''''''''''''''''''
#          SORT QUEUE
def sort(ready_queue):
      
      ready_queue.sort(key=lambda x:x.arrival_time)

#''''''''''''''''''''''''''''''''''''''''



#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#
#    MAIN
#


ready_queue=[]               #READY QUEUE    
input_queue(ready_queue)     #LOADING PROCESSES
sort(ready_queue)            #SORTING QUEUE BY ARRIVAL TIME 
clock_cycles=0               #cpu ticks

print ready_queue[1].tburst
for i in range(0,len(ready_queue) ):

    while(ready_queue[i].tburst > 0):

        if(ready_queue[i].arrival_time>clock_cycles):
             clock_cycles+=1
        
        else:

            if(ready_queue[i].start_time==-1):
                ready_queue[i].start_time=clock_cycles


            clock_cycles +=1
            ready_queue[i].tburst-=1


            if(ready_queue[i].tburst==0):
                ready_queue[i].finish_time=clock_cycles            
    if i==0:
        ready_queue[i].wait_time=0
    else:
        ready_queue[i].wait_time=ready_queue[i-1].finish_time-ready_queue[i].arrival_time #wait time
  
   
    ready_queue[i].turnaround_time=ready_queue[i].finish_time-ready_queue[i].arrival_time  #turnaround time

display(ready_queue)   


sum=0
sumt=0
for i in ready_queue:
    sum+=i.wait_time
    sumt+=i.turnaround_time
ave=sum/len(ready_queue)
avet=sumt/len(ready_queue)
print ('\n\n\nAVERAGE WAITING TIME : '+str(ave)) 
print ('\nAVERAGE TURNAROUND TIME : '+str(avet)) 
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

 ############################################################################################################################
                                       
