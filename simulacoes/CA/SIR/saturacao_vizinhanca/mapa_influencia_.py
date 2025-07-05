import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
import math

def distance_matrix(radius):
    size = 2 * radius + 1
    center = radius
    dist = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            dx = i - center
            dy = j - center
            if dx == 0 and dy == 0:
                dist[i, j] = np.nan  # ignora a célula central
            else:
                dist[i, j] = np.sqrt(dx**2 + dy**2)
    return dist

def tau_inverse_quadratic(d):
    return 1 / (1+d**2)

def tau_inverse_sqrt_safe(d):
    with np.errstate(divide='ignore', invalid='ignore'):
        result = 1 / np.sqrt(d)
        result[np.isnan(d)] = 0  # evita problemas na célula central
    return result

def weighted_kernel(radius, tau_fn):
    dist = distance_matrix(radius)
    kernel = tau_fn(dist)
    kernel[np.isnan(dist)] = 0  # zera a célula central
    return kernel

def weighted_influence(grid, kernel):
    infected = (grid == 1).astype(float)
    return convolve2d(infected, kernel, mode='same', boundary='fill', fillvalue=0)

def save_influence_image(influence_matrix, filename="mapa_influencia.png"):
    plt.figure(figsize=(6, 5))
    plt.imshow(influence_matrix, cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Influência acumulada')
    plt.title("Mapa de Influência Ponderada")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Imagem salva como: {filename}")

# ----- Execução -----

radius = 5
grid = np.zeros((2 * radius + 1, 2 * radius + 1))
grid[radius, radius] = 1  # célula central infectada

kernel = weighted_kernel(radius, tau_inverse_sqrt_safe)
influence = weighted_influence(grid, kernel)

save_influence_image(influence, "mapa_influencia_quadratica.png")
    