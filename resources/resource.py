import json
from flask import request, Response, jsonify
from flask_restful import Resource
from database.model import User,Message,Order,brdy_cake,masterChef,wed_cake,cust_cake,orderCust,orderWed,orderBrdy,Payment,Order
class CustomersApi(Resource):
    def get(self):
        data = User.objects().to_json()
        return Response(data, mimetype='application/json', status=200)
    def post(self):
        body = request.get_json()
        u = User(Name=body["Name"],Email=body["Email"],Password=body["Password"]).save()
        id = u.id
        return {'Added - id': str(id)}, 210

    def put(self):
        reqdata = request.get_json()
        Name = reqdata['Name']
        User.objects.get(Name=Name).update(**reqdata)
        return {'id': str(id)}, 200
class deleteUser(Resource):
    def delete(self, Name):
        User.objects.get(Name=Name).delete()
        return {'id': str(id), 'delete': 'done'}, 200
class CakeApi(Resource):
    def get(self):
        data = brdy_cake.objects().to_json()
        return Response(data, mimetype='application/json', status=200)
    def post(self):
        body = request.get_json()
        file = request.files["file"]
        c = brdy_cake(Name=body["Name"],Price=body["Price"],Quantity=body["Quantity"],Description=body['Description']).save()
        id = c.id
        return {'Added - id': str(id)}, 210
    def put(self):
        reqdata = request.get_json()
        Name = reqdata['Name']
        brdy_cake.objects.get(Name=Name).update(**reqdata)
        return {'id': str(id)}, 200
class deleteCake(Resource):
    def delete(self, Name):
        brdy_cake.objects.get(Name=Name).delete()
        return {'id': str(id), 'delete': 'done'}, 200
class CustCakeApi(Resource):
    def get(self):
        data = cust_cake.objects().to_json()
        return Response(data, mimetype='application/json', status=200)


    def post(self):
        body = request.get_json()
        c = cust_cake(Name=body["Name"],Price=body["Price"],Quantity=body["Quantity"],Description=body['Description']).save()
        id = c.id
        return {'Added - id': str(id)}, 210

    def put(self):
        reqdata = request.get_json()
        Name = reqdata['Name']
        cust_cake.objects.get(Name=Name).update(**reqdata)
        return {'id': str(id)}, 200
class deleteCustCake(Resource):
    def delete(self,Name):
        cust_cake.objects.get(Name=Name).delete()
        return {'id': str(id), 'delete': 'done'}, 200
class WedCakeApi(Resource):
    def get(self):
        data = wed_cake.objects().to_json()
        return Response(data, mimetype='application/json', status=200)
    def post(self):
        body = request.get_json()
        # image = body["c_Image"]
        # image_path = image.filename
        # image.save(image_path)
        #data = {"c_Image": image_path}
        w = wed_cake(Name=body["Name"],Price=body["Price"],Quantity=body["Quantity"],Description=body['Description']).save()
        id = w.id
        return {'Added - id': str(id)}, 210

    def put(self):
        reqdata = request.get_json()
        Name = reqdata['Name']
        wed_cake_obj = wed_cake.objects.get(Name=Name)
        wed_cake_obj.update(**reqdata)
        return {'id': str(wed_cake_obj.id)}, 200
class deleteWedCake(Resource):
    def delete(self, id):
         try:
            p = wed_cake.objects.get(id=id).delete()
            p.delete()
            return Response(p.to_json(), "Product deleted successfully", mimetype="application/json", status=200)
         except Exception as e:
            print(str(e))
class MessageApi(Resource):
    def get(self):
        data = Message.objects().to_json()
        return Response(data, mimetype='application/json', status=200)
    def post(self):
        reqdata=request.get_json()
        print(reqdata)
        mess=Message(**reqdata).save()
        id=mess.id
        return {'id':str(id)},200
class PaymentApi(Resource):
    def get(self):
        data = Payment.objects().to_json()
        return Response(data, mimetype='application/json', status=200)
    def post(self):
        reqdata=request.get_json()
        dataDB = {}
        count = 1
        for i in cart:
            dataDB.update({str(count) : i})
            count = count + 1
        print(dataDB)
        print(type(dataDB))
        pay=Order(email=reqdata['email'], order = dataDB).save()
        id=pay.id
        return {'id':str(id)},200
class masterChefApi(Resource):
    def get(self):
        data = masterChef.objects().to_json()
        return Response(data, mimetype='application/json', status=200)

    def post(self):
        body = request.get_json()
        u = masterChef(m_Name=body["m_Name"],m_Email=body["m_Email"],m_Speciality=body["m_Speciality"],m_Experience=body["m_Experience"]).save()
        id = u.id
        return {'Added - id': str(id)}, 210

    def put(self):
        reqdata = request.get_json()
        m_Name = reqdata['m_Name']
        masterChef.objects.get(m_Name=m_Name).update(**reqdata)
        return {'id': str(id)}, 200
class deleteChef(Resource):
    def delete(self, m_Name):
        masterChef.objects.get(m_Name=m_Name).delete()
        return {'id': str(id), 'delete': 'done'}, 200
class orderCustApi(Resource):
    def post(self):
        reqdata=request.get_json()
        print(reqdata)
        mess=orderCust(**reqdata).save()
        id=mess.id
        return {'id':str(id)},200
class orderBrdyApi(Resource):
    def post(self):
        reqdata=request.get_json()
        print(reqdata)
        mess=orderBrdy(**reqdata).save()
        id=mess.id
        return {'id':str(id)},200
class orderWedApi(Resource):
    def post(self):
        reqdata=request.get_json()
        print(reqdata)
        mess=orderWed(**reqdata).save()
        id=mess.id
        return {'id':str(id)},200

cart = []
class addItem(Resource):
    def post(self):
        print('post')
        if request.get_json:
            global cart
            data = request.get_json(force=True)
            print(data)
            for i in data:
                print('start',i,'i')
                cart.append(data[i])
            submitted = True
            return Response('submitted', mimetype="text/html", status=200)
        else:
            return {"error": "No JSON data found in request"}
class getPayment(Resource):
    def get(self):
        data = Order.objects().to_json()
        return Response(data, mimetype='application/json', status=200)

class getCartInfo(Resource):
    def get(self):
        global cart
        print(cart)
        return Response(json.dumps(cart), mimetype="application/json", status = 200)

class UpdateCart(Resource):
    def post(self):
        data = request.get_json(force=True)
        print(data, 'update')
        global cart
        cart = data
        print('update', cart)
        return 'done'