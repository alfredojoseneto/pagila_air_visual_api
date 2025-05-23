from dotenv import load_dotenv
from importlib import reload

from app.database import connection
from app.util import sql_handler, printer
from app.source import country_api, pagila, weather_api
from app.script import exercise

load_dotenv("app/.env")


def main() -> None:
    """
    Função principal do script que apresenta os resultados dos exercícios.
    """

    printer.session_header("EXERCÍCIO 01")
    exercise.exercise_01()
    printer.session_footer("Fim do Exercício 01")

    printer.session_header("EXERCÍCIO 02")
    exercise.exercise_02()
    printer.session_footer("Fim do Exercício 02")

    printer.session_header("EXERCÍCIO 03")
    exercise.exercise_03()
    printer.session_footer("Fim do Exercício 03")

    printer.session_header("EXERCÍCIO 04")
    exercise.exercise_04()
    printer.session_footer("Fim do Exercício 04")

    printer.session_header("EXERCÍCIO 05")
    exercise.exercise_05()
    printer.session_footer("Fim do Exercício 05")

    printer.session_header("EXERCÍCIO 06")
    exercise.exercise_06()
    printer.session_footer("Fim do Exercício 06")

    printer.session_header("EXERCÍCIO 07")
    exercise.exercise_07()
    printer.session_footer("Fim do Exercício 07")

    printer.session_header("EXERCÍCIO 08")
    exercise.exercise_08()
    printer.session_footer("Fim do Exercício 08")

    printer.session_header("EXERCÍCIO 09")
    exercise.exercise_09()
    printer.session_footer("Fim do Exercício 09")

    printer.session_header("EXERCÍCIO 10")
    print("O script para criar e atualizar o cache do AQI está em 'script.exercise.exercise_10()'")
    printer.session_footer("Fim do Exercício 10")

    printer.session_footer("Fim do Script")


if __name__ == "__main__":
    main()
