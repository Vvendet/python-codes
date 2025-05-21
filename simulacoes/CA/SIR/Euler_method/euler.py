import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import minimize

# === Lê o arquivo e extrai o primeiro bloco ===
arquivo = "infectados.dat"
with open(arquivo, "r") as f:
    linhas = f.readlines()

indices_blocos = [i for i, linha in enumerate(linhas) if linha.strip().startswith("0")]
inicio = indices_blocos[0]
fim = indices_blocos[1] if len(indices_blocos) > 1 else len(linhas)
bloco1 = linhas[inicio:fim]

tempo = []
infectados = []
for linha in bloco1:
    partes = linha.strip().split()
    if len(partes) == 2:
        t, i = map(int, partes)
        tempo.append(t)
        infectados.append(i)

tempo = np.array(tempo)
infectados = np.array(infectados)
N = 10000  # ajuste conforme necessário
I_ac = infectados / N

# === Modelo SIR com método de Euler ===
def euler_sir(S0, I0, R0, beta, gamma, T, dt):
    n_steps = int(T / dt)
    S, I, R = [S0], [I0], [R0]
    t_values = [0.0]
    for _ in range(n_steps):
        s, i, r = S[-1], I[-1], R[-1]
        ds = -beta * s * i
        di = beta * s * i - gamma * i
        dr = gamma * i

        s_new = s + ds * dt
        i_new = i + di * dt
        r_new = r + dr * dt

        # Mantém valores dentro de [0, 1]
        s_new = max(min(s_new, 1.0), 0.0)
        i_new = max(min(i_new, 1.0), 0.0)
        r_new = max(min(r_new, 1.0), 0.0)

        if not all(np.isfinite([s_new, i_new, r_new])):
            break

        S.append(s_new)
        I.append(i_new)
        R.append(r_new)
        t_values.append(t_values[-1] + dt)

    return np.array(t_values), np.array(S), np.array(I), np.array(R)

# === Função de erro para ajuste de beta ===
def erro_quadratico(beta_array, S0, I0, R0, gamma, T, dt, t_ac, I_ac):
    beta = beta_array[0]
    t_modelo, _, I_modelo, _ = euler_sir(S0, I0, R0, beta, gamma, T, dt)
    interp_func = interp1d(t_modelo, I_modelo, kind='linear', bounds_error=False, fill_value="extrapolate")
    I_interp = interp_func(t_ac)
    erro = np.mean((I_interp - I_ac) ** 2)
    return erro

# === Parâmetros iniciais ===
I0 = I_ac[0]
S0 = 1 - I0
R0 = 0.0
gamma = 1 / 10  # duração média da infecção (ajustável)
T = tempo[-1]
dt = 0.0001  # passo pequeno para precisão

# === Ajusta beta com otimização ===
resultado = minimize(
    erro_quadratico,
    x0=[0.7],
    bounds=[(0.1, 3.0)],
    args=(S0, I0, R0, gamma, T, dt, tempo, I_ac),
    method='L-BFGS-B'
)

beta_otimo = resultado.x[0]




# === Gera a curva ajustada ===
t_euler, _, I_euler, _ = euler_sir(S0, I0, R0, beta_otimo, gamma, T, dt)
I_interp = interp1d(t_euler, I_euler)(tempo)


# === Curvas normalizadas ===
I_ac_norm = I_ac / np.max(I_ac)
I_euler_norm = I_euler / np.max(I_euler)
I_interp_norm = interp1d(t_euler, I_euler_norm)(tempo)

# === Plotagem ===
plt.figure(figsize=(10, 6))
plt.plot(tempo, I_ac_norm, 'o--', label='Autômatos Celulares $I_{AC}(t)$', color='blue')
plt.plot(tempo, I_interp_norm, '-', label=f'Modelo SIR (Euler) $\\beta$ ajustado = {beta_otimo:.8f}', color='red')
plt.xlabel('Tempo $t$ (dias)')
plt.ylabel('Fração de infectados')
plt.title('Ajuste de $\\beta$ no Modelo SIR usando Método de Euler')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
