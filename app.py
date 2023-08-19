from flask import Flask, jsonify,request, render_template
from flask_restful import Api,Resource
from database import db
from resources import routes
from database .model import User,brdy_cake,wed_cake,cust_cake,masterChef
from pymongo import MongoClient
import os
from flask_session import Session

client = MongoClient("mongodb://localhost:27017/")
databasem = client["Cake"]

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/Cake'
}
api=Api(app)
db.initialize_db(app)
routes.initialize_routes(api)

@app.route('/getMessage')
def getMessage():
    data=message.objects()
    return jsonify(data)
@app.route('/addMessage' , methods=["POST"])
def addMessage():
    try:
        data=request.get_json()
        t=message(m_Name=data["m_Name"], m_Email=data["m_Email"] ,
                m_Subject=data[" m_Subject"] , m_Message=data[" m_Message"]).save()
        res={'id':str(t.id),'inserted':"done"}
    except Exception as e:
        res = {'exp': str(e), 'inserted': "failed"}

    return jsonify(res)
@app.route('/')
def home():  # put application's code here
    return render_template('Home.html', title="Home")
@app.route('/forget')
def forgetPass():  # put application's code here
    return render_template('forgetPass.html', title="forgetPass")
@app.route('/reset')
def reset():
    return render_template('passwordUpdate.html', title="passwordUpdate")
@app.route('/register')
def register():  # put application's code here
    return render_template('register.html', title="register")
@app.route('/login')
def login():  # put application's code here
    return render_template('log.html', title="log")
@app.route('/about')
def about():  # put application's code here
    return render_template('aboutUs.html', title="aboutUs")
@app.route('/terms')
def terms():  # ut application's code here
    return render_template('terms&conditions.html', title="conditions")
@app.route('/contact')
def contact():  # put application's code here
    return render_template('contact us.html', title="contact us")
@app.route('/birthday')
def birthday():  # put application's code here
    brdy_cake = databasem.brdy_cake.find()
    return render_template('Birthday.html', title="Birthday", brdy_cake=brdy_cake)
@app.route('/custom')
def custom():  # put application's code here
    cust_cake = databasem.cust_cake.find()
    return render_template('custom.html', title="custom",custcakes=cust_cake)
@app.route('/wedding')
def wedding():  # put application's code here
    wed_cake = databasem.wed_cake.find()
    return render_template('wedding.html', title="wedding", wed_cake=wed_cake)
@app.route('/team')
def team():  # put application's code here
    masterChef = databasem.masterChef.find()
    return render_template('MasterCheif.html', title="MasterCheif",masterChef=masterChef)
@app.route('/message')
def message():  # put application's code here
    return render_template('userSendMess.html', title="userSendMess")
@app.route('/payment')
def payment():  # put application's code here
    return render_template('payment.html', title="payment")
@app.route('/paymentDone')
def paymentDone():  # put application's code here
    return render_template('paymentCnfrm.html', title="paymentCnfrm")
@app.route('/user')
def user():
    return render_template('showUser.html', title="showUser")
@app.route('/adminSignIn')
def adminSignIn():
    return render_template('adminSignIn.html', title="adminSignIn")
@app.route('/passUpdate')
def passUpdtae():
    return render_template('passwordUpdate.html', title="passwordUpdate")
@app.route('/addUser')
def addUser():
    return render_template('add_User.html', title="add_User")
@app.route('/updateUser')
def updateUser():
    return render_template('update_user.html', title="update_user")
@app.route('/updateMess')
def updtaeMess():
    return render_template('usrUpdMsj.html', title="usrUpdMsj")
@app.route('/delUser')
def deleteUser():  # put application's code here
    return render_template("delUser.html", title="delUser")
@app.route('/delUserMes')
def deleteUs():  # put application's code here
    return render_template('userDltMsj.html', title="userDltMsj")
@app.route('/updateCake')
def updateCake():
    return render_template('update_cake.html', title="update_cake")
@app.route('/orderCustom',methods=["POST"])
def orderCustom():
    Email = request.form['Email']
    Password = request.form['Password']
    print(Email)
    cust_cake = databasem.cust_cake.find()
    try:
        u = User.objects().get(Email=Email, Password=Password)
    except Exception as e:
        return render_template("log.html", title="log")
    return render_template("orderCustom.html", title="orderCustom",cust_cake=cust_cake)
@app.route('/delCake')
def deleteCake(): 
    return render_template("delCake.html", title="delCake")
@app.route('/showCake')
def showCake():  # put application's code here
    return render_template("show_cake.html", title="show_cake")
@app.route('/addChef')
def addChef():
    return render_template('add_Chef.html', title="add_Chef")
@app.route('/updateChef')
def updateChef():
    return render_template('updateChef.html', title="updateChef")
@app.route('/delChef')
def deleteChef(): 
    return render_template("dltchef.html", title="dltchef")
@app.route('/showChef')
def showChef(): 
    return render_template("showChef.html", title="showChef")
@app.route('/addWed')
def addWed():
    return render_template('addWEdCake.html', title="addWEdCake")
@app.route('/updateWed')
def updateWed():
    return render_template('updateWed.html', title="updateWed")
@app.route('/delWed')
def deleteWed(): 
    return render_template("del_Wed.html", title="del_Wed")
@app.route('/showWed')
def showWed(): 
    return render_template("showWed.html", title="showWed")
@app.route('/addCust')
def addCust():
    return render_template('addCust.html', title="addCust")
@app.route('/addCake')
def addCake():
    return render_template('add_Cake.html', title="add_Cake")
@app.route('/updateCust')
def updateCust():
    return render_template('updateCust.html', title="updateCust")
@app.route('/delCust')
def deleteCust(): 
    return render_template("delCust.html", title="delCust")
@app.route('/showCust')
def showCust(): 
    return render_template("showCust.html", title="showCust")
@app.route('/orederBirthday')
def orderBirthday(): 
    brdy_cake = databasem.brdy_cake.find()
    return render_template('orderBirthdayCake.html', title="orderBirthdayCake", brdy_cake=brdy_cake)
@app.route('/orederWedding')
def orderWedding(): 
    wed_cake = databasem.wed_cake.find()
    return render_template('orderWedding.html', title="orderWedding", wed_cake=wed_cake)
@app.route('/orederCustom')
def orederCustom():
    cus_cake = databasem.cust_cake.find()
    return render_template('orderCustom.html', title="orderCustom", cust_cake=cus_cake)
@app.route("/showPayment")
def showPayment():
    return render_template('showPayment.html', title="showPayment")
@app.route("/showFeedback")
def showFeedback():
    return render_template('userFeedback.html', title="userFeedback")
if __name__ == '__main__':
    app.run(debug=True)

