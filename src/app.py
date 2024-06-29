from flask import Flask, render_template, request, Response, session, redirect, url_for
#importamos e instalamos flask de manera global.
import os

#importamos para la db
import database as db

#acceder de manera mas facil a los directorios y archivos.

#definimos la ruta absoluta del proyecto

template_dir=os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

#unimos las rutas de las carpetas src y templates a la ruta anterior

template_dir=os.path.join(template_dir, 'src','templates')

#indicamos que se busque el archivo index.html o el archivo q tengo el account al ejecutarse

app=Flask(__name__,template_folder=template_dir)

#vamos a generar nuestra primera ruta para poder ejecutar.
#ruta de la app
#@app.route('/')el decorador vincula una funcion especifica del sitio web.
#la func. home() sera la encargada de que se ejecute la pag. principal.

#importante a la primer linea de codigo agregar render_template

@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM usuarios")
    myresult = cursor.fetchall()
    #convertir los datos a diccionario.
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames,record)))
    cursor.close()
    return render_template('account.html', data=insertObject)

#Ruta para guardar usuarios en la bd
@app.route('/user_create', methods=['POST'])
def addUser():
    correo = request.form['email']
    password = request.form['passw']
    nombre = request.form['name']
    apellido = request.form['surname']
    fecha_nacimiento = request.form['fecha-nacimiento']
    genero = request.form['option_genero']
    pais = request.form['pais']
    notificaciones = request.form['notificaciones']
    terminos_condiciones = request.form['check']
#(correo, password, nivel_organizativo, nombre, apellido, fecha_nacimiento, genero, pais, notificaciones, terminos_condiciones)
    if correo and password and nombre and apellido and terminos_condiciones:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuarios (correo, password, nombre, apellido, fecha_nacimiento, genero, pais, notificaciones, terminos_condiciones) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (correo, password, nombre, apellido, fecha_nacimiento, genero, pais, notificaciones, terminos_condiciones)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('vista'))
  #  return redirect(url_for('home'))
   # return render_template('vista.html')
   

@app.vista()
def vista():
    return render_template('vista.html')
"""
@app.account('account')
def account():
    return render_template('account.html')

#Funcion de LOGIN
@app.account('//user',methods=["GET", "POST"])
def login():
    if request.method == 'POST' and 'txtcorreo' in request.form and 'txtpassword':
        _correo = request.form['txtcorreo']
        _password = request.form['txtpassword']

        #empieza a utilizar db
        
        cur-mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE correo = %s AND password = %s',(_correo,_password,))
        account = cur.fetchone()
        #termina de utilizar db.

        if account:
            session['logueado'] = True
            session['id'] = account['id']

            return render_template("index.html")
        else:

            return render_template("account.html",mensaje="usuario incorrecto")

    return render_template('index.html')
"""
#registro---


#ejecucion directa del archivo, en el puerto localhost 4000
if __name__ =='__main__':
    app.run(debug= True,port=4000)

#luego ejecutamos (http /127.0.0 xxx) hacer un click y nos envie al navegador
#si no se ejecuta directamente, en el navegador colocar localhost:4000.
