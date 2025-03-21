output "ec2_public_ip" {
  value = aws_instance.web.public_ip
}

output "ssh_command" {
  value = "ssh -i ${var.key_name}.pem ec2-user@${aws_instance.web.public_ip}"
}
