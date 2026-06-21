import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class HostingProvider:
    name: str
    url: str

class CloudMover:
    def __init__(self, primary_provider, secondary_provider):
        self.primary_provider = primary_provider
        self.secondary_provider = secondary_provider
        self.application_deployed = False

    def deploy_to_primary(self):
        if not self.application_deployed:
            print(f"Deploying application to {self.primary_provider.name}")
            self.application_deployed = True
        else:
            print(f"Application already deployed to {self.primary_provider.name}")

    def deploy_to_secondary(self):
        if self.application_deployed:
            print(f"Deploying application to {self.secondary_provider.name}")
            self.application_deployed = True
        else:
            print(f"Application not deployed to primary provider, cannot deploy to secondary")

    def fallback_to_secondary(self):
        if self.application_deployed:
            print(f"Falling back to {self.secondary_provider.name}")
            self.application_deployed = True
        else:
            print(f"Application not deployed to primary provider, cannot fallback to secondary")

def main():
    parser = ArgumentParser(description="Cloud Mover")
    parser.add_argument("--primary-provider", type=str, help="Primary hosting provider URL")
    parser.add_argument("--secondary-provider", type=str, help="Secondary hosting provider URL")
    args = parser.parse_args()

    primary_provider = HostingProvider("Primary", args.primary_provider)
    secondary_provider = HostingProvider("Secondary", args.secondary_provider)

    cloud_mover = CloudMover(primary_provider, secondary_provider)
    cloud_mover.deploy_to_primary()
    cloud_mover.fallback_to_secondary()

if __name__ == "__main__":
    main()
