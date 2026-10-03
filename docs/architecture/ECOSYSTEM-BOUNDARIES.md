# Ecosystem Boundaries and SoS Control Semantics

**Status:** ARCHITECTURAL DESIGN

## 1. The SoS is a layer, not a container

The System of Systems does not require every ecosystem to be copied into one repository.

Each ecosystem remains independently developed.

The SoS maintains the relationships between them.

This repository records those relationships and the constitutional/control semantics that govern them.

## 2. Boundary table

| System | Owns / maintains | SoS relationship |
|---|---|---|
| KCN | Intelligence, cognition, governance, security, knowledge, execution | Provides and consumes governed capabilities |
| BI | Evidence, verification, qualification machinery | Independently evaluates submitted artifacts/claims |
| MANIFEX | Engineering, integration, provenance, execution infrastructure | Supplies reconciliation and engineering lifecycle |
| KSI-Emergent | Composition experiments and emergence hypotheses | Tests cross-system capability composition |
| Sister/Twin | Independent challenge/evolution/testing | Contests primary-system assumptions and changes |
| SoS | Inter-system control, routing, coordination, lineage, reconciliation | Does not absorb system internals |
| Human authority | Constitutional authority and ratification | External to all computational components |

## 3. Control semantics

The SoS can control:
- whether an interaction is permitted;
- which capability is routed;
- which evidence path is required;
- which system version is eligible;
- whether a delegation is active;
- whether a revocation has occurred;
- whether a state is stale or requires re-verification;
- whether an unresolved conflict must escalate.

The SoS cannot turn those controls into constitutional sovereignty.

## 4. Delegated autonomy

A system may receive bounded delegated autonomy.

Delegation must have:
- defined scope;
- defined conditions;
- defined limits;
- provenance;
- revocation;
- expiration or reevaluation where applicable;
- escalation behavior.

Delegated authority is not self-expanding.

## 5. Interoperability contract

Every inter-system interface should identify at minimum:
SOURCE SYSTEM
DESTINATION SYSTEM
CAPABILITY / ARTIFACT
VERSION
AUTHORIZATION SCOPE
PROVENANCE
EVIDENCE STATE
REQUEST / RESPONSE SEMANTICS
FAILURE BEHAVIOR
REVOCATION BEHAVIOR
HUMAN-REVIEW REQUIREMENT

Transport mechanisms must not be mistaken for authority mechanisms.

## 6. System-of-Systems objective

The desired end state is a federation of independently bounded ecosystems capable of coordinated operation and continuous evolution.

The SoS is the bridge.

It is not a replacement for the ecosystems.

It is not a new sovereign.

It is not a claim that every component is already implemented or qualified.

It is the architectural layer that makes controlled cooperation possible.
