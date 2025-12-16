from enum import Enum, auto

class TxnState(Enum):
    ACTIVE = auto()
    COMMITTED = auto()
    ABORTED = auto()

class Transaction:
    def __init__(self, txn_id: int):
        self.txn_id = txn_id
        self.state = TxnState.ACTIVE
        self.write_set = {}
