def show_menu():
    print("Menu:")
    print("1. Kopi         Rp10.000")
    print("2. Teh          Rp7.000")
    print("3. Jus          Rp15.000")
    print("4. Air Mineral  Rp5.000")

def order_drink():
    show_menu()
    choice = int(input("Pilihan Anda: "))
    quantity = int(input("Jumlah: "))
    if choice == 1:
        price = 10000
        drink = "Kopi"
    elif choice == 2:
        price = 7000
        drink = "Teh"
    elif choice == 3:
        price = 15000
        drink = "Jus"
    elif choice == 4:
        price = 5000
        drink = "Air Mineral"
    else:
        print("Maaf, pilihan tidak tersedia.")
        return