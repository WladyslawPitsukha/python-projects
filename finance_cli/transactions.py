from dataclasses import dataclass 
from datetime import date 
from decimal import Decimal, InvalidOperation
from uuid import uuid4

@dataclass 
class Transaction: 
    id: str
    date: str
    kind: str
    amount: Decimal
    note: str = ""
    
    def __post_init__(self):
        if self.kind not in {"income", "expense"}:
            raise ValueError("Transaction type must be income or expense")
        if not self.amount.is_finite() or self.amount <= 0:
            raise ValueError("Amount must be a positive number")
        
        try: 
            date.fromisoformat(self.date)
        
        except ValueError as error:
            raise ValueError("Date must be in YYYY-MM-DD format")
        
        
    def to_dict(self) -> dict[str, str]:
        return {
            "id": self.id,
            "date": self.date,
            "kind": self.kind,
            "amount": str(self.amount),
            "note": self.note,
        }
        
    @classmethod
    def from_dict(cls, data: dict[str, str]) -> "Transaction":
        try: 
            return cls(
                id = data['id'],
                date = data['date'],
                kind = data['kind'],
                amount = Decimal(data['amount']),
                note = data.get('note', ""),
            )
        except (KeyError, InvalidOperation) as error:
            raise ValueError("Invalid data for creating a Transaction")
        
def create_transaction(
    kind: str,
    amount: str,
    note: str = "",
    transaction_data: str | None = None,
) -> Transaction:
    try: 
        parsed_amount = Decimal(amount)
    except InvalidOperation as error:
        raise ValueError("Invalid amount format")
    
    return Transaction(
        id = str(uuid4()),
        date = transaction_data or date.today().isoformat(),
        kind = kind,
        amount = parsed_amount,
        note = note,
    )