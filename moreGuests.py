# part 1. Snipped to save space.
guests = ["Ada Lovelace", "Albert Einstein", "Steve Jobs"]
guests.remove("Albert Einstein")
guests.insert(1, "Bill Gates")
for guest in guests:
    print(f"{guest}, you are invited to attend my dinner at 123 example street at 5:55PM.")


# additions
print("A bigger table has been found. More guests will be added.")
guests.insert(0, "Elon Musk")
guests.insert(2, "Marie Curie")
guests.append("Mark Zuckerburg")
print("Updated invitations...")
for guest in guests:
    print(f"{guest}, you are invited to attend my dinner at 123 example street at 5:55PM.")

