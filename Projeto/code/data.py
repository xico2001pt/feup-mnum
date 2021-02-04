import math

# Data to be filled
Ka = 0  # kinetic absorption constant (min^-1)


# Utility Functions
def days_to_minutes(days):
    return 24 * 60 * days


def update_ka(val):
    global Ka
    Ka = val


# Statement Data
daily_dose = 150  # daily dose ingested (mg)
intake_interval = days_to_minutes(0.5)  # time interval between dose consumption (min)
treatment_duration = days_to_minutes(3)  # total duration of the treatment (min)
doses_per_day = days_to_minutes(1) / intake_interval  # number of doses taken in a day (doses/day)
Vap = 3250  # apparent volume of plasma (mL)
Ket = 0.17325 / 60  # kinetic total elimination constant (min^-1)
t_max = 4 * 60  # instant when the maximum drug plasma concentration occur (min)


# Abstract Data
mi_initial = 0  # initial drug's mass in the central compartment (mg)
mp_initial = 0  # initial drug's mass in the plasma compartment (mg)
administration_duration = 10 / 60  # minutes it takes to administer an ampoule (min)
reach_duration = 2 / 60  # minutes it takes for the administration function to reach its peak (min)
peak_duration = administration_duration - 2 * reach_duration  # amount of time the administration function is on its peak (min)
max_dose = daily_dose / doses_per_day / (administration_duration - reach_duration)  # administered dose when the peak is reached (mg)


# Non-Linear Equations
def non_linear_equation(Ka):
    return Ka * math.exp(-Ka * t_max) - Ket * math.exp(-Ket * t_max)


def non_linear_equation_derivative(Ka):
    # This function was obtained using Maxima
    return math.exp(-Ka * t_max) - t_max * Ka * math.exp(-Ka * t_max)


def picard_peano_equation1(Ka):
    return math.log(Ka * math.exp(Ket * t_max) / Ket) / t_max


def picard_peano_equation2(Ka):
    return Ket * math.exp(Ka * t_max - Ket * t_max)


# Differential Equations
def dual_model_equation_1(t, mi, mp):
    return D(t) - Ka * mi

def dual_model_equation_2(t, mi, mp):
    return Ka * mi - Ket * mp


# Administration Function
def D(t):
    if t >= treatment_duration:
        return 0

    t = t % intake_interval  # Modulate time
    if t < reach_duration:
        return t * max_dose / reach_duration
    elif t < reach_duration + peak_duration:
        return max_dose
    elif t < administration_duration:
        return (administration_duration - t) * max_dose / reach_duration
    else:
        return 0
