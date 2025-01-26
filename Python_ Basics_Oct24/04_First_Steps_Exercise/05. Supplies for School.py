
pack_pens = 5.80
pack_markers = 7.20
cleaning_supplies_per_littre = 1.20

amount_pack_pens = int(input())
amount_pack_markers = int(input())
litres_cleaning_suply = int(input())
discount = int(input()) / 100

amount = (amount_pack_pens * pack_pens) + (amount_pack_markers * pack_markers) + (
        litres_cleaning_suply * cleaning_supplies_per_littre)
total_amount = amount - (amount * discount)
print(total_amount)

# amount_pack_pens = int(input())
# amount_pack_markers = int(input())
# litres_cleaning_suply = int(input())
# discount = int(input())
#
# total_price = amount_pack_pens * 5.80 + amount_pack_markers * 7.20 + litres_cleaning_suply * 1.20
# total_price_after_discount = total_price * (1 - discount / 100)
# print(total_price_after_discount)