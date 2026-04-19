ventas = [
    {"fecha": "2025-01-15", "producto": "Proteína ISO", "cantidad": 20, "precio": 40000},
{"fecha": "2025-02-10", "producto": "Proteína ISO", "cantidad": 18, "precio": 40000},
{"fecha": "2025-05-20", "producto": "Proteína ISO", "cantidad": 10, "precio": 40000},
{"fecha": "2025-01-08", "producto": "Creatina", "cantidad": 25, "precio": 20000},
{"fecha": "2025-02-14", "producto": "Creatina", "cantidad": 15, "precio": 20000},
{"fecha": "2025-06-03", "producto": "Creatina", "cantidad": 10, "precio": 20000},
{"fecha": "2025-01-22", "producto": "Omega 3", "cantidad": 5, "precio": 35000},
{"fecha": "2025-02-28", "producto": "Omega 3", "cantidad": 5, "precio": 35000},
{"fecha": "2025-04-11", "producto": "Omega 3", "cantidad": 8, "precio": 35000},
{"fecha": "2025-06-19", "producto": "Omega 3", "cantidad": 10, "precio": 35000}
]
# Punto 2 - Ingresos totales
total = 0
for venta in ventas:
    total += venta["cantidad"] * venta["precio"]

print("Ingresos totales:", total)
# Punto 3 - Producto más vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += venta["cantidad"]
    else:
        ventas_por_producto[producto] = venta["cantidad"]

mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print("Producto más vendido:", mas_vendido, "-", ventas_por_producto[mas_vendido], "unidades")
# Punto 4 - Promedio de precio por producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    if producto in precios_por_producto:
        precios_por_producto[producto] = (
            precios_por_producto[producto][0] + venta["precio"],
            precios_por_producto[producto][1] + 1
        )
    else:
        precios_por_producto[producto] = (venta["precio"], 1)

for producto, datos in precios_por_producto.items():
    promedio = datos[0] / datos[1]
    print(f"Precio promedio {producto}: ${promedio:,.0f}")
# Punto 5 - Ingresos por día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

for fecha, ingreso in ingresos_por_dia.items():
    print(f"{fecha}: ${ingreso:,.0f}")
# Punto 6 - Resumen de ventas
resumen_ventas = {}
for venta in ventas:
    producto = venta["producto"]
    ingreso = venta["cantidad"] * venta["precio"]
    if producto in resumen_ventas:
        resumen_ventas[producto]["cantidad_total"] += venta["cantidad"]
        resumen_ventas[producto]["ingresos_totales"] += ingreso
    else:
        resumen_ventas[producto] = {
            "cantidad_total": venta["cantidad"],
            "ingresos_totales": ingreso,
            "precio_promedio": venta["precio"]
        }

for producto, datos in resumen_ventas.items():
    datos["precio_promedio"] = datos["ingresos_totales"] / datos["cantidad_total"]
    print(f"\n{producto}:")
    print(f"  Cantidad total: {datos['cantidad_total']}")
    print(f"  Ingresos totales: ${datos['ingresos_totales']:,.0f}")
    print(f"  Precio promedio: ${datos['precio_promedio']:,.0f}")