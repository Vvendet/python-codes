import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

def euler_sir(S0, I0, beta, gamma, T, dt=0.00001):
    S, I = [S0], [I0]
    for _ in range(T):
        S_new = S[-1] - beta * S[-1] * I[-1] * dt
        I_new = I[-1] + (beta * S[-1] * I[-1] - gamma * I[-1]) * dt
        S.append(S_new)
        I.append(I_new)
    return np.array(S), np.array(I)
def plotar(T,I,beta_est,gamma):
    plt.figure(figsize=(10, 6))
    plt.plot(1/i for i in range(T + 1), I, label='Infectados $I_{Euler}(t)$', color='red')
    plt.xlabel('Tempo (passos)')
    plt.ylabel('Fração de infectados')
    plt.title(f'Evolução de I(t) com método de Euler (β = {beta_est}, γ = {gamma})')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
# Suponha que você tem os dados I_AC de sua simulação com autômatos celulares
# para uma certa α:


I_ac = np.array([985,2687,5180,7495,9035,9704,9921,9000,7313,4820,2505,965,296,79,15])
while len(I_ac)<50:
    I_ac = np.append(I_ac,[0])

Ie= euler_sir(10000-985, 985, 2, 1/3,len(I_ac)*1000)[1]
plotar(len(I_ac)*1000,Ie,2,1/3)

def fit_beta(I_ac, S0, I0, gamma, dt=0.01):
    T = (len(I_ac) - 1)*1000
    def error(beta):
        _, I_euler = euler_sir(S0, I0,beta, gamma, T, dt)
        return np.mean((I_ac - I_euler[:len(I_ac)])**2)
    
    res = minimize_scalar(error, bounds=(0, 5), method='bounded')

    plotar(T,euler_sir(10000-985, 985, res.x, 1/3,T)[1],res.x,gamma)
    return res.x  # β ótimo

# Agora associe isso ao α usado na simulação de I_ac

#print(fit_beta(I_ac,9015,985,1/7))


