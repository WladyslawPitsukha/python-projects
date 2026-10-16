import json 
from pathlib import Path
from finance_cli.transactions import Transaction

DEFAULT_DATA_FILE = Path.home() / ".finance_cli" / "transactions.json"

def load_transactions(path: Path = DEFAULT_DATA_FILE) -> list[Transaction]: 
    if not path.exists():
        return []
    
    try: 
        data = json.loads(path.read_text(encoding="utf-8"))
        
        if not isinstance(data, list):
            raise ValueError("Transactions storag must contain a JSON list.")
        return [Transaction.from_dict(item) for item in data]
    
    except (json.JSONDecodeError, TypeError) as error:
        raise ValueError("Could not load transaction data from {}".format(path))
    
    
def save_transactions(
    transactions: list[Transaction],
    path: Path = DEFAULT_DATA_FILE
) -> None:
    path.parent.mkdir(parents = True, exist_ok = True)
    data = [transaction.to_dict() for transaction in transactions]
    path.write_text(json.dumps(data, indent = 2), encoding = "utf-8")