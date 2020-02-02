def binary_search(arr, x):
   left = 0
   right = len(arr) - 1
   mid = ((right-left)//2) + left

   while(left <= right):
      if(x > arr[mid]):
         left = mid + 1
      
      elif(x < arr[mid]):
         right = mid - 1
      
      else:
         return "found at index "  + str(mid)
      
      mid = ((right-left)//2) + left
   
   return "not found"


print(binary_search([1,2,3,4,5,6,7,8], 5))