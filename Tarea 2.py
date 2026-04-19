ventas = [
    {"fecha": "2024-01-01", "producto": "Proteína", "cantidad": 2, "precio": 25.0},
    {"fecha": "2024-01-01", "producto": "Creatina", "cantidad": 1, "precio": 15.0},
    {"fecha": "2024-01-02", "producto": "Proteína", "cantidad": 1, "precio": 25.0},
    {"fecha": "2024-01-02", "producto": "Omega 3", "cantidad": 3, "precio": 10.0},
    {"fecha": "2024-01-03", "producto": "Creatina", "cantidad": 2, "precio": 15.0},
]
ingresos_totales = 0

for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print("Ingresos totales:", ingresos_totales)
ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]

    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

print("Producto más vendido:", producto_mas_vendido)
print("Cantidad total:", ventas_por_producto[producto_mas_vendido])
precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]

    if producto in precios_por_producto:
        suma_precios, total_unidades = precios_por_producto[producto]
        precios_por_producto[producto] = (
            suma_precios + (precio * cantidad),
            total_unidades + cantidad
        )
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)

# Calcular promedio
for producto, (suma, cantidad) in precios_por_producto.items():
    promedio = suma / cantidad
    print(f"{producto}: Precio promedio = {promedio}")
ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]

    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

print(ingresos_por_dia)
resumen_ventas = {}

for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos = precios_por_producto[producto][0]
    promedio = ingresos / cantidad_total

    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos,
        "precio_promedio": promedio
    }

print(resumen_ventas)