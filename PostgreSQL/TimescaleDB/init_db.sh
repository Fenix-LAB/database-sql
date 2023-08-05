#!/bin/bash

# Function to check if the database exists
database_exists() {
    psql -U postgres -lqt | cut -d \| -f 1 | grep -wq "$1"
}

# Check if the database exists
if database_exists "db_scrap_detector"; then
    echo "Database 'db_scrap_detector' already exists."
else
    echo "Creating database 'db_scrap_detector'..."
    psql -U postgres -c "CREATE DATABASE db_scrap_detector;"
    echo "Database 'db_scrap_detector' created."
fi