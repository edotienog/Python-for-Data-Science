# A list of integers
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]

print("Lenght of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])
#Get minimum value using min()
print("Minimum:", min(hardcover_sales))
#Get maximum value using max()
print("Maximum:", max(hardcover_sales))
#To add everything use sum()
print("Total books sold in one week:", sum(hardcover_sales))
#Use slice to obtain the sales for 5 days of the week 
print("Average books sold in the first five days:", sum(hardcover_sales[:5])/5)