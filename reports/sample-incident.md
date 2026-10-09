# Incident Report

## Incident

Elevated application latency and HTTP 500 errors.

## Detection

AIOps log analysis detected repeated database timeout patterns.

## Symptoms

- HTTP 500 responses
- 5000ms latency
- Database timeout errors

## Root Cause

Simulated database connectivity/timeout failure.

## Investigation

1. Reviewed application logs.
2. Correlated timeout and HTTP 500 patterns.
3. Checked Kubernetes workload health.
4. Reviewed monitoring metrics.

## Remediation

Restore database connectivity and validate timeout configuration.

## Verification

Application returned to normal request latency and error rate.

## SRE Metrics

MTTD: measured during simulation.

MTTR: measured from detection until recovery.
