from transaction.transaction import Transaction, TxnState
from logging.wal import WriteAheadLog

class TransactionManager:
    def __init__(self, datastore, lock_manager):
        self.datastore = datastore
        self.lock_manager = lock_manager
        self.wal = WriteAheadLog()
        self.txn_id_counter = 0

    def begin(self):
        self.txn_id_counter += 1
        return Transaction(self.txn_id_counter)

    def read(self, txn, key):
        return self.datastore.read(key)

    def write(self, txn, key, value):
        self.lock_manager.acquire(key)
        old_value = self.datastore.read(key)

        self.wal.append({
            "txn_id": txn.txn_id,
            "key": key,
            "old": old_value,
            "new": value
        })

        txn.write_set[key] = value

    def commit(self, txn):
        for key, value in txn.write_set.items():
            self.datastore.write(key, value)
            self.lock_manager.release(key)
        txn.state = TxnState.COMMITTED

    def rollback(self, txn):
        logs = reversed(self.wal.read_all())
        for rec in logs:
            if rec["txn_id"] == txn.txn_id:
                if rec["old"] is None:
                    self.datastore.delete(rec["key"])
                else:
                    self.datastore.write(rec["key"], rec["old"])
                self.lock_manager.release(rec["key"])
        txn.state = TxnState.ABORTED
