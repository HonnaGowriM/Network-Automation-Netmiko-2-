import getconfig
import ospfconfig
import diffconfig
from flask import Flask, render_template,redirect, url_for, request
app = Flask(__name__)

handle=getconfig.config()
handle2=ospfconfig.OSPF()
handle3=diffconfig.diff_config()

@app.route("/")
def hello():
    return '''
    <html>
    <head>
        <title>AUTOMATION - 2</title>
    </head>
    <body>
        <h1>Hello</h1>
        <a href="link1">Click here to gets the config of the routers</a> <br />
        <a href="link2">Click here to configure OSPF </a> <br />
        <a href="link7">Click here to gets the details in the difference of config of the routers</a> <br /><br /><br /><br />
        <a href="link8">Click here post OSPF configuration to print the neighbour details of R2 and R4</a><br />
        <a href="link9">Click here post OSPF configuration to view the ping results</a>
    </body>
</html>
        '''

@app.route('/link1' )
def get():
    a=handle.fetch()
    print(a)
    return render_template('test.html', name =a )


@app.route('/link2',methods = ['POST', 'GET'])
def details():
    return '''
    <html>
    <head>
        <title>AUTOMATION - 2</title>
    </head>
    <body>
        <h1>OSPF</h1>
        <a href="link3">Click here configure OSPF for the R1</a> <br />
        <a href="link4">Click here configure OSPF for the R2</a> <br />
        <a href="link5">Click here configure OSPF for the R3</a> <br />
        <a href="link6">Click here configure OSPF for the R4</a> <br />
    </body>
</html>
        '''


'''
R1 CONFIGURATION
'''
@app.route('/link3',methods = ['POST', 'GET'])
def R1():
    network=[]
    if request.method=='POST':
        user=request.form['USERNAME']
        password=request.form['PASSWORD']
        process_id=request.form['PROCESS']
        network1=request.form['NETWORK_1']
        network2=request.form['NETWORK_2']
        area1=request.form['AREA']
        loopip=request.form['IP']
        network.append(network1)
        network.append(network2)
        go=handle2.begin1(user,password,process_id,network,area1,loopip)
        return'''
        <html>
    <body>
        <h1>Thanks for the update kindly fill in the details for R2,R3 and R4 routers respectively.Ignore if already filled.</h1>
        <a href="link">Click here to go back</a> <br />
    </body>
</html>
        '''
    return render_template("details.html")

'''
R2 CONFIGURATION
'''

@app.route('/link4',methods = ['POST', 'GET'])
def R2():
    network=[]
    area=[]
    if request.method=='POST':
        user=request.form['USERNAME']
        password=request.form['PASSWORD']
        process_id=request.form['PROCESS']
        network1=request.form['NETWORK_1']
        network2=request.form['NETWORK_2']
        area1=request.form['AREA_1']
        area2=request.form['AREA_2']
        loopip=request.form['IP']
        network.append(network1)
        network.append(network2)
        area.append(area1)
        area.append(area2)
        go2=handle2.begin2(user,password,process_id,network,area,loopip)
        #work(user,password,process_id,network,area,loopip)
        return'''

        <html>
    <body>
        <h1>Thanks for the update kindly fill in the details for R1,R3 and R4 routers respectively. Ignore if already filled.</h1>
        <a href="link">Click here to go back</a> <br />
    </body>
</html>
        '''
    return render_template("details2.html")


'''
R4 CONFIGURATION
'''

@app.route('/link6',methods = ['POST', 'GET'])
def R4():
    network=[]
    area=[]
    if request.method=='POST':
        user=request.form['USERNAME']
        password=request.form['PASSWORD']
        process_id=request.form['PROCESS']
        network1=request.form['NETWORK_1']
        network2=request.form['NETWORK_2']
        area1=request.form['AREA_1']
        area2=request.form['AREA_2']
        loopip=request.form['IP']
        network.append(network1)
        network.append(network2)
        area.append(area1)
        area.append(area2)
        go4=handle2.begin4(user,password,process_id,network,area,loopip)
        return'''

        <html>
    <body>
        <h1>Thanks for the update kindly fill in the details for R2,R3 and R1 routers respectively.Ignore if already filled.</h1>
        <a href="link">Click here to go back</a> <br />
    </body>
</html>
        '''
    return render_template("details4.html")


'''
R3 CONFIGURATION
'''

@app.route('/link5',methods = ['POST', 'GET'])
def R3():
    if request.method=='POST':
        user=request.form['USERNAME']
        password=request.form['PASSWORD']
        process_id=request.form['PROCESS']
        network=request.form['NETWORK_1']
        area=request.form['AREA']
        loopip=request.form['IP']
        go3=handle2.begin3(user,password,process_id,network,area,loopip)
        return'''
        <html>
    <body>
        <h1>Thanks for the update kindly fill in the details for R2,R1 and R4 routers respectively.Ignore if already filled.</h1>
        <a href="link">Click here to go back</a> <br />
    </body>
</html>
        '''
    return render_template("details3.html")

@app.route('/link')
def do():
    return redirect(url_for('details'))


@app.route('/link8')
def out():
    handle2.neiout()
    return("Output will be present on the console")

@app.route('/link9')
def inside():
    a=handle2.ping()
    return (a)

@app.route('/link7')
def inside_outside():
    handle3.fetch()
    handle3.compare()
    return("Output will be present on the console")





if __name__ == "__main__":
    app.run()
