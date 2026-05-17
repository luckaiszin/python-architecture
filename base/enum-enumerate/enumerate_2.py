temps = [28, 31, 27, 35, 29, 33, 26]

for dia, temperatura in enumerate(temps, start=1):
    if temperatura > 30:
        print(f"Dia {dia}: {temperatura}°C")
