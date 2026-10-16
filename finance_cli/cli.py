import argparse
from decimal import Decimal
from pathlib import Path 

from finance_cli.storage import DEFAULT_DATA_FILE, load_transactions, save_transactions 
from finance_cli.transactions import create_transaction 

def build_parser() -> argparse.ArgumentParser: 
    parser = argparse.ArgumentParser(description="Track personal income and expenses")
    parser.add_argument(
        "--data-file",
        type=Path,
        default=DEFAULT_DATA_FILE,
        help="Path to the JSON file where transactions are stored"
    )
    
    commands = parser.add_subparsers(dest="command", required=True)
    
    add_parser = commands.add_parser("add", help="Add income or expense transactions")
    add_parser.add_argument("kind", choices=["income", "expense"], help="Type of transaction (income or expense)")
    add_parser.add_argument("amount", help="Positive amount of the transaction")
    add_parser.add_argument("--note", default="", help="Optional transaction note")
    add_parser.add_argument("--date", dest="transaction_date", help="Transaction date in YYYY-MM-DD format")
    
    list_parser = commands.add_parser("list", help="List saved transactions")
    list_parser.add_argument("--kind", choices=["income", "expense"], help="Filter transactions by type")
    
    commands.add_parser("summary", help="Show a summary of income and expenses")
    
    return parser

def main() -> None: 
    parser = build_parser()
    args = parser.parse_args()
    
    try: 
        transactions = load_transactions(args.data_file)
        
        if args.command == "add":
            transaction = create_transaction(
                kind=args.kind,
                amount=args.amount,
                note=args.note,
                transaction_data=args.transaction_date,
            )
            
            transactions.append(transaction)
            save_transactions(transactions, args.data_file)
            print("Transaction added successfully.")
            
        elif args.command == "list":
            matches = [
                item for item in transactions
                if args.kind is None or item.kind == args.kind
            ]
            
            if not matches:
                print("No transactions found.")

            for item in matches: 
                note = f" - {item.note}" if item.note else ""
                print(f"{item.date} {item.kind:7} {item.amount:.2f}{note}")
                
        elif args.command == "summary": 
            income = sum(
                (item.amount for item in transactions if item.kind == 'income'),
                Decimal("0"),
            )
            expense = sum(
                (item.amount for item in transactions if item.kind == 'expense'),
                Decimal("0"),
            )
            
            print(f"Income: {income:.2f}")
            print(f"Expense: {expense:.2f}")
            print(f"Balance: {income - expense:.2f}")
            
    except (OSError, ValueError) as error:
        print(f"Error: {error}")