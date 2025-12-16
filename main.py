from storage.datastore import DataStore
from concurrency.lock_manager import LockManager
from transaction.txn_manager import TransactionManager

ds = DataStore()
lm = LockManager()
tm = TransactionManager(ds, lm)

t1 = tm.begin()
tm.write(t1, "balance", 500)
tm.commit(t1)

print("Balance:", ds.read("balance"))
