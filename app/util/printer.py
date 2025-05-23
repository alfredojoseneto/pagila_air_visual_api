from pandas import DataFrame


def session_header(title: str) -> None:
    print(f"{'':#^120}")
    print(f"{title:^120}")
    print(f"{'':#^120}")


def session_footer(text: str) -> None:
    text = f"   {text}   "
    print(f"{text:#^120}\n")


def tables(title: str, df: DataFrame) -> None:
    print(f"{'':=<120}")
    print(f"{title}")
    print(f"{'':-<120}")
    print(df)
    print(f"{'':=<120}\n")
