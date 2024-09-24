FROM mysql:8.0

# Enable file loading and set the secure-file-priv to the correct directory
CMD ["mysqld", "--secure-file-priv=/docker-entrypoint-initdb.d", "--local-infile=1"]


# Set environment variables for MySQL (change as necessary)
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=basketball_db
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=adminpassword

# Create a directory to hold the SQL scripts and data
RUN mkdir -p /docker-entrypoint-initdb.d

# Copy the SQL scripts to create schema and load data
COPY ./init.sql /docker-entrypoint-initdb.d/
COPY ./awards_players.csv /docker-entrypoint-initdb.d/
COPY ./coaches.csv /docker-entrypoint-initdb.d/
COPY ./players.csv /docker-entrypoint-initdb.d/
COPY ./players_teams.csv /docker-entrypoint-initdb.d/
COPY ./series_post.csv /docker-entrypoint-initdb.d/
COPY ./teams.csv /docker-entrypoint-initdb.d/
COPY ./teams_post.csv /docker-entrypoint-initdb.d/

