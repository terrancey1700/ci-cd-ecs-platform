terraform {
  backend "s3" {
    bucket         = "empowered-ecs-platform-tf-state-1"
    key            = "global/dev/terraform.tfstate"
    region         = "us-east-2"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
