n_lattine = 6
capienza_lattina = 12  # once!

n_bottiglie = 1
capienza_bottiglia = 2 # litri

ONCIA = 0.355 / 12 # litri/once

litri_in_lattine = n_lattine * capienza_lattina * ONCIA
litri_in_bottiglia = n_bottiglie * capienza_bottiglia

print('Se compro lattine avrò', litri_in_lattine, 'litri')
print('Se compro bottiglie avrò', litri_in_bottiglia, 'litri')
