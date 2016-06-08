list = ['11', 'Quebec', 'City', 'Quebec', 'ville', '454.10', '516,622', '491,142', '476,330', '467,728', '5.2', '10.5']
index = list.index("Quebec")
if "Quebec" in list:
        index = list.index("Quebec")
        list.remove("City")
        list[index] = "Quebec" + " " + "City"
print(index)
print(list)