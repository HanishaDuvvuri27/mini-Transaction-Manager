class RecoveryManager:
    def __init__(self, datastore, wal):
        self.datastore = datastore
        self.wal = wal

    def recover(self):
        logs = self.wal.read_all()
        committed = set(rec["txn_id"] for rec in logs)

        for rec in logs:
            if rec["txn_id"] in committed:
                self.datastore.write(rec["key"], rec["new"])
