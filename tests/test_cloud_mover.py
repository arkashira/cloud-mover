from cloud_mover import CloudMover, Provider
import pytest

def test_add_provider():
    cloud_mover = CloudMover()
    cloud_mover.add_provider('provider1', {'username': 'user1', 'password': 'pass1'})
    assert cloud_mover.get_provider('provider1').credentials == {'username': 'user1', 'password': 'pass1'}

def test_initiate_failover():
    cloud_mover = CloudMover()
    cloud_mover.add_provider('provider1', {'username': 'user1', 'password': 'pass1'})
    assert cloud_mover.initiate_failover('provider1')
    assert len(cloud_mover.get_failover_log()) == 1

def test_prioritize_failover():
    cloud_mover = CloudMover()
    assert cloud_mover.prioritize_failover()

def test_log_failover():
    cloud_mover = CloudMover()
    cloud_mover.log_failover('provider1')
    assert len(cloud_mover.get_failover_log()) == 1

def test_get_failover_log():
    cloud_mover = CloudMover()
    cloud_mover.log_failover('provider1')
    log = cloud_mover.get_failover_log()
    assert len(log) == 1
    assert 'timestamp' in log[0]
    assert 'provider' in log[0]

def test_initiate_failover_invalid_provider():
    cloud_mover = CloudMover()
    assert not cloud_mover.initiate_failover('invalid_provider')
