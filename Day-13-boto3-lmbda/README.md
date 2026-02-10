Day 13 — boto3 (AWS SDK for Python)

Overview
-
boto3 is the official AWS SDK for Python. It provides both high-level "resource" abstractions and low-level "client" access to AWS services. In DevOps workflows, boto3 is commonly used to automate infrastructure provisioning, configuration, backups, deployments, and operational tasks.

Key concepts
-
- **Client vs Resource**: `client` gives low-level service operations, `resource` offers higher-level object-oriented interfaces for some services (S3, EC2, etc.).
- **Sessions**: manage credentials, region and configuration using `boto3.Session()`.
- **Paginators**: handle large responses that are returned in pages.
- **Waiters**: poll for resource state transitions (e.g., instance running).

Authentication
-
Use the standard AWS credential methods: environment variables, `~/.aws/credentials`, or IAM roles when running on EC2/ECS. Example env vars: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`.

DevOps use-cases
-
- Automated infrastructure lifecycle (create/start/stop/terminate EC2 instances)
- Storage management and backups (S3 uploads, lifecycle policies, object inventories)
- IAM automation (provision users/roles and attach policies)
- CI/CD integration (upload build artifacts to S3, trigger Lambda functions)
- Monitoring and remediation (describe resources, gather metrics, auto-scale)

Example files in this folder
-
- [s3_examples.py](s3_examples.py) — common S3 operations (list, upload, download)
- [ec2_examples.py](ec2_examples.py) — create/list/start/stop EC2 instances
- [iam_examples.py](iam_examples.py) — simple IAM user operations
- [requirements.txt](requirements.txt) — dependencies

Best practices
-
- Least-privilege IAM policies for automation scripts.
- Avoid hard-coding credentials; use roles or env vars.
- Use retries and exponential backoff for API calls.
- Use paginators for APIs that may return large lists.

Quick start
-
1. Install dependencies:

	pip install -r requirements.txt

2. Configure credentials (one of):

	- `aws configure`
	- set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` env vars

3. Run the example scripts (edit parameters in the `if __name__ == '__main__'` sections first).

Notes
-
These example scripts are minimal and meant for learning and integration into larger automation pipelines. Always test scripts in a safe AWS account or sandbox.

