# Development

## Location

```bash
cd /home/erpnext/frappe-bench/frontend/printechs-web
```

## Node

Bench default Node may be older than Next.js requires. Use nvm for this frontend only:

```bash
source ~/.nvm/nvm.sh
nvm use 20
```

## Commands

```bash
npm run dev      # http://localhost:3000/newwebsite
npm run lint
npm run build
npm run start -- -H 127.0.0.1 -p 3000
```

## Demo URL (Nginx)

```text
https://demo.printechs.com/newwebsite
```

- Next.js `basePath` is `/newwebsite` in `next.config.mjs`
- Nginx location is only on the **demo** server block
- Does not affect `site1.local` / live `printechs.com`
- Demo remains `noindex, nofollow`

## Auto-start (Supervisor)

The website process is managed like ERPNext:

```bash
supervisorctl status printechs-web
supervisorctl restart printechs-web
supervisorctl stop printechs-web
supervisorctl start printechs-web
```

- Autostart / autorestart enabled
- Logs: `logs/printechs-web.log` and `logs/printechs-web.error.log`
- Start script: `frontend/printechs-web/scripts/start-production.sh`
- Supervisor snippet backup: `config/printechs-web-supervisor.conf`

After code changes:

```bash
source ~/.nvm/nvm.sh && nvm use 20
cd ~/frappe-bench/frontend/printechs-web
npm run build
supervisorctl restart printechs-web
```

If `bench setup supervisor` regenerates `config/supervisor.conf`, re-append from `config/printechs-web-supervisor.conf` and run `supervisorctl reread && supervisorctl update`.

## Environment

Copy `.env.example` to `.env.local` if needed. Never commit secrets.

## Frappe relationship

- Frappe app shell: `apps/printechs_digital`
- Installed only on site `demo`
- No DocTypes / APIs in frontend phases F1–F2

## Homepage review widths

```text
390px  mobile
768px  tablet
1440px desktop
```
