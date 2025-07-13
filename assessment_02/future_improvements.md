# 1. Idempotent Event Processing
* We can keep a track of the processed `event_id` values.
* Before writing the event to the file, check if the `event_id` has already been processed to avoid emitting duplicates.

# 2. Strong Keys
* We can use `event_id` as a **partitioning key**
* This will ensure that same events will be processed in the same partition, preventing multiple workers from simultaneously handling the same event

# 3. Distributed Locks
* We can use a distributed lock manager like **Zookeeper** to ensure that only one worker can access a given event at a given time.

# 4. Exactly-once semantics
* Some frameworks like Kafka support Exactly-Once Semantics by using **Checkpoints** and **Transactional Writes**.

# 5. TTL Windows
* We can introduce **Time-to-Live** windows for events
* Events older than these windows are discarded to avoid introducing duplicate data after the original stream.

