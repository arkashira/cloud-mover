# Provider Onboarding
A Python project for onboarding new providers with minimal configuration.

## Usage
1. Create a new provider instance with `Provider(name, api_version, edge_cases)`.
2. Add the provider to the onboarding process with `ProviderOnboarding().add_provider(provider)`.
3. Validate API compatibility with `ProviderOnboarding().validate_api_compatibility(provider_name, api_version)`.
4. Document edge cases with `ProviderOnboarding().document_edge_cases(provider_name, edge_cases)`.
5. Get provider information with `ProviderOnboarding().get_provider_info(provider_name)`.

## Testing
Run tests with `python -m pytest`.
