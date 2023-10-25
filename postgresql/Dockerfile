# Menggunakan image PostgreSQL resmi dari Docker Hub
FROM postgres:latest

# Menetapkan variabel lingkungan
ENV POSTGRES_USER=alex
ENV POSTGRES_PASSWORD=alex2323
ENV PGDATA=/var/lib/postgresql/data

# Menetapkan port default yang digunakan oleh PostgreSQL
EXPOSE 5432

# Memperbarui user yang berjalan sebagai PostgreSQL
USER postgres

# Menyalin data dari volume
VOLUME /var/lib/postgresql/data
