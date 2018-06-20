from netmiko import ConnectHandler

class OSPF():
    def __init__(self):
        self.i=0

    def begin1(self,user,password,process_id,network,area1,loopip):
        self.user=user
        self.password=password
        self.process_id=process_id
        self.network=network
        self.area1=area1
        self.loopip=loopip

        COMMAND=['router ospf '+str(self.process_id),'network '+str(self.loopip)+' 0.0.0.0 area '+str(self.area1),'network '+str(self.network[0])+' 0.0.0.255 area '+str(self.area1),'network '+str(self.network[1])+' 0.0.0.255 area '+str(self.area1)]
        print(COMMAND)
        self.name='R_Manjunath'
        self.name={
            'device_type':'cisco_ios',
            'ip':'198.51.100.1',
            'username':self.user,
            'password':self.password,
             }
        conn=ConnectHandler(**self.name)
        output = conn.send_config_set(COMMAND)
        print("Sent1")

    def begin2(self,user,password,process_id,network,area,loopip):
        self.user=user
        self.password=password
        self.process_id=process_id
        self.network=network
        self.area=area
        self.loopip=loopip

        COMMAND2=['router ospf '+str(self.process_id),'maximum paths 2','network '+str(self.loopip)+' 0.0.0.0 area '+str(self.area[0]),'network '+str(self.network[0])+' 0.0.0.255 area '+str(self.area[0]),'network '+str(self.network[1])+' 0.0.0.255 area '+str(self.area[1])]
        print(COMMAND2)
        self.name='R_Manjunath'
        self.name={
            'device_type':'cisco_ios',
            'ip':'198.51.101.2',
            'username':self.user,
            'password':self.password,
             }
        conn=ConnectHandler(**self.name)
        output = conn.send_config_set(COMMAND2)
        print("Sent2")

    def begin3(self,user,password,process_id,network,area,loopip):
        self.user=user
        self.password=password
        self.process_id=process_id
        self.network=network
        self.area=area
        self.loopip=loopip

        COMMAND3=['router ospf '+str(self.process_id),'network '+str(self.loopip)+' 0.0.0.0 area '+str(self.area),'network '+str(self.network)+' 0.0.0.255 area '+str(self.area)]
        print(COMMAND3)
        self.name='R_Manjunath'
        self.name={
            'device_type':'cisco_ios',
            'ip':'172.16.1.3',
            'username':self.user,
            'password':self.password,
             }
        conn=ConnectHandler(**self.name)
        output = conn.send_config_set(COMMAND3)
        print("Sent3")


    def begin4(self,user,password,process_id,network,area,loopip):
        self.user=user
        self.password=password
        self.process_id=process_id
        self.network1=network
        self.area1=area
        self.loopip=loopip


        print(self.area1[0])
        COMMAND4=['router ospf '+str(self.process_id),'maximum paths 2','network '+str(self.loopip)+' 0.0.0.0 area '+str(self.area1[0]),'network '+str(self.network1[0])+' 0.0.0.255 area '+str(self.area1[0]),'network '+str(self.network1[1])+' 0.0.0.255 area '+str(self.area1[1])]
        print(COMMAND4)
        self.name='R_Manjunath'
        self.name={
            'device_type':'cisco_ios',
            'ip':'198.51.101.3',
            'username':self.user,
            'password':self.password,
             }
        conn=ConnectHandler(**self.name)
        output = conn.send_config_set(COMMAND4)
        print("Sent4")

    def neiout(self):
        IP=['198.51.101.2','198.51.101.3']
        user=['Honna','Honna']
        password=['LAB','LAB']

        n=0
        for num,name,pwd in zip(IP,user,password):
            if num:
                CISCO_ROUTER={
                    'device_type':'cisco_ios',
                    'ip':num,
                    'username':name,
                    'password':pwd,
                     }
                conn=ConnectHandler(**CISCO_ROUTER)
                out=conn.send_command("show ip ospf neighbor")
                openhandle=open(str(n)+'ospf.txt','w')
                openhandle.write(out)
                openhandle.close()
                n=n+1
        self.FILE()


    def FILE(self):
        ID=[]
        State=[]
        Interface=[]
        file=open('0ospf.txt','r')
        handle=file.readlines()[2:]
        for i in handle:
            if i:
                ID.append(i.split()[0])
                State.append(i.split()[2])
                Interface.append(i.split()[5])

        print("RESULTS FOR R2")
        print("*"*70)
        print ("Neighbor ID" +'          '+  "State" + '              ' + "Interface" )
        print("*"*70)
        print(str(ID[0]) +'             '+ str(State[0])  + '                ' +  str(Interface[0]))
        print("\n")
        print(str(ID[1]) +'             '+ str(State[1])  + '                ' +  str(Interface[1]))
        print("\n")
        print(str(ID[2]) +'             '+ str(State[2])  + '                ' +  str(Interface[2]))
        print("\n")
        print(str(ID[3]) +'             '+ str(State[3])  + '                ' +  str(Interface[3]))
        print("\n")


        ID2=[]
        State2=[]
        Interface2=[]
        file=open('1ospf.txt','r')
        handle=file.readlines()[2:]
        for i in handle:
            if i:
                ID2.append(i.split()[0])
                State2.append(i.split()[2])
                Interface2.append(i.split()[5])



        print("RESULTS FOR R4")
        print("*"*70)
        print ("Neighbor ID" +'          '+  "State" + '              ' + "Interface" )
        print("*"*70)
        print(str(ID2[0]) +'             '+ str(State2[0])  + '                ' +  str(Interface2[0]))
        print("\n")
        print(str(ID2[1]) +'             '+ str(State2[1])  + '                ' +  str(Interface2[1]))
        print("\n")
        print(str(ID2[2]) +'             '+ str(State2[2])  + '                ' +  str(Interface2[2]))
        print("\n")
        print(str(ID2[3]) +'             '+ str(State2[3])  + '                ' +  str(Interface2[3]))
        print("\n")

    def ping(self):
        CISCO_ROUTER={
                    'device_type':'cisco_ios',
                    'ip':'198.51.100.1',
                    'username':'Honna',
                    'password':'LAB',
                     }
        conn=ConnectHandler(**CISCO_ROUTER)
        output = conn.send_command("ping 30.0.0.1")

        print(output)
        if "Success rate is 0 percent (0/5)" in output:
            return ("OSPF has not been successfully configured")
        else:
            return("OSPF has  been successfully configured")


if __name__=='__main__':
    call=OSPF()
    call.ping()

