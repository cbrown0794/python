contacts = {'Jenny': 8675309, 'James':551212}
print(*contacts)
print('Jennys number is', contacts['Jenny'])
brian = contacts.get('James')
print("Brian has new number", brian)