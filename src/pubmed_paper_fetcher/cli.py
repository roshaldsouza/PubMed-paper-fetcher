import typer
from pubmed_paper_fetcher.fetcher import search_pubmed, fetch_pubmed_details
from pubmed_paper_fetcher.utils import save_to_csv
import json

app = typer.Typer()

@app.command()
def get(
    query: str = typer.Argument(..., help="Query to search PubMed."),
    file: str = typer.Option(None, "-f", "--file", help="Filename to save CSV."),
    debug: bool = typer.Option(False, "-d", "--debug", help="Enable debug output.")
):
    if debug:
        typer.echo(f"Searching PubMed for: {query}")
    ids = search_pubmed(query)
    if debug:
        typer.echo(f"Found {len(ids)} papers.")
    data = fetch_pubmed_details(ids)
    if file:
        save_to_csv(data, file)
        typer.echo(f"Saved {len(data)} entries to {file}")
    else:
        typer.echo(json.dumps(data, indent=2))

@app.command()
def help_command():
    typer.echo("Usage: poetry run get-papers-list get '<QUERY>' [-f output.csv] [-d]")
    typer.echo("Use --help for more options.")

if __name__ == "__main__":
    app()
