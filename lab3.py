sandar = [1, 1, 1, 1, 5, 6]
kbadrat_sandar = map(lambda x: x ** 2, sandar)
result = list(kbadrat_sandar)
filter_sandar = filter(lambda x: x > 2, result)
sum_result = sum(filter_sandar)
print("2 den ulken sandardin hosndisi:", sum_result)
print("tizimdegi sandardin kbadrat tubiri:", result)
