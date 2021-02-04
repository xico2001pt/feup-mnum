import math
import matplotlib.pyplot as plt

# Abstract Data
day_to_minutes = 24 * 60  # number of minutes in a day (min)
mi_initial = 0  # initial drug's mass in the central compartment (mg)
mp_initial = 0  # initial drug's mass in the plasma compartment (mg)
consumption_duration = 0.5  # minutes it takes to consume an ampoule (min)


# Statement Data
daily_dose = 150  # daily dose ingested (mg)
intake_interval = 12 * 60  # time interval between dose consumption (min)
treatment_duration = 3 * day_to_minutes  # total duration of the treatment (min)
doses_per_day = day_to_minutes / intake_interval  # number of doses taken in a day (doses/day)
Vap = 3250  # apparent volume of plasma (mL)
Ket = 0.17325 / 60  # kinetic total elimination constant (min^-1)
t_max = 4 * 60  # instant when the maximum drug plasma concentration occur (min)


# Data to be filled
x_axis = []  # elapsed time (min)
y_axis = []  # drug's concentration in blood plasma (mg mL^-1)
z_axis = []
w_axis = []
Ka = 0  # kinetic absorption constant (min^-1)


# Numerical methods used
def newton_equation_method(x, f, fx, precision):
    prev_x = x + 10  # Make sure x - prev != 0
    while abs(x - prev_x) > precision:
        prev_x = x
        x = x - f(x) / fx(x)
    return x


def diff_eq_rk4_sup(diffy, diffz, xi, xf, yi, zi, h):
    n = (xf - xi) / h
    x, y, z = xi, yi, zi
    for _ in range(0, int(n)):
        dy1, dz1 = h * diffy(x, y, z), h * diffz(x, y, z)
        dy2, dz2 = h * diffy(x + h / 2, y + dy1 / 2, z + dz1 / 2), h * diffz(x + h / 2, y + dy1 / 2, z + dz1 / 2)
        dy3, dz3 = h * diffy(x + h / 2, y + dy2 / 2, z + dz2 / 2), h * diffz(x + h / 2, y + dy2 / 2, z + dz2 / 2)
        dy4, dz4 = h * diffy(x + h, y + dy3, z + dz3), h * diffz(x + h, y + dy3, z + dz3)

        new_x = x + h
        new_y = y + (dy1 / 6 + dy2 / 3 + dy3 / 3 + dy4 / 6)
        new_z = z + (dz1 / 6 + dz2 / 3 + dz3 / 3 + dz4 / 6)
        x, y, z = new_x, new_y, new_z
        x_axis.append(x)
        y_axis.append(y)
        z_axis.append(z)
    return


def non_linear_equation(Ka):
    return Ka * math.exp(-Ka * t_max) - Ket * math.exp(-Ket * t_max)


def non_linear_equation_derivative(Ka):
    # This function was obtained using Maxima
    return math.exp(-Ka * t_max) - t_max * Ka * math.exp(-Ka * t_max)


def d(t):
    if (0 <= t % intake_interval <= consumption_duration) and t < treatment_duration:
        return 2 * (t % intake_interval) * (daily_dose / doses_per_day) / consumption_duration ** 2
    return 0

def dual_model_equation_1(t, mi, mp):
    return d(t) - Ka * mi

def dual_model_equation_2(t, mi, mp):
    return Ka * mi - Ket * mp

# Tests
def main():
    # Define precision
    precision = 10 ** -19

    # Calculate Ka
    global Ka
    Ka = newton_equation_method(0.005, non_linear_equation, non_linear_equation_derivative, precision)
    print("Ka = {}".format(Ka))

    # Modelate graphic
    diff_eq_rk4_sup(dual_model_equation_1, dual_model_equation_2, 0, 7000, mi_initial, mp_initial, 0.01)

    # Draw graph

    # Plot d(t) function
    for t in range(0, 7000*10):
        w_axis.append(d(t/10))

    plt.plot(x_axis, y_axis)
    plt.plot(x_axis, z_axis)
    plt.legend(["mi", "mp"])
    #plt.plot(x_axis, w_axis)
    #plt.ylabel("Drug's concentration (mg mL^-1)")
    plt.ylabel("Drug's mass (mg)")
    plt.xlabel("Elapsed time (min)")
    #plt.xlim([0, 7000])
    #plt.ylim([0, 0.008])
    plt.show()
    return 0

main()