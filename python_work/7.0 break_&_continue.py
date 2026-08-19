#%%
# break statement.
i = 1
while i <= 5:
    print(i)
    if(i==3.0):
        break # break statement terminates the loop.
    i += 1
print("End of loop.")

#%%
# Continue statement.
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

# %%
#printing elements from a list using for loop.

list = [1, 2, 3, 6, 3, 9, 7]
for val in list:
    print(val)
# %%
