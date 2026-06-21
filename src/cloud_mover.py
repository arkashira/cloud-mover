import json
from dataclasses import dataclass
from datetime import datetime
from typing import Dict

@dataclass
class Provider:
    name: str
    credentials: Dict[str, str]

class CloudMover:
    def __init__(self):
        self.providers = {}
        self.failover_log = []

    def add_provider(self, name: str, credentials: Dict[str, str]):
        self.providers[name] = Provider(name, credentials)

    def get_provider(self, name: str):
        return self.providers.get(name)

    def initiate_failover(self, provider_name: str):
        provider = self.get_provider(provider_name)
        if provider:
            self.failover_log.append({
                'timestamp': datetime.now().isoformat(),
                'provider': provider_name
            })
            return True
        return False

    def prioritize_failover(self):
        # Simulate prioritization by marking the job as high-priority
        return True

    def log_failover(self, provider_name: str):
        self.failover_log.append({
            'timestamp': datetime.now().isoformat(),
            'provider': provider_name
        })

    def get_failover_log(self):
        return self.failover_log
