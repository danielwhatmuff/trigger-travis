# trigger-travis
![](https://cdn.travis-ci.com/images/logos/TravisCI-Full-Color-45e242791b7752b745a7ae53f265acd4.png)

## Overview
* Install and execute this CLI to trigger Travis CI builds on a particular branch, optionally overriding env vars or the script section
* For more information, see https://docs.travis-ci.com/user/triggering-builds/

### Get a token from Travis-ci.org 
```yaml
travis login --org
travis token --org
```

### Get a token from Travis-ci.com
```yaml
travis login --org --pro
travis token --org --pro
```

### Install the CLI and view the available options
```yaml
$ pip install trigger-travis
$ trigger-travis --help
```

### Example of running a build and passing environment variables
```yaml
$ trigger-travis -t yourtoken -r yourorg/yourrepo --branch develop --env SOMEENV=value,ANOTHERENV=anothervalue --mergemode deep_merge --pro
```

### Example of running a build and overriding the commit message
```yaml
$ trigger-travis -t yourtoken -c 'This build was triggered by the API' --branch master
```

### Example of running a build and overriding the script
```yaml
$ trigger-travis -t yourtoken -s 'exit 0' -m replace --branch master
```

## Related docs
* [Travis Build Docs](https://docs.travis-ci.com/user/customizing-the-build)
* [Triggering Builds APIv3](https://docs.travis-ci.com/user/triggering-builds/)

## Known issues
* Encrypted environment variables defined within your travis.yml don't work with the deep_merge option - you must define them in the repo settings using the Travis UI, this is a limitation with Travis...
