# part 1
guests = ["Ada Lovelace", "Albert Einstein", "Steve Jobs"]
for guest in guests:
    print(f"{guest}, you are invited to attend my dinner at 123 example street at 5:55PM.")
# Additional code
print("Albert Einstein cannot attend. Therefore Bill Gates will take his place.")
guests.remove("Albert Einstein")
guests.insert(1, "Bill Gates")
print("Sending out new invitations...")
for guest in guests:
    print(f"{guest}, you are invited to attend my dinner at 123 example street at 5:55PM.")
