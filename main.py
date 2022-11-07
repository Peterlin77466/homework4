def quadraticFormula1(a,b,c):
    y1= (-b+((b**2)-4*a*c)**0.5)/2*a
    return y1

def quadraticFormula2(a,b,c):
    y2= (-b-((b**2)-4*a*c)**0.5)/2*a
    return y2

print(quadraticFormula1(1,2,-3))
print(quadraticFormula2(1,2,-3))