import greedypacker

M = greedypacker.BinManager(8, 4, pack_algo='shelf', heuristic='best_width_fit', wastemap=True, rotation=True)
ITEM = greedypacker.Item(4, 2)
ITEM2 = greedypacker.Item(5, 2)
ITEM3 = greedypacker.Item(2, 2)

M.add_items(ITEM, ITEM2, ITEM3)

M.execute()
print(M.bins)
# [Sheet(width=8, height=4, shelves=[{'y': 2, 'x': 8, 'available_width': 0, 'area': 6, 'vertical_offset': 0, 'items': [Item(width=5, height=2, x=0, y=0)]}, {'y': 2, 'x': 8, 'available_width': 4, 'area': 8, 'vertical_offset': 2, 'items': [Item(width=4, height=2, x=0, y=2)]}])]
