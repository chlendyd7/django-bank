python -c "import secrets; print(secrets.token_urlsafe(38))"

mkdir -p .envs && touch .envs/.env.local && touch .envs/.env.example
mkdir .envs
echo. > .envs\.env.local
echo. > .envs\.env.example