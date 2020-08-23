# Docker
![](https://www.tatvasoft.com/blog/wp-content/uploads/2017/05/Docker.png)

- [Official docs](https://docs.docker.com/get-docker/)
- [How to install in Fedora](https://docs.docker.com/engine/install/fedora/)
- [How to install in MacOS](https://docs.docker.com/docker-for-mac/install/)
- [How to install in Windows](https://docs.docker.com/docker-for-windows/install/)

# docker-compose
![](https://miro.medium.com/proxy/0*lQHBTNViWBhPsTtF.)

- [How to install docker compose](https://docs.docker.com/compose/install/)

#### Commits

- Each commit should be a single logical change. Don't make several logical changes in one commit. For example, if a patch fixes a bug and optimizes the performance of a feature, split it into two separate commits.

- Don't split a single logical change into several commits. For example, the implementation of a feature and the corresponding tests should be in the same commit.

- Commit early and often. Small, self-contained commits are easier to understand and revert when something goes wrong.

- Commits should be ordered logically. For example, if commit X depends on changes done in commit Y, then commit Y should come before commit X.

##### Types:

- **feat**: Implementation of something new: A feature, functionality, scren, action option, etc.
- **fix**: Implementation in which the sole purpose is to correct any erroneous behavior in the system.
- **docs**: Changes or increments in the project documentation.
- **style**: Refactorings of indentation, missing commas, optimization of imports and etc.
- **refactor**: Refactoring / improving code without changing functionality.
- **test**: Refactoring or adding testes. Tests only.
- **config**: Changes to project or environment configurations files. Logs, packages, dependecies and etc.



