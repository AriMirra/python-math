f = open("./test.csv", "w+")

for i in range(0, 10):
  f.write("Aloha " + str(i) + "\n")

f.close()