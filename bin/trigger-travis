#!/usr/bin/env python
import json
import requests
import argparse
import os
import sys
"""
Trigger Travis CI build.

Args:
    -b --branch        Git branch to build (defaults to master)
    -e --env           Environment variables to inject (Optional)
    -m --mergemode     Merge mode - deep_merge, merge, replace (defaults to merge) https://docs.travis-ci.com/user/triggering-builds/
    -s --script        Script to run on triggered build
    -c --commitmessage Commit message to display on the triggered build
    -r --reposlug      Travis repo slug to trigger e.g. owner_name/repo_name
    -p --pro           Whether to use pro (travis-ci.com) or free (travis-ci.org)
    -t --token         Travis API token
    -v --verbose         Enable verbose mode
"""


def parse_arguments():
    PARSER = argparse.ArgumentParser(description='Travis Build Trigger CLI')
    PARSER.add_argument('-b', '--branch', help="Branch to trigger", default='master')
    PARSER.add_argument('-e', '--env', help="Slack API token", default=False)
    PARSER.add_argument('-r', '--reposlug', help="Travis repo slug", required=True)
    PARSER.add_argument('-m', '--mergemode', help="Merge mode", default='merge')
    PARSER.add_argument('-s', '--script', help="Script to run on the triggered build", default=False)
    PARSER.add_argument('-c', '--commitmessage', help="Commit message to display", default=False)
    PARSER.add_argument('-p', '--pro', help="Use --pro if you are using travis-ci.com. Defaults to travis-ci.org", action='store_true')
    PARSER.add_argument('-t', '--token', help="Travis API token", required=True)
    PARSER.add_argument('-v', '--verbose', help="Enable verbose output", action='store_true')
    return PARSER.parse_args()

ARGS = parse_arguments()

branch = ARGS.branch
reposlug = ARGS.reposlug
pro = ARGS.pro
env = ARGS.env
token = ARGS.token
merge_mode = ARGS.mergemode
script = ARGS.script
commit_message = ARGS.commitmessage
verbose = ARGS.verbose

if pro:
    gtld = '.com'
else:
    gtld = '.org'

owner = reposlug.split('/')[0]
repo = reposlug.split('/')[1]

travis_api_url = 'https://api.travis-ci{}/repo/{}%2F{}/requests'.format(gtld, owner, repo)

if not commit_message:
    commit_message = 'This build was triggered using the trigger-travis CLI'
else:
    commit_message = str(commit_message)

if env:
    env = str(env).split(',')

request_body = {}
request = {}
request['message'] = commit_message
request['branch'] = branch

if env:
    request['config'] = {}
    request['config']['merge_mode'] = merge_mode
    request['config']['env'] = {}
    request['config']['env']['global'] = env

if script:
    request['config']['env']['script'] = str(script)

request_body['request'] = request

request_body = json.dumps(request_body)

print(request_body)

headers = { "Content-Type": "application/json", "Accept": "application/json", "Travis-API-Version": "3", "Authorization": "token {}".format(token)}

if verbose:
    print('Sending HTTP Headers {}'.format(headers))
    print('Sending request body {}'.format(str(request_body)))

print('Calling Travis API V3 to trigger build for {}'.format(reposlug))

response = requests.post(travis_api_url, headers=headers, data=request_body)

if response.status_code == 202:
    print('Trigger successful')
    sys.exit(0)
else:
    print('Trigger failed, response code {}'.format(response.status_code))
    sys.exit(1)
