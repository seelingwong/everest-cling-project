variable "aws_region" {
  default = "ap-southeast-2"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  default = "my-key-pair"
}

variable "github_key_name" {
  default = "github_deploy_key"
}

variable "github_repo_url" {
  default = "git@github.com:everest-engineering/rd_people_matcher.git"
}
