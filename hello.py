from flask import Flask,render_template,redirect,request
import csv
app = Flask(__name__)

@app.route('/')
def abc():
    return render_template('index.html')

def savingMethod(data):
    with open('./Database.csv','w', newline='') as csvfile:
        
        li=['Email','Number','Name','Message','Address','Area']
        spamwriter = csv.DictWriter(csvfile, fieldnames=li)
        spamwriter.writeheader()
        spamwriter.writerow(({'Email': data['email'],'Area': data['parts'], 'Number': data['phone'],'Name':data['first-name'],'Address':data['Address'],
                              'Message':data['message']}))    
@app.route('/submit', methods=['POST', 'GET'])
def blog2():
    if(request.method == 'POST'):
        try:
            data=request.form.to_dict()
            savingMethod(data)
            return render_template('thankyu.html', name=data['first-name'])
        except:
            return "something went run, its exception"
    else:
        return 'something went wrong'
@app.route('/<username>')
def blog(username):
    return render_template(username)