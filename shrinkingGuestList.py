# part 1. Snipped to save space.
guests = ["Ada Lovelace", "Albert Einstein", "Steve Jobs"]
guests.remove("Albert Einstein")
guests.insert(1, "Bill Gates")
guests.insert(0, "Elon Musk")
guests.insert(2, "Marie Curie")
guests.append("Mark Zuckerburg")
for guest in guests:
    print(f"{guest}, you are invited to attend my dinner at 123 example street at 5:55PM.")


# additions
print("Unfortunately, the table did not arrive on time, so only two guests can attend the dinner.")
uninv1 = guests.pop(0)
uninv2 = guests.pop(2)
uninv3 = guests.pop(2)
uninv4 = guests.pop(2)
uninvited = [uninv1, uninv2, uninv3, uninv4]
for uninv in uninvited:
    print(f"{uninv} has been uninvited from the dinner.")
print("Updated invitations...")
for guest in guests:
    print(f"{guest}, you are invited to attend my dinner at 123 example street at 5:55PM.")


# Deleting all items.
del guests[1]
del guests[0]
print(guests)