from django.shortcuts import render

perifericos = [
    {
        "id": 1,
        "nome": "INTEL CORE I3-13100F",
        "descricao": "Com suporte para DDR4 e DDR5, os processadores para desktop Intel Core i3 de 13ª geração são otimizados para produtividade. É necessário ter gráficos discretos. Compatível com placas-mãe com base em chipset Intel Série 700 e Intel Serie 600. Potência de base do processador 58W.",
        "foto": "https://images.kabum.com.br/produtos/fotos/405768/processador-intel-core-i3-13100f-4-5ghz-max-turbo-cache-12mb-4-nucleos-8-threads-lga-1700-bx8071513100f_1672748380_gg.jpg"
    },
    {
        "id": 2,
        "nome": "INTEL CORE I5-10400",
        "descricao": "Os novos processadores Intel® Core™ da 10ª geração oferecem atualizações de desempenho incríveis para melhorar a produtividade e proporcionar entretenimento surpreendente.",
        "foto": "https://images.kabum.com.br/produtos/fotos/112991/processador-intel-core-i5-10400f-cache-12mb-2-9ghz-lga-1200-bx8070110400f_1589199927_gg.jpg"
     },
    {
        "id": 3,
        "nome": "INTEL CORE I9-11900KF",
        "descricao": "Atuando em uma harmonia sem precedentes, o novo núcleo e arquiteturas gráficas, desempenho inteligente baseado em IA e a melhor conectividade sem fio e com fio da categoria, os processadores Intel® Core™ da 11ª Geração elevam o desempenho de notebooks e desktops a novos patamares.",
        "foto": "https://images.kabum.com.br/produtos/fotos/386971/processador-intel-core-i9-13900k-5-8ghz-max-turbo-cache-36mb-24-nucleos-32-threads-lga-1700-video-integrado-bx8071513900k_1664286209_gg.jpg"
    },
]

def listar_coisas(request):
    return render(request, 'listar_coisas.html')

def detalhar_processadores(request, id):
    periferico = perifericos[id-1]
    return render(request, 'detalhar_processadores.html', {"periferico": periferico})

def processadores(request):
    return render(request, 'processadores.html')

def memorias(request):
    return render(request, 'memorias.html')

def video(request):
    return render(request, 'placas_video.html')

def mae(request):
    return render(request, 'placas_mae.html')