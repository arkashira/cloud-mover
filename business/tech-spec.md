# tech-spec.md – Cloud‑Mover v1

---

## 1. Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **Runtime** | **Node.js 20.x** (LTS) | Mature ecosystem, fast I/O, native support for async/await, good for CLI/HTTP services. |
| **Framework** | **Fastify 5.x** | Minimal, high‑performance HTTP framework with built‑in schema validation and plugin system. |
| **CLI** | **oclif 4.x** | Structured CLI framework, auto‑generates help, supports plugins, ideal for multi‑platform deployer. |
| **Container** | **Docker** | Consistent runtime across dev/CI/Prod. |
| **Language** | **TypeScript 5.x** | Strong typing, better DX, auto‑generated docs. |
| **Package Manager** | **pnpm** | Faster installs, strict lockfile. |
| **Testing** | **Jest + ts-jest** | Snapshot + unit tests, coverage. |
| **Linting** | **ESLint + Prettier** | Code quality. |
| **Documentation** | **TypeDoc** | Generate API docs from TS. |

---

## 2. Hosting

| Tier | Platform | Notes |
|------|----------|-------|
| **Free‑Tier‑First** | **GitHub Actions** | CI/CD, free minutes, self‑hosted runner optional. |
| | **Fly.io** | Free tier for small apps, global edge. |
| | **Render** | Free static sites & web services. |
| **Paid** | **AWS (ECS/Fargate)** | Enterprise‑grade, IAM, VPC. |
| | **Azure Container Apps** | Serverless containers, easy scaling. |
| | **Google Cloud Run** | Fully managed, pay‑per‑second. |
| | **DigitalOcean App Platform** | Simple, cost‑effective. |
| | **Vercel** | Edge‑first, great for static + serverless. |

> **Why**: The core value is *platform‑agnosticism*. The product must run on any of the above without code changes. The free tier list ensures early adopters can test without cost.

---

## 3. Data Model

| Collection/Table | Key Fields | Description |
|-------------------|------------|-------------|
| **`projects`** | `id` (UUID, PK) <br> `name` <br> `owner_id` <br> `created_at` <br> `updated_at` | Metadata for each deployment project. |
| **`platforms`** | `id` (UUID, PK) <br> `name` <br> `type` (e.g., `docker`, `k8s`, `fly`, `render`) <br> `config_schema` (JSON) | Supported hosting platforms. |
| **`deployments`** | `id` (UUID, PK) <br> `project_id` (FK) <br> `platform_id` (FK) <br> `status` (`queued`, `running`, `succeeded`, `failed`) <br> `started_at` <br> `finished_at` <br> `log_url` | Historical deployment runs. |
| **`secrets`** | `id` (UUID, PK) <br> `project_id` (FK) <br> `name` <br> `value` (encrypted) | Sensitive data per project. |
| **`users`** | `id` (UUID, PK) <br> `email` <br> `hashed_password` | Auth users. |
| **`api_keys`** | `id` (UUID, PK) <br> `user_id` (FK) <br> `key` (hashed) <br> `scopes` | API key auth. |

> **Storage**: PostgreSQL 15 (cloud provider‑agnostic, can run locally or in any cloud). All secrets encrypted at rest with a master key stored in the platform’s KMS (AWS KMS / Azure Key Vault / GCP KMS).

---

## 4. API Surface

| Method | Path | Purpose |
|--------|------|---------|
| **POST** | `/v1/projects` | Create new project. |
| **GET** | `/v1/projects/{id}` | Retrieve project details. |
| **PATCH** | `/v1/projects/{id}` | Update project metadata. |
| **DELETE** | `/v1/projects/{id}` | Delete project & all related data. |
| **GET** | `/v1/platforms` | List supported platforms. |
| **POST** | `/v1/deployments` | Trigger a deployment. Body: `{project_id, platform_id, config}` |
| **GET** | `/v1/deployments/{id}` | Get deployment status & logs. |
| **GET** | `/v1/deployments?project_id=...` | List deployments for a project. |
| **POST** | `/v1/secrets` | Store a secret. |
| **GET** | `/v1/secrets/{id}` | Retrieve secret (only metadata). |
| **DELETE** | `/v1/secrets/{id}` | Delete secret. |
| **POST** | `/v1/auth/login` | Email/password login → JWT. |
| **GET** | `/v1/auth/me` | Current user info. |

> **Auth**: All endpoints except `/auth/*` require a bearer JWT or API key. JWTs signed with RS256; keys rotated quarterly.

---

## 5. Security Model

| Layer | Mechanism | Details |
|-------|-----------|---------|
| **Auth** | **JWT + API Keys** | JWTs issued on login, short‑lived (15 min), refresh token (7 days). API keys stored hashed (bcrypt). |
| **Secrets** | **Encrypted at rest** | AES‑256‑GCM, master key from KMS. |
| **Transport** | **TLS 1.3** | All traffic HTTPS. |
| **IAM** | **Role‑based** | `admin`, `developer`, `viewer`. Enforced via middleware. |
| **Rate Limiting** | **IP + key** | 100 req/min per key. |
| **Audit** | **Event log** | Every CRUD operation logged to `audit_logs` table. |
| **Secrets in CLI** | **`.env` + `--secret` flag** | CLI never logs secret values. |

---

## 6. Observability

| Type | Tool | Purpose |
|------|------|---------|
| **Logs** | **Structured JSON logs** (winston) | Centralized via CloudWatch / Stackdriver / Azure Monitor. |
| **Metrics** | **Prometheus** (exporter) | Deployment counts, success rate, latency. |
| **Tracing** | **OpenTelemetry** | End‑to‑end tracing for deployment pipeline. |
| **Health Checks** | `/healthz` | Liveness & readiness probes. |
| **Alerting** | **PagerDuty / Opsgenie** | Trigger on deployment failures > 5% in 15 min. |

---

## 7. Build / CI

| Stage | Tool | Steps |
|-------|------|-------|
| **Lint** | ESLint | `pnpm lint` |
| **Test** | Jest | `pnpm test --coverage` |
| **Build** | tsc | `pnpm build` |
| **Docker** | Dockerfile | `docker build -t cloud-mover:latest .` |
| **Publish** | GitHub Packages | `pnpm publish` (semver bump) |
| **CI** | GitHub Actions | - `node:20` matrix <br> - Cache pnpm <br> - Run lint, test, build <br> - Push Docker image to ghcr.io |
| **CD** | GitHub Actions | Deploy Docker image to Fly.io / Render (free tier) on `main` merge. |
| **Versioning** | Conventional Commits | Auto‑bump via `semantic-release`. |

> **Secrets in CI**: `GH_TOKEN`, `DOCKERHUB_TOKEN`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, etc., stored in GitHub Secrets.

---

### End of tech‑spec.md
