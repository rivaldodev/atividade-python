import numpy as np

def laplace_equation_oblique(U, h, k, max_iterations=1000, tolerance=1e-6):
    """
    Aluno: Rivaldo Freitas de Carvalho
    Disciplina: Tópicos Especiais Em Ciência e Tecnologia
    Desafio de código: Resolva a equação de Laplace em coordenadas oblíquas para θ = 45º
    com ordem O(h² + k²).
    
    Argumentos:
        U (numpy.ndarray): estimativa inicial para a solução.
        h (float): Tamanho do passo na direção x.
        k (float): Tamanho do passo na direção y.
        max_iterations (int): Número máximo de iterações.
        tolerância (float): Tolerância para convergência.
        
    Retorna:
        numpy.ndarray: Solução para a equação de Laplace.
    """
    # Constantes
    theta = np.pi / 4
    sqrt2 = np.sqrt(2)
    h_k_sqrt2 = h * k * sqrt2
    
    # Obter dimensões
    m, n = U.shape
    
    # Copie a estimativa inicial para evitar modificá-la
    new_U = np.copy(U)
    
    # Execute iterações até atingir a convergência ou o máximo de iterações
    for _ in range(max_iterations):
        max_diff = 0.0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                # Calcular o novo valor usando a discretização da equação de Laplace
                        # Fórmula de discretização
                new_val = ((U[i + 1, j] - 2 * U[i, j] + U[i - 1, j]) / (h**2) +
                           (U[i, j + 1] - 2 * U[i, j] + U[i, j - 1]) / (k**2) -
                           (sqrt2 / (4 * h * k)) * (U[i + 1, j + 1] - U[i - 1, j + 1] -
                                                        U[i + 1, j - 1] + U[i - 1, j - 1]))

                
                # Atualizar a diferença máxima
                max_diff = max(max_diff, abs(new_val - U[i, j]))
                
                # Atualizar o valor na nova matriz com os limites verificados
                new_U[i, j] = min(max(new_val, 0), 1)
        
        # Trocar matrizes para a próxima iteração
        U, new_U = new_U, U
        
        # Verificar convergência
        if max_diff < tolerance:
            break
    
    return U

# Definir parâmetros da malha
m = 3  # Número de pontos na direção X
n = 3  # Número de pontos na direção X
h = 1.0  # Tamanho do passo na direção x
k = 1.0  # Tamanho do passo na direção y

# Suposição inicial para a solução
U = np.zeros((m, n))

# Definir condições de limite
U[:, 0] = 0  # limite esquerdo
U[:, -1] = 0  # limite direito
U[0, :] = 1  # limite superior
U[-1, :] = 1  # limite inferior

# Resolver equação de laplace
solution = laplace_equation_oblique(U, h, k)

print("Solução :")
print(solution)
