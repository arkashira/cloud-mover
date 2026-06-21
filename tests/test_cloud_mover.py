import pytest
from cloud_mover import CloudMover, MigrationStatus

def test_get_providers():
    cloud_mover = CloudMover()
    assert cloud_mover.get_providers() == ["aws", "gcp", "azure"]

def test_migrate_success():
    cloud_mover = CloudMover()
    job_id = cloud_mover.migrate("aws", "gcp")
    assert cloud_mover.get_job_status(job_id) == MigrationStatus.SUCCESS

def test_migrate_failure():
    cloud_mover = CloudMover()
    job_id = cloud_mover.migrate("aws", "aws")
    assert cloud_mover.get_job_status(job_id) == MigrationStatus.FAILURE

def test_get_job_status():
    cloud_mover = CloudMover()
    job_id = cloud_mover.migrate("aws", "gcp")
    assert cloud_mover.get_job_status(job_id) == MigrationStatus.SUCCESS

def test_get_logs_success():
    cloud_mover = CloudMover()
    job_id = cloud_mover.migrate("aws", "gcp")
    assert cloud_mover.get_logs(job_id) == "Migration successful"

def test_get_logs_failure():
    cloud_mover = CloudMover()
    job_id = cloud_mover.migrate("aws", "aws")
    assert cloud_mover.get_logs(job_id) == "Migration failed"

def test_get_job_status_non_existent_job():
    cloud_mover = CloudMover()
    assert cloud_mover.get_job_status("non_existent_job") == MigrationStatus.FAILURE
