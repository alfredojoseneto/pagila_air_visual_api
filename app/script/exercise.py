from importlib import reload
from app.source import country_api, pagila, weather_api, airvisual_api
from app.util import printer
import json
import os
import datetime


reload(pagila)
reload(weather_api)
reload(country_api)
reload(airvisual_api)


def __get_cache_data() -> dict:
    # lê o arquivo que já contém os dados
    with open("app/cache/data.json", "r") as file:
        cache_data = dict(json.loads(file.read()))
        file.close()
    return cache_data


def exercise_01() -> None:
    """
    Exercício 1 - Temperatura Média das Capitais dos Clientes
    •    Recupere as cidades dos clientes com mais de 10 transações.
    •    Use a WeatherAPI para buscar a temperatura atual dessas cidades.
    •    Calcule a temperatura média ponderada por número de clientes.
    •    Insight esperado: quais cidades concentram clientes e temperaturas extremas?
    """

    print("Retrieving data...")
    data = pagila.exercise_01_data()
    data["temp_c"] = data["city"].map(
        weather_api.paralle_get_city_temp_c(set(data["city"]))
    )
    total_clients = data["transactions_amount"].sum()
    data["weighted_temp_by_clients"] = data.apply(
        lambda x: x["transactions_amount"] / total_clients * x["temp_c"], axis=1
    )
    printer.tables(
        title="As 10 cidades com maior número de transações e suas temperaturas",
        df=data.sort_values(by=["transactions_amount"], ascending=False).head(10),
    )
    printer.tables(
        title="As 10 cidades com menor número de transações e suas temperaturas",
        df=data.sort_values(by=["transactions_amount"], ascending=False).tail(10),
    )
    printer.tables(
        title="As 10 cidades com maiores temperaturas",
        df=data.sort_values(by=["temp_c"], ascending=False).head(10),
    )
    printer.tables(
        title="As 10 cidades com menores temperaturas",
        df=data.loc[(data["temp_c"].notnull())]
        .sort_values(by=["temp_c"], ascending=False)
        .tail(10),
    )
    return None


def exercise_02() -> None:
    """
    Exercício 2 - Receita Bruta em Cidades com Clima Ameno
    •   Calcule a receita bruta por cidade.
    •   Use a WeatherAPI para consultar a temperatura atual.
    •   Filtre apenas cidades com temperatura entre 18°C e 24°C.
    •   Resultado: qual o faturamento total vindo dessas cidades?
    """
    print("Retrieving data...")
    data = pagila.exercise_02_data()
    data["temp_c"] = data["city"].map(
        weather_api.paralle_get_city_temp_c(set(data["city"]))
    )
    data = data.loc[(data["temp_c"].between(left=18, right=24))]
    printer.tables(
        title="Faturamento das cidades com temperatura entre 18°C e 24°C",
        df=data.sort_values(by=["invoicing"], ascending=False).reset_index(drop=True),
    )
    printer.tables(
        title="Faturamento TOTAL das cidades com temperatura entre 18°C e 24°C",
        df=data.agg(TOTAL_INVOICING=("invoicing", "sum")),
    )
    return None


def exercise_03() -> None:
    """
    Exercício 3 - Aluguel de Filmes por Região e População
    •   Identifique os países dos clientes com maior número de aluguéis.
    •   Use a REST Countries API para obter a população desses países.
    •   Calcule o número de aluguéis por 1.000 habitantes.
    •   Análise: quais países são mais “cinéfilos” proporcionalmente?
    """

    print("Retrieving data...")
    data = pagila.exercise_03_data()
    countries = list(data["country"].values)
    result = country_api.parallel_get_country_info(countries=countries)
    population = {}
    for key, value in result.items():
        population[key] = value["population"]
    data["population"] = data["country"].map(population)
    data["rents_by_population"] = data.apply(
        lambda x: (x["rents_amount"] / x["population"] * 1000), axis=1
    )

    printer.tables(
        title="Os 10 países como maior taxa de aluguéis por 1000 habitantes",
        df=data.sort_values(by=["rents_by_population"], ascending=False)
        .reset_index(drop=True)
        .iloc[0:10],
    )

    return None


def exercise_04() -> None:
    """
    Exercício 4 - Filmes Mais Populares em Cidades Poluídas
    •   Liste as 10 cidades com maior número de clientes.
    •   Use a AirVisual API para consultar o AQI dessas cidades.
    •   Relacione os filmes mais alugados em cidades com AQI > 150.
    •   Discussão: poluição impacta preferências de filmes?
    """

    print("Retrieving data... max waiting = 60 seconds")
    data = pagila.exercise_04_data()
    air_visual = {}
    for value in data[["country", "district", "city"]].to_dict("records"):
        air_visual[value["city"]] = airvisual_api.get_air_quality(**value)

    iqa = {}
    for key, value in air_visual.items():
        if value:
            iqa[key] = value.get("data").get("current").get("pollution").get("aqius")

    data["iqa"] = data["city"].map(iqa)

    printer.tables(title="As 10 cidades com maior número de clientes", df=data)

    # obtém os dados que já estão em cache
    cache_data = __get_cache_data()

    # lista as cidades que possuem dados de aqi no cache
    aqi_150_data = {}
    for key, value in cache_data.items():
        try:
            city_name = value["data"]["city"]
            aqi = value["data"]["current"]["pollution"]["aqius"]
            aqi_150_data[city_name] = aqi
        except KeyError as e:
            continue

    # lista apenas as cidades com aqi maior ou igual a 150
    aqi_150_cities = []
    for city, aqi in aqi_150_data.items():
        if aqi >= 150:
            aqi_150_cities.append(city)

    # obtém apenas os filmes com rental_rate acima de 4 e cidades com aqi acima de 150
    data_aqi = pagila.exercise_04_data_aqi_150(*aqi_150_cities)
    printer.tables(
        title="Cidades com AQI maior ou igual a 150 e com filmes com rental rate acima de 4",
        df=data_aqi,
    )

    return None


def exercise_05() -> None:
    """
    Exercício 5 - Clientes em Áreas Críticas
    •   Recupere os clientes com endereço em cidades com AQI acima de 130.
    •   Combine nome do cliente, cidade, país, temperatura e AQI.
    •   Classifique os clientes em “zona de atenção” com base nos critérios ambientais.
    """

    print("Retrieving data...")

    # lista as cidades que possuem dados de aqi no cache
    cache_data = __get_cache_data()
    aqi_data = {}
    for key, value in cache_data.items():
        try:
            city_name = value["data"]["city"]
            aqi = value["data"]["current"]["pollution"]["aqius"]
            aqi_data[city_name] = aqi
        except KeyError as e:
            continue

    # lista apenas as cidades com aqi maior ou igual a 150
    aqi_130_cities = {}
    for city, aqi in aqi_data.items():
        if aqi > 130:
            aqi_130_cities[city] = aqi

    data = pagila.exercise_05_data(*aqi_130_cities.keys())

    # adiciona a informação do aqi
    data["aqi"] = data["city"].map(aqi_130_cities)

    # obtendo dados da temperatura
    data["temp_c"] = data["city"].map(
        weather_api.paralle_get_city_temp_c(set(data["city"]))
    )

    # reorderna o data frame pelo nome do customer
    data = data.sort_values(by=["customer"])

    # adicionando o critério ambiental
    data["air_quality"] = "zona de atenção"

    # apresentando os resultados
    printer.tables(title="Cidades com AQI maior que 130 - zona de atenção", df=data)

    return None


def exercise_06() -> None:
    """
    Exercício 6 - Receita por Continente
    •   Use a REST Countries API para mapear o continente de cada país.
    •   Agrupe a receita total por continente.
    •   Exiba os resultados em um gráfico de pizza com matplotlib.
    """
    print("Retrieving data...")

    # obtendo os dados do pagila
    data = pagila.exercise_06_data()

    # obtendo as informações pela country api
    requests = country_api.parallel_get_country_info(list(data["country"].values))

    # organizando as informações dos continentes para o mapping
    continents = {}
    for country, info in requests.items():
        continents[country] = info["continents"]

    # mapeando os resultados
    data["continent"] = data["country"].map(continents)

    # agrupando os dados
    data_invoice = (
        data.groupby(by=["continent"])
        .agg(total_invoice=("amount", "sum"))
        .sort_values(by=["continent"])
        .reset_index()
    )

    # apresentação dos resultados
    printer.tables(
        title="Receita total (total invoice) por continente", df=data_invoice
    )

    return None


def exercise_07() -> None:
    """
    Exercício 7 - Tempo Médio de Aluguel vs Clima
    •   Calcule o tempo médio de aluguel por cidade (entre rental_date e return_date).
    •   Combine com a temperatura atual dessas cidades.
    •   Visualize a correlação entre temperatura e tempo médio de aluguel (scatterplot + linha de tendência).
    """

    data = pagila.exercise_07_data()

    data["temp_c"] = data["city"].map(
        weather_api.paralle_get_city_temp_c(set(data["city"]))
    )

    printer.tables(
        title="As 20 cidades com menores temperaturas e suas médias de dias de filmes alugados",
        df=data.sort_values(
            by=["temp_c", "avg_rent_days"], ascending=[True, True]
        ).reset_index(drop=True)[:20],
    )

    printer.tables(
        title="As 20 cidades com maiores temperaturas e suas médias de dias de filmes alugados",
        df=data.sort_values(
            by=["temp_c", "avg_rent_days"], ascending=[False, False]
        ).reset_index(drop=True)[:20],
    )

    return None


#   Exercício 8 – Perfil de Clima por Cliente
#   •   Para cada cliente, crie um perfil com:
#   •   cidade, temperatura, AQI, total de aluguéis, gasto total.
#   •   Agrupe os perfis por faixa etária (simulada ou fictícia) e avalie padrões.
#   •   Objetivo: conectar comportamento de consumo e ambiente.

# ⸻

#   Exercício 9 – Exportação Inteligente
#   •   Gere um relatório Excel com os seguintes critérios:
#   •   Clientes de países com temperatura < 15°C
#   •   AQI acima de 100
#   •   Receita individual > média geral
#   •   Utilize OpenPyXL e organize em múltiplas abas: Clientes, Temperaturas, Alertas.

# ⸻


def exercise_10() -> dict:
    """
    Exercício 10 - API Cache Inteligente (Desafio)
    •   Implemente uma lógica que salve os dados de clima e AQI localmente em CSV.
    •   Ao consultar novamente a mesma cidade, busque do CSV ao invés da API.
    •   Evite chamadas redundantes — bom para práticas de performance e economia de requisições.
    """

    # obtém as cidades já encontradas
    os.makedirs("app/cache", exist_ok=True)
    cache_data = __get_cache_data()

    # obtém dados das cidades a serem encontrada
    pagila_cities = pagila.pagila_all_cities()
    data = pagila_cities[["country", "district", "city"]].to_dict("records")

    # cria a validação das cidades que já foram obtidas
    cache_city = {}
    for key, value in cache_data.items():
        try:
            cache_city[value["city"]] = True
        except KeyError:
            cache_city[value["data"]["city"]] = True

    # obtém os novos dados
    start_time = datetime.datetime.now()
    for i, value in enumerate(data):
        if cache_city.get(value["city"]):
            continue
        print(value)
        new_data = {i: value}
        try:
            aqi_data = airvisual_api.get_air_quality(**value)
            print(aqi_data)
            if aqi_data:
                new_data = {i: aqi_data}
        except Exception as e:
            print(e)
        finally:
            cache_data.update(new_data)
    end_time = datetime.datetime.now()
    print(end_time - start_time)

    # update cache
    with open("app/cache/data.json", "w") as file:
        file.seek(0)
        json.dump(cache_data, file, indent=4)
        file.truncate()

    return cache_data
