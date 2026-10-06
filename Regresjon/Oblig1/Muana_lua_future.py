import matplotlib.pyplot as plt
import numpy as np
plt.close('all')
#X is years, Y is CO2-levels in ppm
X, Y = np.loadtxt("Regresjon/Datasett2.dat", unpack=True)

a = 407.09 #konstant (bruker den jeg fant fra lineær regresjon)
b = 2.87 #stigningstall (bruker den jeg fant fra lineær regresjon)
c = 3 #Amplitude (så litt på scatter punktene og den lineære regresjonen og 3 virket som en grei gjettning)
d = 2*np.pi #vinklfrekvens (så at det var ca en periode i året på scatter plottet. og i en tidligere utregning fant vi at T = 2pi / d så da er en grei gjettning 2pi)
f = 0 #Faseforskyving (ser heller ikke ut som at den er forskyvet så mye ut i fra scatter plottet så lar denne forbli 0)

dif = 1*10**-5 #gradient steg lengde
h = 0.0001 #den lille verdien for midtpunktsformelen for numerisk derivasjon

def S(a,b,c,d,f): #definerer funksjonen for summen av a,b,c,d,f
    return sum((Y-(a+b*X+c*np.sin(d*X+f)))**2)

iterations = 100000 #antall ganger for løkken skal kjøre og prøve å få en nærmere gjettning
def find_parameters(a,b,c,d,f,iterations,h,dif):
    for n in range(iterations): #bruker midtpunktsmetoden for numerisk derivasjon for å finne verdier for a,b,c,d,f som gjør at alle de delvis deriverte kommer så nærme 0 som mulig.
        da = (S(a+h, b, c, d, f) - S(a-h, b, c, d, f)) / (2*h)
        db = (S(a, b+h, c, d, f) - S(a, b-h, c, d, f)) / (2*h)
        dc = (S(a, b, c+h, d, f) - S(a, b, c-h, d, f)) / (2*h)
        dd = (S(a, b, c, d+h, f) - S(a, b, c, d-h, f)) / (2*h)
        df = (S(a, b, c, d, f+h) - S(a, b, c, d, f-h)) / (2*h)
        
        a -= dif * da
        b -= dif * db
        c -= dif * dc
        d -= dif * dd
        f -= dif * df
    return a,b,c,d,f
a, b, c, d, f = find_parameters(a,b,c,d,f,iterations,h,dif) #kjører funksjonen returnerer variablene og definerer de nye verdiene globalt

print(f"a={a:.4f}, b={b:.4f}, c={c:.4f}, d={d:.4f}, f={f:.4f}")  # skriver ut koeffisientene i terminalen
x_smooth = np.linspace(5, 6, 1000)
#formula for the linear regression with the sinus term
X_Y_sinreg = a + b*x_smooth + c*np.sin(d*x_smooth + f)

CO2_start_of_2027 = a + b*5 + c*np.sin(d*5 + f)
print(f"the CO2 concentration on muana loa at new year this year (1.jan.2027) is {CO2_start_of_2027:.5f}")

plt.title("CO2 levels in Muana lua")
plt.xlabel("Years")
plt.ylabel("CO2, ppm")
plt.grid()
#plotting the graph with the sinus term
plt.plot (x_smooth, X_Y_sinreg, color="hotpink")

plt.show()