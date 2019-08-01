def pi_montecarlo(n_ele, n_exp):
    # Simulación de Monte Carlos.
    import matplotlib.pyplot as plt
    import numpy as np
    """
    1 - Generamos dos números aleatorios x e y entre 0 y 1.
    2 - Calculamos x * x + y * y
        Si el valor es inferior a 1 -> estamos dentro del círculo.
        Si el valor es superior a 1 -> estamos fuera del círculo.
    3 - Calculamos el número total de veces que está dentro del círculo
        y lo dividimos entre el número total de intentos para pbtener una
        aproximación de la probabilidad de caer dentro del círculo.
    4 - Usamos dicha probabilidad para aproximar el valor de PI.
    5 - Repetimos el experimento un número suficiente de veces (por ejemplo
        1000), para obtener (1000) diferentes aproximaciones de PI.
    6 - Calculamos el promedio de los 1000 experimentos anteriores para dar un valor final de PI."""

    pi_avg = 0
    pi_value_list = []
    for i in range(n_exp):
        value = 0
        x = np.random.uniform(0, 1, n_ele).tolist()
        y = np.random.uniform(0, 1, n_ele).tolist()
        for j in range(n_ele):
            z = np.sqrt(x[j] * x[j] + y[j] * y[j])
            if z < 1:
                value += 1
        float_value = float(value)
        pi_value = float_value * 4 / n_ele
        pi_value_list.append(pi_value)
        pi_avg += pi_value

    pi = pi_avg / n_exp

    print(pi)
    plt.plot(pi_value_list)
    plt.show()


pi_montecarlo(100, 100)