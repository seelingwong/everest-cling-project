resource "aws_db_instance" "postgres" {
  allocated_storage    = 20 # Free tier allows up to 20GB
  storage_type        = "gp2"
  engine             = "postgres"
  engine_version     = var.postgres_version
  instance_class     = "db.t4g.micro"
  identifier         = "my-postgres-db"
  username          = "adminuser"
  password          = var.postgres_password
  publicly_accessible = true
  vpc_security_group_ids = [aws_security_group.postgres_sg.id]
  skip_final_snapshot = true
  backup_retention_period = 0
}

resource "aws_security_group" "postgres_sg" {
  name_prefix = "postgres-sg"
  
  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allow connections from any IP (consider restricting this for security)
  }
}
