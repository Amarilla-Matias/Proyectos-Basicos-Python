menu = {
    1:{"Producto": "Cafe Americano", "precio": 15000},
    2:{"Producto": "Cafe con Leche", "precio": 20000},
    3:{"Producto": "Te", "precio": 25000},
    4:{"Producto": "Frappuccino", "precio": 30000},
    5:{"Producto": "Torta de Caramelo", "precio": 10000},
    6:{"Producto": "Cocido con Pan", "precio": 50000}
    }

pedido = []
total = 0
while True:
    print("\nMenu:")
    for key, item in menu.items():
        print(f"{key}.{item["Producto"]} - G{item["Producto"]:.2f}")
        eleccion = int(input("Selecciona un Producto (0 para Finalizar): "))
        if eleccion == 0:
            break

        if eleccion in menu:
            pedido.append(menu[eleccion]["Producto"])
            total += menu[eleccion]["precio"]
            print(f"{menu[eleccion]["Producto"]} añadido al pedido")

            print("\nResumen del pedido: ")
            for item in pedido:
                print(f"- {item}")
                print(f"Total: G{total:.2f}")