pi = 3.14159
A, B, C = map(float, input().split())
print(f'TRIANGULO: {((A*C)/2):.3f}\n'
      f'CIRCULO: {pi*(C**2):.3f}\n'
      f'TRAPEZIO: {((A+B)*C)/2:.3f}\n'
      f'QUADRADO: {B**2:.3f}\n'
      f'RETANGULO: {A*B:.3f}')