ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "Singapore!")
ft_set.clear()
ft_set.add("Hello")
ft_set.add("Singapore!")
ft_dict["Hello"] = "42Singapore!"

print(ft_list)
print(ft_tuple)
print(sorted(ft_set))
print(ft_dict)
