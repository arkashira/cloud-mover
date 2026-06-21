import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Provider:
    name: str
    api_version: str
    edge_cases: List[str]

class ProviderOnboarding:
    def __init__(self):
        self.providers = {}

    def add_provider(self, provider: Provider):
        self.providers[provider.name] = provider

    def validate_api_compatibility(self, provider_name: str, api_version: str) -> bool:
        if provider_name in self.providers:
            return self.providers[provider_name].api_version == api_version
        return False

    def document_edge_cases(self, provider_name: str, edge_cases: List[str]) -> None:
        if provider_name in self.providers:
            self.providers[provider_name].edge_cases = edge_cases

    def get_provider_info(self, provider_name: str) -> Dict:
        if provider_name in self.providers:
            return {
                "name": self.providers[provider_name].name,
                "api_version": self.providers[provider_name].api_version,
                "edge_cases": self.providers[provider_name].edge_cases
            }
        return {}
