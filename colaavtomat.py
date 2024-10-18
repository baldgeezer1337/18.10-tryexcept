def main():
    total_amount = 0
    coke_price = 50

    print("Добро пожаловать в автомат с Coca-Cola!")
    print("Пожалуйста, вставьте монету (5, 10 или 25 центов).")

    while total_amount < coke_price:
        try:
            coin = int(input("Введите номинал монеты: "))
            if coin in [5, 10, 25]:
                total_amount += coin
                if total_amount < coke_price:
                    print(f"Сумма к оплате: {coke_price - total_amount} центов.")
            else:
                print("Неподдерживаемый номинал монеты. Пожалуйста, вставьте 5, 10 или 25 центов.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    change = total_amount - coke_price
    print(f"Спасибо за покупку! Ваша сдача: {change} центов.")

if __name__ == "__main__":
    main()
