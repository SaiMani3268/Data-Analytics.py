#SET OPERATIONS
#TWO SETS ARE E AND N
E={0,2,4,6,8};
N={1,2,3,4,5};
print("Union of E and N is",E|N)
print("Intersection of E and N is",E&N)
print("Difference of E and N is",E-N)
print("Symmetric difference of E and N is",E^N)

#OUTPUT:
#Union of E and N is {0,1,2,3,4,5,6,8}
#Intersection of E and N is {2,4}
#Difference of E and N is {0,8,6}
#Symmetric difference of E and N is {0,1,3,5,6,8}