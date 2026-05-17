palavras = ["Python", "AI", "Desenvolvimento", "API", "Web", "Framework"]

print(palavras)

palavras_maiusculo = [p.upper() if len(p) > 5 else p.lower() for p in palavras]

print(palavras_maiusculo)
