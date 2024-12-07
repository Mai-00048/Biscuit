import tkinter as tk
from tkinter import ttk

def calculate_time():
    # Constants
    D = 0.6  # Porosity coefficient
    L_values = {"خفيف": 0.3, "متوسط": 0.5, "عميق": 0.8}  # Dip levels
    viscosity_values = {
        "شاي كرك - ساخن": 0.6,
        "شاي كرك - دافئ": 0.8,
        "شاي كرك - بارد": 1.2,
        "شاي أحمر - ساخن": 0.4,
        "شاي أحمر - دافئ": 0.6,
        "شاي أحمر - بارد": 0.9,
        "شاي أخضر - ساخن": 0.3,
        "شاي أخضر - دافئ": 0.5,
        "شاي أخضر - بارد": 0.7,
    }

  
    tea_type = tea_type_var.get()
    temperature = temperature_var.get()
    dip_level = dip_level_var.get()
    
    #  Validate inputs
    if not tea_type or not temperature or not dip_level:
        result_label.config(text="يرجى اختيار جميع الخيارات.")
        return

    #  Calculate time
    key = f"{tea_type} - {temperature}"
    η = viscosity_values.get(key, 0.6)   
    L = L_values[dip_level]  
    
    try:
        t = (L ** 2) / (D * η)
        result_label.config(text=f"الزمن المثالي لغمر الشابورة: {t:.2f} ثانية")
    except ZeroDivisionError:
        result_label.config(text="خطأ: لزوجة غير صالحة.")

# ------------------------------------------------------<<GUI>>--------------------------------------------
root = tk.Tk()
root.title("حساب زمن غمر الشابورة")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="نوع الشاي:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
tea_type_var = tk.StringVar()
tea_type_combobox = ttk.Combobox(frame, textvariable=tea_type_var, state="readonly")
tea_type_combobox["values"] = ["شاي كرك", "شاي أحمر", "شاي أخضر"]
tea_type_combobox.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="درجة الحرارة:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
temperature_var = tk.StringVar()
temperature_combobox = ttk.Combobox(frame, textvariable=temperature_var, state="readonly")
temperature_combobox["values"] = ["ساخن", "دافئ", "بارد"]
temperature_combobox.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="فترة التغلغل:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
dip_level_var = tk.StringVar()
dip_level_combobox = ttk.Combobox(frame, textvariable=dip_level_var, state="readonly")
dip_level_combobox["values"] = ["خفيف", "متوسط", "عميق"]
dip_level_combobox.grid(row=2, column=1, padx=5, pady=5)

calculate_button = ttk.Button(frame, text="احسب الزمن", command=calculate_time)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="", anchor="center")
result_label.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()