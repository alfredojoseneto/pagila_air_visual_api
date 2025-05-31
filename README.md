# PAGILA AIR VISUAL API

## 📝 Descrição

Este é um projeto que foi elaborando utilizando a base de dados Sakila que foi
brilhantemente adaptada para Pagila pelo [devrimgunduz](https://github.com/devrimgunduz)
e as APIs [Air Visual API](https://api-docs.iqair.com/?version=latest),
[Weather API](https://www.weatherapi.com/) e [REST Countries API](https://restcountries.com/)
para o desenvolvimento de uma atividade relacionada à disciplina de Pythons
para Engenharia de Dados do MBA em Engenharia de Dados pela PUC-MG.

O objetivo do projeto foi elaborar o consumo destas API utilizando informações
dos nomes das cidades a fim de se obter temperatura e qualidade do ar para que
fosse possível realizar algumas análises.

## 💻 Pré-requisitos

Antes de começar, verifique requisitos para o projeto:

- Foi utilizada a versão `3.12.9` do python.
- Para gerenciamento das versões e do ambiente foi utilizado o [pyenv](https://github.com/pyenv/pyenv)
- O ambiente de desenvolvimento:
     - `Ubuntu 22.04 LTS`.
     - `pyenv 2.5.7-9-g70b973fd`
     - `Python version 3.12.9`
     - `Docker version 28.1.1, build 4eba377`
     - `Docker Compose version v2.35.1`

### Estrutura do projeto

O pojeto está estruturado de acordo com o modelo abaixo. No repositório não há o arquivo `.env`.
Abaixo será descrito o conteúdo do arquivo `.env`.

```text
pagila_air_visual_api
├── app
│   ├── cache
│   │   ├── data.json
│   │   └── data.json.bkp
│   ├── database
│   │   ├── connection_factory.py
│   │   ├── connection.py
│   │   └── __init__.py
│   ├── __main__.py
│   ├── .python-version
│   ├── report
│   │   └── report.xlsx
│   ├── requirements.txt
│   ├── script
│   │   └── exercise.py
│   ├── source
│   │   ├── airvisual_api.py
│   │   ├── country_api.py
│   │   ├── pagila.py
│   │   └── weather_api.py
│   └── util
│       ├── printer.py
│       └── sql_handler.py
├── app.Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
├── README.md
└── scripts
    ├── pagila-data-apt-jsonb.backup
    ├── pagila-data.sql
    ├── pagila-data-yum-jsonb.backup
    ├── pagila-insert-data.sql
    ├── pagila-schema-diagram.png
    ├── pagila-schema-jsonb.sql
    ├── pagila-schema.sql
    └── restore-pagila-data-jsonb.sh
```

### Arquivo `.env`

Como é um ambiente de teste com os dos do pagila, o banco de dados e o usuário
precisam ser `postgres` devido os scritps para a recriação do dos dados do pagila
estarem atrelados ao banco de dados postgres.

Quanto à `AIRVISUAL_KEY` e a `WEATHER_KEY` é necessário criar essa chaves nos
respectivos sites informados na sessão [descrição](#-descrição)

```text
AIRVISUAL_KEY=""
POSTGRES_DATABASE="postgres"
POSTGRES_HOST="db"
POSTGRES_PASSWORD=""
POSTGRES_PORT="5432"
POSTGRES_USER="postgres"
WEATHER_KEY = ""
```


## 🚀 Instalação

- Para criação do ambiente e execução do projeto:

```bash
# clonar o projeto
$ git@github.com:alfredojoseneto/pagila_air_visual_api.git

# criar as imagens
$ docker compose build

# inicializar os containers
$ docker compose up -d

# executar o app
$ docker exec -it app python -m app
``` 

## 📝 Outputs

Abaixo estão alguns exemplos de outputs do projeto elaborado.

```
########################################################################################################################
                                                      EXERCÍCIO 01                                                      
########################################################################################################################
Retrieving data...
========================================================================================================================
As 10 cidades com maior número de transações e suas temperaturas
------------------------------------------------------------------------------------------------------------------------
   customer_id                  city  transactions_amount  temp_c  weighted_temp_by_clients
0          148           Saint-Denis                   46    22.3                  0.063917
1          526        Cape Canaveral                   45    30.7                  0.086080
2          236                 Tanza                   42    29.4                  0.076939
3          144             Molodetno                   42     NaN                       NaN
4           75              Changhwa                   41    12.9                  0.032955
5          469               Ourense                   40     NaN                       NaN
6          197             Changzhou                   40    15.7                  0.039130
7          178  Santa Barbara dOeste                   39    29.3                  0.071201
8          468               Bijapur                   39    23.7                  0.057592
9          137             Apeldoorn                   39     4.4                  0.010692
========================================================================================================================

========================================================================================================================
As 10 cidades com menor número de transações e suas temperaturas
------------------------------------------------------------------------------------------------------------------------
     customer_id           city  transactions_amount  temp_c  weighted_temp_by_clients
589          164         Tarsus                   16    22.1                  0.022033
590          398            Bag                   16    20.0                  0.019939
591          464       Rancagua                   16    13.1                  0.013060
592          492    Kanchrapara                   16    27.4                  0.027316
593          136  Hubli-Dharwad                   15    22.5                  0.021029
594          248    Tallahassee                   15    34.4                  0.032152
595          110          Enshi                   14    15.0                  0.013085
596          281         Fuzhou                   14    26.2                  0.022855
597           61          Basel                   14     8.4                  0.007328
598          318      Bydgoszcz                   12     5.0                  0.003739
========================================================================================================================

========================================================================================================================
As 10 cidades com maiores temperaturas
------------------------------------------------------------------------------------------------------------------------
     customer_id                  city  transactions_amount  temp_c  weighted_temp_by_clients
352          343              Mexicali                   25    41.1                  0.064023
390          582     Huejutla de Reyes                   25    39.0                  0.060751
418          243  San Miguel de Tucumn                   24    38.0                  0.056826
135          275                Peoria                   30    37.3                  0.069724
500          443           So Leopoldo                   22    37.2                  0.050994
467          177             Matamoros                   23    37.0                  0.053025
228            6                Laredo                   28    36.7                  0.064029
75           451             El Fuerte                   33    35.9                  0.073818
344          570              Monclova                   26    35.8                  0.057997
185           25             Shikarpur                   29    35.3                  0.063786
========================================================================================================================

========================================================================================================================
As 10 cidades com menores temperaturas
------------------------------------------------------------------------------------------------------------------------
     customer_id             city  transactions_amount  temp_c  weighted_temp_by_clients
199          265          Olomouc                   29     5.0                  0.009035
155           23          Liepaja                   30     5.0                  0.009346
110          128  Jastrzebie-Zdrj                   32     5.0                  0.009969
9            137        Apeldoorn                   39     4.4                  0.010692
216          132       Botshabelo                   28     4.3                  0.007502
56           138           Hohhot                   34     4.3                  0.009110
245          376           Kurgan                   28     4.0                  0.006979
533          301      Kaliningrad                   21     3.3                  0.004318
42           207             Nuuk                   34     2.2                  0.004661
363          155             Bern                   25     2.2                  0.003427
========================================================================================================================

###############################################   Fim do Exercício 01   ################################################

########################################################################################################################
                                                      EXERCÍCIO 02                                                      
########################################################################################################################
Retrieving data...
========================================================================================================================
Faturamento das cidades com temperatura entre 18°C e 24°C
------------------------------------------------------------------------------------------------------------------------
              city invoicing  temp_c
0      Saint-Denis    216.54    22.3
1          Qomsheh    186.62    22.2
2          Bijapur    175.61    23.7
3    Lengshuijiang    159.64    18.3
4      Probolinggo    158.66    23.6
..             ...       ...     ...
110            Bag     78.84    20.0
111         Tarsus     66.84    22.1
112          Tegal     66.81    23.1
113  Hubli-Dharwad     62.85    22.5
114           Tete     58.82    20.3

[115 rows x 3 columns]
========================================================================================================================

========================================================================================================================
Faturamento TOTAL das cidades com temperatura entre 18°C e 24°C
------------------------------------------------------------------------------------------------------------------------
                invoicing
TOTAL_INVOICING  13074.96
========================================================================================================================

###############################################   Fim do Exercício 02   ################################################

########################################################################################################################
                                                      EXERCÍCIO 03                                                      
########################################################################################################################
Retrieving data...
========================================================================================================================
Os 10 países como maior taxa de aluguéis por 1000 habitantes
------------------------------------------------------------------------------------------------------------------------
                         country  rents_amount  population  rents_by_population
0                          India          1572      3000.0           524.000000
1  Holy See (Vatican City State)            34       451.0            75.388027
2                          Nauru            31     10834.0             2.861362
3                       Anguilla            35     13452.0             2.601844
4                         Tuvalu            26     11792.0             2.204885
5                  Liechtenstein            28     38137.0             0.734195
6                      Greenland            34     56367.0             0.603190
7                  Faroe Islands            28     48865.0             0.573007
8                 American Samoa            20     55197.0             0.362339
9           Virgin Islands, U.S.            32    106290.0             0.301063
========================================================================================================================

###############################################   Fim do Exercício 03   ################################################

########################################################################################################################
                                                      EXERCÍCIO 04                                                      
########################################################################################################################
Retrieving data... max waiting = 60 seconds
Waiting... 10 seconds
Waiting... 20 seconds
Waiting... 30 seconds
========================================================================================================================
As 10 cidades com maior número de clientes
------------------------------------------------------------------------------------------------------------------------
       country    district                  city  clients_amount   iqa
0       France     Reunion           Saint-Denis              46  24.0
1          USA     Florida        Cape Canaveral              45   NaN
2      Belarus       Minsk             Molodetno              42   NaN
3  Philippines  Calabarzon                 Tanza              42   NaN
4       Taiwan    Changhwa              Changhwa              41   NaN
5        China     Jiangsu             Changzhou              40   NaN
6        Spain     Galicia               Ourense              40  84.0
7  Netherlands  Gelderland             Apeldoorn              39   NaN
8       Brazil   Sao Paulo  Santa Barbara dOeste              39   NaN
9        India   Karnataka               Bijapur              39   NaN
========================================================================================================================

========================================================================================================================
Cidades com AQI maior ou igual a 150 e com filmes com rental rate acima de 4
------------------------------------------------------------------------------------------------------------------------
                    title rental_rate     country     city
0   STAGECOACH ARMAGEDDON        4.99       China  Tianjin
1          LIAISONS SWEET        4.99       China  Tianjin
2             MILLION ACE        4.99       China  Tianjin
3           BUBBLE GROSSE        4.99       China  Tianjin
4             CLOSER BANG        4.99       China  Tianjin
5    PITTSBURGH HUNCHBACK        4.99       China  Tianjin
6               COMA HEAD        4.99       China  Tianjin
7          CANDLES GRAPES        4.99       China  Tianjin
8               ZORRO ARK        4.99       China  Tianjin
9            ROAD ROXANNE        4.99       China  Tianjin
10      VIDEOTAPE ARSENIC        4.99       China  Tianjin
11        GROUNDHOG UNCUT        4.99  Bangladesh    Dhaka
12         LAWLESS VISION        4.99  Bangladesh    Dhaka
13       SLACKER LIAISONS        4.99  Bangladesh    Dhaka
14        MOONWALKER FOOL        4.99  Bangladesh    Dhaka
15           TRUMAN CRAZY        4.99  Bangladesh    Dhaka
16           MINDS TRUMAN        4.99  Bangladesh    Dhaka
17          WANDA CHAMBER        4.99  Bangladesh    Dhaka
18        AIRPORT POLLOCK        4.99  Bangladesh    Dhaka
19            RULES HUMAN        4.99  Bangladesh    Dhaka
========================================================================================================================

###############################################   Fim do Exercício 04   ################################################

########################################################################################################################
                                                      EXERCÍCIO 05                                                      
########################################################################################################################
Retrieving data...
========================================================================================================================
Cidades com AQI maior que 130 - zona de atenção
------------------------------------------------------------------------------------------------------------------------
           customer         city     country  aqi  temp_c      air_quality
2       DORA MEDINA      Tianjin       China  154    15.2  zona de atenção
1    GLENDA FRAZIER  Qinhuangdao       China  137    16.0  zona de atenção
7      JESSIE MILAM      Binzhou       China  132    13.8  zona de atenção
4  LEROY BUSTAMANTE     Tongliao       China  145    14.1  zona de atenção
0     MICHELE GRANT     Yuncheng       China  142    13.2  zona de atenção
5        ROBERTO VU     Yinchuan       China  138    14.4  zona de atenção
6      ROLAND SOUTH      Yingkou       China  145    13.3  zona de atenção
3    STEPHEN QUALLS        Dhaka  Bangladesh  178    26.3  zona de atenção
========================================================================================================================

###############################################   Fim do Exercício 05   ################################################

########################################################################################################################
                                                      EXERCÍCIO 06                                                      
########################################################################################################################
Retrieving data...
========================================================================================================================
Receita total (total invoice) por continente
------------------------------------------------------------------------------------------------------------------------
       continent total_invoice
0         Africa       6783.98
1           Asia      28621.25
2         Europe      13985.05
3  North America       9047.35
4        Oceania        743.27
5  South America       7777.70
========================================================================================================================

###############################################   Fim do Exercício 06   ################################################

########################################################################################################################
                                                      EXERCÍCIO 07                                                      
########################################################################################################################
Retrieving data...
========================================================================================================================
As 20 cidades com menores temperaturas e suas médias de dias de filmes alugados
------------------------------------------------------------------------------------------------------------------------
               city             country avg_rent_days  temp_c
0              Nuuk           Greenland          5.29     2.0
1              Bern         Switzerland          4.26     2.2
2       Kaliningrad  Russian Federation          3.62     3.1
3        Amersfoort         Netherlands          3.96     3.1
4         Apeldoorn         Netherlands          5.36     3.1
5            Kurgan  Russian Federation          4.07     4.0
6            Hohhot               China          3.56     4.1
7        Botshabelo        South Africa          4.14     4.2
8           Liepaja              Latvia          4.38     4.4
9         Bydgoszcz              Poland          4.42     5.0
10  Jastrzebie-Zdrj              Poland          4.44     5.0
11          Olomouc      Czech Republic          4.62     5.0
12           Witten             Germany          4.40     5.2
13           Kalisz              Poland          4.96     5.3
14  s-Hertogenbosch         Netherlands          4.52     5.4
15         Erlangen             Germany          5.59     6.0
16            Plock              Poland          5.25     6.1
17        Kimberley        South Africa          5.25     6.2
18           Siegen             Germany          4.32     6.4
19        Newcastle        South Africa          5.04     6.6
========================================================================================================================

========================================================================================================================
As 20 cidades com maiores temperaturas e suas médias de dias de filmes alugados
------------------------------------------------------------------------------------------------------------------------
                    city      country avg_rent_days  temp_c
0               Mexicali       Mexico          5.16    41.1
1      Huejutla de Reyes       Mexico          4.63    39.0
2   San Miguel de Tucumn    Argentina          3.42    38.0
3                 Peoria          USA          4.30    37.4
4            So Leopoldo       Brazil          4.73    37.0
5              Matamoros       Mexico          3.52    37.0
6                 Laredo          USA          5.07    36.7
7              El Fuerte       Mexico          4.36    35.9
8               Monclova       Mexico          4.00    35.8
9                   Naju  South Korea          5.00    35.3
10             Shikarpur     Pakistan          4.00    35.3
11               Garland          USA          4.73    35.2
12                 Okara     Pakistan          4.90    34.5
13           Tallahassee          USA          4.33    34.4
14           Naala-Porto   Mozambique          4.68    34.0
15                Dallas          USA          4.86    33.9
16      Jalib al-Shuyukh       Kuwait          4.80    33.7
17                Sokoto      Nigeria          4.68    33.7
18         Grand Prairie          USA          4.52    33.6
19             Arlington          USA          4.44    33.6
========================================================================================================================

###############################################   Fim do Exercício 07   ################################################

########################################################################################################################
                                                      EXERCÍCIO 08                                                      
########################################################################################################################
Retrieving data...
========================================================================================================================
Informações dos clientes
------------------------------------------------------------------------------------------------------------------------
             customer            city      country  rent_amount payment_amount  temp_c   aqi  age age_group
0        ELEANOR HUNT     Saint-Denis       France           46         216.54    22.3   NaN   65       60+
1           KARL SEAL  Cape Canaveral          USA           45         221.55    30.7   NaN   28     25-29
2          CLARA SHAW       Molodetno      Belarus           42         195.58     NaN   NaN   74       60+
3         MARCIA DEAN           Tanza  Philippines           42         175.58    29.2   NaN   34     30-34
4       TAMMY SANDERS        Changhwa       Taiwan           41         155.59    12.9   NaN   37     35-39
..                ...             ...          ...          ...            ...     ...   ...  ...       ...
594     ANITA MORALES   Hubli-Dharwad        India           15          62.85    22.5   NaN   51     50-54
595    TIFFANY JORDAN           Enshi        China           14          59.86    15.0  61.0   43     40-44
596  KATHERINE RIVERA           Basel  Switzerland           14          58.86     8.4   NaN   64       60+
597      LEONA OBRIEN          Fuzhou        China           14          50.86    26.2  54.0   18       <18
598       BRIAN WYMAN       Bydgoszcz       Poland           12          52.88     5.0   NaN   42     40-44

[599 rows x 9 columns]
========================================================================================================================

###############################################   Fim do Exercício 08   ################################################

########################################################################################################################
                                                      EXERCÍCIO 09                                                      
########################################################################################################################
Retrieving data...
Retrieving data...
========================================================================================================================
Dados exportados dos customers com payment acima da média, cidade com temperatura abaixo de 15C e AQI acima de 100
------------------------------------------------------------------------------------------------------------------------
               customer       city country  rent_amount payment_amount  temp_c    aqi  age age_group
40         REGINA BERRY   Jinchang   China           34         135.66    13.7  124.0   66       60+
57        CARRIE PORTER  Liaocheng   China           34         124.66    14.3  127.0   57     55-59
60         JESSIE MILAM    Binzhou   China           33         141.67    13.8  132.0   27     25-29
81     LEROY BUSTAMANTE   Tongliao   China           32         118.68    14.1  145.0   48     45-49
139       MICHELE GRANT   Yuncheng   China           30         130.70    13.2  142.0   64       60+
144  TERRENCE GUNDERSON    Jinzhou   China           30         117.70    14.2  122.0   65       60+
149     WALTER PERRYMAN   Xinxiang   China           30         127.70    14.5  110.0   52     50-54
152          ROBERTO VU   Yinchuan   China           30         139.70    14.4  138.0   69       60+
205       MARION OCAMPO    Weifang   China           29         115.71    13.1  117.0   67       60+
========================================================================================================================

###############################################   Fim do Exercício 09   ################################################

########################################################################################################################
                                                      EXERCÍCIO 10                                                      
########################################################################################################################
O script para criar e atualizar o cache do AQI está em 'script.exercise.exercise_10()'
###############################################   Fim do Exercício 10   ################################################

##################################################   Fim do Script   ###################################################
```
