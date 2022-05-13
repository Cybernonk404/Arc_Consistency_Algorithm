import sys;
import copy;

# List of domains
domains = []
#lists of states
states = []
# List of constraints as adjacent
constraints = []

j = int(input("Enter number of states: "))
for i in range(j):
    const = []
    vari = input("Enter state: ")
    k = int(input("Enter number of the state's neighbour: "))
    for a in range(k):
        consta = input("Enter the neighbour: ")
        const.append(consta)
    states.append(vari)
    constraints.append(const)

l = int(input("Enter number of colors for coloring the map: "))
for i in range(j):
    colors = []
    for a in range(l):
        color = input("Enter color: ")
        colors.append(color)
    domains.append(colors)

agenda = { }
arcs = []

def ac3_algorithm():

    # Make a queue and fill it with the arcs
    queue()

    while arcs:
        arcVars = arcs.pop(0)
        if revising(arcVars[0], arcVars[1]):

            dIIndex = states.index(arcVars[0])
            if len(domains[dIIndex]) == 0:
                print ("No Solution")
                return False

            neighbors = list(constraints[dIIndex])
            neighbors.remove(arcVars[1])

            for xk in neighbors:
                arcs.append([xk, arcVars[0]])

    print (agenda)
    return True

def queue():
    for var in states:
        varIndex = states.index(var)
        for arc in constraints[varIndex]:
            arcs.append([var, arc])

# Revise if the domain has changed
def revising( Xi, Xj):
    revised = False
    Iindex = states.index(Xi);

    # Each value in the domains
    for x in domains[Iindex]:

        # If state is not the neighbour go to next x
        if Xj not in constraints[Iindex]:
            break

        if Xj not in agenda:
            continue

        # If the neighbour state has the current assignment of X or same color, remove x from Di
        if x in agenda[Xj]:
            domains[Iindex].remove(x)
            revised = True

    if not revised and len(domains[Iindex]) > 0:
        agenda[Xi] = domains[Iindex][0]

    return revised

print('-----------RESULT---------')
print('States: ', states)
print('Domains: ', domains, '\n')
print('Constraints: ', constraints, '\n')
print('Result = ', ac3_algorithm())
print('--------------------------')
