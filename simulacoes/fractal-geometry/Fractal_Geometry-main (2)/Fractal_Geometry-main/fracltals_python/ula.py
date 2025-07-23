import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parâmetros
size = 201    # Tamanho da grade (ímpar)
steps = 100   # Número de gerações
center = size // 2

# Inicializa a grade com a célula central ativa
current = np.zeros((size, size), dtype=int)
current[center, center] = 1

# Figura
fig, ax = plt.subplots()
im = ax.imshow(current, cmap='Greys', interpolation='nearest', animated=True)
ax.set_title("Autômato de Ulam–Warburton")
ax.axis('off')

# Função para atualizar o estado do autômato
def update(frame):
    global current
    new = current.copy()
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            if current[i, j] == 0:
                neighbors = (
                    current[i - 1, j] + current[i + 1, j] +
                    current[i, j - 1] + current[i, j + 1]
                )
                if neighbors == 1:
                    new[i, j] = 1
    current = new
    im.set_array(current)
    return [im]

# Criar animação
ani = animation.FuncAnimation(
    fig, update, frames=steps, interval=100, blit=True, repeat=False
)

plt.tight_layout()
plt.show()
