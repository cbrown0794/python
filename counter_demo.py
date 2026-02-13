from counter import Counter

tally = Counter()
tally.reset()

# Call click several times
tally.click()
tally.click()
tally.click()

result = tally.getValue()
print("Value:", result)