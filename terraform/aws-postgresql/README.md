# AWS RD People Matcher Terraform Setup

This README provides instructions on how to set up and execute Terraform for [AWS PostgreSQL](https://aws.amazon.com/rds/postgresql/).

## Prerequisites

Before you begin, ensure you have the following installed:

- [Terraform](https://www.terraform.io/downloads.html) (v0.12 or later)
- [AWS CLI](https://aws.amazon.com/cli/) (v2 or later)

Setup AWS access. Prefer use set AWS environment variables:
```sh
export AWS_ACCESS_KEY_ID="your key id"
export AWS_SECRET_ACCESS_KEY="your secret access key"
export AWS_SESSION_TOKEN="your session token"
```

## Setup

1. **Clone the repository and change direcotry to terraform/aws-postgresql**
2. **Initialize Terraform:**

    ```sh
    terraform init
    ```

3. **Review and edit variables:**

    Edit the `variables.tf` file to set the necessary variables for your AWS environment.

4. **Plan the Terraform deployment:**

    ```sh
    terraform plan
    ```

    Review the plan output to ensure it matches your expectations.

5. **Apply the Terraform deployment:**

    ```sh
    terraform apply
    ```

    Confirm the apply step when prompted.

## Cleanup

To destroy the resources created by Terraform, run:

```sh
terraform destroy
```

## Additional Information

For more details on Terraform commands and configurations, refer to the [Terraform documentation](https://www.terraform.io/docs/).

## Important Note

**Warning:** This database will be open to the public. Please ensure you understand the security implications and take necessary precautions to protect your data. Be careful when configuring security groups and other access controls.