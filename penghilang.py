def show_menu():
    print("Menu:")
    print("1. Kopi         Rp10.000")
    print("2. Teh          Rp7.000")
    print("3. Jus          Rp15.000")
    print("4. Air Mineral  Rp5.000")

def calculate_total_price(quantity, price):
    return quantity * price

def order_drink():
    while True:
        show_menu()
        choice = int(input("Pilihan Anda: "))
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
            continue

        quantity = int(input("Jumlah: "))
        total_price = calculate_total_price(quantity, price)
        print(f"Anda memesan {quantity} {drink}. Total harga: Rp{total_price}")

        another_order = input("Apakah Anda ingin memesan lagi? (y/n) ")
        if another_order.lower() == "y":
            continue
        elif another_order.lower() == "n":
            print("Terima kasih telah berkunjung!")
            break
        else:
            print("Maaf, pilihan tidak tersedia.")
            break

while True:
    print("Selamat datang di Kafe XYZ!")
    print("Silakan pilih:")
    print("1. Pesan minuman")
    print("2. Keluar")
    choice = int(input("Pilihan Anda: "))
    if choice == 1:
        order_drink()
    elif choice == 2:
        print("Terima kasih telah berkunjung!")
        break
    else:
        print("Maaf, pilihan tidak tersedia.")
