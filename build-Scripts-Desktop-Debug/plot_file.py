import matplotlib.pyplot as plt

x = []

infile = open('MC_20.txt', 'r')
#names = infile.readline().split()

for line in infile.readlines():
    x.append([float(x) for x in line.split()])

#x.reverse()

infile.close()

a,b,c,d,e,f,g = zip(*x)
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

#(exec(f"plt.plot(range(len(x)), {letter}, label = names[{index}])") for letter, index in zip([a,b,c,d,e], range(5)))

plt.plot(g, b, label = "<M>")
plt.plot(g, c, label = "<|M|>")
"""
plt.plot(range(len(x)), a, "--", label = names[0])
plt.plot(range(len(x)), b, "--", label = names[1])
plt.plot(range(len(x)), c, label = names[2])
plt.plot(range(len(x)), d, label = names[3])
plt.plot(range(len(x)), e, label = names[4])
plt.plot(range(len(x)), f, label = names[5])
plt.plot(range(len(x)), g, label = names[6])
plt.plot(range(len(x)), h, label = names[7])
plt.plot(range(len(x)), i, label = names[8])
plt.plot(range(len(x)), j, label = names[9])
plt.plot(range(len(x)), k, label = names[10])
plt.plot(range(len(x)), l, label = names[11])
"""
plt.title("Comparing mean magnetization and absolute mean magnetization")
plt.legend()
plt.xlabel("cycles")
plt.ylabel("<M>/<|M|>")
#plt.savefig("MC_20_M")
plt.show()