import re

with open("arbol.html", "r", encoding="utf-8") as f:
    text = f.read()

target = """                let isIslandSupplement = false;
                if (isBalearesCeutaMelilla) {
                    if (isRestaurantDelivery) cost = 3;
                    else {
                        if (isPickup) cost = 2;
                        else cost = 3;
                        isIslandSupplement = true;
                    }
                } else if (isCanarias) {
                    if (isRestaurantDelivery) cost = 3;
                    else {
                        if (isPickup) cost = 5;
                        else cost = 6;
                        isIslandSupplement = true;
                    }
                }"""

replacement = """                let isIslandSupplement = false;
                if (isBalearesCeutaMelilla) {
                    isIslandSupplement = true;
                    if (isRestaurantDelivery) cost = 3;
                    else {
                        if (isPickup) cost = 2;
                        else cost = 3;
                    }
                } else if (isCanarias) {
                    isIslandSupplement = true;
                    if (isRestaurantDelivery) cost = 3;
                    else {
                        if (isPickup) cost = 5;
                        else cost = 6;
                    }
                }"""

text = text.replace(target, replacement)

with open("arbol.html", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated isIslandSupplement logic")
