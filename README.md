# JIRA Ansible role

This Ansible role installs Atlassian JIRA in a Debian Stretch environment. The app will expose the endpoint `yourip:8080`.

There is optiontal setups for:
- Database
- Okta SSO integration
- Datacenter

All built with CircleCI: [![CircleCI](https://circleci.com/gh/peertransfer/jira_role.svg?style=svg)](https://circleci.com/gh/peertransfer/jira_role)

![Flywire Engineering](flywire_engineering.png)

<!-- TOC -->
- [JIRA Ansible role](#jira-ansible-role)
- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Testing](#testing)
- [Developing](#developing)
	- [Built With](#built-with)
	- [Contributing](#contributing)
	- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)

<!-- /TOC -->

## Getting Started

### Prerequisities

Ansible 2.8.3.0 version installed, or a Docker environment to develop.

For DataCenter we'll need a mountpoint with shared home. This playbook doesn't create that folder because some JIRA limitations, you'll need to start a installation to create home folder, and copy it over shared folder:

```sh
$ cp -R /path/to/jira-local-home/{data,plugins,logos,import,export,caches} /data/jira/sharedhome
```

### Installing

Add role dependecy to your requirements file ([Installing roles from file](https://docs.ansible.com/ansible/latest/reference_appendices/galaxy.html#installing-multiple-roles-from-a-file)).

Use the following example as a guide for specifying roles in *requirements.yml*:

```yaml
- src: flywire.jira_role
  version: 0.1.0
  name: jira
```
Use the following command to install roles included in requirements.yml:

```sh
ansible-galaxy install -r requirements.yml
```

Then you'll be able to use the role in your playbooks:

```yaml
- hosts: jira-server
  become: yes
  roles:
    - { role: flywire.jira_role }

```

## Testing

For testing we've used [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver, and [Testinfra](https://testinfra.readthedocs.io/en/latest/) as verifier.

In order to run the tests you can:

```sh
$ pipenv install -r test-requirements.txt
$ pipenv run molecule test
```

Also you can play each stage of __Molecule__ separated from this matrix, *test* will do all the steps:

```
└── default
    ├── lint
    ├── cleanup
    ├── destroy
    ├── dependency
    ├── syntax
    ├── create
    ├── prepare
    ├── converge
    ├── idempotence
    ├── side_effect
    ├── verify
    ├── cleanup
    └── destroy
```

## Developing

### Built With

![Ansible](https://img.shields.io/badge/ansible-2.8.3-green.svg)
![Python](https://img.shields.io/pypi/pyversions/3)
![Molecule](https://img.shields.io/static/v1?label=molecule&message=2.20.2&color=green)
![Testinfra](https://img.shields.io/static/v1?label=testinfra&message=3.0.6&color=orange)

### Contributing

### Versioning

We use the semver system to version all of our ansible roles, https://semver.org/

The current version is kept in plain text in a .semver file Ej: v1.2.5

## Authors

* **Flywire** - [flywire](https://github.com/peertransfer)

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.
