import math
from flask import render_template, request

def calcular():

    try:
        num1 = float(request.form["num1"])
    except (ValueError, KeyError):
        return render_template(
            "calculadora.html", 
            etapas="Erro: Informe um número válido no primeiro campo." ,
            resultados="" ,
        )
    operacao= request.form.get("operacao", "+")

    if operacao == "sqrt":
        if num1 < 0:
            etapas = f"Não existe raiz real de {num1}"
            resultado = "Erro: número negativo"
        else:
            resultado = math.sqrt(num1)
            etapas = f"raiz de {num1} = {resultado}"
        return render_template(
            "calculadora.html",
            etapas=etapas,
            resultados=resultado,
        )
    if operacao == "log":
        if num1 <= 0:
            etapas = f"Logaritmp indefinido para {num1} (deve ser > 0)."
            resultado = "Erro: número Invalido para log"
        else:
            resultado = math.log10(num1)
            etapas = f"log10({num1}) = {resultado}"
        return render_template(
            "calculadora.html",
            etapas=etapas,
            resultados=resultado,
        )
    num2_valor = request.form.get("num2", "").strip()
    if not num2_valor:
        return render_template(
            "calculadora.html",
            etapas="informe o segundo número para esta operação.",
            resultados="",
        )
    try:
        num2 = float(num2_valor)
    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Erro: informe um número valido no segundo campo.",
            resultados="",
        )
    
    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2} = {resultado}"
    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2} = {resultado}"
    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} x {num2} = {resultado}"
    elif operacao == "/":
        if num2 == 0:
            return render_template(
                "calculadora.html",
                etapas="Erro: divisão por zero não é permitida. ",
                resultado="Indefinido",
            )
        resultado = num1 / num2
        etapas = f"{num1} / {num2} = {resultado}"
    elif operacao == "**":
        resultado = num1 ** num2
        etapas = f"{num1} ^ {num2} = {resultado}"
    else:
        return render_template(
            "calculadora.html",
            etapas=f"Operação '{operacao}' não reconhecida.",
            resultados="",
        )
    return render_template(
        "calculadora.html",
        etapas=etapas,
        resultados=resultado,
    )