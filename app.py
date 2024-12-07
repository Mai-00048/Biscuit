import tkinter as tk
from tkinter import ttk

def calculate_time():
    # Constants
    D = 0.6  # Porosity coefficient
    L_values = {"خفيف": 0.5, "متوسط": 1.0, "عميق": 1.5}  # Dip levels in cm
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
    
    # Get the selected inputs
    tea_type = tea_type_var.get()
    temperature = temperature_var.get()
    dip_level = dip_level_var.get()
    
    # Validation check for empty selections
    if not tea_type or not temperature or not dip_level:
        result_label.config(text="يرجى اختيار جميع الخيارات.")
        return

    # Calculate time if the dip level is not "خفيف"
    if dip_level == "خفيف":
        result_label.config(text="الزمن: تقريبًا 1 ثانية")
        return

    # Get the viscosity (η) and dip level (L) based on selections
    key = f"{tea_type} - {temperature}"
    η = viscosity_values.get(key, 0.6)  # Default to 0.6 if not found
    L = L_values[dip_level]  # Get dip level in cm
    
    try:
        # Calculate time using the formula: t = L² / (D * η)
        t = (L ** 2) / (D * η)
        
        # Show the result with the calculated time
        result_label.config(text=f"الزمن المثالي لغمر الشابورة: {t:.2f} ثانية")
        
    except ZeroDivisionError:
        result_label.config(text="خطأ: لزوجة غير صالحة.")
        
# Tkinter GUI Setup
root = tk.Tk()
root.title("حساب زمن غمر الشابورة")

# Variables for storing selected values
tea_type_var = tk.StringVar()
temperature_var = tk.StringVar()
dip_level_var = tk.StringVar()

# Tea type options
tea_type_label = tk.Label(root, text="نوع الشاي:")
tea_type_label.grid(row=0, column=0)
tea_type_menu = ttk.Combobox(root, textvariable=tea_type_var, values=["شاي كرك", "شاي أحمر", "شاي أخضر"])
tea_type_menu.grid(row=0, column=1)

# Temperature options
temperature_label = tk.Label(root, text="درجة حرارة الشاي:")
temperature_label.grid(row=1, column=0)
temperature_menu = ttk.Combobox(root, textvariable=temperature_var, values=["ساخن", "دافئ", "بارد"])
temperature_menu.grid(row=1, column=1)

# Dip level options
dip_level_label = tk.Label(root, text="مستوى التغلغل:")
dip_level_label.grid(row=2, column=0)
dip_level_menu = ttk.Combobox(root, textvariable=dip_level_var, values=["خفيف", "متوسط", "عميق"])
dip_level_menu.grid(row=2, column=1)

# Calculate button
calculate_button = tk.Button(root, text="حساب الزمن", command=calculate_time)
calculate_button.grid(row=3, column=0, columnspan=2)

# Label for showing results
result_label = tk.Label(root, text="الزمن المثالي لغمر الشابورة:")
result_label.grid(row=4, column=0, columnspan=2)

# Run the GUI application
root.mainloop()
