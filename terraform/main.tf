variable "base_url" {
  type = string
}

variable "owner" {
  type = string
}

variable "app_id" {
  type = string
}

variable "installation_id" {
  type = string
}

variable "pem_file_path" {
  type = string
}

variable "repo_name" {
  type = string
}

provider "github" {
  base_url = var.base_url
  owner    = var.owner
  app_auth {
    id              = var.app_id
    installation_id = var.installation_id
    pem_file        = file(var.pem_file_path)
  }
}

terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "5.23.0"
    }
  }
}

data "github_repository" "gh_repo" {
  full_name = var.repo_name
}

output "gh_repo" {
  value = data.github_repository.gh_repo
}

