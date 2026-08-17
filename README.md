### Printechs Digital

Printechs Digital Experience Platform and B2B Website Content Management

This repository contains:

- `printechs_digital/` — Frappe app (CMS / ERPNext integration foundation)
- `frontend/printechs-web/` — Next.js corporate website (`/newwebsite`)
- `printechs_digital/Document/` — project specifications and phase documents

### Frontend (Next.js website)

```bash
cd frontend/printechs-web
npm install
npm run dev
```

Production build and deploy notes are in `frontend/printechs-web/docs/`.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app printechs_digital
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/printechs_digital
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
