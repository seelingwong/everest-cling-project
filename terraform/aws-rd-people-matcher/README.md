# AWS RD People Matcher Terraform Setup

This README provides instructions on how to set up and execute Terraform for the AWS RD People Matcher project.
For more information about RD People Matcher project please refer [github](https://github.com/everest-engineering/rd_people_matcher.git)

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

1. **Clone the repository and change direcotry to terraform/aws-rd-people-matcher**
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
    When first time execute the instance will created but the application will deploy fail. Because we haven't add the deploy keys into Github. Please process step 6.

6. **(Optional) Apply when first time generate key file:** 
    1. ***Setup Github deploy keys:***
        1. Go to your GitHub repo → Settings → Deploy Keys.
        2. Click "Add deploy key".
        3. Paste the contents of github_deploy_key.pub and enable "Allow read access".

    2. ***Update my-key-pair.pem permission:**
        ```sh
        chmod 400 "my-key-pair.pem"
        ```
    
    3. ***Continue Step 5***

## Verify
1. **SSH into instance and check the log:**
    ```sh
    ssh -i my-key-pair.pem ec2-user@your-ec2-public-ip

    ## Check the log for terraform script
    cat /var/log/user-data.log

    ## Check the log for application
    cat /home/ec2-user/streamlit.log
    ```

2. **Verify application:**
    Open browser with url: http:your-ec2-public-ip:8501

## Cleanup

To destroy the resources created by Terraform, run:

```sh
terraform destroy
```

## Additional Information

For more details on Terraform commands and configurations, refer to the [Terraform documentation](https://www.terraform.io/docs/).

## Important Note

**Warning:** This application will be open to the public. Please ensure you understand the security implications and take necessary precautions to protect your data. Be careful when configuring security groups and other access controls.