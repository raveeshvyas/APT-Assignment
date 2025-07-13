# Root Cause Breakdown

### 1. Parallel Processing Without Global Coordination

* Multiple workers independently pick up events for processing.
* If two workers begin processing the same `event_ID` due to a timeout, scheduling race, or retry, they may both emit output.
  
**Observed evidence**:  
`worker_logs.csv` contains the same `event_id` processed by multiple workers, sometimes with overlapping `start_time`.

---

### 2. Retries After Timeout Cause Reprocessing

* Events with status = timeout are retried by the orchestrator.
* However, if the original worker finishes late and emits output, both outputs are captured.
  
**Observed evidence**:  
Some `event_id`s have:
- null `end_time` in one row
- Re-attempted by another worker
- Still appear twice*in final_output.csv

---

### 3. Lack of Deduplication or Idempotency at Output Sink

* The output writer does not check for duplicates using event_id.
* As a result, multiple versions of the same tick (same symbol and timestamp) are written.
* This leads to slight variations in price or timestamp jitter.

**Observed evidence**:  
- `final_output.csv` contains duplicate (symbol, timestamp) entries.
- Some duplicates have different price values.

