import json

# cargar noticias limpias
with open("data/news_clean.json", "r") as f:
    news = json.load(f)

items = []

for n in news:
    title = n.get("title", "")
    source = n.get("source", "")
    url = n.get("url", "")

    items.append(f"- {title} | Fuente: {source} | {url}")

news_text = "\n".join(items)

prompt = f"""
Actuarás como un curador de noticias en el enfoque de ciberseguridad.

La audiencia son profesionales de seguridad, ejecutivos y profesionales del área.

Con las noticias disponibles, construye un boletín con las siguientes reglas:

1. Para cada sección selecciona **las 3 noticias más relevantes**
2. No repitas noticias entre secciones
3. Usa múltiples fuentes si aplican

Secciones:

Geopolítica
Ciberataques: ataques no ransomware
Vulnerabilidades
Ransomware
Brechas de datos
Para el CISO: consideraciones estratégicas
Para el CISO: relación con equipos ejecutivos
Ciberseguridad e IA
Ciberresiliencia y riesgo cibernético
Investigaciones sobre ciberseguridad
Algo más

Luego agrega:

Pensamiento de la semana  
(3 reflexiones tipo cita basadas en las noticias)

Datos estadísticos de la semana  
(3 datos relevantes, preferiblemente porcentuales)

Noticias disponibles:

{news_text}
"""

print(prompt)
# workflow test
