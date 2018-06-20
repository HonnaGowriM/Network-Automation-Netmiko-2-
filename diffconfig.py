from netmiko import ConnectHandler
import difflib,sys
import os

class diff_config():

    def __init__(self):
        self.old=['R1_old_Manjunath','R2_old_Manjunath','R3_old_Manjunath','R4_old_Manjunath']
        #self.fetch()
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
            savefile=open('R'+str(count)+'Manjunath',"w")
            savefile.write(outcome)
            self.res.append('R'+str(count)+'Manjunath'+'.txt')



    def compare(self):
        n=1
        self.res=['R1Manjunath', 'R2Manjunath', 'R3Manjunath', 'R4Manjunath']
        for a,b in zip(self.old,self.res):
            with open(a,'r') as f1, open(b,'r') as f2:
                diff = difflib.ndiff(f1.readlines(),f2.readlines())
                print("********Difference in R"+str(n)+'_Manjunath********')
                for line in diff:
                    if line.startswith('-'):
                        sys.stdout.write(line)
                    elif line.startswith('+'):
                        sys.stdout.write('\t\t'+line)
                n=n+1

'''
if __name__=='__main__':
    A=diff_config()
    A.fetch()
    A.compare()
'''
