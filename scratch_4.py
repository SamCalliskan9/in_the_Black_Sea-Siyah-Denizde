Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... import random
... import time
... 
... print("=== BLACK SEA - KRAKEN ENCOUNTER ===")
... print("=== BLACK SEA - KRAKEN KARŞILAŞMASI ===\n")
... print("You are sailing across the Black Sea... The waves are silent...")
... print("Black Sea'de yelken açıyorsun... Dalgalar sessiz...\n")
... time.sleep(1)
... 
... print("Suddenly, the sea turns dark. A gigantic KRAKEN appears in front of ship!")
... print("Birden, deniz kararıyor. Devasa bir KRAKEN geminin önünde beliriyor!")
... print("You must survive. / Hayatta kalmalısın.\n")
... 
... # ---- Basic Stats / TemeL Can ----
... player_hp = 40
... kraken_hp = 50
... print(f"Your HP: {player_hp} / Senin Canın: {player_hp}")
... print(f"Kraken HP: {kraken_hp} / Kraken Canı: {kraken_hp}\n")
... 
... # ---- Battle Loop / Döngü ----
... while player_hp > 0 and kraken_hp > 0:
...     print("\nChoose an action: / Bir eylem seç:")
...     print("1) Slash Attack / Kılıç Darbesi")
...     print("2 Defend / Savun")
...     print("3) Heavy Strike (risky) / Güçlü vuruş (riskli)")
...     choice = input("Action (1/2/3):")
... 
...     if choice == "1":
...         dmg = random.randint(5,12)
...         kraken_hp = dmg
...         print(f" You slash The Kraken! Damage: {dmg} / Kraken'e kılıç darbesi! Hasar: {dmg}")
...     elif choice == "2":
...         dmg = random.randint(0,20)
...         kraken_hp = dmg
        print(f" You attempt a heavy strike! Damage: {dmg} / Güçlü vuruş denedin! Hasar: {dmg}")
    else:
        print("> İnvalid action - you lose your turn! / Geçersiz eylem - bu turu kaybettin!")

# ---- Kraken Attack / Kraken Saldırısı ----
if kraken_hp > 0:
    if choice == "2":
        k_dmg = max(3, random.randint(8,15) -8)
    else:
        k_dmg = random.randint(8, 15)
    player_hp -= k_dmg
    print(f"Kraken hits! Damage: {k_dmg} / Kraken saldırdı! Hasar: {k_dmg}")

time.sleep(0.7)
print(f" Your HP: {player_hp} / Senin Canın: {player_hp}")
print(f"Kraken HP: {kraken_hp} / Kraken Canı: {kraken_hp}")
print("-" * 40)
time.sleep(0.4)

# ---- Outcome / Sonuç ----

if player_hp <= 0 and kraken_hp <= 0:
    print("\nBoth you and the Kraken fall into the sea. A draw... / Sen ve Kraken denize gömüldünüz. Berabere...")
elif player_hp <= 0:
    print("\nThe Kraken pulls your ship under. You are defeated. / Kraken gemini derinlere çekti. kaybettin.")
else:
    print("\nYou pierce the Kraken's hearth! The beast sinks. / Kraken'in kalbini deldin! Canavar dalgaların arasında kayboldu.")
    print("You survived the Black Sea! / Black Sea'de hayatta kaldın!")

