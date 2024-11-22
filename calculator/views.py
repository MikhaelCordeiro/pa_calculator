from django.shortcuts import render

def calculadora_pa(request):
    if request.method == "POST":
        # Obtém os valores enviados pelo formulário
        primeiro_termo = request.POST.get("primeiro_termo")
        razao = request.POST.get("razao")
        quantidade_termos = request.POST.get("quantidade_termos")

        # Verifica se todos os valores foram preenchidos
        if not primeiro_termo or not razao or not quantidade_termos:
            erro = "Por favor, preencha todos os campos corretamente."
            return render(request, "calculator/calculadora_pa.html", {"erro": erro})

        try:
            # Converte os valores para inteiros
            primeiro_termo = int(primeiro_termo)
            razao = int(razao)
            quantidade_termos = int(quantidade_termos)

            # Calcula os termos da PA
            termos = [primeiro_termo + razao * i for i in range(quantidade_termos)]
            soma = sum(termos)

            return render(request, "calculator/calculadora_pa.html", {
                "termos": termos,
                "soma": soma
            })

        except ValueError:
            # Trata o caso em que a conversão para inteiro falhar
            erro = "Os valores devem ser números inteiros."
            return render(request, "calculator/calculadora_pa.html", {"erro": erro})

    return render(request, "calculator/calculadora_pa.html")
