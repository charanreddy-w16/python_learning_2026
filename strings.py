# %% Length
a = len('hello')
print(a)

# %% Concatenation
b = 'AB' + 'Cd'
print(b)
# %% in operator
c='my name is Charan'
if 'h' in c:
    print('The letter h is in the string')

# %% Slices
d='abcdefghij'
d[2:5]
d[:5]
d[5:]
d[9]
d=d[:4]+'X'+d[5:]
print(d)



# %%
d='abcdefghij'
d.upper()
d.isalpha()
print(d.count("a"))

# %% isalpha
s=input("Enter a string: ")

if s[0].isalpha():
    print('Your sentence starts with a letter.')
else:
    print("Your string doesn't start with a letter.")    

# %% Escape Characters
print('Hi\nthere!')

# %% location of 'a' in a string
x=input('Enter your string: ')
for i in range(len(x)):
    if s[i]=='a':
        print(i)

# %% doubles each character of the string
f=input('Enter your string: ')
doubled_f='';
for i in f:
    doubled_f=doubled_f + i*2
print(doubled_f)

# %%
f=input('Enter your string: ')

for i in f:
 print(i,end=' ')