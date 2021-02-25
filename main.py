lst = open("26-k6.txt").readlines()
lst = [[int(n) for n in x.split()] for x in lst]
print(lst)
lst = sorted(lst)
print(lst)
lst.sort(key=lambda x: x[1])
print(lst)
m = int(input("Максимальный бюджет (как бы в задаче очень плохо написано требование вот и выдумал его в виде максимальной суммы, которую вводит пользователь, а ещё там задача имеет кое-какое противоречие): "))
total = 0
total_weight = 0
weight_max = 0
perm1 = 0
perm2 = 0
price = 0
prev = 0
cont = 0
while total <= m:
    perm1 = lst[0][1]
    perm2 = lst[0][0]
    total += (perm1 * perm2)
    total_weight += perm2
    if weight_max < perm2 and total <= m:
        prev = weight_max
        cont = price
        weight_max = perm2
        price = perm1
    lst.remove(lst[0])
total -= (perm1 * perm2)
total_weight -= perm2
print(total)
print("Answer:")
print(total_weight, price)