import os
from jinja2 import Template

# Read GitHub provided env variables
repo_name = os.getenv('REPO_NAME')
repo_description = os.getenv('REPO_DESCRIPTION')
repo_owner = os.getenv('REPO_OWNER')
created_at = os.getenv('REPO_CREATED_AT')

# Load template
with open('readme_template.j2') as f:
    template = Template(f.read())

# Render with variables
rendered = template.render(
    repo_name=repo_name,
    repo_description=repo_description,
    repo_owner=repo_owner,
    created_at=created_at
)

# Save to README.md
with open('README.md', 'w') as f:
    f.write(rendered)

print("README.md generated successfully.")
