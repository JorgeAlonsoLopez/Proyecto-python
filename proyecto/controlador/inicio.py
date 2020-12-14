import tkinter as tk
from tkcalendar import *
from tkinter import ttk
from datetime import datetime
from math import ceil
from tkinter import messagebox
import servicio.ParkingService as park_serv
import servicio.AbonoService as abon_serv
import servicio.ClienteService as clin_serv
import servicio.TicketService as tick_serv
import servicio.FacturaService as fact_serv
from modelo.Parking import *
from modelo.Cliente import *
from modelo.Vehiculo import *
lista_abonos = abon_serv.load_file()
lista_tickets = tick_serv.load_file()
lista_facturas = fact_serv.load_file()
parking = park_serv.load_file()


import servicio.AbonoService as serv_abo
LARGE_FONT= ("Verdana", 10)
# Configuración de la raíz
root = tk.Tk()
root.geometry("900x800")



fec = tk.StringVar()
sol = tk.StringVar()
dni = tk.StringVar()
nom = tk.StringVar()
apl = tk.StringVar()
taj = tk.StringVar()
mail = tk.StringVar()
matrc = tk.StringVar()
tip_park = tk.IntVar()
tip_abon = tk.IntVar()

def date():
    anio1 = int(fec.get()[6:10])
    mes1= int(fec.get()[0:2])
    dia1= int(fec.get()[3:5])
    return datetime(anio1, mes1, dia1)

def client():
    cliente = Cliente(dni.get().upper(),nom.get(),apl.get(),mail.get(),taj.get(),Vehiculo(matrc.get().upper()))
    return cliente

def abono(sol):
    print("")
    fecha = date()
    cliente = client()
    resl = abon_serv.crear_abono(lista_abonos,lista_facturas, parking, tip_abon.get(),tip_park.get(),fecha,cliente)
    abon_serv.save_file(lista_abonos)
    fact_serv.save_file(lista_facturas)
    park_serv.save_file(parking)
    sol.set(resl)

label_tex = tk.Label(root, text="Complete los datos para crear un abono", font=LARGE_FONT).pack(pady=10)


frame_1=tk.Frame(root)
frame_1.pack(pady=5)

label_tex = tk.Label(frame_1, text="DNI ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
Inp_dni = tk.Entry(frame_1, textvariable=dni).pack(padx=5, pady=5, side=tk.LEFT)
label_tex = tk.Label(frame_1, text="Nombre ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
Inp_nom = tk.Entry(frame_1, textvariable=nom).pack(padx=5, pady=5, side=tk.LEFT)
label_tex = tk.Label(frame_1, text="Apellidos ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
Inp_ape = tk.Entry(frame_1, textvariable=apl).pack(padx=5, pady=5, side=tk.LEFT)

frame_2=tk.Frame(root)
frame_2.pack(pady=5)

label_tex = tk.Label(frame_2, text="Nº tarjeta ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
Inp_tarj = tk.Entry(frame_2, textvariable=taj).pack(padx=5, pady=5, side=tk.LEFT)
label_tex = tk.Label(frame_2, text="Correo ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
Inp_mail = tk.Entry(frame_2, textvariable=mail).pack(padx=5, pady=5, side=tk.LEFT)
label_tex = tk.Label(frame_2, text="Matrícula ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
Inp_matric = tk.Entry(frame_2, textvariable=matrc).pack(padx=5, pady=5, side=tk.LEFT)

label_tex = tk.Label(root, text="Tipo de vehículo", font=LARGE_FONT).pack(pady=5)

frame_opt_park=tk.Frame(root)
frame_opt_park.pack(pady=5)

tk.Radiobutton(frame_opt_park, text="Coche", variable=tip_park, value=1).pack(side=tk.LEFT, padx = 5)
tk.Radiobutton(frame_opt_park, text="Moto", variable=tip_park, value=2).pack(side=tk.LEFT, padx = 5)
tk.Radiobutton(frame_opt_park, text="Movilidad reducida",variable=tip_park, value=3).pack(side=tk.LEFT, padx = 5)

label_tex = tk.Label(root, text="Tipo de abono", font=LARGE_FONT).pack(pady=5)

frame_opt_ab=tk.Frame(root)
frame_opt_ab.pack(pady=5)

tk.Radiobutton(frame_opt_ab, text="Mensual (25€)", variable=tip_abon, value=1).pack(side=tk.LEFT, padx = 5)
tk.Radiobutton(frame_opt_ab, text="Trimestral (70€)", variable=tip_abon, value=2).pack(side=tk.LEFT, padx = 5)
tk.Radiobutton(frame_opt_ab, text="Semestral (130€)",variable=tip_abon, value=3).pack(side=tk.LEFT, padx = 5)
tk.Radiobutton(frame_opt_ab, text="Anual (200€)",variable=tip_abon, value=4).pack(side=tk.LEFT, padx = 5)

cal1 = Calendar(root, selectmode="day",date_pattern='mm/dd/y', year=2020, month=12, day=10)
cal1.pack(pady=5)

def fecha():
    fec.set(cal1.get_date())

frame_1=tk.Frame(root)
frame_1.pack(pady=5)

botonFec1 = tk.Button(root, text="Confrimar fecha de inicio de abono",command=fecha, font=LARGE_FONT).pack(pady=5)

frame_h=tk.Frame(root)
frame_h.pack(pady=5)

label_tex = tk.Label(frame_h, text="La fecha y hora de inicio es: ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
fech1 = tk.Label(frame_h, textvariable=fec)
fech1.pack(side=tk.LEFT)

boton = tk.Button(root, text="Confrimar solicitud de abono",command= lambda : abono(sol), font=LARGE_FONT).pack(pady=5)



label_tex = tk.Label(root, textvariable=sol, font=LARGE_FONT).pack()



boton2 = tk.Button(root, text="Salir", font=LARGE_FONT).pack(pady=20)

root.mainloop()
