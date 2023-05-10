"""A GitHub Python Pulumi program"""

import pulumi
import pulumi_github as github


config = pulumi.Config()

with open(config.get('pem_file_path'), 'r') as f:
    pem_file_content = f.read()

github_provider = github.Provider(
    "github-provider",
    base_url=config.get('base_url'),
    owner=config.get('owner'),
    app_auth=github.ProviderAppAuthArgs(
        id=config.get('app_id'),
        installation_id=config.get('installation_id'),
        pem_file=pem_file_content,
    )
)


repo = github.get_repository(full_name=config.get('repo_name'), opts=pulumi.InvokeOptions(provider=github_provider))

pulumi.export("gh_repo", repo)