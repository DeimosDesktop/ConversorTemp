#CONVERTIDOR FAHRENHEIT / CELSIUS#
#Intefáz gráfica básica.
import tkinter as tk
from tkinter import ttk
def convertir_temp_fahrenheit():
    temp_celsius = float(caja_temp_celsius.get())
    temp_fahrenheit = temp_celsius*1.8 + 32
    etiqueta_temp_fahrenheit.config(text=f"Temperatura en ºF: {temp_fahrenheit}")
def convertir_temp_celsius():
    temp_fahrenheit = float(caja_temp_fahrenheit.get())
    temp_celsius = (temp_fahrenheit -32) / 1.8
    etiqueta_temp_fahrenheit.config(text=f"Temperatura en ºC: {temp_celsius}")
marco = tk.Tk()
marco.title("Conversor de temperaturas")
marco.config(width=450, height=300)
# widgets para el CELSIUS
etiqueta_fahrenheit_celsius = ttk.Label(text="Temperatura en ºF:")
etiqueta_fahrenheit_celsius.place(x=220, y=20)
caja_temp_fahrenheit = ttk.Entry()
caja_temp_fahrenheit.place(x=340, y=20, width=60)
boton_convertir = ttk.Button(text="Convertir a CELSIUS", command=convertir_temp_celsius)
boton_convertir.place(x=220, y=60)
#Widges para el FAHRENHEIT
etiqueta_temp_celsius = ttk.Label(text="Temperatura en ºC:")
etiqueta_temp_celsius.place(x=20, y=20)
caja_temp_celsius = ttk.Entry()
caja_temp_celsius.place(x=140, y=20, width=60)
boton_convertir = ttk.Button(text="Convertir a FAHRENHEIT", command=convertir_temp_fahrenheit)
boton_convertir.place(x=20, y=60)
etiqueta_temp_fahrenheit = ttk.Label(text="Temperatura en ºF: n/a")
etiqueta_temp_fahrenheit.place(x=20, y=160)
marco.mainloop()