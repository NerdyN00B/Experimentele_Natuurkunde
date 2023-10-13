import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

datafile = 'EN1_EXP4_M1.csv'

R_REF = 10000  # Referentieweerstand in ohm
V_BRON = 5  # Bronspanning in volt
meetbereik = 20  # Ingestelde meetbereik van de myDAQ

schatwaarde_T0 = 36
schatwaarde_Tomgeving = 21
schatwaarde_tau = 10


def mydaq_fout(spanning, meetbereik):
    """Bepaald de fout op de gemeten spanning bij gebruik van een myDAQ.

    Parameters
    ----------
    spanning (int, float): De door de myDAQ gemeten spanning in volt.
    meetbereik (int, float): Het ingestelde meetbereik op de myDAQ in volt.
        Dit kan 0.2, 2, 20 of 200 volt zijn.
        Als een waarde tussen de mogelijke waardes opgegeven wordt zal de
        eerstvolgende waarde gebruikt worden.

    Returns
    -------
    float: De fout op de gemeten spanning in volt.
    """
    # Bepaal het meetbereik en stel de digit in.
    if meetbereik <= 0.2:
        digit = 0.0002
    elif spanning <= 2:
        digit = 0.002
    elif spanning <= 20:
        digit = 0.02
    elif spanning <= 200:
        digit = 0.2

    # return de fout
    return 0.5/100 * spanning + digit


def func(x, T_0, T_omgeving, tau):
    """Functie die een exponentiele afname in temperatuur modelleert.
    y = (T_0 - T_omgeving) * exp(-x / tau) + T_omgeving
    """
    return (T_0 - T_omgeving) * np.exp(-x / tau) + T_omgeving


# Lees data in
tijd, spanning = np.loadtxt(datafile, delimiter=',', unpack=True)

# Slice data indien nodig.
begin_data = 0
tijd, spanning = tijd[begin_data:], spanning[begin_data:]

# Bepaal fout op gemeten spanning
sigma_V = mydaq_fout(spanning, meetbereik)

# Bepaal de weerstand en de fout hierop.
weerstand = -1 * (R_REF*(V_BRON - 2*spanning)) / (2*spanning - V_BRON)
sigma_R = np.abs(
    (2*R_REF*V_BRON - 2*R_REF*(2*spanning - V_BRON) - 2*(R_REF*spanning)) /
    ((2*spanning - V_BRON)**2)
    ) * sigma_V

# Bepaal de temperatuur en de fout hierop.
temperatuur = (np.log(weerstand/35000)) / -0.046
sigma_T = np.abs(1 / (-0.046 * weerstand)) * sigma_R

# Maak een figuur en assenstelsel aan.
fig, ax = plt.subplots(dpi=300)

# Plot de data.
ax.errorbar(tijd, temperatuur, yerr=sigma_T, fmt='.k', capsize=2,
            label='meetdata')

# Fit een exponentiele curve naar de data.
schatwaardes = (schatwaarde_T0, schatwaarde_Tomgeving, schatwaarde_tau)
popt, pcov = curve_fit(func, tijd, temperatuur, schatwaardes, sigma_T,
                       absolute_sigma=True)
ax.plot(tijd, func(tijd, *popt, ls='--', c='k',
                   label='fit naar exponentiele afname'))

# Maak plot mooi.
ax.grid()
ax.legend()
ax.set_xlabel('tijd $t$ ($s$)')
ax.set_ylabel('temperatuur $T$ ($^{\circ}C$)')

fig.show()
# fig.savefig('plot.pdf')
print(popt)
print(np.diagonal(pcov))
