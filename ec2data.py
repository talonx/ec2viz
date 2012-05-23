import boto.ec2 as ec2
from collections import defaultdict
import json
import sys
import ConfigParser
import os

class ec2data:

    def __init__(self):
        self.key, self.secret = self.read_creds()

    def read_creds(self):
        cfp = ConfigParser.ConfigParser()
        a = cfp.read(['settings.conf', os.path.expanduser('~/settings.conf')])
        return cfp.get('Credentials', 'key'), cfp.get('Credentials', 'secret')
    
    def dictify(self, i):
        d = {}
        d['root_device_type'] = str(i.root_device_type)
        d['private_dns_name'] = str(i.private_dns_name)
        d['public_dns_name'] = str(i.public_dns_name)
        d['id'] = str(i.id)
        d['state'] = str(i.state)
        d['architecture'] = str(i.architecture)

        tags = i.tags
        self.get_and_set_tags(tags, 'Name', d)
        self.get_and_set_tags(tags, 'Type', d)

        d['key_name'] = str(i.key_name)
        d['image_id'] = str(i.image_id)
        d['ip_address'] = str(i.ip_address)
        d['placement'] = str(i.placement)
        d['instance_type'] = str(i.instance_type)
        
        gs = i.groups
        groupnames = ''
        for g in gs:
            groupnames += str(g.name)
            groupnames += ','
        d['groups'] = groupnames

        bdm = i.block_device_mapping
        bdms = ''
        for k, v in bdm.iteritems():
            bdms += str(k)
            bdms += ':'
            bdms += str(v.volume_id)
            bdms += ","
        d['block_device_mapping'] = bdms

        return d

    def get_and_set_tags(self, tags, key, d):
        if key in tags:
            d[key] = tags[key]
        else:
            d[key] = 'Unknown'

    def GET(self):
        conn = ec2.EC2Connection(self.key, self.secret)
        rsvs = conn.get_all_instances()
        instances = [i for r in rsvs for i in r.instances]
        data = defaultdict(list)
        #default key is avzone
        for i in instances:
            pc = str(i.placement)
            data[pc].append(self.dictify(i))
        return json.dumps(data)


#Standalone run
if __name__ == '__main__':
    #if len(sys.argv) != 3:
    #    print "Usage: ec2data.py <AWS key> <AWS secret>"
    #    sys.exit()
    ec2d = ec2data()
    print ec2d.GET()
