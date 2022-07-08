#Delete an EBS Snapshot

import boto3

ec2_client=boto3.client("ec2")

ec2_client.delete_snapshot(SnapshotId='snap-0f23b4c70f064104c')