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

app=Flask(__name__)

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
@app.route('/user_create', methods=['GET','POST'])
def registrar_usuario():
    if request.method == 'POST'
        #obteniendo datos del form
        correo = request.form.get('email')
        password = request.form.get('passw')
        nombre = request.form.get('name')
        apellido = request.form.get('surname')
        fecha_nacimiento = request.form.get('fecha-nacimiento')
        genero = request.form.get('option_genero')
        pais = request.form.get('pais')
        notificaciones = int (request.form.get('notificaciones'))
        terminos_condiciones = int (request.form.get('check'))

        #verifico pais.
        if pais == "otro":
            pais = request.form.get('nombrePais')
        #checkeds
        if notificaciones != 1:
            notificaciones = 0
        if terminos_condiciones != 1:
            terminos_condiciones = 0

        #verificacion que los campos no den null
        if not correo or not password or not nombre or not apellido or not fecha_nacimiento or not genero or not pais or not terminos_condiciones:
            return "Error: faltan campos requeridos."

        #insertar los datos en la db
        cursor = db.database.cursor()
        query = """
        INSERT INTO usuarios (correo, password, nombre, apellido, fecha_nacimiento, genero, pais, notificaciones, terminos_condiciones) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(query,(correo,password,nombre,apellido,fecha_nacimiento,genero,pais,notificaciones,terminos_condiciones))
        db.database.commit()

        #cerrando el cursor
        cursor.close()
        #redirigiendo a página home, en home poner despues el index, cuando quede bien.
    return redirect(url_for('home'))

#eliminé el resto para limpiar vista del .py

#ejecucion directa del archivo, en el puerto localhost 4000
if __name__ =='__main__':
    app.run(debug= True) #elimine el puerto para que no produsca error.

#luego ejecutamos (http /127.0.0 xxx) hacer un click y nos envie al navegador
#si no se ejecuta directamente, en el navegador colocar localhost:4000.
