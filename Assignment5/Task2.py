'''
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

L1 = [1,2,3,4,5,6,7,8,9,10]
L2 = L1[0:5]
L3 = L2[::-1]
print("Original list:",L1)
print("Extracted the first five elements:",L2)
print("Reversed the extracted elements:",L3)
