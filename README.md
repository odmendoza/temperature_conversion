# temperature_conversion

Paquete de conversión de temperaturas

El módulo del paquete contiene las funciones siguientes:

- Una función llamada F_to_K que convierte temperaturas en Fahrenheit a Kelvin.
- Una función llamada C_to_R que convierte temperaturas en Celsius a Rankine.
- Una función llamada C_to_F que convierte temperaturas en Celsius a Fahrenheit.

## Instalación
```
pip install temperature_conversion
```

## Forma de uso

```python
from temperature_conversion.convert import f_to_k, c_to_r, c_to_f

# Convierta temperaturas de Fahrenheit a Kelvin, haciendo uso de su función F_to_K.

print('Conversión de Fahrenheit a Kelvin')
temp_k = f_to_k(45)


# Convierta temperaturas en Celsius a Rankine, haciendo uso de su función C_to_R.

print('Conversión de Celsius a Rankine')
temp_r = c_to_r(25)


# convierta temperaturas en Celsius a Fahrenheit, haciendo uso de su función C_to_F.

print('Conversión de Celsius a Fahrenheit')
temp_f = c_to_f(12)
```