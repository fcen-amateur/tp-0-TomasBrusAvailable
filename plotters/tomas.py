import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[gapminder.continent == "Americas"],
            x="year",
            y="lifeExp",
        )
        .add(so.Line(), color = "country")
        .label(
            title="Expectativa de vida en America",
            x="Año",
            y="Expectativa de vida",
            color="País",
        )
    )
    return dict(
        descripcion="La expectatica de vida de los paises de America durante los años",
        autor="Tomas",
        figura=figura,
    )