def C_into_F(c_temp): 
    f_temp = c_temp * 1.8 + 32
    print (f'{c_temp}°C in Fareneit is: {f_temp} °F.')
    return f_temp

def F_into_C(F_temp):
    c_temp = (F_temp - 32) / 1.8
    print (f'{F_temp}°F in Celsius is: {c_temp} °C.')
    return c_temp

def main():
    temperature = int(input('Type temperature: '))
    measurement = input('Type system of measurement: "F" or "C" ').lower()
    if measurement == 'c':
        return C_into_F(temperature)
    elif measurement == 'f':
        return F_into_C(temperature)
    else: 
        print('Oops, something get wrong!')
    
main()