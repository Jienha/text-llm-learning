1) Scelta degli snapshot e definizione del target (problema temporale)

Prima di tutto definisci come etichettare “inattivo” e “riattivato” in modo coerente nel tempo.

Regola di inattività: >120 giorni dall’ultimo acquisto.

Snapshot date (index date): scegli una data di riferimento sulla quale calcoli lo stato di inattività e le feature (es. snapshot = '2024-09-30' o una serie di snapshot retrospettivi per fare backtesting).

Perché : i tuoi transactions arrivano fino al 2024-12-31, quindi per poter osservare la riattivazione nel futuro devi scegliere snapshot abbastanza indietro da avere un “finestra di osservazione” (es. reattivazione entro 90 giorni → snapshot ≤ 2024-10-02).

Label di reattivazione (supervised): per ogni cliente inattivo al snapshot, definiamo reactivated = 1 se compie almeno un acquisto entro react_window_days dopo lo snapshot (es. 90 giorni), altrimenti 0.

Pratica: costruisci più snapshot (rolling monthly) per aumentare il dataset di training e test temporale.