print("*** Bienvenidos ***")
print("INGRESAR BALANCE GENERAL")
SEPARADOR1= "*"*70
SEPARADOR2= "-"*70

# ACTIVOS CIRCULANTES
print("ACTIVOS CIRCULANTES")
Efectivo=float(input("Efectivo: "))
Clientes=float(input("Clientes: "))
Deudores_Diversos=float(input("Deudores Diversos: "))
Funcionarios_Y_Empleados=float(input("Funcionarios Y Empleados: "))
Inventario_de_Materiales=float(input("Inventario de Materiales: "))
Inventario_de_Producto_Terminado=float(input("Inventario de Producto Terminado: "))
Total_Activo_Circulante= Efectivo + Clientes + Deudores_Diversos + Funcionarios_Y_Empleados + Inventario_de_Materiales + Inventario_de_Producto_Terminado
print("Total de Activo Circulante: ",Total_Activo_Circulante)
print("")


# ACTIVOS NO CIRCULANTES
print("ACTIVOS NO CIRCULANTES")
Terreno=float(input("Terreno: "))
Planta_Y_Equipo=float(input("Planta y Equipo: "))
Depreciacion_Acumulada=float(input("Depreciación Acumulada: "))
Total_Activo_NO_Circulante= Terreno + Planta_Y_Equipo - Depreciacion_Acumulada
print("Total de Activo NO Circulante: ",Total_Activo_NO_Circulante)
print("")

Activo_Total= Total_Activo_Circulante + Total_Activo_NO_Circulante
print("Total de Activos: ",Activo_Total)
print("")
print(SEPARADOR2)

# PASIVOS
print("PASIVOS")
Proveedores=float(input("Proveedores: "))
Documentos_por_Pagar=float(input("Documentos por Pagar: "))
ISR_por_Pagar=float(input("ISR por Pagar: "))
Total_Pasivo_CortoPlazo= Proveedores + Documentos_por_Pagar + ISR_por_Pagar
print("Total de Pasivo Corto Plazo: ",Total_Pasivo_CortoPlazo)
print("")


Prestamos_Bancarios=float(input("Prestamos Bancarios: "))
Total_Pasivo_LargoPlazo= Prestamos_Bancarios
print("Total Pasivo Largo Plazo: ",Total_Pasivo_LargoPlazo)
Pasivo_Total= Total_Pasivo_CortoPlazo + Total_Pasivo_LargoPlazo
print("PASIVO TOTAL: ",Pasivo_Total)
print("")
print(SEPARADOR2)

print("CAPITAL CONTABLE")
Capital_Contribuido=float(input("Capital Contribuido: "))
Capital_Ganado=float(input("Capital Ganado: "))
Capital_Contable_Total= Capital_Contribuido + Capital_Ganado
print("CAPITAL CONTABLE TOTAL: ",Capital_Contable_Total)
print("")

Suma_Pasivo_Capital= Pasivo_Total + Capital_Contable_Total
print("SUMA DEL PASIVO Y CAPITAL: ",Suma_Pasivo_Capital)
print("")
print(SEPARADOR2)

# REQUERIMENTO DE MATERIALES
print("REQUERIMIENTO DE MATERIALES")
print("PRODUCTO CL")
Materia_PrimaA_CL=float(input("Materia Prima A metros: "))
Materia_PrimaB_CL=float(input("Materia Prima B metros: "))
Materia_PrimaC_CL=float(input("Materia Prima C piezas: "))
Horas_Mano_Obra_CL=float(input("Horas Mano de Obra: "))
print("")
print(SEPARADOR2)

print("PRODUCTO CE")
Materia_PrimaA_CE=float(input("Materia Prima A metros: "))
Materia_PrimaB_CE=float(input("Materia Prima B metros: "))
Materia_PrimaC_CE=float(input("Materia Prima C piezas: "))
Horas_Mano_Obra_CE=float(input("Horas Mano de Obra: "))
print("")
print(SEPARADOR2)

print("PRODUCTO CR")
Materia_PrimaA_CR=float(input("Materia Prima A metros: "))
Materia_PrimaB_CR=float(input("Materia Prima B metros: "))
Materia_PrimaC_CR=float(input("Materia Prima C piezas: "))
Horas_Mano_Obra_CR=float(input("Horas Mano de Obra: "))
print("")
print(SEPARADOR2)

print("La hora de Mano de Obra Directa")
Mano_Obra_Primer_Semestre=float(input("Costo de Mano de Obra el Primer Semestre: "))
Mano_Obra_Segundo_Semestre=float(input("Costo de Mano de Obra el Segundo Semestre: "))
print("")
print(SEPARADOR2)

# INFORMACION DE INVENTARIOS
print("INFORMACION DE INVENTARIOS")
print("")

print("Inventario Inicial Primer Semestre")
Materia_PrimaA_Inventario_Inicial=float(input("Materia Prima A metros: "))
Materia_PrimaB_Inventario_Inicial=float(input("Materia Prima B metros: "))
Materia_PrimaC_Inventario_Inicial=float(input("Materia Prima C piezas: "))
Producto_CL_Inventario_Inicial=float(input("Producto CL: "))
Producto_CE_Inventario_Inicial=float(input("Producto CE: "))
Producto_CR_Inventario_Inicial=float(input("Producto CR: "))
print("")
print(SEPARADOR2)

print("Inventario Final Segundo Semestre")
Materia_PrimaA_Inventario_Final=float(input("Materia Prima A metros: "))
Materia_PrimaB_Inventario_Final=float(input("Materia Prima B metros: "))
Materia_PrimaC_Inventario_Final=float(input("Materia Prima C piezas: "))
Producto_CL_Inventario_Final=float(input("Producto CL: "))
Producto_CE_Inventario_Final=float(input("Producto CE: "))
Producto_CR_Inventario_Final=float(input("Producto CR: "))
print("")
print(SEPARADOR2)

print("Costo Primer Semestre")
Materia_PrimaA_Costo_1er_Semestre=float(input("Materia Prima A metros: "))
Materia_PrimaB_Costo_1er_Semestre=float(input("Materia Prima B metros: "))
Materia_PrimaC_Costo_1er_Semestre=float(input("Materia Prima C piezas: "))
print("")
print(SEPARADOR2)

print("Costo Segundo Semestre")
Materia_PrimaA_Costo_2do_Semestre=float(input("Materia Prima A metros: "))
Materia_PrimaB_Costo_2do_Semestre=float(input("Materia Prima B metros: "))
Materia_PrimaC_Costo_2do_Semestre=float(input("Materia Prima C piezas: "))
print("")
print(SEPARADOR2)
# PRODUCTOS
print("PRODUCTOS")
print("PRODUCTO CL")
Precio_Venta_Primer_Semestre_CL=float(input("Precio de Venta Primer Semestre: "))
Precio_Venta_Segundo_Semestre_CL=float(input("Precio de Venta Segundo Semestre: "))
Ventas_Planeadas_Primer_Semestre_CL=float(input("Ventas planeadas Primer Semestre: "))
Ventas_Planeadas_Segundo_Semestre_CL=float(input("Ventas planeadas Segundo Semestre: "))
print("")
print(SEPARADOR2)
print("PRODUCTO CE")
Precio_Venta_Primer_Semestre_CE=float(input("Precio de Venta Primer Semestre: "))
Precio_Venta_Segundo_Semestre_CE=float(input("Precio de Venta Segundo Semestre: "))
Ventas_Planeadas_Primer_Semestre_CE=float(input("Ventas planeadas Primer Semestre: "))
Ventas_Planeadas_Segundo_Semestre_CE=float(input("Ventas planeadas Segundo Semestre: "))
print("")
print(SEPARADOR2)
print("PRODUCTO CR")
Precio_Venta_Primer_Semestre_CR=float(input("Precio de Venta Primer Semestre: "))
Precio_Venta_Segundo_Semestre_CR=float(input("Precio de Venta Segundo Semestre: "))
Ventas_Planeadas_Primer_Semestre_CR=float(input("Ventas planeadas Primer Semestre: "))
Ventas_Planeadas_Segundo_Semestre_CR=float(input("Ventas planeadas Segundo Semestre: "))
print("")
print(SEPARADOR2)

# GASTOS DE ADMINISTRACION Y VENTAS
print("Gastos de Administración y Ventas")
Depreciacion=float(input("Depreciacion: "))
Sueldos_Y_Salarios=float(input("Sueldos y Salarios: "))
Comisiones=float(input("Comisiones: "))
Varios_1er_Semestre=float(input("Varios (Primer Semestre): "))
Varios_2do_Semestre=float(input("Varios (Segundo Semestre): "))
Intereses_por_Prestamo=float(input("Intereses por Préstamo: "))
print("")
print(SEPARADOR2)

# GASTOS DE FABRICACION
print("Gastos de Fabricación Indirectos")
Depreciacion_Indirectos=float(input("Depreciacion: "))
Seguros=float(input("Seguros: "))
Mantenimiento_1er_Semestre=float(input("Mantenimiento (Primer Semestre): "))
Mantenimiento_2do_Semestre=float(input("Mantenimiento (Segundo Semestre): "))
Energeticos_1er_Semestre=float(input("Energeticos (Primer Semestre): "))
Energeticos_2do_Semestre=float(input("Energeticos (Segundo Semestre): "))
Varios_Indirectos=float(input("Varios: "))
print(SEPARADOR2)

print("")
print("")
print("PRESUPUESTO MAESTRO")
print("")
print("Maquilados Regionales S.A de C.V.")
print("")
print("I. Presupuesto de Operación")
print("")

# PRESUPUESTO 1
print("1. Presupuesto de Ventas")
print("")
print("PRODUCTO CL")
print("Primer Semestre")
Unidades_Vender_1er_Semestre_CL=Ventas_Planeadas_Primer_Semestre_CL
print("Unidades a Vender: ",Unidades_Vender_1er_Semestre_CL)
Precio_1er_Semestre_CL=Precio_Venta_Primer_Semestre_CL
print("Precio de Venta: ",Precio_1er_Semestre_CL)
Importe_Venta_1er_Semestre_CL=Unidades_Vender_1er_Semestre_CL * Precio_1er_Semestre_CL
print("Importe de Venta: ",Importe_Venta_1er_Semestre_CL)
print("")

print("Segundo Semestre")
Unidades_Vender_2do_Semestre_CL=Ventas_Planeadas_Segundo_Semestre_CL
print("Unidades a Vender: ",Unidades_Vender_2do_Semestre_CL)
Precio_2do_Semestre_CL=Precio_Venta_Segundo_Semestre_CL
print("Precio de Venta: ",Precio_2do_Semestre_CL)
Importe_Venta_2do_Semestre_CL=Unidades_Vender_2do_Semestre_CL * Precio_2do_Semestre_CL
print("Importe de Venta: ",Importe_Venta_2do_Semestre_CL)
Total_Importe_Venta_CL= Importe_Venta_1er_Semestre_CL + Importe_Venta_2do_Semestre_CL
print("")
print("Importe de Venta: ",Total_Importe_Venta_CL)
print("")
print(SEPARADOR2)

print("PRODUCTO CE")
print("Primer Semestre")
Unidades_Vender_1er_Semestre_CE=Ventas_Planeadas_Primer_Semestre_CE
print("Unidades a Vender: ",Unidades_Vender_1er_Semestre_CE)
Precio_1er_Semestre_CE=Precio_Venta_Primer_Semestre_CE
print("Precio de Venta: ",Precio_1er_Semestre_CE)
Importe_Venta_1er_Semestre_CE=Unidades_Vender_1er_Semestre_CE * Precio_1er_Semestre_CE
print("Importe de Venta: ",Importe_Venta_1er_Semestre_CE)
print("")


print("Segundo Semestre")
Unidades_Vender_2do_Semestre_CE=Ventas_Planeadas_Segundo_Semestre_CE
print("Unidades a Vender: ",Unidades_Vender_2do_Semestre_CE)
Precio_2do_Semestre_CE=Precio_Venta_Segundo_Semestre_CE
print("Precio de Venta: ",Precio_2do_Semestre_CE)
Importe_Venta_2do_Semestre_CE= Unidades_Vender_2do_Semestre_CE * Precio_2do_Semestre_CE
print("Importe de Venta: ",Importe_Venta_2do_Semestre_CE)
Total_Importe_Venta_CE= Importe_Venta_1er_Semestre_CE + Importe_Venta_2do_Semestre_CE
print("")
print("Importe de Venta: ",Total_Importe_Venta_CE)
print("")
print(SEPARADOR2)

print("PRODUCTO CR")
print("Primer Semestre")
Unidades_Vender_1er_Semestre_CR=Ventas_Planeadas_Primer_Semestre_CR
print("Unidades a Vender: ",Unidades_Vender_1er_Semestre_CR)
Precio_1er_Semestre_CR=Precio_Venta_Primer_Semestre_CR
print("Precio de Venta: ",Precio_1er_Semestre_CR)
Importe_Venta_1er_Semestre_CR= Unidades_Vender_1er_Semestre_CR * Precio_1er_Semestre_CR
print("Importe de Venta: ",Importe_Venta_1er_Semestre_CR)
print("")

print("Segundo Semestre")
Unidades_Vender_2do_Semestre_CR=Ventas_Planeadas_Segundo_Semestre_CR
print("Unidades a Vender: ",Unidades_Vender_2do_Semestre_CR)
Precio_2do_Semestre_CR=Precio_Venta_Segundo_Semestre_CR
print("Precio de Venta: ",Precio_2do_Semestre_CR)
Importe_Venta_2do_Semestre_CR= Unidades_Vender_2do_Semestre_CR * Precio_2do_Semestre_CR
print("Importe de Venta: ",Importe_Venta_2do_Semestre_CR)
print("")
Total_Importe_Venta_CR= Importe_Venta_1er_Semestre_CR + Importe_Venta_2do_Semestre_CR
print("Importe de Venta: ",Total_Importe_Venta_CR)
print("")
print(SEPARADOR2)

print("Total de Ventas por Semestre")
print("Primer Semestre")
Total_ventas_1er_semestre=Importe_Venta_1er_Semestre_CL+Importe_Venta_1er_Semestre_CE+Importe_Venta_1er_Semestre_CR
print("Total de Ventas: ",Total_ventas_1er_semestre)
print("")
print("Segundo Semestre")
Total_ventas_2do_semestre=Importe_Venta_2do_Semestre_CL+Importe_Venta_2do_Semestre_CE+Importe_Venta_2do_Semestre_CR
print("Total de Ventas: ",Total_ventas_2do_semestre)
print("")


Total_Ventas=Total_ventas_1er_semestre+Total_ventas_2do_semestre
print("Total de Ventas: ",Total_Ventas)
print(SEPARADOR2)
print("")
print("")

# PROCESO 2
print("2. Determinación del saldo de Clientes y Flujo de Entradas")
print("Saldo de clientes 31-Dic-2015: ",Clientes)
print("Ventas 2016: ",Total_Ventas)
Total_Clientes=Clientes+Total_Ventas
print("Total de Clientes 2016: ",Total_Clientes)
print("")
print("Entradas de Efectivo")
Saldo_Clientes=float(input("¿Que cantidad en % que va cobrar del saldo de Clientes? (Dato en DECIMALES): "))
Por_Cobranza_2015=Clientes*Saldo_Clientes
print("Por Cobranza del 2015: ",Por_Cobranza_2015)
Saldo_Ventas=float(input("¿Que cantidad en % que va cobrar de las ventas presupuestadas? (Dato en DECIMALES): "))
Por_Cobranza_2016=Total_Ventas*Saldo_Ventas
print("Por Cobranza del 2016: ",Por_Cobranza_2016)
Total_Entradas_Efectivo=Por_Cobranza_2015+Por_Cobranza_2016
print("TOTAL: ",Total_Entradas_Efectivo)
print("")
Saldo_Clientes_2016=Total_Clientes-Total_Entradas_Efectivo
print("Saldo de Clientes del 2016: ",Saldo_Clientes_2016)
print("")
print("")

# PROCESO 3
print("3. Presupuesto de Producción")
print("PRODUCTO CL")
print("Primer Semestre")
print("Unidades a Vender: ",Unidades_Vender_1er_Semestre_CL)
print("Inventario Final: ",Producto_CL_Inventario_Inicial)
Total_Unidades_1erSemestre_CL=Unidades_Vender_1er_Semestre_CL+Producto_CL_Inventario_Inicial
print("Total de Unidades: ",Total_Unidades_1erSemestre_CL)
print("Inventario Inicial: ",Producto_CL_Inventario_Inicial)
Unidades_Producir_1erSemestre_CL=Total_Unidades_1erSemestre_CL-Producto_CL_Inventario_Inicial
print("Unidades a Producir: ",Unidades_Producir_1erSemestre_CL)
print("")

print("Segundo Semestre")
print("Unidades a Vender: ",Unidades_Vender_2do_Semestre_CL)
print("Inventario Final: ",Producto_CL_Inventario_Final)
Total_Unidades_2doSemestre_CL=Unidades_Vender_2do_Semestre_CL+Producto_CL_Inventario_Final
print("Total de Unidades: ",Total_Unidades_2doSemestre_CL)
print("Inventario Inicial: ",Producto_CL_Inventario_Inicial)
Unidades_Producir_2doSemestre_CL=Total_Unidades_2doSemestre_CL-Producto_CL_Inventario_Inicial
print("Unidades a Producir: ",Unidades_Producir_2doSemestre_CL)
print("")

print("Total Anualmente")
Total_Unidades_Vender_CL=Unidades_Vender_1er_Semestre_CL+Unidades_Vender_2do_Semestre_CL
print("Unidades a Vender: ",Total_Unidades_Vender_CL)
print("Inventario Final: ",Producto_CL_Inventario_Final)
Total_Unidades_CL=Total_Unidades_Vender_CL+Producto_CL_Inventario_Final
print("Total de Unidades: ",Total_Unidades_CL)
print("Inventario Inicial: ",Producto_CL_Inventario_Inicial)
Total_Unidades_Producir_CL=Total_Unidades_CL-Producto_CL_Inventario_Inicial
print("Unidades a Producir: ",Total_Unidades_Producir_CL)
print("")
print(SEPARADOR2)

print("PRODUCTO CE")
print("Primer Semestre")
print("Unidades a Vender: ",Unidades_Vender_1er_Semestre_CE)
print("Inventario Final: ",Producto_CE_Inventario_Inicial)
Total_Unidades_1erSemestre_CE=Unidades_Vender_1er_Semestre_CE+Producto_CE_Inventario_Inicial
print("Total de Unidades: ",Total_Unidades_1erSemestre_CE)
print("Inventario Inicial: ",Producto_CE_Inventario_Inicial)
Unidades_Producir_1erSemestre_CE=Total_Unidades_1erSemestre_CE-Producto_CE_Inventario_Inicial
print("Unidades a Producir: ",Unidades_Producir_1erSemestre_CE)
print("")
print("Segundo Semestre")
print("Unidades a Vender: ",Unidades_Vender_2do_Semestre_CE)
print("Inventario Final: ",Producto_CE_Inventario_Final)
Total_Unidades_2doSemestre_CE=Unidades_Vender_2do_Semestre_CE+Producto_CE_Inventario_Final
print("Total de Unidades: ",Total_Unidades_2doSemestre_CE)
print("Inventario Inicial: ",Producto_CE_Inventario_Inicial)
Unidades_Producir_2doSemestre_CE=Total_Unidades_2doSemestre_CE-Producto_CE_Inventario_Inicial
print("Unidades a Producir: ",Unidades_Producir_2doSemestre_CE)
print("")
print("Total Anualmente")
Total_Unidades_Vender_CE=Unidades_Vender_1er_Semestre_CE+Unidades_Vender_2do_Semestre_CE
print("Unidades a Vender: ",Total_Unidades_Vender_CE)
print("Inventario Final: ",Producto_CE_Inventario_Final)
Total_Unidades_CE=Total_Unidades_Vender_CE+Producto_CE_Inventario_Final
print("Total de Unidades: ",Total_Unidades_CE)
print("Inventario Inicial: ",Producto_CE_Inventario_Inicial)
Total_Unidades_Producir_CE=Total_Unidades_CE-Producto_CE_Inventario_Inicial
print("Unidades a Producir: ",Total_Unidades_Producir_CE)
print("")
print(SEPARADOR2)

print("PRODUCTO CR")
print("Primer Semestre")
print("Unidades a Vender: ",Unidades_Vender_1er_Semestre_CR)
print("Inventario Final: ",Producto_CR_Inventario_Inicial)
Total_Unidades_1erSemestre_CR=Unidades_Vender_1er_Semestre_CR+Producto_CR_Inventario_Inicial
print("Total de Unidades: ",Total_Unidades_1erSemestre_CR)
print("Inventario Inicial: ",Producto_CR_Inventario_Inicial)
Unidades_Producir_1erSemestre_CR=Total_Unidades_1erSemestre_CR-Producto_CR_Inventario_Inicial
print("Unidades a Producir: ",Unidades_Producir_1erSemestre_CR)
print("")
print("Segundo Semestre")
print("Unidades a Vender: ",Unidades_Vender_2do_Semestre_CR)
print("Inventario Final: ",Producto_CR_Inventario_Final)
Total_Unidades_2doSemestre_CR=Unidades_Vender_2do_Semestre_CR+Producto_CR_Inventario_Final
print("Total de Unidades: ",Total_Unidades_2doSemestre_CR)
print("Inventario Inicial: ",Producto_CR_Inventario_Inicial)
Unidades_Producir_2doSemestre_CR=Total_Unidades_2doSemestre_CR-Producto_CR_Inventario_Inicial
print("Unidades a Producir: ",Unidades_Producir_2doSemestre_CR)
print("")
print("Total Anualmente")
Total_Unidades_Vender_CR=Unidades_Vender_1er_Semestre_CR+Unidades_Vender_2do_Semestre_CR
print("Unidades a Vender: ",Total_Unidades_Vender_CR)
print("Inventario Final: ",Producto_CR_Inventario_Final)
Total_Unidades_CR=Total_Unidades_Vender_CR+Producto_CR_Inventario_Final
print("Total de Unidades: ",Total_Unidades_CR)
print("Inventario Inicial: ",Producto_CR_Inventario_Inicial)
Total_Unidades_Producir_CR=Total_Unidades_CR-Producto_CR_Inventario_Inicial
print("Unidades a Producir: ",Total_Unidades_Producir_CR)
print(SEPARADOR2)
print("")
print("")

## PROCESO 4
print("4. Presupuesto de Requerimiento de Materiales")
print("PRODUCTO CL")
print("")
print("Primer Semestre")
print("Unidades a producir: ",Unidades_Producir_1erSemestre_CL)
print("")
print("Segundo Semestre")
print("Unidades a producir: ",Unidades_Producir_2doSemestre_CL)
print("")
print("Total: ",Total_Unidades_Producir_CL)
print("")
## Primer Semestre PRODUCTO CL
print("Primer Semestre")
print("Material A")
print("Requerimiento de material: ",Materia_PrimaA_CL)
Total_Material_A_Requerido_1erSemestre_CL=Unidades_Producir_1erSemestre_CL*Materia_PrimaA_CL
print("Total de Material A requerido: ",Total_Material_A_Requerido_1erSemestre_CL)
print("")

print("Material B")
print("Requerimiento de material: ",Materia_PrimaB_CL)
Total_Material_B_Requerido_1erSemestre_CL=Unidades_Producir_1erSemestre_CL*Materia_PrimaB_CL
print("Total de Material A requerido: ",Total_Material_B_Requerido_1erSemestre_CL)
print("")

print("Material C")
print("Requerimiento de material: ",Materia_PrimaC_CL)
Total_Material_C_Requerido_1erSemestre_CL=Unidades_Producir_1erSemestre_CL*Materia_PrimaC_CL
print("Total de Material A requerido: ",Total_Material_C_Requerido_1erSemestre_CL)
print("")

## Segundo Semestre PRODUCTO CL
print("Segundo Semestre")
print("Material A")
print("Requerimiento de material: ",Materia_PrimaA_CL)
Total_Material_A_Requerido_2doSemestre_CL=Unidades_Producir_2doSemestre_CL*Materia_PrimaA_CL
print("Total de Material A requerido: ",Total_Material_A_Requerido_2doSemestre_CL)
print("")

print("Material B")
print("Requerimiento de material: ",Materia_PrimaB_CL)
Total_Material_B_Requerido_2doSemestre_CL=Unidades_Producir_2doSemestre_CL*Materia_PrimaB_CL
print("Total de Material A requerido: ",Total_Material_B_Requerido_2doSemestre_CL)
print("")

print("Material C")
print("Requerimiento de material: ",Materia_PrimaC_CL)
Total_Material_C_Requerido_2doSemestre_CL=Unidades_Producir_2doSemestre_CL*Materia_PrimaC_CL
print("Total de Material A requerido: ",Total_Material_C_Requerido_2doSemestre_CL)
print("")

print("TOTAL")
Total_Material_A_CL= Total_Material_A_Requerido_1erSemestre_CL + Total_Material_A_Requerido_2doSemestre_CL
print("Total de Material A requerido: ",Total_Material_A_CL)
Total_Material_B_CL= Total_Material_B_Requerido_1erSemestre_CL + Total_Material_B_Requerido_2doSemestre_CL
print("Total de Material A requerido: ",Total_Material_B_CL)
Total_Material_C_CL= Total_Material_C_Requerido_1erSemestre_CL + Total_Material_C_Requerido_2doSemestre_CL
print("Total de Material A requerido: ",Total_Material_C_CL)
print(SEPARADOR2)
print("")
print("")

# PRODUCTO CE
print("PRODUCTO CE")
print("")
print("Primer Semestre")
print("Unidades a producir: ",Unidades_Producir_1erSemestre_CE)
print("")
print("Segundo Semestre")
print("Unidades a producir: ",Unidades_Producir_2doSemestre_CE)
print("")
print("Total: ",Total_Unidades_Producir_CE)
print("")

# PRIMER SEMESTRE
print("Primer Semestre")
print("Material A")
print("Requerimiento de material: ",Materia_PrimaA_CE)
Total_Material_A_Requerido_1erSemestre_CE=Unidades_Producir_1erSemestre_CE*Materia_PrimaA_CE
print("Total de Material A requerido: ",Total_Material_A_Requerido_1erSemestre_CE)
print("")

print("Material B")
print("Requerimiento de material: ",Materia_PrimaB_CE)
Total_Material_B_Requerido_1erSemestre_CE=Unidades_Producir_1erSemestre_CE*Materia_PrimaB_CE
print("Total de Material A requerido: ",Total_Material_B_Requerido_1erSemestre_CE)
print("")

print("Material C")
print("Requerimiento de material: ",Materia_PrimaC_CE)
Total_Material_C_Requerido_1erSemestre_CE=Unidades_Producir_1erSemestre_CE*Materia_PrimaC_CE
print("Total de Material A requerido: ",Total_Material_C_Requerido_1erSemestre_CE)
print("")

## Segundo Semestre PRODUCTO CE
print("Segundo Semestre")
print("Material A")
print("Requerimiento de material: ",Materia_PrimaA_CE)
Total_Material_A_Requerido_2doSemestre_CE=Unidades_Producir_2doSemestre_CE*Materia_PrimaA_CE
print("Total de Material A requerido: ",Total_Material_A_Requerido_2doSemestre_CE)
print("")

print("Material B")
print("Requerimiento de material: ",Materia_PrimaB_CE)
Total_Material_B_Requerido_2doSemestre_CE=Unidades_Producir_2doSemestre_CE*Materia_PrimaB_CE
print("Total de Material A requerido: ",Total_Material_B_Requerido_2doSemestre_CE)
print("")

print("Material C")
print("Requerimiento de material: ",Materia_PrimaC_CE)
Total_Material_C_Requerido_2doSemestre_CE=Unidades_Producir_2doSemestre_CE*Materia_PrimaC_CE
print("Total de Material A requerido: ",Total_Material_C_Requerido_2doSemestre_CE)
print("")

print("TOTAL")
Total_Material_A_CE= Total_Material_A_Requerido_1erSemestre_CE + Total_Material_A_Requerido_2doSemestre_CE
print("Total de Material A requerido: ",Total_Material_A_CE)

Total_Material_B_CE= Total_Material_B_Requerido_1erSemestre_CE + Total_Material_B_Requerido_2doSemestre_CE
print("Total de Material A requerido: ",Total_Material_B_CL)

Total_Material_C_CE= Total_Material_C_Requerido_1erSemestre_CE + Total_Material_C_Requerido_2doSemestre_CE
print("Total de Material A requerido: ",Total_Material_C_CE)
print(SEPARADOR2)
print("")
print("")

# PRODUCTO CR
print("PRODUCTO CR")
print("")
print("Primer Semestre")
print("Unidades a producir: ",Unidades_Producir_1erSemestre_CR)
print("")
print("Segundo Semestre")
print("Unidades a producir: ",Unidades_Producir_2doSemestre_CR)
print("")
print("Total: ",Total_Unidades_Producir_CR)
print("")

# PRIMER SEMESTRE
print("Primer Semestre")
print("Material A")
print("Requerimiento de material: ",Materia_PrimaA_CR)
Total_Material_A_Requerido_1erSemestre_CR=Unidades_Producir_1erSemestre_CR*Materia_PrimaA_CR
print("Total de Material A requerido: ",Total_Material_A_Requerido_1erSemestre_CR)
print("")

print("Material B")
print("Requerimiento de material: ",Materia_PrimaB_CR)
Total_Material_B_Requerido_1erSemestre_CR=Unidades_Producir_1erSemestre_CR*Materia_PrimaB_CR
print("Total de Material A requerido: ",Total_Material_B_Requerido_1erSemestre_CR)
print("")

print("Material C")
print("Requerimiento de material: ",Materia_PrimaC_CR)
Total_Material_C_Requerido_1erSemestre_CR=Unidades_Producir_1erSemestre_CR*Materia_PrimaC_CR
print("Total de Material A requerido: ",Total_Material_C_Requerido_1erSemestre_CR)
print("")

## Segundo Semestre PRODUCTO CR
print("Segundo Semestre")
print("Material A")
print("Requerimiento de material: ",Materia_PrimaA_CR)
Total_Material_A_Requerido_2doSemestre_CR=Unidades_Producir_2doSemestre_CR*Materia_PrimaA_CR
print("Total de Material A requerido: ",Total_Material_A_Requerido_2doSemestre_CR)
print("")

print("Material B")
print("Requerimiento de material: ",Materia_PrimaB_CR)
Total_Material_B_Requerido_2doSemestre_CR=Unidades_Producir_2doSemestre_CR*Materia_PrimaB_CR
print("Total de Material A requerido: ",Total_Material_B_Requerido_2doSemestre_CR)
print("")

print("Material C")
print("Requerimiento de material: ",Materia_PrimaC_CR)
Total_Material_C_Requerido_2doSemestre_CR=Unidades_Producir_2doSemestre_CR*Materia_PrimaC_CR
print("Total de Material A requerido: ",Total_Material_C_Requerido_2doSemestre_CR)
print("")

print("TOTAL")
Total_Material_A_CR= Total_Material_A_Requerido_1erSemestre_CR + Total_Material_A_Requerido_2doSemestre_CR
print("Total de Material A requerido: ",Total_Material_A_CR)

Total_Material_B_CR= Total_Material_B_Requerido_1erSemestre_CR + Total_Material_B_Requerido_2doSemestre_CR
print("Total de Material A requerido: ",Total_Material_B_CR)

Total_Material_C_CR= Total_Material_C_Requerido_1erSemestre_CR + Total_Material_C_Requerido_2doSemestre_CR
print("Total de Material A requerido: ",Total_Material_C_CR)
print(SEPARADOR2)
print("")

print("TOTALES PRIMER SEMESTRE")
# TOTAL DE A
Total_Material_1erSemestre_A= Total_Material_A_Requerido_1erSemestre_CL + Total_Material_A_Requerido_1erSemestre_CE +Total_Material_A_Requerido_1erSemestre_CR
print("Material A: ",Total_Material_1erSemestre_A)

# TOTAL DE B
Total_Material_1erSemestre_B= Total_Material_B_Requerido_1erSemestre_CL + Total_Material_B_Requerido_1erSemestre_CE +Total_Material_B_Requerido_1erSemestre_CR
print("Material B: ",Total_Material_1erSemestre_B)

# TOTAL C
Total_Material_1erSemestre_C= Total_Material_C_Requerido_1erSemestre_CL + Total_Material_C_Requerido_1erSemestre_CE +Total_Material_C_Requerido_1erSemestre_CR
print("Material B: ",Total_Material_1erSemestre_C)
print("")

print("TOTALES SEGUNDO SEMESTRE")
# TOTAL DE A
Total_Material_2doSemestre_A= Total_Material_A_Requerido_2doSemestre_CL + Total_Material_A_Requerido_2doSemestre_CE +Total_Material_A_Requerido_2doSemestre_CR
print("Material A: ",Total_Material_2doSemestre_A)

# TOTAL DE B
Total_Material_2doSemestre_B= Total_Material_B_Requerido_2doSemestre_CL + Total_Material_B_Requerido_2doSemestre_CE +Total_Material_B_Requerido_2doSemestre_CR
print("Material A: ",Total_Material_2doSemestre_B)

# TOTAL DE C
Total_Material_2doSemestre_C= Total_Material_C_Requerido_2doSemestre_CL + Total_Material_C_Requerido_2doSemestre_CE +Total_Material_C_Requerido_2doSemestre_CR
print("Material A: ",Total_Material_2doSemestre_C)
print(SEPARADOR2)
print("")

print("TOTAL DE A")
Total_MaterialA= Total_Material_1erSemestre_A + Total_Material_2doSemestre_A
print("Total A: ",Total_MaterialA)
print("")

print("TOTAL DE B")
Total_MaterialB= Total_Material_1erSemestre_B + Total_Material_2doSemestre_B
print("Total B: ",Total_MaterialB)
print("")

print("TOTAL DE C")
Total_MaterialC= Total_Material_1erSemestre_C + Total_Material_2doSemestre_C
print("Total C: ",Total_MaterialC)
print(SEPARADOR2)
print("")


# PROCEDIMIENTO 5
print("5. Presupuesto de Compra de Materiales")
print("")
# Material A
print("Material A")

# Primer Semestre
print("Primer Semestre")
print("Requerimiento de materiales: ",Total_Material_1erSemestre_A)
print("Inventario Final: ",Materia_PrimaA_Inventario_Inicial)
Total_Materiales_1erSemestre_A= Total_Material_1erSemestre_A + Materia_PrimaA_Inventario_Inicial
print("Total de Materiales: ",Total_Materiales_1erSemestre_A)
print("Inventario Inicial: ",Materia_PrimaA_Inventario_Inicial)
Materiales_Comprar_1erSemestre_A=Total_Materiales_1erSemestre_A - Materia_PrimaA_Inventario_Inicial
print("Material a comprar: ",Materiales_Comprar_1erSemestre_A)
print("Precio de Compra: ",Materia_PrimaA_Costo_1er_Semestre)
Total_Materiales_1erSemestre_Dinero_A=Materiales_Comprar_1erSemestre_A * Materia_PrimaA_Costo_1er_Semestre
print("Total de Material A en $: ",Total_Materiales_1erSemestre_Dinero_A)
print("")

# Segundo Semestre
print("Material A")
print("Segundo Semestre")
print("Requerimiento de materiales: ",Total_Material_2doSemestre_A)
print("Inventario Final: ",Materia_PrimaA_Inventario_Final)
Total_Materiales_2doSemestre_A= Total_Material_2doSemestre_A + Materia_PrimaA_Inventario_Final
print("Total de Materiales: ",Total_Materiales_2doSemestre_A)
print("Inventario Inicial: ",Materia_PrimaA_Inventario_Inicial)
Materiales_Comprar_2doSemestre_A = Total_Materiales_2doSemestre_A - Materia_PrimaA_Inventario_Inicial
print("Precio de Compra: ",Materiales_Comprar_2doSemestre_A)
print("Precio de Compra: ",Materia_PrimaA_Costo_2do_Semestre)
Total_Materiales_2doSemestre_Dinero_A=Materiales_Comprar_2doSemestre_A * Materia_PrimaA_Costo_2do_Semestre
print("Total de Material A en $: ",Total_Materiales_2doSemestre_Dinero_A)
print("")
#print("Total")
#Total_RequeridoA_CL=Total_Materiales_1erSemestre_Dinero_A+Total_Materiales_2doSemestre_Dinero_A
#print("Requerimiento de materiales: ",Total_RequeridoA_CL)

# TOTAL
print("TOTAL")
print("Requerimiento de materiales: ",Total_MaterialA)
print("Inventario Final: ",Materia_PrimaA_Inventario_Final)
Total_2016_Materiales_A= Total_MaterialA + Materia_PrimaA_Inventario_Final
print("Total de Materiales: ",Total_2016_Materiales_A)
print("Inventario Inicial: ",Materia_PrimaA_Inventario_Inicial)
Material_Comprar_A= Total_2016_Materiales_A - Materia_PrimaA_Inventario_Inicial
print("Material a comprar: ",Material_Comprar_A)
Total_Materiales_Dinero_A= Total_Materiales_1erSemestre_Dinero_A + Total_Materiales_2doSemestre_Dinero_A
print("Total de Material A en $: ",Total_Materiales_Dinero_A)
print(SEPARADOR2)
print("")
print("")

# MATERIAL B
print("Material B")
print("")

# PRIMER SEMESTRE
print("PRIMER SEMESTRE")
print("Requerimiento de materiales: ",Total_Material_1erSemestre_B)
print("Inventario Final: ",Materia_PrimaB_Inventario_Inicial)
Total_Materiales_1erSemestre_B= Total_Material_1erSemestre_B + Materia_PrimaB_Inventario_Inicial
print("Total de Materiales: ",Total_Materiales_1erSemestre_B)
print("Inventario Inicial: ",Materia_PrimaB_Inventario_Inicial)
Materiales_Comprar_1erSemestre_B=Total_Materiales_1erSemestre_B - Materia_PrimaB_Inventario_Inicial
print("Material a comprar: ",Materiales_Comprar_1erSemestre_B)
print("Precio de Compra: ",Materia_PrimaB_Costo_1er_Semestre)
Total_Materiales_1erSemestre_Dinero_B=Materiales_Comprar_1erSemestre_B * Materia_PrimaB_Costo_1er_Semestre
print("Total de Material A en $: ",Total_Materiales_1erSemestre_Dinero_B)
print("")

# SEGUNDO SEMESTRE
print("SEGUNDO SEMESTRE")
print("Requerimiento de materiales: ",Total_Material_2doSemestre_B)
print("Inventario Final: ",Materia_PrimaB_Inventario_Final)
Total_Materiales_2doSemestre_B= Total_Material_2doSemestre_B + Materia_PrimaB_Inventario_Final
print("Total de Materiales: ",Total_Materiales_2doSemestre_B)
print("Inventario Inicial: ",Materia_PrimaB_Inventario_Inicial)
Materiales_Comprar_2doSemestre_B= Total_Materiales_2doSemestre_B - Materia_PrimaB_Inventario_Inicial
print("Material a comprar: ",Materiales_Comprar_2doSemestre_B)
print("Precio de Compra: ",Materia_PrimaB_Costo_2do_Semestre)
Total_Materiales_2doSemestre_Dinero_B= Materiales_Comprar_2doSemestre_B * Materia_PrimaB_Costo_2do_Semestre
print("Total de Material A en $: ",Total_Materiales_2doSemestre_Dinero_B)
print("")

# TOTAL
print("TOTAL")
print("Requerimiento de materiales: ",Total_MaterialB)
print("Inventario Final: ",Materia_PrimaB_Inventario_Final)
Total_2016_Materiales_B= Total_MaterialB + Materia_PrimaB_Inventario_Final
print("Total de Materiales: ",Total_2016_Materiales_B)
print("Inventario Inicial: ",Materia_PrimaB_Inventario_Inicial)
Material_Comprar_B= Total_2016_Materiales_B - Materia_PrimaB_Inventario_Inicial
print("Material a comprar: ",Material_Comprar_B)
Total_Materiales_Dinero_B= Total_Materiales_1erSemestre_Dinero_B + Total_Materiales_2doSemestre_Dinero_B
print("Total de Material A en $: ",Total_Materiales_Dinero_B)
print(SEPARADOR2)
print("")
print("")

# MATERIAL C
print("Material C")

# Primer Semestre
print("Primer Semestre")
print("Requerimiento de materiales: ",Total_Material_1erSemestre_C)
print("Inventario Final: ",Materia_PrimaC_Inventario_Inicial)
Total_Materiales_1erSemestre_C= Total_Material_1erSemestre_C + Materia_PrimaC_Inventario_Inicial
print("Total de Materiales: ",Total_Materiales_1erSemestre_C)
print("Inventario Inicial: ",Materia_PrimaC_Inventario_Inicial)
Materiales_Comprar_1erSemestre_C=Total_Materiales_1erSemestre_C - Materia_PrimaC_Inventario_Inicial
print("Material a comprar: ",Materiales_Comprar_1erSemestre_C)
print("Precio de Compra: ",Materia_PrimaC_Costo_1er_Semestre)
Total_Materiales_1erSemestre_Dinero_C=Materiales_Comprar_1erSemestre_C * Materia_PrimaC_Costo_1er_Semestre
print("Total de Material A en $: ",Total_Materiales_1erSemestre_Dinero_C)
print("")

# Segundo Semestre
print("Material C")
print("Segundo Semestre")
print("Requerimiento de materiales: ",Total_Material_2doSemestre_C)
print("Inventario Final: ",Materia_PrimaC_Inventario_Final)
Total_Materiales_2doSemestre_C= Total_Material_2doSemestre_C + Materia_PrimaC_Inventario_Final
print("Total de Materiales: ",Total_Materiales_2doSemestre_C)
print("Inventario Inicial: ",Materia_PrimaC_Inventario_Inicial)
Materiales_Comprar_2doSemestre_C = Total_Materiales_2doSemestre_C - Materia_PrimaC_Inventario_Inicial
print("Precio de Compra: ",Materiales_Comprar_2doSemestre_C)
print("Precio de Compra: ",Materia_PrimaC_Costo_2do_Semestre)
Total_Materiales_2doSemestre_Dinero_C=Materiales_Comprar_2doSemestre_C * Materia_PrimaC_Costo_2do_Semestre
print("Total de Material A en $: ",Total_Materiales_2doSemestre_Dinero_C)
print("")

# TOTAL
print("TOTAL")
print("Requerimiento de materiales: ",Total_MaterialC)
print("Inventario Final: ",Materia_PrimaC_Inventario_Final)
Total_2016_Materiales_C= Total_MaterialC + Materia_PrimaC_Inventario_Final
print("Total de Materiales: ",Total_2016_Materiales_C)
print("Inventario Inicial: ",Materia_PrimaC_Inventario_Inicial)
Material_Comprar_C= Total_2016_Materiales_C - Materia_PrimaC_Inventario_Inicial
print("Material a comprar: ",Material_Comprar_C)
Total_Materiales_Dinero_C= Total_Materiales_1erSemestre_Dinero_C + Total_Materiales_2doSemestre_Dinero_C
print("Total de Material A en $: ",Total_Materiales_Dinero_C)
print(SEPARADOR2)
print("")
print("")

# Compras totales
print("PRIMER SEMESTRE")
Compras_Totales_1erSemestre= Total_Materiales_1erSemestre_Dinero_A + Total_Materiales_1erSemestre_Dinero_B + Total_Materiales_1erSemestre_Dinero_C
print("Compras totales: ",Compras_Totales_1erSemestre)
print("")

# SEGUNDO SEMESTRE
print("SEGUNDO SEMESTRE")
Compras_Totales_2doSemestre=Total_Materiales_2doSemestre_Dinero_A + Total_Materiales_2doSemestre_Dinero_B + Total_Materiales_2doSemestre_Dinero_C
print("Compras totales: ",Compras_Totales_2doSemestre)
print("")

# COMPRAS TOTALES ANUALES
Compras_Totales_Anuales= Compras_Totales_1erSemestre + Compras_Totales_2doSemestre
print("Compras Totales Anuales: ",Compras_Totales_Anuales)
print(SEPARADOR2)
print("")
print("")

# PROCESO 6
print("6. Determinación del saldo de Proveedores y Flujo de Salidas")
print("Saldo de Proveedores: ",Proveedores)
print("Compras: ",Compras_Totales_Anuales)
Total_Proveedores = Proveedores + Compras_Totales_Anuales
print("Total de Proveedores: ",Total_Proveedores)
print("")

print("Salidas de Efectivo")
Proveedores_2015=float(input("¿Que cantidad en % que va cobrar del saldo de Proveedores 2015? (Dato en DECIMALES): "))
Por_Proveedores_2015= Proveedores * Proveedores_2015
print("Por Proveedores del 2015: ",Por_Proveedores_2015)
Proveedores_2016=float(input("¿Que cantidad en % que va cobrar del saldo de Proveedores 2016? (Dato en DECIMALES): "))
Por_Proveedores_2016= Compras_Totales_Anuales * Proveedores_2016
print("Por Proveedores del 2016: ",Por_Proveedores_2016)
Total_Salidas_2016= Por_Proveedores_2015 + Por_Proveedores_2016
print("Total de Salidas 2016: ",Total_Salidas_2016)
print("")

Saldo_Proveedores_2016= Total_Proveedores - Total_Salidas_2016
print("Saldo de Proveedores del 2016: ",Saldo_Proveedores_2016)
print(SEPARADOR2)
print("")
print("")

# PROCESO 7
print("7. Presupuesto de Mano de Obra Directa")
print("")
print("PRODUCTO CL")
print("Primer Semestre")
print("Unidades a producir: ",Unidades_Producir_1erSemestre_CL)
print("Horas requeridas por unidad: ",Horas_Mano_Obra_CL)
Total_Horas_1erSemestre_CL= Unidades_Producir_1erSemestre_CL * Horas_Mano_Obra_CL
print("Total de horas requeridas: ",Total_Horas_1erSemestre_CL)
print("Cuota por hora: ",Mano_Obra_Primer_Semestre)
Importe_MOD_1erSemestre_CL= Total_Horas_1erSemestre_CL * Mano_Obra_Primer_Semestre
print("Importe de M.O.D.: ",Importe_MOD_1erSemestre_CL)
print("")

# SEGUNDO SEMESTRE
print("Segundo Semestre")
print("Unidades a producir: ",Unidades_Producir_2doSemestre_CL)
print("Horas requeridas por unidad: ",Horas_Mano_Obra_CL)
Total_Horas_2doSemestre_CL= Unidades_Producir_2doSemestre_CL * Horas_Mano_Obra_CL
print("Total de horas requeridas: ",Total_Horas_2doSemestre_CL)
print("Cuota por hora: ",Mano_Obra_Segundo_Semestre)
Importe_MOD_2doSemestre_CL= Total_Horas_2doSemestre_CL * Mano_Obra_Segundo_Semestre
print("Importe de M.O.D.: ",Importe_MOD_2doSemestre_CL)
print("")

# TOTAL
print("TOTAL")
print("Unidades a producir: ",Total_Unidades_Producir_CL)
print("Horas requeridas por unidad: ",Horas_Mano_Obra_CL)
Total_Horas_Requeridas_CL= Total_Unidades_Producir_CL * Horas_Mano_Obra_CL
print("Total de horas requeridas: ",Total_Horas_Requeridas_CL)
Importe_MOD_CL= Importe_MOD_1erSemestre_CL + Importe_MOD_2doSemestre_CL
print("Importe de M.O.D.: ",Importe_MOD_CL)
print(SEPARADOR2)
print("")

# PRODUCTO CE
print("PRODUCTO CE")
print("Primer Semestre")
print("Unidades a producir: ",Unidades_Producir_1erSemestre_CE)
print("Horas requeridas por unidad: ",Horas_Mano_Obra_CE)
Total_Horas_1erSemestre_CE= Unidades_Producir_1erSemestre_CE * Horas_Mano_Obra_CE
print("Total de horas requeridas: ",Total_Horas_1erSemestre_CE)
print("Cuota por hora: ",Mano_Obra_Primer_Semestre)
Importe_MOD_1erSemestre_CE= Total_Horas_1erSemestre_CE * Mano_Obra_Primer_Semestre
print("Importe de M.O.D.: ",Importe_MOD_1erSemestre_CE)
print("")

# SEGUNDO SEMESTRE
print("Segundo Semestre")
print("Unidades a producir: ",Unidades_Producir_2doSemestre_CE)
print("Horas requeridas por unidad: ",Horas_Mano_Obra_CE)
Total_Horas_2doSemestre_CE= Unidades_Producir_2doSemestre_CE * Horas_Mano_Obra_CE
print("Total de horas requeridas: ",Total_Horas_2doSemestre_CE)
print("Cuota por hora: ",Mano_Obra_Segundo_Semestre)
Importe_MOD_2doSemestre_CE= Total_Horas_2doSemestre_CE * Mano_Obra_Segundo_Semestre
print("Importe de M.O.D.: ",Importe_MOD_2doSemestre_CE)
print("")

# TOTAL
print("TOTAL")
print("Unidades a producir: ",Total_Unidades_Producir_CE)
print("Horas requeridas por unidad: ",Horas_Mano_Obra_CE)
Total_Horas_Requeridas_CE= Total_Unidades_Producir_CE * Horas_Mano_Obra_CE
print("Total de horas requeridas: ",Total_Horas_Requeridas_CE)
Importe_MOD_CE= Importe_MOD_1erSemestre_CE + Importe_MOD_2doSemestre_CE
print("Importe de M.O.D.: ",Importe_MOD_CE)
print(SEPARADOR2)
print("")

# PRODUCTO CR
print("PRODUCTO CR")
print("Primer Semestre")
print("Unidades a producir: ",Unidades_Producir_1erSemestre_CR)
print("Horas requeridas por unidad: ",Horas_Mano_Obra_CR)
Total_Horas_1erSemestre_CR= Unidades_Producir_1erSemestre_CR * Horas_Mano_Obra_CR
print("Total de horas requeridas: ",Total_Horas_1erSemestre_CR)
print("Cuota por hora: ",Mano_Obra_Primer_Semestre)
Importe_MOD_1erSemestre_CR= Total_Horas_1erSemestre_CR * Mano_Obra_Primer_Semestre
print("Importe de M.O.D.: ",Importe_MOD_1erSemestre_CR)
print("")

# SEGUNDO SEMESTRE
print("Segundo Semestre")
print("Unidades a producir: ",Unidades_Producir_2doSemestre_CR)
print("Horas requeridas por unidad: ",Horas_Mano_Obra_CR)
Total_Horas_2doSemestre_CR= Unidades_Producir_2doSemestre_CR * Horas_Mano_Obra_CR
print("Total de horas requeridas: ",Total_Horas_2doSemestre_CR)
print("Cuota por hora: ",Mano_Obra_Segundo_Semestre)
Importe_MOD_2doSemestre_CR= Total_Horas_2doSemestre_CR * Mano_Obra_Segundo_Semestre
print("Importe de M.O.D.: ",Importe_MOD_2doSemestre_CR)
print("")

# TOTAL
print("TOTAL")
print("Unidades a producir: ",Total_Unidades_Producir_CR)
print("Horas requeridas por unidad: ",Horas_Mano_Obra_CR)
Total_Horas_Requeridas_CR= Total_Unidades_Producir_CR * Horas_Mano_Obra_CR
print("Total de horas requeridas: ",Total_Horas_Requeridas_CR)
Importe_MOD_CR= Importe_MOD_1erSemestre_CR + Importe_MOD_2doSemestre_CR
print("Importe de M.O.D.: ",Importe_MOD_CR)
print(SEPARADOR2)
print("")

# TOTALES
print("Total de horas requeridas por semestre")
print("")
print("PRIMER SEMESTRE")
Total_Horas_Requeridas_1erSemestre= Total_Horas_1erSemestre_CL + Total_Horas_1erSemestre_CE + Total_Horas_1erSemestre_CR
print(Total_Horas_Requeridas_1erSemestre)
print("")
print("SEGUNDO SEMESTRE")
Total_Horas_Requeridas_2doSemestre= Total_Horas_2doSemestre_CL + Total_Horas_2doSemestre_CE + Total_Horas_2doSemestre_CR
print(Total_Horas_Requeridas_2doSemestre)
print("")
print("ANUALMENTE")
Total_Horas_Requeridas= Total_Horas_Requeridas_CL + Total_Horas_Requeridas_CE + Total_Horas_Requeridas_CR
print(Total_Horas_Requeridas)
print(SEPARADOR2)
print("")

print("Total de M.O.D. por semestre")
print("")

print("PRIMER SEMESTRE")
Total_MOD_1erSemestre= Importe_MOD_1erSemestre_CL + Importe_MOD_1erSemestre_CE + Importe_MOD_1erSemestre_CR
print(Total_MOD_1erSemestre)
print("")

print("SEGUNDO SEMESTRE")
Total_MOD_2doSemestre= Importe_MOD_2doSemestre_CL + Importe_MOD_2doSemestre_CE + Importe_MOD_2doSemestre_CR
print(Total_MOD_2doSemestre)
print("")

print("TOTAL")
Total_MOD= Importe_MOD_CL + Importe_MOD_CE + Importe_MOD_CR
print(Total_MOD)
print(SEPARADOR2)
print("")
print("")

# PRIOCEDIMIENTO 8
print("8. Presupuesto de Gastos Indirectos de Fabricación")

# PRIMER SEMESTRE
print("Primer Semestre")
Depreciacion_1erSemestre= Depreciacion_Indirectos/2
print("Depreciación: ",Depreciacion_1erSemestre)
Seguros_1erSemestre= Seguros/2
print("Seguros: ",Seguros_1erSemestre)
print("Mantenimiento: ",Mantenimiento_1er_Semestre)
print("Energeticos: ",Energeticos_1er_Semestre)
Varios_Indirectos_1erSemestre=Varios_Indirectos/2
print("Varios: ",Varios_Indirectos_1erSemestre)
Total_GIF_1erSemestre=Depreciacion_1erSemestre + Seguros_1erSemestre + Mantenimiento_1er_Semestre + Energeticos_1er_Semestre + Varios_Indirectos_1erSemestre
print("Total G.I.F. por semestre: ",Total_GIF_1erSemestre)
print("")

# SEGUNDO SEMESTRE
Depreciacion_2doSemestre= Depreciacion_Indirectos/2
print("Depreciación: ",Depreciacion_2doSemestre)
Seguros_2doSemestre= Seguros/2
print("Seguros: ",Seguros_2doSemestre)
print("Mantenimiento: ",Mantenimiento_2do_Semestre)
print("Energeticos: ",Energeticos_2do_Semestre)
Varios_Indirectos_2doSemestre=Varios_Indirectos/2
print("Varios: ",Varios_Indirectos_2doSemestre)
Total_GIF_2doSemestre=Depreciacion_2doSemestre+Seguros_2doSemestre+Mantenimiento_2do_Semestre+Energeticos_2do_Semestre+Varios_Indirectos_2doSemestre
print("Total G.I.F. por semestre: ",Total_GIF_2doSemestre)
print("")

# TOTALES ANUALES
print("Anualmente")
Depreciacion_Total= Depreciacion_1erSemestre + Depreciacion_2doSemestre
print("Depreciación: ",Depreciacion_Total)
Seguros_Total= Seguros_1erSemestre + Seguros_2doSemestre
print("Seguros: ",Seguros_Total)
Mantenimiento_Total = Mantenimiento_1er_Semestre +Mantenimiento_2do_Semestre
print("Mantenimiento: ",Mantenimiento_Total)
Energeticos_Total = Energeticos_1er_Semestre + Energeticos_2do_Semestre
print("Energeticos: ",Energeticos_Total)
Varios_Total = Varios_Indirectos_1erSemestre + Varios_Indirectos_2doSemestre
print("Varios: ",Varios_Total)
Total_GIF = Depreciacion_Total + Seguros_Total + Mantenimiento_Total + Energeticos_Total + Varios_Total
print(f"Total G.I.F. por semestre: {Total_GIF:.2f}")
print("")

# DETERMINAR COSTO POR HORA
print("Coeficiente para determinar el costo por hora de Gastos Indirectos de Fabricación")
print(f"Total G.I.F. por semestre: {Total_GIF:.2f}")
print("Total horas M.O.D. Anual: ",Total_Horas_Requeridas)
Costo_Hora_GIF = Total_GIF/Total_Horas_Requeridas
print("Costo por Hora de G.I.F.: ",Costo_Hora_GIF)
print(SEPARADOR2)
print("")
print("")

# PROCESO 9
print("9. Presupuesto de Gastos de Operación")

# PRIMER SEMESTRE
print("Primer Semestre")
Depreciacion_1erSemestre_Administracion= Depreciacion/2
print("Depreciación: ",Depreciacion_1erSemestre_Administracion)
Sueldos_Y_Salarios_1erSemestre= Sueldos_Y_Salarios/2
print("Sueldos y Salarios: ",Sueldos_Y_Salarios_1erSemestre)
Comisiones_1erSemestre= Total_ventas_1er_semestre * Comisiones
print("Comisiones: ",Comisiones_1erSemestre)
print("Varios: ",Varios_1er_Semestre)
Intereses_por_Prestamo_1erSemestre = Intereses_por_Prestamo/2
print("Intereses del Prestamo: ",Intereses_por_Prestamo_1erSemestre)
Total_Gastos_Operacion_1erSemestre= Depreciacion_1erSemestre_Administracion+Sueldos_Y_Salarios_1erSemestre+Comisiones_1erSemestre+Varios_1er_Semestre+Intereses_por_Prestamo_1erSemestre
print("Total de Gastos de Operación: ",Total_Gastos_Operacion_1erSemestre)
print("")

# SEGUNDO SEMESTRE
print("Segundo Semestre")
Depreciacion_2doSemestre_Administracion=Depreciacion/2
print("Depreciación: ",Depreciacion_2doSemestre_Administracion)
Sueldos_Y_Salarios_2doSemestre= Sueldos_Y_Salarios/2
print("Sueldos y Salarios: ",Sueldos_Y_Salarios_2doSemestre)
Comisiones_2doSemestre= Total_ventas_2do_semestre * Comisiones
print("Comisiones: ",Comisiones_2doSemestre)
print("Varios: ",Varios_2do_Semestre)
Intereses_por_Prestamo_2doSemestre = Intereses_por_Prestamo/2
print("Intereses del Prestamo: ",Intereses_por_Prestamo_2doSemestre)
Total_Gastos_Operacion_2doSemestre= Depreciacion_2doSemestre_Administracion+Sueldos_Y_Salarios_2doSemestre+Comisiones_2doSemestre+Varios_2do_Semestre+Intereses_por_Prestamo_2doSemestre
print("Total de Gastos de Operación: ",Total_Gastos_Operacion_2doSemestre)
print("")

# TOTALES
Depreciacion_Total_Operacion= Depreciacion_1erSemestre_Administracion + Depreciacion_2doSemestre_Administracion
print("Depreciación: ",Depreciacion_Total_Operacion)
Sueldos_Y_Salarios_Total= Sueldos_Y_Salarios_1erSemestre + Sueldos_Y_Salarios_2doSemestre
print("Sueldos y Salarios: ",Sueldos_Y_Salarios_Total)
Comisiones_Total = Comisiones_1erSemestre + Comisiones_2doSemestre
print("Comisiones: ",Comisiones_Total)
Varios_Total_Operacion = Varios_1er_Semestre + Varios_2do_Semestre
print("Varios: ",Varios_Total_Operacion)
Intereses_por_Prestamo_Total = Intereses_por_Prestamo_1erSemestre + Intereses_por_Prestamo_2doSemestre
print("Intereses del Prestamo :",Intereses_por_Prestamo_Total)
Total_Gastos_Operacion = Depreciacion_Total_Operacion + Sueldos_Y_Salarios_Total + Comisiones_Total + Varios_Total_Operacion + Intereses_por_Prestamo_Total
print("Total de Gastos de Operación: ",Total_Gastos_Operacion)
print(SEPARADOR2)
print("")
print("")

# PROCESO 10
print("10. Determinación del Costo Unitario de Productos Terminados")
print("")
print("PRODUCTO CL")
print("Costo")
print("Material A: ",Materia_PrimaA_Costo_2do_Semestre)
print("Material B: ",Materia_PrimaB_Costo_2do_Semestre)
print("Material C: ",Materia_PrimaC_Costo_2do_Semestre)
print("Mano de Obra: ",Mano_Obra_Segundo_Semestre)
print("Gastos Indirectos de Fabricación: ",Costo_Hora_GIF)
print("")

# CANTIDAD
print("Cantidad")
print("Material A: ",Materia_PrimaA_CL)
print("Material B: ",Materia_PrimaB_CL)
print("Material C: ",Materia_PrimaC_CL)
print("Mano de Obra: ",Horas_Mano_Obra_CL)
print("Gastos Indirectos de Fabricación: ",Horas_Mano_Obra_CL)
print("")

# COSTO UNITARIO
print("COSTO UNITARIO")
Costo_MateriaA_CL=Materia_PrimaA_Costo_2do_Semestre * Materia_PrimaA_CL
Costo_MateriaB_CL=Materia_PrimaB_Costo_2do_Semestre * Materia_PrimaB_CL
Costo_MateriaC_CL= Materia_PrimaC_Costo_2do_Semestre * Materia_PrimaC_CL
Costo_Mano_Obra_CL= Mano_Obra_Segundo_Semestre * Horas_Mano_Obra_CL
Costo_GastosFabricacion_CL= Costo_Hora_GIF * Horas_Mano_Obra_CL

print("Material A: ",Costo_MateriaA_CL)
print("Material B: ",Costo_MateriaB_CL)
print("Material C: ",Costo_MateriaC_CL)
print("Mano de Obra: ",Costo_Mano_Obra_CL)
print("Gastos Indirectos de Fabricación: ",Costo_GastosFabricacion_CL)
Costo_Unitario_CL = Costo_MateriaA_CL + Costo_MateriaB_CL + Costo_MateriaC_CL + Costo_Mano_Obra_CL + Costo_GastosFabricacion_CL
print("Costo Unitario: ",Costo_Unitario_CL)
print(SEPARADOR2)
print("")
print("")

# PRODUCTO CE
print("PRODUCTO CE")
print("Costo")
print("Material A: ",Materia_PrimaA_Costo_2do_Semestre)
print("Material B: ",Materia_PrimaB_Costo_2do_Semestre)
print("Material C: ",Materia_PrimaC_Costo_2do_Semestre)
print("Mano de Obra: ",Mano_Obra_Segundo_Semestre)
print("Gastos Indirectos de Fabricación: ",Costo_Hora_GIF)
print("")

# CANTIDAD
print("Cantidad")
print("Material A: ",Materia_PrimaA_CE)
print("Material B: ",Materia_PrimaB_CE)
print("Material C: ",Materia_PrimaC_CE)
print("Mano de Obra: ",Horas_Mano_Obra_CE)
print("Gastos Indirectos de Fabricación: ",Horas_Mano_Obra_CE)
print("")

# COSTO UNITARIO
print("COSTO UNITARIO")
Costo_MateriaA_CE= Materia_PrimaA_Costo_2do_Semestre * Materia_PrimaA_CE
Costo_MateriaB_CE= Materia_PrimaB_Costo_2do_Semestre * Materia_PrimaB_CE
Costo_MateriaC_CE= Materia_PrimaC_Costo_2do_Semestre * Materia_PrimaC_CE
Costo_Mano_Obra_CE= Mano_Obra_Segundo_Semestre * Horas_Mano_Obra_CE
Costo_GastosFabricacion_CE= Costo_Hora_GIF * Horas_Mano_Obra_CE

print(f"Material A: {Costo_MateriaA_CE:.2f}")
print(f"Material B: {Costo_MateriaB_CE:.2f}")
print("Material C: ",Costo_MateriaC_CE)
print("Mano de Obra: ",Costo_Mano_Obra_CE)
print(f"Gastos Indirectos de Fabricación: {Costo_GastosFabricacion_CE:.2f}")
Costo_Unitario_CE = Costo_MateriaA_CE + Costo_MateriaB_CE + Costo_MateriaC_CE + Costo_Mano_Obra_CE + Costo_GastosFabricacion_CE
print("Costo Unitario: ",Costo_Unitario_CE)
print(SEPARADOR2)
print("")
print("")

# PRODUCTO CR
print("PRODUCTO CR")
print("Costo")
print("Material A: ",Materia_PrimaA_Costo_2do_Semestre)
print("Material B: ",Materia_PrimaB_Costo_2do_Semestre)
print("Material C: ",Materia_PrimaC_Costo_2do_Semestre)
print("Mano de Obra: ",Mano_Obra_Segundo_Semestre)
print(f"Gastos Indirectos de Fabricación: {Costo_Hora_GIF:.2f}")
print("")

# CANTIDAD
print("Cantidad")
print("Material A: ",Materia_PrimaA_CR)
print("Material B: ",Materia_PrimaB_CR)
print("Material C: ",Materia_PrimaC_CR)
print("Mano de Obra: ",Horas_Mano_Obra_CR)
print("Gastos Indirectos de Fabricación: ",Horas_Mano_Obra_CR)
print("")

# COSTO UNITARIO
print("COSTO UNITARIO")
Costo_MateriaA_CR=Materia_PrimaA_Costo_2do_Semestre * Materia_PrimaA_CR
Costo_MateriaB_CR=Materia_PrimaB_Costo_2do_Semestre * Materia_PrimaB_CR
Costo_MateriaC_CR= Materia_PrimaC_Costo_2do_Semestre * Materia_PrimaC_CR
Costo_Mano_Obra_CR= Mano_Obra_Segundo_Semestre * Horas_Mano_Obra_CR
Costo_GastosFabricacion_CR= Costo_Hora_GIF * Horas_Mano_Obra_CR

print("Material A: ",Costo_MateriaA_CR)
print("Material B: ",Costo_MateriaB_CR)
print("Material C: ",Costo_MateriaC_CR)
print("Mano de Obra: ",Costo_Mano_Obra_CR)
print(f"Gastos Indirectos de Fabricación: {Costo_GastosFabricacion_CR:.2f}")
Costo_Unitario_CR = Costo_MateriaA_CR + Costo_MateriaB_CR + Costo_MateriaC_CR + Costo_Mano_Obra_CR + Costo_GastosFabricacion_CR
print(f"Costo Unitario: {Costo_Unitario_CR:.2f}")
print(SEPARADOR2)
print("")
print("")

# PROCESO 11
print("11. Valuación de Inventarios Finales")
print("")
print("Inventario Final de Materiales")
print("Unidades")
print("Material A: ",Materia_PrimaA_Inventario_Final)
print("Material B: ",Materia_PrimaB_Inventario_Final)
print("Material C: ",Materia_PrimaC_Inventario_Final)
print("")

# COSTO
print("Costo Unitario")
print("Material A: ",Materia_PrimaA_Costo_2do_Semestre)
print("Material B: ",Materia_PrimaB_Costo_2do_Semestre)
print("Material C: ",Materia_PrimaC_Costo_2do_Semestre)

# COSTO TOTAL
print("COSTO TOTAL")
Costo_Total_MaterialA= Materia_PrimaA_Inventario_Final * Materia_PrimaA_Costo_2do_Semestre
Costo_Total_MaterialB= Materia_PrimaB_Inventario_Final * Materia_PrimaB_Costo_2do_Semestre
Costo_Total_MaterialC= Materia_PrimaC_Inventario_Final * Materia_PrimaC_Costo_2do_Semestre
print("Material A: ",Costo_Total_MaterialA)
print("Material B: ",Costo_Total_MaterialB)
print("Material C: ",Costo_Total_MaterialC)
Inventario_Final_Materiales= Costo_Total_MaterialA + Costo_Total_MaterialB + Costo_Total_MaterialC
print("Inventario Final de Materiales: ",Inventario_Final_Materiales)
print(SEPARADOR2)
print("")
print("")

# INVENTARIO FINAL PRODUCTO TERMINADO
print("Inventario Final de Producto Terminado")
print("Unidades")
print("Producto CL: ",Producto_CL_Inventario_Final)
print("Producto CE: ",Producto_CE_Inventario_Final)
print("Producto CR: ",Producto_CR_Inventario_Final)
print("")

# Costo Unitario
print("Costo Unitario")
print(f"Producto CL: {Costo_Unitario_CL:.2f}")
print(f"Producto CE: {Costo_Unitario_CE:.2f}")
print(f"Producto CR: {Costo_Unitario_CR:.2f}")
print("")

# Costo Total
Costo_Total_ProductoA=Producto_CL_Inventario_Final * Costo_Unitario_CL
Costo_Total_ProductoB=Producto_CE_Inventario_Final * Costo_Unitario_CE
Costo_Total_ProductoC=Producto_CR_Inventario_Final * Costo_Unitario_CR
print("Costo Total")
print(f"Producto CL: {Costo_Total_ProductoA:.2f}")
print(f"Producto CE: {Costo_Total_ProductoB:.2f}")
print(f"Producto CR: {Costo_Total_ProductoC:.2f}")
Inventario_Fianl_Producto=Costo_Total_ProductoA + Costo_Total_ProductoB + Costo_Total_ProductoC
print(f"Inventario Final de Producto Terminado: {Inventario_Fianl_Producto:.2f}")
print(SEPARADOR2)
print("")
print("")
print("")

# II. Presupuesto Financiero.
print("II. Presupuesto Financiero.")
print("")

print("Estado de Costo de Producción y Ventas")
print("Saldo Inicial de Materiales: ",Inventario_de_Materiales)
print("Compras de Materiales: ",Compras_Totales_Anuales)
Material_Disponible= Inventario_de_Materiales + Compras_Totales_Anuales
print("Material Disponible: ",Material_Disponible)
print("Inventario Final de Materiales: ",Inventario_Final_Materiales)
Materiales_Utilizados= Material_Disponible - Inventario_Final_Materiales
print("Materiales Utilizados: ",Materiales_Utilizados)
print("Mano de Obra Directa: ",Total_MOD)
print("Gastos de Fabricación Indirectos: ",Total_GIF)
Costo_Produccion= Materiales_Utilizados + Total_MOD + Total_GIF
print("Costo de Producción: ",Costo_Produccion)
print("Inventario Inicial de Productos Terminados: ",Inventario_de_Producto_Terminado)
Total_Produccion_Disponible= Costo_Produccion + Inventario_de_Producto_Terminado
print("Total de Producción Disponible: ",Total_Produccion_Disponible)
print(f"Inventario Final de Productos Terminados: {Inventario_Fianl_Producto:.2f}")
Costo_Ventas= Total_Produccion_Disponible - Inventario_Fianl_Producto
print(f"Costo de Ventas: {Costo_Ventas:.2f}")
print(SEPARADOR2)
print("")
print("")

# Estado de Resultados
print("Estado de Resultados")
print("")

ISR_Dato=float(input("Ingrese el porcentaje del ISR (EN DECIMALES): "))
PTU_Dato=float(input("Ingrese el porcentaje del PTU (EN DECIMALES): "))

print("Ventas: ",Total_Ventas)
print(f"Costo de Ventas: {Costo_Ventas:.2f}")
Utilidad_Bruta=Total_Ventas - Costo_Ventas
print(f"Utilidad Bruta: {Utilidad_Bruta:.2f}")
print(f"Gastos de Operación: {Total_Gastos_Operacion:.2f}")
Utilidad_Operacion=Utilidad_Bruta - Total_Gastos_Operacion
print(f"Utilidad de Operación: {Utilidad_Operacion:.2f}")
ISR_Total=Utilidad_Operacion * ISR_Dato
Total_PTU=Utilidad_Operacion * PTU_Dato
print(f"ISR: {ISR_Total:.2f}")
print(f"PTU: {Total_PTU:.2f}")
Utilidad_Neta=Utilidad_Operacion - ISR_Total - Total_PTU
print(f"Utilidad Neta: {Utilidad_Neta:.2f}")
print(SEPARADOR2)
print("")
print("")

# Estado de Flujo de Efectivo
print("Estado de Flujo de Efectivo")
print("")
print("Saldo Inicial de Efectivo: ",Efectivo)
print("Entradas:")
print("Cobranza 2016: ",Por_Cobranza_2016)
print("Cobranza 2015: ",Por_Cobranza_2015)
Total_Entradas=Por_Cobranza_2016+Por_Cobranza_2015
print("Total de Entradas: ",Total_Entradas)
Efectivo_Disponible=Total_Entradas+Efectivo
print("Efectivo Disponible: ",Efectivo_Disponible)
print("")

Maquinaria=float(input("Si se adquiere nueva maquinaria ingrese su valor: "))
print("Salidas:")
print("Proveedores 2016: ",Por_Proveedores_2016)
print("Proveedores 2015: ",Por_Proveedores_2015)
print("Pago Mano de Obra Directa: ",Total_MOD)
Pago_Gastos_Indirectos= Total_GIF-Depreciacion_Total
print("Pago Gastos Indirectos de Fabricación: ",Pago_Gastos_Indirectos)
Pago_Gastos_Operacion= Total_Gastos_Operacion-Depreciacion_Total_Operacion
print("Pago de Gastos de Operación: ",Pago_Gastos_Operacion)
print("Compra de Activo Fijo (Maquinaria): ",Maquinaria)
print("Pago ISR 2015: ",ISR_por_Pagar)
print("")

Total_Salidas=Por_Proveedores_2016 + Por_Proveedores_2015 + Total_MOD + Pago_Gastos_Indirectos + Pago_Gastos_Operacion + Maquinaria + ISR_por_Pagar
print("Total de Salidas: ",Total_Salidas)
Flujo_Efectivo_Actual= Efectivo_Disponible - Total_Salidas
print("Flujo de Efectivo Actual: ",Flujo_Efectivo_Actual)
print(SEPARADOR2)
print("")
print("")

# BALANCE GENERAL
print("Balance General")
print("ACTIVO")
print("Circulante")
print("")

print("Efectivo: ",Flujo_Efectivo_Actual)
print("Clientes: ",Saldo_Clientes_2016)
print("Deudores Diversos: ",Deudores_Diversos)
print("Funcionarios y Empleados: ",Funcionarios_Y_Empleados)
print("Inventario de Materiales: ",Inventario_Final_Materiales)
print(f"Inventario de Producto Terminado: {Inventario_Fianl_Producto:.2f}")
Total_Activo_Circulante_Balance=Flujo_Efectivo_Actual + Saldo_Clientes_2016 + Deudores_Diversos + Funcionarios_Y_Empleados + Inventario_Final_Materiales + Inventario_Fianl_Producto
print(f"Total de Activos Circulantes: {Total_Activo_Circulante_Balance:.2f}")
print("")

print("No Circulante")
print("Terreno: ",Terreno)
Planta_Equipo_NoCirculante= Planta_Y_Equipo + Maquinaria
print("Planta y Equipo: ",Planta_Equipo_NoCirculante)
Depreciación_Acumulada_NoCirculante= Depreciacion_Acumulada - Depreciacion_Total - Depreciacion_Total_Operacion
print("Depreciación Acumulada: ",Depreciación_Acumulada_NoCirculante)
Total_Activo_NoCirculante_Balance= Terreno + Planta_Equipo_NoCirculante + Depreciación_Acumulada_NoCirculante
print("Total Activos No Circulante: ",Total_Activo_NoCirculante_Balance)
Activo_Total_Balance= Total_Activo_Circulante_Balance + Total_Activo_NoCirculante_Balance
print(f"ACTIVO TOTAL: {Activo_Total_Balance:.2f}")
print("")

print("PASIVO")
print("Corto Plazo")
print("Proveedores: ",Saldo_Proveedores_2016)
print("Documentos por Pagar: ",Documentos_por_Pagar)
print(f"ISR por Pagar: {ISR_Total:.2f}")
print(f"PTU por Pagar: {Total_PTU:.2f}")
Total_Pasivo_CortoPlazo_Balance= Saldo_Proveedores_2016 + Documentos_por_Pagar + ISR_Total + Total_PTU
print(f"Total de Pasivo Corto Plazo: {Total_Pasivo_CortoPlazo_Balance:.2f}")
print("")

print("Largo Plazo")
print("Préstamos bancarios: ",Prestamos_Bancarios)
print("Total de Pasivo Largo Plazo: ",Prestamos_Bancarios)
Pasivo_Total_Balance= Total_Pasivo_CortoPlazo_Balance + Prestamos_Bancarios
print(f"PASIVO TOTAL: {Pasivo_Total_Balance:.2f}")
print("")

print("CAPITAL CONTABLE")
print("Capital Contribuido: ",Capital_Contribuido)
print("Capital Ganado: ",Capital_Ganado)
print(f"Utilidad del Ejercicio: {Utilidad_Neta:.2f}")
Total_Capital_Contable= Capital_Contribuido + Capital_Ganado + Utilidad_Neta
print(f"Total de Capital Contable: {Total_Capital_Contable:.2f}")
Suma_Pasivo_Capital_Balance= Pasivo_Total_Balance + Total_Capital_Contable
print(f"SUMA DE PASIVO Y CAPITAL: {Suma_Pasivo_Capital_Balance:.2f}")