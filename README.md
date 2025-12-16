# MiniRelDB – Transactional Storage Engine (Python)

MiniRelDB is a database kernel project implementing ACID-compliant
transaction management using write-ahead logging and two-phase locking.

## Features
- BEGIN / COMMIT / ROLLBACK
- Write-Ahead Logging (WAL)
- Rollback & crash recovery
- Two-Phase Locking (2PL)
- Thread-safe storage layer

## Architecture
Client → Transaction Manager → Lock Manager → Data Store → WAL → Recovery

## Why this project
This project focuses on database internals, concurrency, and reliability,
demonstrating system-level engineering skills beyond CRUD applications.
