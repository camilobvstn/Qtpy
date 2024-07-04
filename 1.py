import re
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate

app = QtWidgets.QApplication([])

login = uic.loadUi("Credenciales.ui")
form1 = uic.loadUi("FormPersonal.ui")
form2 = uic.loadUi("FormLaboral.ui")

def gui_login():
    email = login.InputEmail.text()
    password = login.InputConstra.text()
    valid = True

    if len(email) == 0:
        login.ErrorEmail.setText("Ingrese un email.")
        valid = False
    else:
        login.ErrorEmail.setText("")
    
    if len(password) == 0:
        login.ErrorConstra.setText("Ingrese una contraseña.")
        valid = False
    else:
        login.ErrorConstra.setText("")
    
    if valid:
        gui_entrar()

def gui_personal():
    nombre = form1.InputNombre.text()
    telefono = form1.InputTel.text()
    rut = form1.InputRut.text()
    direccion = form1.InputDir.text()
    valid = True

    # Verificar que el nombre no contenga números
    if len(nombre) == 0:
        form1.ErrorNombreCom.setText("Ingrese un nombre.")
        valid = False
    elif any(char.isdigit() for char in nombre):
        form1.ErrorNombreCom.setText("El nombre no debe contener números.")
        valid = False
    else:
        form1.ErrorNombreCom.setText("")

    # Verificar que el teléfono sea solo números y tenga 9 dígitos
    if len(telefono) == 0:
        form1.ErrorTEl.setText("Ingrese un número de teléfono.")
        valid = False
    elif not telefono.isdigit() or len(telefono) != 9:
        form1.ErrorTEl.setText("Debe tener 9 dígitos y sin letras.")
        valid = False
    else:
        form1.ErrorTEl.setText("")

    # Verificar que el RUT tenga 10 dígitos incluyendo un guion
    if len(rut) == 0:
        form1.ErrorRut.setText("Ingrese un RUT.")
        valid = False
    elif not re.match(r"^\d{7,8}-\d{1}$", rut):
        form1.ErrorRut.setText("(ejemplo: 12345678-9)")
        valid = False
    else:
        form1.ErrorRut.setText("")

    if len(direccion) == 0:
        form1.ErrorDire.setText("Ingrese una dirección.")
        valid = False
    else:
        form1.ErrorDire.setText("")

    if valid:
        gui_sgt1()

def gui_laboral():
    cargo = form2.InputCargo.text()
    fecha = form2.dateEdit.date()
    area = form2.InputArea.text()
    valid = True

    # Verificar que el cargo no esté vacío
    if len(cargo) == 0:
        form2.ErrorCargo.setText("Ingrese un cargo.")
        valid = False
    else:
        form2.ErrorCargo.setText("")

    # Verificar que la fecha no sea superior a la actual
    if fecha > QDate.currentDate():
        form2.ErrorFecha.setText("La fecha no puede ser superior a la actual.")
        valid = False
    else:
        form2.ErrorFecha.setText("")

    # Verificar que el área no esté vacía
    if len(area) == 0:
        form2.ErrorArea.setText("Ingrese un área.")
        valid = False
    else:
        form2.ErrorArea.setText("")

    if valid:
        # Puedes agregar aquí la lógica para continuar después de validar form2
        print("Formulario laboral validado correctamente")

def gui_entrar():
    login.hide()
    form1.show()

def gui_sgt1():
    form1.hide()
    form2.show()

def volver_1():
    form2.hide()
    form1.show()

login.btnIngresar.clicked.connect(gui_login)


form1.btnStg1.clicked.connect(gui_personal)

form2.btnAtras1.clicked.connect(volver_1)


login.show()
app.exec()

