# #🧩 Ejercicio 6: Refactorizar procesamiento de ventas (separar lógica/I-O + eficiencia + pruebas)

# Código inicial (mejorable)

# def totalize(sales):
#     t = 0
#     for s in sales:
#         if s["status"] == "ok":
#             price = s["price"]
#             qty = s["qty"]
#             disc = 0
#     if qty >= 10:
#         disc = 0.1
#         if s["customer"] == "vip":
#             disc = disc + 0.05
#             subtotal = price * qty
#             subtotal = subtotal - (subtotal * disc)
#             t = t + subtotal
#     else:
#         print("bad sale:", s)
#         print("TOTAL:", t)
#         return t

# Problemas típicos
# • Mezcla lógica con print (difícil de testear)
# • Descuentos “pegados” en el loop
# • No define claramente qué hacer con ventas inválidas
# • Variable disc y t poco descriptivas

# Tu objetivo
# Refactoriza para que:
# • Exista una función pura: calculate_sale_total(sale: dict) -> float (solo calcula)
# • Otra función: calculate_total(sales: list[dict]) -> float (suma)
# • La función que imprime quede aparte (opcional): report_invalid_sales(...)
# • Use nombres claros (total, discount, subtotal)
# • Maneje ventas inválidas sin imprimir en la función de cálculo (por ejemplo: ignorarlas o lanzar excepción, tú defines y lo documentas)

# Pruebas sugeridas
# Crea un conjunto de ventas y verifica:
# • Suma correcta con ventas “ok”
# • Descuento por cantidad ≥ 10 (10%).
# • Descuento extra por customer == "vip" (+5%).
# • Qué pasa con status != "ok" según tu decisión (ignora o error), y prueba ese comportamiento.




def calcular_total_venta(venta: dict) -> float:
    """
    Calcula el total de una venta válida.
    """

    # Validar si la venta es correcta
    if venta.get("status") != "ok":
        return 0  # ignoramos la venta

    # Datos de la venta
    precio = venta.get("price", 0)
    cantidad = venta.get("quantity", 0)
    cliente = venta.get("customer", "")

    # Total sin descuento
    subtotal = precio * cantidad

    # Descuento inicial
    descuento = 0

    # Si compra 10 o más productos → 10% de descuento
    if cantidad >= 10:
        descuento += 0.10

    # Si es cliente VIP → 5% adicional
    if cliente == "vip":
        descuento += 0.05

    # Aplicar descuento
    total = subtotal - (subtotal * descuento)

    return total


def calcular_total_ventas(lista_ventas: list[ dict]) -> float:
    """
    Suma todas las ventas válidas.
    """

    total = 0

    for venta in lista_ventas:
        total += calcular_total_venta(venta)

    return total


def mostrar_ventas_invalidas(lista_ventas: list[dict]) -> None:
    """
    Muestra ventas inválidas (solo para visualización).
    """

    for venta in lista_ventas:
        if venta.get("status") != "ok":
            print("Venta inválida:", venta)

