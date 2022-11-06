import matplotlib.pyplot as plt
from math import e, pi


def fft(data):
    if len(data) == 1:
        return data

    res_even = fft(data[::2])
    res_odd = fft(data[1::2])

    res = [0]*len(data)
    for i in range(len(data)//2):
        res[i] = res_even[i] + pow(e, -1j*2*pi*i/len(data)) * res_odd[i]
        res[len(data)//2 + i] = res_even[i] - pow(e, -1j*2*pi*i/len(data)) * res_odd[i]
    return res


def ifft_inner(data):
    if len(data) == 1:
        return data

    res_even = ifft_inner(data[0::2])
    res_odd = ifft_inner(data[1::2])

    res = [0]*len(data)
    for i in range(len(data)//2):
        res[i] = res_even[i] + pow(e, 1j*2*pi*i/len(data)) * res_odd[i]
        res[len(data)//2 + i] = res_even[i] - pow(e, 1j*2*pi*i/len(data)) * res_odd[i]
    return res


def ifft(data):
    X = ifft_inner(data)
    l = len(data)
    return [abs(x)/l for x in X]

if __name__ == "__main__":
    data = [0.9219899378035104, 0.927964275688795, 0.09891569750612006, 0.001206699667402833, 0.17955801858527365, 0.15627432431634902, 0.7319043918375725, 0.23491123593450403, 0.36567403093317474, 0.3468435546737556, 0.472695405655969, 0.8896155072569817, 0.49225477297459175, 0.5388840933883622, 0.8168910115180003, 0.9920437590193059, 0.14210012965080387, 0.6245844567685869, 0.9285080324043271, 0.2703539406519947, 0.027136067440795886, 0.3355706335838774, 0.17084209674938977, 0.5802384981592698, 0.6987545997637991, 0.9982699382464586, 0.14381103436409415, 0.0707454974153785, 0.5338014072152318, 0.9040918063353081, 0.4702384981592698, 0.3202384981592698]
    fig, axs = plt.subplots(3)
    axs[0].plot(data)

    transformed = fft(data)
    axs[1].plot([abs(i) for i in transformed])

    back = ifft(transformed)
    axs[2].plot(back)
    plt.show()
