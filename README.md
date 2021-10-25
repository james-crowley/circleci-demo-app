# CircleCI Demo Application
[![CircleCI Build Status](https://circleci.com/gh/james-crowley/circleci-demo-app.svg?style=shield)](https://circleci.com/gh/james-crowley/circleci-demo-app) [![Software License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/james-crowley/circleci-demo-app/main/LICENSE) [![Docker Pulls](https://img.shields.io/docker/pulls/jimcrowley/circleci-demo-app)](https://hub.docker.com/r/jimcrowley/circleci-demo-app)

This demo aims to show users some key features of CircleCI's platform.

The features shown off in the demo are:

- [Snyk](https://snyk.co/udBRL) Integration via the [official Orb](https://circleci.com/developer/orbs/orb/snyk/snyk) that scans Docker Images
- [Sonar Qube](https://www.sonarqube.org/) Integration via the [official Orb](https://circleci.com/developer/orbs/orb/sonarsource/sonarcloud) that does static code analysis
- Deployment utilizing [IP Ranges](https://circleci.com/docs/2.0/ip-ranges/) which provides a list of well-defined IP address ranges associated with the CircleCI service
- Browser Testing using CircleCI's [Convenience Images](https://circleci.com/docs/2.0/circleci-images/)
- Showing of Test Concurrency/Parallelism to achieve faster builds
- CircleCI's [Docker Layer Caching](https://circleci.com/docs/2.0/docker-layer-caching/) to speed up Docker Builds
- Holding/Approval of Jobs for manually review
- Utilizing CircleCI's [Test Insights](https://circleci.com/docs/2.0/collect-test-data/) to take a deeper look at jobs
- Plus many more features!

Currently, the demo deploys a Flask based website utilizing Docker. You can view the live site [here](http://18.191.154.49).