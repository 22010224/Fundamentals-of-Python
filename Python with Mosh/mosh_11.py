# set -> unordered collection, unindexed, no duplicate value

saxa = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup"}
saxa.add("napkin")
saxa.remove("knife")
saxa.clear()
dishes.update(saxa)
dinnenr_table = saxa.union(dishes)
for x in dinnenr_table:
    print(x)

print(saxa.difference(dishes))
print(dishes.difference(saxa))
print(dinnenr_table.difference(saxa))
print(saxa.intersection(dinnenr_table))