#PROGRAMA QUE CALCULA EL VALOR DEL IVA DE 19% SOBRE EL VALOR TOTAL DE LA COMPRA


def taxes_shopping(p):
    total_price = p*1.19
    return (total_price)

price = float(input("What is the final price of the shopping?: "))

final_price = taxes_shopping(price)

print(f"The final price of the shop with taxes are : {round(final_price,2)}")