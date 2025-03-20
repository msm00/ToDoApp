import typer
from rich import print
from .services import add_item, list_items, complete_item, delete_item

app = typer.Typer()

@app.command()
def add(title: str):
    add_item(title)
    print(f"[green]Úkol přidán:[/green] {title}")

@app.command()
def list():
    items = list_items()
    for item in items:
        status = "[x]" if item.completed else "[ ]"
        print(f"{status} {item.id}: {item.title}")

@app.command()
def complete(id: int):
    complete_item(id)
    print(f"[yellow]Úkol {id} označen jako dokončený.[/yellow]")

@app.command()
def delete(id: int):
    delete_item(id)
    print(f"[red]Úkol {id} smazán.[/red]")

if __name__ == "__main__":
    app()