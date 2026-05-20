a = input()
l_value = a[-1]


if l_value == "C" :
    Celsius = a[:len(a)-1]
    Celsius = float(Celsius)
    Fahrenheit = round(Celsius * 9/5 + 32,2)
    Kelvin = round(Celsius + 273 , 2)

elif l_value == "F" :
    Fahrenheit = a[:len(a)-1]
    Fahrenheit = float(Celsius)
    Celsius = round((Fahrenheit-32)*5/9,2)
    Kelvin = round(Celsius + 273 , 2)
    
elif l_value == "K" :
    Kelvin = a[:len(a)-1]
    Kelvin = float(Kelvin)
    Celsius = round(Kelvin-273,2)
    Fahrenheit = round(Celsius* 9/5 +32, 2)
    
print(str(Celsius) + "C")
print(str(Fahrenheit) + "F")
print(str(Kelvin) + "K")


    