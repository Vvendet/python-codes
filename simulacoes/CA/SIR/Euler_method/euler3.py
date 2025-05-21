import numpy as np
import matplotlib.pyplot as plt

def euler_sir(S0, I0, R0, beta, gamma, T, dt):
    """
    Resolve o modelo SIR com o método de Euler usando passo dt.
    
    Parâmetros:
    - S0, I0, R0: valores iniciais
    - beta: taxa de transmissão
    - gamma: taxa de recuperação
    - T: tempo total de simulação (em unidades reais)
    - dt: passo de tempo (ex: 0.00001)
    
    Retorna:
    - vetores tempo t, S(t), I(t), R(t)
    """
    n_steps = int(T / dt)
    S, I, R = [S0], [I0], [R0]
    t_values = [0.0]

    for step in range(n_steps):
        S_new = S[-1] - beta * S[-1] * I[-1] * dt
        I_new = I[-1] + (beta * S[-1] * I[-1] - gamma * I[-1]) * dt
        R_new = R[-1] + gamma * I[-1] * dt

        # Garante que os valores fiquem no intervalo [0, 1]
        S.append(max(min(S_new, 1.0), 0.0))
        I.append(max(min(I_new, 1.0), 0.0))
        R.append(max(min(R_new, 1.0), 0.0))
        t_values.append(t_values[-1] + dt)

    return np.array(t_values), np.array(S), np.array(I), np.array(R)

# Parâmetros iniciais
N = 10000
I0 = 1 / N
S0 = 1 - I0
R0 = 0.0
gamma = 1 / 3       # Tempo médio de recuperação: 5 unidades
beta_est = 2      # Substitua pelo valor estimado
T = 5000             # Tempo total da simulação (ex: 10 unidades de tempo)
dt = 0.00001        # Passo de tempo muito pequeno

# Executa o modelo
t, S, I, R = euler_sir(S0, I0, R0, beta_est, gamma, T, dt)

# Plota a curva I(t)
plt.figure(figsize=(10, 6))
plt.plot(t, I, label='Infectados $I_{Euler}(t)$', color='red')
plt.xlabel('Tempo contínuo $t$')
plt.ylabel('Fração de infectados')
plt.title(f'Evolução de $I(t)$ com método de Euler\n(β = {beta_est}, γ = {gamma}, dt = {dt})')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()