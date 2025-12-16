def test_atomicity():
    from storage.datastore import DataStore
    from concurrency.lock_manager import LockManager
    from transaction.txn_manager import TransactionManager

    ds = DataStore()
    tm = TransactionManager(ds, LockManager())

    t = tm.begin()
    tm.write(t, "x", 10)
    tm.rollback(t)

    assert ds.read("x") is None
