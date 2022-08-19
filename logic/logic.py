# 1. Toda célula contagiada, continúa contagiada si tiene exactamente 2 o 3 células contagiadas en las celdas vecinas, de lo contrario sana para el siguiente periodo.
# 2. Cualquier célula sana que tenga exactamente 3 células contagiadas en las celdas vecinas, se contagia para el siguiente período.

# a. Que el patrón inicial se repita siempre después de “N” períodos, en este caso la enfermedad produce un caso grave. Si “N” es igual a 1, entonces, el paciente morirá a causa de la enfermedad, ya que ésta será incurable.
# b. Que algún patrón, distinto al patrón inicial, se repita luego de “N” períodos cada “N1” períodos, en este caso la enfermedad producirá un caso grave. Si “N1” es igual a 1, entonces, el paciente morirá a causa de la enfermedad, ya que ésta será incurable, en caso de que “N1” es mayor que 1, la enfermedad será grave.
