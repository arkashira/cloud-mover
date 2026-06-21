from cloud_mover import CloudMover, HostingProvider

def test_deploy_to_primary():
    primary_provider = HostingProvider("Primary", "https://primary.com")
    secondary_provider = HostingProvider("Secondary", "https://secondary.com")
    cloud_mover = CloudMover(primary_provider, secondary_provider)
    cloud_mover.deploy_to_primary()
    assert cloud_mover.application_deployed

def test_deploy_to_secondary():
    primary_provider = HostingProvider("Primary", "https://primary.com")
    secondary_provider = HostingProvider("Secondary", "https://secondary.com")
    cloud_mover = CloudMover(primary_provider, secondary_provider)
    cloud_mover.deploy_to_primary()
    cloud_mover.deploy_to_secondary()
    assert cloud_mover.application_deployed

def test_fallback_to_secondary():
    primary_provider = HostingProvider("Primary", "https://primary.com")
    secondary_provider = HostingProvider("Secondary", "https://secondary.com")
    cloud_mover = CloudMover(primary_provider, secondary_provider)
    cloud_mover.deploy_to_primary()
    cloud_mover.fallback_to_secondary()
    assert cloud_mover.application_deployed

def test_fallback_to_secondary_without_primary_deployment():
    primary_provider = HostingProvider("Primary", "https://primary.com")
    secondary_provider = HostingProvider("Secondary", "https://secondary.com")
    cloud_mover = CloudMover(primary_provider, secondary_provider)
    cloud_mover.fallback_to_secondary()
    assert not cloud_mover.application_deployed
