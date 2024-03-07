import numpy as np
import matplotlib.pyplot as plt

def discretize_laplace(r_min, r_max, theta_min, theta_max, h, k):
  """
  Aluno: Rivaldo Freitas de Carvalho
  Disciplina: Tópicos Especiais Em Ciência e Tecnologia
  Desafio de código: Discretizar a equação de Laplace em coordenadas polares e plotar os pontos.

  Argumentos:
    r_min: Raio mínimo da malha.
    r_max: Raio máximo da malha.
    theta_min: Ângulo mínimo da malha (em radianos).
    theta_max: Ângulo máximo da malha (em radianos).
    h: Espaçamento nos eixos r.
    k: Espaçamento nos eixos θ.

  Retorna:
    Uma matriz bidimensional com os valores discretizados da equação de Laplace.
  """

  # Cria uma matriz para armazenar os valores discretizados
  u = np.zeros((int((r_max - r_min) / h) + 1, int((theta_max - theta_min) / k) + 1))

  # Cria arrays vazios para armazenar as coordenadas cartesianas
  x = np.zeros_like(u)
  y = np.zeros_like(u)

  # Itera sobre os pontos da malha e aplica a equação discretizada
  for i in range(1, int((r_max - r_min) / h)):
    for j in range(1, int((theta_max - theta_min) / k)):
      # Cria coordenadas polares
      r = h * i + r_min
      theta = k * j + theta_min

      # Converte para cartesianas
      x[i, j] = r * np.cos(theta)
      y[i, j] = r * np.sin(theta)

      # Aplica a equação discretizada
      u[i, j] = (((u[i+1, j] - 2*u[i, j] + u[i-1, j]) / h**2) +
                 (1 / (i*h)**2) * ((u[i, j+1] - 2*u[i, j] + u[i, j-1]) / k**2) +
                 (1 / (i*h)) * ((u[i+1, j] - u[i-1, j]) / 2*h))

      # Plota o texto com o valor discretizado
      plt.text(x[i, j], y[i, j], f"{u[i, j]:.2f}")

  return u

# Mostra o gráfico
plt.show()

if __name__ == "__main__":
  # Define os parâmetros da malha
  r_min = 0.0
  r_max = 1.0
  theta_min = 0.0
  theta_max = 2.0 * np.pi
  h = 0.1
  k = 0.1

  # Plota a malha e aplica a discretização
  discretize_laplace(r_min, r_max, theta_min, theta_max, h, k)
