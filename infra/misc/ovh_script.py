#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import ovh
import json
import argparse


class OvhApi:
    def __init__(self, zone=None, subdomain=None, record=None):
        # Took configuration from ovh.conf file or env variables
        self.client = ovh.Client()
        self.zone = zone
        self.subdomain = subdomain
        self.record = record
        self.domain_id = None

    def getDomainId(self):
        result = self.client.get(
            f"/domain/zone/{self.zone}/record",
            fieldType=self.record,
            subDomain=self.subdomain,
        )

        # Return first element
        try:
            setattr(self, "domain_id", json.dumps(result[0], indent=4))
        except IndexError as err:
            print("Domain not found!")
            raise

    def alterDomainById(self, target):
        result = self.client.put(
            f"/domain/zone/{self.zone}/record/{self.domain_id}",
            subDomain=self.subdomain,
            target=target,
        )
        print("Domain altered!")

    def refreshZone(self):
        result = self.client.post(f"/domain/zone/{self.zone}/refresh")
        print("Zone refreshed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ovh_script", description="Modify domain record via OVH Api"
    )
    parser.add_argument("-z", "--zone", help="Zone name", required=True)
    parser.add_argument("-s", "--subdomain", help="Subdomain to modify", required=True)
    parser.add_argument("-r", "--record", help="Record to be modified", required=True)
    parser.add_argument("-t", "--target", help="Target to be set", required=True)
    parser.add_argument("-v", dest="verbose", action="store_true")
    cliargs = parser.parse_args()

    api = OvhApi(
        zone=cliargs.zone,
        subdomain=cliargs.subdomain,
        record=cliargs.record,
    )
    api.getDomainId()
    api.alterDomainById(cliargs.target)
    api.refreshZone()
