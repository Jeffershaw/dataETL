# from flask import Flask, escape, request

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     name = request.args.get("name", "World")
#     return f'Hello, {escape(name)}!'

# @app.route('/hello')
# def printhello():
#     return 'H!!!'

# @app.route('/greet')
# def greet():
#     user = {'username': 'John', 'age': "20"}
#     return '''
# <html>
#     <head>
#         <title>Greeting</title>
#     </head>
#     <body>
#         <h1>Hello, ''' + user['username'] + '''!, you’re ''' + user['age'] + ''' years old.</h1>
#     </body>
# </html>'''




# if __name__ =="__main__":
#     app.run(debug=True, port=8080)

# # from flask import Flask
# # from flask import Flask
# # from flask import render_template
# # from flask import request
# # from flask import redirect
# # from flask import url_for

# # app = Flask(__name__)

# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     return render_template('index.html')



# # @app.route('/user/<name>')
# # def user(name):
# #     return '<h1>Hello, {}!</h1>'.format(name)


# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         username = request.form.get('username')
# #         password = request.form.get('password')
# #         print('login')
# #         print(request.method) #获取访问方式 GET
# #         print(request.url) #获取url http://127.0.0.1:5000/req?id=1&name=wl
# #         print(request.cookies) #获取cookies {}
# #         print(request.path)  # 获取访问路径 /req
# #         print(request.args) #获取url传过来的值  ImmutableMultiDict([('id', '1'), ('name', 'wl')])

# #         return redirect(url_for('index'))
# #     return '<h1>login!</h1>'

# # if __name__ == '__main__':

# #     print(__name__)
# #     app.run(host='0.0.0.0', port=8000)


from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Encrypt':
            # pass
            print("Encrypted")
        elif  request.form.get('Decrypt') == 'Decrypt':
            # pass # do something else
            print("Decrypted")
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")


if __name__ == '__main__':
    app.run()