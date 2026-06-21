from provider_onboarding import Provider, ProviderOnboarding

def test_add_provider():
    onboarding = ProviderOnboarding()
    provider = Provider("Test Provider", "1.0", [])
    onboarding.add_provider(provider)
    assert onboarding.get_provider_info("Test Provider") == {
        "name": "Test Provider",
        "api_version": "1.0",
        "edge_cases": []
    }

def test_validate_api_compatibility():
    onboarding = ProviderOnboarding()
    provider = Provider("Test Provider", "1.0", [])
    onboarding.add_provider(provider)
    assert onboarding.validate_api_compatibility("Test Provider", "1.0") == True
    assert onboarding.validate_api_compatibility("Test Provider", "2.0") == False

def test_document_edge_cases():
    onboarding = ProviderOnboarding()
    provider = Provider("Test Provider", "1.0", [])
    onboarding.add_provider(provider)
    edge_cases = ["Case 1", "Case 2"]
    onboarding.document_edge_cases("Test Provider", edge_cases)
    assert onboarding.get_provider_info("Test Provider") == {
        "name": "Test Provider",
        "api_version": "1.0",
        "edge_cases": edge_cases
    }

def test_get_provider_info():
    onboarding = ProviderOnboarding()
    provider = Provider("Test Provider", "1.0", [])
    onboarding.add_provider(provider)
    assert onboarding.get_provider_info("Test Provider") == {
        "name": "Test Provider",
        "api_version": "1.0",
        "edge_cases": []
    }
    assert onboarding.get_provider_info("Non-existent Provider") == {}
