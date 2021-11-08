#soal 4

para = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

word_list = len(para.split(" "))
a_list = para.count("a")
i_list = para.count("i")
u_list = para.count("u")
e_list = para.count("e")
o_list = para.count("o")

print(para )
print(" ")
print(f"Jumlah Kata = {word_list}")
print(f"Banyak huruf a = {a_list}")
print(f"Banyak huruf i = {i_list}")
print(f"Banyak huruf u = {u_list}")
print(f"Banyak huruf e = {e_list}")
print(f"Banyak huruf o = {o_list}")