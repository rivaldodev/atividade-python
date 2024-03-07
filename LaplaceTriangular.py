import numpy as np

def laplace_equation_triangular(U, delta_q, delta_r, delta_s):
    """
    Aluno: Rivaldo Freitas de Carvalho
    Disciplina: Tópicos Especiais Em Ciência e Tecnologia
    Desafio de código: Discretize a equação de Laplace em coordenadas triangulares com θ = 60° e β = 120°.
    
    Argumentos:
        U (numpy.ndarray): estimativa inicial para a solução.
        delta_q (float): Tamanho do passo na direção q.
        delta_r (float): Tamanho do passo na direção r.
        delta_s (float): Tamanho do passo na direção s.
        
    Retorna:
        numpy.ndarray: Solução da equação de Laplace discretizada.
    """
    # Obter dimensões
    m, n, p = U.shape
    
    # Copie a estimativa inicial para evitar modificá-la
    new_U = np.copy(U)
    
    # Executar iterações
    max_diff = np.inf
    tolerance = 1e-6
    while max_diff > tolerance:
        max_diff = 0.0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                for k in range(1, p - 1):
                    # Calcule o novo valor usando a discretização da equação de Laplace
                    new_val = (2/3) * ((((U[i+1, j, k] - 2*U[i, j, k] + U[i-1, j, k]) / (delta_q ** 2)) +
                                        ((U[i, j+1, k] - 2*U[i, j, k] + U[i, j-1, k]) / (delta_r ** 2)) +
                                        ((U[i, j, k+1] - 2*U[i, j, k] + U[i, j, k-1]) / (delta_s ** 2))))
                    
                    # Atualize a diferença máxima
                    max_diff = max(max_diff, abs(new_val - U[i, j, k]))
                    
                    # Atualize o valor na nova matriz
                    new_U[i, j, k] = new_val
        
        # Trocar matrizes para a próxima iteração
        U, new_U = new_U, U
    
    return U

# Definir parâmetros da malha
m = 10  # Número de pontos na malha na direção q
n = 10  # Número de pontos na malha na direção r
p = 10  # Número de pontos na malha na direção s
delta_q = 1.0  # Tamanho do passo na direção q
delta_r = 1.0  # Tamanho do passo na direção r
delta_s = 1.0  # Tamanho do passo na direção s

U = np.zeros((m, n, p))

# Resolver a equação de Laplace
solution = laplace_equation_triangular(U, delta_q, delta_r, delta_s)

print("Discretized solution to the Laplace equation in triangular coordinates:")
print(solution)
