# Starting a rails project from scratch

```shell
# Get inside the container
docker compose run web bash

# Install rails
gem install rails

# Check the version
rails --version

# Create a new project
rails new . --force --database=postgresql

# Exit the container
exit

# Fix the permissions
sudo chown -R $USER:$USER .

# Build the container
docker compose build

# Start the container
docker compose up
```