# ROADMAP.md – Cloud‑Mover

> **Project**: Cloud‑Mover  
> **Repo**: `arkashira/cloud-mover`  
> **Goal**: Simplify onboarding of new cloud providers with a zero‑config, API‑compatible, edge‑case‑aware workflow.

---

## 1. Vision

Cloud‑Mover turns a handful of declarative inputs into a fully‑validated, documented provider profile that can be consumed by downstream services (e.g., deployment orchestrators, billing systems, compliance engines).  
The product must:

1. **Validate** API compatibility automatically.  
2. **Document** edge cases and quirks.  
3. **Expose** a clean, versioned API for other services.  
4. **Scale** to dozens of providers with minimal manual effort.

---

## 2. MVP Milestone (Launch)

| # | Feature | Description | Deliverable | MVP‑Critical |
|---|---------|-------------|-------------|--------------|
| 1 | **Provider Model** | `Provider(name, api_version, edge_cases)` – immutable data class. | Python module `cloud_mover/provider.py` | ✔ |
| 2 | **Onboarding Engine** | `ProviderOnboarding` with `add_provider`, `validate_api_compatibility`, `document_edge_cases`, `get_provider_info`. | `cloud_mover/onboarding.py` | ✔ |
| 3 | **CLI Tool** | `cloud-mover-cli` – interactive wizard to create providers and run validations. | `scripts/cloud-mover-cli.py` | ✔ |
| 4 | **Unit Test Suite** | 100 % coverage on core logic. | `tests/` | ✔ |
| 5 | **Documentation** | README + API reference + usage examples. | `docs/` | ✔ |
| 6 | **CI Pipeline** | GitHub Actions: lint, type‑check, test, build wheel. | `.github/workflows/ci.yml` | ✔ |
| 7 | **Packaging** | PyPI distribution (wheel & source). | `setup.cfg`, `pyproject.toml` | ✔ |

> **MVP‑Critical** items are marked with a check.  
> These deliver a minimal, ship‑ready product that satisfies the core onboarding workflow and can be released to internal stakeholders for early feedback.

---

## 3. Version 1 (v1.0 – 6 months)

### 3.1 Theme: **Provider Marketplace & Discovery**

| # | Feature | Description | Owner | ETA |
|---|---------|-------------|-------|-----|
| 1 | **Provider Registry** | Central JSON/YAML store of all onboarded providers. | Backend | 1 mo |
| 2 | **Search API** | REST endpoint to query providers by name, API version, tags. | API | 1 mo |
| 3 | **Provider Tags** | Allow tagging (e.g., “compute”, “storage”, “regional”). | UI | 1 mo |
| 4 | **Marketplace UI** | Simple web UI to list providers and view details. | Frontend | 2 mo |
| 5 | **Export/Import** | CSV/JSON import of provider data for bulk onboarding. | CLI | 2 mo |

### 3.2 Theme: **Automation & CI/CD Integration**

| # | Feature | Description | Owner | ETA |
|---|---------|-------------|-------|-----|
| 1 | **GitHub Action** | `cloud-mover-onboard` action to run onboarding as part of PR checks. | DevOps | 1 mo |
| 2 | **Webhook Hook** | Notify downstream services when a provider is added/updated. | Backend | 2 mo |
| 3 | **Version Pinning** | Auto‑generate `requirements.txt` for provider SDKs. | Backend | 2 mo |
| 4 | **Health Checks** | Endpoint to verify provider SDK connectivity. | Backend | 3 mo |

### 3.3 Theme: **Edge‑Case Intelligence**

| # | Feature | Description | Owner | ETA |
|---|---------|-------------|-------|-----|
| 1 | **Edge‑Case Templates** | Pre‑defined templates for common quirks (e.g., pagination, rate‑limits). | Docs | 1 mo |
| 2 | **Auto‑Detection** | Simple heuristics to flag potential edge cases during validation. | Engine | 2 mo |
| 3 | **Edge‑Case Library** | Public repo of community‑submitted edge cases. | Community | 3 mo |

---

## 4. Version 2 (v2.0 – 12 months)

### 4.1 Theme: **Advanced Validation & Governance**

| # | Feature | Description | Owner | ETA |
|---|---------|-------------|-------|-----|
| 1 | **Schema Validation** | Validate provider API against OpenAPI/GraphQL specs. | Backend | 1 mo |
| 2 | **Compliance Checks** | Verify provider meets internal compliance (e.g., GDPR, SOC‑2). | Compliance | 2 mo |
| 3 | **Audit Trail** | Immutable log of provider onboarding events. | Backend | 3 mo |
| 4 | **Version Rollback** | Ability to revert to previous provider configuration. | Backend | 4 mo |

### 4.2 Theme: **Marketplace Enhancements**

| # | Feature | Description | Owner | ETA |
|---|---------|-------------|-------|-----|
| 1 | **Provider Ratings** | User‑generated ratings & reviews. | UI | 2 mo |
| 2 | **Marketplace Analytics** | Usage stats, popularity heatmap. | Analytics | 3 mo |
| 3 | **Search Filters** | Advanced filtering (
