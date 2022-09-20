# [1, 2, 3, 4] -> [24, 12, 8, 6]

def print_everything(arr, left, right, product):
    print(f"Input array: {arr}")
    print(f"left array: {left}")
    print(f"right array: {right}")
    print(f"Product array: {product}")
    print('---------------------')

def get_product_array(arr):
    n = len(arr)
    left, right = [1]*n, [1]*n
    product_array=[]
    print_everything(arr, left, right, product_array)
    
    for i in range(1, n):
        left[i] = left[i-1]*arr[i-1]
    
    print_everything(arr, left, right, product_array)
    
    for i in range(1, n):
        right[i] = right[i-1]*arr[::-1][i-1]
        
    print_everything(arr, left, right, product_array)
    
    for i in range(n):
        product_array.append(left[i] * right[::-1][i])
        
    print_everything(arr, left, right, product_array)
    
get_product_array([1, 2, 3, 4])
