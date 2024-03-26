#!/bin/sh

cat <<EOF >> .env
SECRET_KEY=$SECRET_KEY
DB_NAME=$POSTGRES_DB
DB_USER=$POSTGRES_USER
DB_PASS=$POSTGRES_PASSWORD
DB_HOST=$POSTGRES_HOST
DJANGO_DEBUG=True
EOF

echo "alias fly='flyctl'" >> ~/.bashrc
echo "alias fly='flyctl'" >> ~/.zshrc
