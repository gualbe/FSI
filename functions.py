def es_primo (n):
  divisores = [i for i in range(2, n) if n % i == 0]
  return len(divisores) == 0

