## Ecuaciones diferenciales para modelar impacto de la pandemia COVID-19

## documentacion de odeint --> https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html
## referencia al libro del cual extraimos el ejercicio --> https://python.quantecon.org/sir_model.html
import numpy as np
from numpy import exp

import matplotlib.pyplot as plt

## odeint es un paquete para resolver ecuaciones diferenciales
from scipy.integrate import odeint

## utilizaremos a EEUU como caso estudio
poblacion = 3.3e8

## el primer parametro representa el promedio de incubacion promedio (5.2 dias)
σ = 1 / 5.2

## el segundo parametro reprensenta la duracion promedio de la enfermedad (18 dias)
γ = 1 / 18

def F(x, t, R0=1.6):
    """
    Derivada tiempo del vector estado.

        * x es el vector estado (tipo array)
        * t es tiempo (scalar)
        * R0 es la tasa de transmision, la cual resulta en una constante

    """
    s, e, i = x ## s = susceptible, e = expuesto, i = infectado

    # Nueva exposicion a suceptibles
    β = R0(t) * γ if callable(R0) else R0 * γ
    ne = β * s * i

    # Derivadas de tiempo
    ds = - ne
    de = ne - σ * e
    di = σ * e - γ * i

    return ds, de, di

# condiciones iniciales de s, e, i
i_0 = 1e-7
e_0 = 4 * i_0
s_0 = 1 - i_0 - e_0

## en forma de vector
x_0 = s_0, e_0, i_0

def solve_path(R0, t_vec, x_init=x_0):
    """
    Resolver para i(t) y c(t) integrando,
    dado el tiempo para R0.

    """
    G = lambda x, t: F(x, t, R0)
    s_path, e_path, i_path = odeint(G, x_init, t_vec).transpose()

    c_path = 1 - s_path - e_path   ## casos cumulativos
    return i_path, c_path


## perfecto, ahora hagamos algunos experimentos para testear nuestro programa
t_length = 550
grid_size = 1000
t_vec = np.linspace(0, t_length, grid_size)


## probemos cuando R0 es constante
R0_vals = np.linspace(1.6, 3.0, 6)
labels = [f'$R0 = {r:.2f}$' for r in R0_vals] ## r = paciente removido
i_paths, c_paths = [], []

for r in R0_vals:
    i_path, c_path = solve_path(r, t_vec)
    i_paths.append(i_path)
    c_paths.append(c_path)


## grafiquemos nuestros resultados
def plot_paths(paths, labels, times=t_vec):

    fig, ax = plt.subplots()

    for path, label in zip(paths, labels):
        ax.plot(times, path, label=label)

    ax.legend(loc='upper left')

    plt.show()

## casos actuales como fraccion de la poblacion
#plot_paths(i_paths, labels) ## menor tasa de transmision = mas bajo el pico como es de esperarse

## casos cumulativos como fraccion de la poblacion
plot_paths(c_paths, labels)