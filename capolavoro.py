import os
import matplotlib.pyplot as plt
import fastf1
import fastf1.plotting

cache_dir = 'f1_cache'

if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

fastf1.Cache.enable_cache(cache_dir)

fastf1.plotting.setup_mpl(color_scheme='fastf1', misc_mpl_mods=False)

anno = 2024
gp = 'Monza'
sessione_tipo = 'R'

print(f"Caricamento dei dati del GP di {gp} {anno} in corso...")
print("Nota: La prima volta potrebbe richiedere un minuto per scaricare i dati.")

session = fastf1.get_session(anno, gp, sessione_tipo)
session.load()

pilota1 = 'LEC'  
pilota2 = 'PIA'  

giro_p1 = session.laps.pick_driver(pilota1).pick_fastest()
giro_p2 = session.laps.pick_driver(pilota2).pick_fastest()

telemetria_p1 = giro_p1.get_telemetry().add_distance()
telemetria_p2 = giro_p2.get_telemetry().add_distance()

colore_p1 = fastf1.plotting.get_team_color(giro_p1['Team'], session=session)
colore_p2 = fastf1.plotting.get_team_color(giro_p2['Team'], session=session)

fig, ax = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

ax[0].plot(telemetria_p1['Distance'], telemetria_p1['Speed'], color=colore_p1, label=pilota1, linewidth=1.5)
ax[0].plot(telemetria_p2['Distance'], telemetria_p2['Speed'], color=colore_p2, label=pilota2, linewidth=1.5)
ax[0].set_ylabel('Velocità (km/h)')
ax[0].set_title(f'Confronto Telemetria: {pilota1} vs {pilota2}\n{anno} {gp} Grand Prix - Giro più veloce in Gara')
ax[0].legend(loc='lower left')
ax[0].grid(True, linestyle='--', alpha=0.5)

ax[1].plot(telemetria_p1['Distance'], telemetria_p1['Brake'], color=colore_p1, label=pilota1, linewidth=1.5)
ax[1].plot(telemetria_p2['Distance'], telemetria_p2['Brake'], color=colore_p2, label=pilota2, linewidth=1.5)
ax[1].set_ylabel('Uso del Freno (0/1 o %)')
ax[1].set_xlabel('Distanza sul tracciato (metri)')
ax[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
print("generazione grafico.")
plt.show()
