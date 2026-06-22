# REQUIREMENTS.md  

**Project:** cloud‑mover  
**Owner:** Axentx OS – Provider Onboarding Team  
**Author:** Senior Product/Engineering Lead  
**Date:** 2026‑06‑22  

---  

## 1. Introduction  

cloud‑mover is a lightweight Python library that enables Axentx to onboard third‑party cloud‑service providers (e.g., storage, compute, networking) with minimal configuration. The library abstracts provider‑specific API version checks, edge‑case documentation, and runtime discovery of provider metadata.  

The goal of this document is to capture **all** functional and non‑functional requirements that must be satisfied before the first production release (v1.0.0). Requirements are written to be **testable**, **traceable**, and **shippable**.  

---  

## 2. Scope  

| In‑Scope | Out‑of‑Scope |
|----------|--------------|
| • Definition of a `Provider` object (name, API version, edge‑case list).<br>• Registration of providers via `ProviderOnboarding.add_provider`. <br>• Validation of API compatibility (`validate_api_compatibility`). <br>• Documentation of edge cases (`document_edge_cases`). <br>• Retrieval of provider metadata (`get_provider_info`). <br>• Persistence of provider registry to a JSON file. <br>• CLI wrapper (`cloud-mover-cli`). | • Actual communication with provider APIs (cloud‑mover only validates compatibility). <br>• UI/UX beyond the CLI. <br>• Provider credential management. <br>• Billing or usage metering. |

---  

## 3. Definitions  

| Term | Meaning |
|------|---------|
| **Provider** | A third‑party cloud service offering identified by a unique `name` and supporting a specific `api_version`. |
| **Edge case** | Any known limitation, deviation, or special handling required for a provider (e.g., rate‑limit, unsupported feature). |
| **Registry** | The in‑memory collection of `Provider` objects managed by `ProviderOnboarding`. |
| **Persistence Store** | A JSON file (`providers.json`) located in the user’s config directory (`$XDG_CONFIG_HOME/cloud-mover/`). |
| **CLI** | Command‑line interface exposing the core onboarding functions. |

---  

## 4. Functional Requirements  

| ID | Requirement | Rationale / Acceptance Test |
|----|-------------|------------------------------|
| **FR‑1** | The library shall expose a `Provider` class with immutable attributes: `name` (string, required), `api_version` (semantic version string, required), `edge_cases` (list of strings, optional, default `[]`). | Unit test: `Provider('aws', '2023‑01‑01').name == 'aws'`. |
| **FR‑2** | `ProviderOnboarding` shall be a singleton‑style manager that maintains a registry of providers. | Integration test: two instances of `ProviderOnboarding()` reference the same internal registry. |
| **FR‑3** | `add_provider(provider: Provider) -> None` shall add a provider to the registry **iff** the provider name is unique. Duplicate names raise `ProviderAlreadyExistsError`. | Test adding the same provider twice results in exception. |
| **FR‑4** | `validate_api_compatibility(provider_name: str, api_version: str) -> bool` shall return `True` when the supplied `api_version` matches the stored version for the named provider, otherwise `False`. | Test with matching and mismatching versions. |
| **FR‑5** | `document_edge_cases(provider_name: str, edge_cases: List[str]) -> None` shall replace the existing edge‑case list for the provider with the supplied list. | Verify that after call, `get_provider_info` returns the new list. |
| **FR‑6** | `get_provider_info(provider_name: str) -> Provider` shall return a deep copy of the stored `Provider` object. If the provider does not exist, raise `ProviderNotFoundError`. | Test retrieval of known provider and exception for unknown name. |
| **FR‑7** | The registry shall be persisted to `providers.json` after each successful mutation (`add_provider`, `document_edge_cases`). Persistence must be atomic (write‑temp‑rename). | Simulate crash during write; file remains valid JSON. |
| **FR‑8** | On library import, if `providers.json` exists, it shall be loaded automatically; otherwise an empty registry is created. | Verify that a previously persisted provider is available after a fresh interpreter start. |
| **FR‑9** | The library shall expose a CLI (`cloud-mover-cli`) with sub‑commands: `add`, `validate`, `edgecases`, `info`, `list`. Each sub‑command maps to the corresponding API call. | End‑to‑end test: `cloud-mover-cli add --name azure --api-version 2024.02`. |
| **FR‑10** | The CLI shall output human‑readable JSON for `info` and `list`, and exit with status `0` on success, non‑zero on error. | Verify exit codes and output format. |
| **FR‑11** | All public functions shall raise typed exceptions (`ProviderAlreadyExistsError`, `ProviderNotFoundError`, `InvalidAPIVersionError`). | Unit tests assert exception types. |
| **FR‑12** | The library shall provide a `__version__` attribute following PEP 440 (`major.minor.patch`). | `import cloud_mover; assert cloud_mover.__version__ == '1.0.0'`. |
| **FR‑13
