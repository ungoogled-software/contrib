# contrib

A collection of community contributions for [ungoogled-chromium](https://github.com/Eloston/ungoogled-chromium). Inspired by [this blog post by Drew DeVault](https://drewdevault.com/2020/06/06/Add-a-contrib-directory.html)

## Layout

All docker-related things are in [`/docker`](/docker) and are mostly intended to move ungoogled-chromium towards a more reproducible build system. 
You can easily build ungoogled-chromium in a containerized (or remote) environment using the tools in [`/docker`](/docker).

Further information can be found at [`/docker/README.md`](/docker/README.md).

## Motivation

The target audience includes those who maintain their own ungoogled-chromium-based browsers. Some potential use cases include:

* Someone wrote some scripts around the Python utilities to automate some workflow
* Someone has a patch fixing some system library dependency that is useful for others
* Someone wrote a new feature or script that doesn't conform to ungoogled-chromium's contribution guidelines and standards, but others may find useful.

To clarify the purpose and usage a bit more, I quote the blog post linked above:

> The contrib [repo] is used as an unorganized (or, at best, lightly organized) bin of various useful things **contrib**uted by the community around the software, but which is not necessarily a good candidate for being a proper part of the software. Things in contrib should not be wired into your build system, shouldn’t be part of your automated testing, shouldn’t be included in your documentation, and should not be installed with your packages. contrib entries are not supported by the maintainers, and are given only a light code review at the most. There is no guarantee whatsoever of workitude or maintenance for anything found in contrib.
>
> Nevertheless, it is often useful to have such a place to put various little scripts, config files, and so on, which provide a helpful leg-up for users hoping to integrate the software with some third-party product, configure it to fit nicely into an unusual environment, coax it into some unusual behavior, or whatever else the case may be. The idea is to provide a place to drop a couple of files which might save a future someone facing similar problems from doing all of the work themselves. Such people can contribute back small fixes or improvements, and the maintenance burden of such contributions lies entirely with the users.
>
> If the contributor wants to take on a greater maintenance burden, this kind of stuff is better suited to a standalone project, with its own issue tracking, releases, and so on. If you just wrote a little script and want somewhere to drop it so that others may find it useful, then contrib is the place for you.

## How to contribute

Simply create a pull request with your files. Here are some additional considerations:

* Add some documentation. If it's a single file, a comment should suffice. If it's a directory of files, add a README. Some things to consider adding:
	* Add a brief description of your contribution
	* Add some usage instructions
	* If you would like to be a point-of-contact (through Issues), add your GitHub username.
* Please specify the license(s) for your files. Any files without an explicit license is assumed to be public domain. However for everyone's convenience, please try to contribute under public domain.

If you are a contributor or a regular user in issues, then feel free to request direct write access.

## License

Public domain, unless otherwise specified.
