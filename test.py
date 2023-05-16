import ldai

# LED-Streifen erstellen und mit einem Namen versehen
strip1 = ldai.led.LEDStrip("Strip1")
strip2 = ldai.led.LEDStrip("Strip2")

# LED auswählen und verwenden
ldai.led.select("Strip1", "LED1")
ldai.ldai.led.select("Strip2", "LED2")
