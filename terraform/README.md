# Terraform Project

This project uses Terraform to manage infrastructure as code.

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) installed on your machine.

## Installation

### Install Terraform

1. Download the appropriate package for your operating system from the [Terraform downloads page](https://www.terraform.io/downloads.html).
2. Unzip the package.
3. Move the `terraform` binary to a directory included in your system's `PATH`.

For example, on macOS:

```sh
$ brew install terraform
```

On Windows, you can use [Chocolatey](https://chocolatey.org/):

```sh
$ choco install terraform
```

On Linux, you can use a package manager like `apt`:

```sh
$ sudo apt-get update && sudo apt-get install -y terraform
```

## Usage

1. Clone the repository:

```sh
$ git clone https://github.com/seelingwong/everest-cling-project.git
$ cd your-repo/terraform
```

2. Initialize the Terraform configuration:

```sh
$ terraform init
```

3. Review the execution plan:

```sh
$ terraform plan
```

4. Apply the changes:

```sh
$ terraform apply
```

5. Destroy the infrastructure when no longer needed:

```sh
$ terraform destroy
```
