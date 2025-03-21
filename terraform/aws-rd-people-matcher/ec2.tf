resource "aws_instance" "web" {
  ami                    = "ami-03f052ebc3f436d52" # redhat
  instance_type          = var.instance_type
  key_name               = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  root_block_device {
    volume_size = 30 # 30GB Storage
  }

  iam_instance_profile = "PeopleMatcherReadSecretsManagerRole"  # Attach IAM Role

  user_data = <<-EOF
        #!/bin/bash
        exec > /var/log/user-data.log 2>&1  # Capture logs for debugging
        set -x  # Enable debug mode

        echo "Updating system..."
        sudo dnf update -y

        echo "Installing required dependencies..."
        sudo dnf install -y git python3.12 python3.12-devel

        echo "Setting up virtual environment..."
        python3.12 -m venv /home/ec2-user/venv

        echo "Activating virtual environment..."
        source /home/ec2-user/venv/bin/activate

        echo "Installing Git and cloning repository..."
        ssh-keyscan github.com >> ~/.ssh/known_hosts
        echo "${file("github_deploy_key")}" > ~/.ssh/id_rsa
        chmod 600 ~/.ssh/id_rsa
        cd /home/ec2-user
        git clone ${var.github_repo_url}

        echo "Creating .env file..."
        cat <<EOT > /home/ec2-user/rd_people_matcher/.env
        DEPLOYMENT_ENV=production
        PINECONE_INDEX_NAME=precise-targeted-data
        EOT

        echo "Installing Python dependencies..."
        pip install --upgrade pip
        pip install -r /home/ec2-user/rd_people_matcher/requirements.txt

        echo "Running Streamlit application..."
        cd /home/ec2-user/rd_people_matcher
        nohup streamlit run app/main.py --server.port 8501 --server.headless true > /home/ec2-user/streamlit.log 2>&1 &

        echo "User data script execution completed!"
    EOF

  user_data_replace_on_change = true
  tags = {
    Name = "Terraform-EC2-01"
  }
}
