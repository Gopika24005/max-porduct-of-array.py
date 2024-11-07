def max_product(arr):
  arr.sort(reverse = True)
  return arr[0]*arr[1]

arr=[1,10,2,6,5,3]
product = max_product(arr)
print(product)

arr=[10,20,30,40,50]
product = max_product(arr)
print(product)
