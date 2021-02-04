from numerical_methods import *
from data import *
import matplotlib.pyplot as plt

# Data to be filled
x_axis = []  # elapsed time (min)
y1_axis = []  # drug's mass in blood plasma (mg)
y2_axis = []  # drug's concentration in blood plasma (mg mL^-1)
z_axis = []  # drug's mass in central compartment (mg)

# Test and Debug
def main():
    global x_axis, y1_axis, y2_axis, z_axis
    precision = 10 ** -19  # precision used
    h = 1 / 60 / 4  # iterative step

    print("Solution 1:")
    print("Newton method Ka = ", newton_method(0.005, non_linear_equation, non_linear_equation_derivative, precision))
    print("Bissection method Ka = ", bisection_method(0.003, 0.006, non_linear_equation, precision))
    print("String method Ka = ", string_method(0.003, 0.006, non_linear_equation, precision))
    print("Picard-peano method Ka = ", picard_peano_method(0.005, picard_peano_equation1, precision))

    print("\nSolution 2:")
    print("Newton method Ka = ", newton_method(0.003, non_linear_equation, non_linear_equation_derivative, precision))
    print("Bissection method Ka = ", bisection_method(0, 0.003, non_linear_equation, precision))
    print("String method Ka = ", string_method(0, 0.003, non_linear_equation, precision))
    print("Picard-peano method Ka = ", picard_peano_method(0.003, picard_peano_equation2, precision))
    update_ka(newton_method(0.005, non_linear_equation, non_linear_equation_derivative, precision))

    print("\nPlotting graphs...")
    x_axis, z_axis, y1_axis = rk4_method(0, days_to_minutes(4), mi_initial, mp_initial, dual_model_equation_1, dual_model_equation_2, h)
    #x_axis, z_axis, y1_axis = rk2_method(0, c, mi_initial, mp_initial, dual_model_equation_1, dual_model_equation_2, h)
    #x_axis, z_axis, y1_axis = euler_method(0, days_to_minutes(4), mi_initial, mp_initial, dual_model_equation_1, dual_model_equation_2, h)

    # Plot mass functions
    plt.plot(x_axis, z_axis)
    plt.plot(x_axis, y1_axis)
    plt.legend(["central comp.", "plasma comp."])
    plt.title("Temporal behavior of the drug's mass")
    plt.ylabel("Drug's mass (mg)")
    plt.xlabel("Elapsed time (min)")
    plt.show()

    # Plot concentration function
    y2_axis = [y/Vap for y in y1_axis]
    plt.plot(x_axis, y2_axis)
    plt.legend(["plasma comp."])
    plt.title("Temporal behaviour of drug's concentration")
    plt.ylabel("Drug's concentration in blood plasma (mg mL^-1)")
    plt.xlabel("Elapsed time (min)")
    plt.show()

    # Plot administration function
    a = [t for t in range(30)]
    b = [D(t/60) for t in a]
    plt.plot(a, b)
    plt.title("Temporal behaviour of the administration function")
    plt.ylabel("Administered dose (mg min^-1)")
    plt.xlabel("Elapsed time (sec)")
    plt.show()

    # Plot estimate error function
    print("Plotting error function... (this may take a while)")
    points0 = rk4_method(0, days_to_minutes(4), mi_initial, mp_initial, dual_model_equation_1, dual_model_equation_2, h)[2]
    p0 = [points0[i] for i in range(0, len(points0))]
    points1 = rk4_method(0, days_to_minutes(4), mi_initial, mp_initial, dual_model_equation_1, dual_model_equation_2, h/2)[2]
    p1 = [points1[i] for i in range(0, len(points1), 2)]
    points2 = rk4_method(0, days_to_minutes(4), mi_initial, mp_initial, dual_model_equation_1, dual_model_equation_2, h/4)[2]
    p2 = [points2[i] for i in range(0, len(points2), 4)]

    error_mp = [(s2 - s1) / ((2 ** 4) - 1) for s0, s1, s2 in zip(p0, p1, p2)]

    print(f"Maximum error: {max(error_mp)}")
    print(f"Average error: {sum(error_mp) / len(error_mp)}")

    plt.plot(x_axis, error_mp)
    plt.legend(["rk4 method"])
    plt.title("Temporal behaviour of the observed error")
    plt.ylabel("Administered dose (mg min^-1)")
    plt.xlabel("Elapsed time (min)")
    plt.show()

    return 0

main()
