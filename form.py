import tkinter as tk

def suma():
    try:
        n1 = int(numero1.get())
        n2 = int(numero2.get())
        res = n1+n2
        resultado.config(text=f"Resultado: {res}")
    except:
        resultado.config(text="Ingresa solo número enteros")

formulario = tk.Tk()
formulario.title("Suma de dos numeros")
formulario.geometry("550x330")

numero1 = tk.StringVar()
numero2 = tk.StringVar()

tk.Label(formulario, text="Numero 1:").pack(pady=10)
tk.Entry(formulario, textvariable=numero1, width=50).pack(pady=5)

tk.Label(formulario, text="Numero 2:").pack(pady=10)
tk.Entry(formulario, textvariable=numero2, width=50).pack(pady=5)

tk.Button(formulario, text="Suma", command=suma, bg="lavender", fg="black").pack(pady=20)

resultado = tk.Label(formulario, text="Resultado: ")
resultado.pack(pady=20)

formulario.mainloop()