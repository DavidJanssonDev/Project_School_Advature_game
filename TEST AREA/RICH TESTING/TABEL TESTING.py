

from rich.console import Console
from rich.table import Table

pprint = Console()
table = Table(show_header=True, header_style="bold cyan")

table.add_column("Player Stats", style="dim", width=12)

table.add_row("Damage", "12")
pprint.print(table)
