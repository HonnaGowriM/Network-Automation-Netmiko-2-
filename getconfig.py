from datetime import datetime
from netmiko import ConnectHandler

class config():

    def __init__(self):
        self.res=[]

    def fetch(self):
        self.res=[]
        IP=['198.51.100.1','198.51.101.2','198.51.101.3','172.16.1.3']
        username='Honna'
        password='LAB'
        count=0
        for num in IP:
            #print("SSHing into: "+str(num))
            self.name='R'+str(count)+'Manjunath'
            self.name={
                'device_type':'cisco_ios',
                'ip':num,
                'username':username,
                'password':password,
                 }
            count=count+1

            conn=ConnectHandler(**self.name)
            outcome=conn.send_command("show run")
            a=datetime.now()
            savefile=open('R'+str(count)+'Manjunath'+'_'+str(a),"w")
            savefile.write(outcome)
            savefile1=open('R'+str(count)+'_old_Manjunath',"w")
            savefile1.write(outcome)
            self.res.append('R'+str(count)+'Manjunath'+'_'+str(a)+'.txt')
        return(self.res)


'''
if __name__=='__main__':
    Start=config()
    Start.fetch()
'''
