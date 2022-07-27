from shiny import App, render, ui
from siuba.data import mtcars
from siuba import filter, _

app_ui = ui.page_fluid(
    
    ui.h2("Hello ThinkR!"),
    ui.input_slider("mpg", "Filter on mpg column:", 0, 50, 10),
    ui.output_table("render_mtcars")
)


def server(input, output, session):
    @output
    @render.table
    def render_mtcars():
        mtcars_filtered = mtcars >> filter(_.mpg <= input.mpg())
        return mtcars_filtered

app = App(app_ui, server)
