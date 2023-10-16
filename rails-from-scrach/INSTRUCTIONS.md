# Starting a rails project from scratch

```shell
# Get inside the container
docker compose run --no-deps --rm web bash

# Install rails
gem install rails

# Check the version
rails --version

# Create a new project
rails new . --force --database=postgresql

# Exit the container
exit

# List the files
ll -lah

# Fix the permissions (do not forget the dot at the end)
sudo chown -R $USER:$USER .

# Build the container
docker compose build

# Start the container
docker compose up
```