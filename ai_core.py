import os
import yaml

# Load configuration
config_path = "config.yaml"
with open(config_path, "r") as file:
    config = yaml.safe_load(file)

print(f"Starting AI Core: {config['ai_model']}")
