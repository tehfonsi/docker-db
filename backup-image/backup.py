import os

print("Create database backup...")
os.system("docker exec mariadb sh -c 'exec mysqldump --all-databases -uroot -p\"$MARIADB_ROOT_PASSWORD\"' > /backup/all-databases.sql")
print("Database backup created!")