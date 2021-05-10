# Start the application after a system reboot
#!/bin/bash

# Start the MariaDB instance
mysql.server start

# To use same meilisearch data files, change directory into 
# existing meilisearch data files location
cd /Users/satya_lalam/Desktop/clinical-codes-lookup/meilisearch

# Launch meilisearch with a max payload of 600MB (taken in bytes)
meilisearch --http-payload-size-limit '629145600'

# Set the global variable FLASK_APP to app.py file
export FLASK_APP=app.py

# Run the flask app in development mode
flask run