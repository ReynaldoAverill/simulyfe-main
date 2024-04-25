from pathlib import Path

def relative_to_assets(pagename: str,path: str) -> Path:
    OUTPUT_PATH = Path(__file__).parent
    return OUTPUT_PATH / Path(r"assets") / Path(pagename) / Path(path)