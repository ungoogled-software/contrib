#!/usr/bin/env python
"""
This script downloads and installs the binary dictionary files
that ungoogled chromium uses for its spell checking feature.

It will look for both OS install and Flatpak install config directories
and installs to both/either of them if they exist.

A custom install directory can also be specified.

Currently only works on Linux.

Adapted from the instructions in the FAQ here:
https://ungoogled-software.github.io/ungoogled-chromium-wiki/faq#how-do-i-fix-the-spell-checker



Usage:

Pass no arguments to list the available language files:
    ./spellcheck-installer.py

Pass language file name as first argument to install that language:
    ./spellcheck-installer.py en-GB-10-1

To install to a custom directory (must exist):
    ./spellcheck-installer.py en-GB-10-1 ~/my_dictionaries



After installing your required dictionary restart chromium,
and check your language settings at chrome://settings/languages
"""


import os
import sys
import base64
import requests
from bs4 import BeautifulSoup

repo_url = "https://chromium.googlesource.com"
file_ext = ".bdic"


def get_lang_file_links():
    """
    This function gets and returns a dictionary with the
    names of all the .bdic files in the chrome repo as the keys,
    and the URL of the files as the values.
    """
    url = f"{repo_url}/chromium/deps/hunspell_dictionaries/+/master"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")

    soup = BeautifulSoup(response.text, "html.parser")

    file_links = soup.find_all("a", class_="FileList-itemLink")

    links_dict = {
        link_text.replace(file_ext, ""): link.get("href")
        for link in file_links
        if (link_text := link.get_text(strip=True)).endswith(file_ext)
    }

    return links_dict


def download_lang_file_binary(links_dict, lang_code):
    """
    This file downloads the binary language file
    specified by its name `lang_code`
    """
    url = f"{repo_url}{links_dict[lang_code]}?format=TEXT"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")

    return response.text


def install_lang_file(lang_code, lang_file_binary, directory_path):
    """This function installs the binary language file to the specified directory"""
    dictionary_file_path = os.path.join(directory_path, f"{lang_code}{file_ext}")
    with open(dictionary_file_path, "wb") as f:
        f.write(lang_file_binary)

    print(f"Saved `{lang_code}{file_ext}` to {dictionary_file_path}")

    return True


def print_available(links_dict):
    """Prints the available language files and example usage for this script"""
    print("\nAvailable language file names:")
    print(list(links_dict.keys()))
    print("\nExample usage:\n\t./spellcheck-installer.py en-GB-10-1")


def main():
    # Get a list of the language files and their URLs
    links_dict = get_lang_file_links()

    if len(sys.argv) < 2:
        print(
            "First argument should be the name of the binary language dictionary file you require."
        )
        print_available(links_dict)
        return

    lang_code = sys.argv[1]

    if lang_code not in links_dict:
        print("Unavailable or invalid language code passed.")
        print_available(links_dict)
        return

    custom_install_directory = None
    if len(sys.argv) >= 3:
        custom_install_directory = os.path.expanduser(sys.argv[2])
        print(
            f"Using custom configuration directory: {custom_install_directory}\n"
            "Any detected OS or Flatpak install directories will be ignored.\n"
        )

    # Download the language file
    base64_lang_file = download_lang_file_binary(links_dict, lang_code)
    lang_file_binary = base64.b64decode(base64_lang_file)

    # Check if either of the OS Install and/or Flatpak install directories exist
    lang_file_installed = False
    os_install_dir = os.path.expanduser("~/.config/chromium/Dictionaries/")
    os_install_exists = os.path.exists(os_install_dir)

    flatpak_install_dir = os.path.expanduser(
        "~/.var/app/com.github.Eloston.UngoogledChromium/config/chromium/Dictionaries/"
    )
    flatpak_install_exists = os.path.exists(flatpak_install_dir)

    custom_directory_exists = custom_install_directory and os.path.exists(
        custom_install_directory
    )

    # Decide where to install the file/s and install them
    if custom_install_directory and custom_directory_exists:
        lang_file_installed = install_lang_file(
            lang_code, lang_file_binary, custom_install_directory
        )
    elif not custom_install_directory:
        if os_install_exists:
            lang_file_installed = install_lang_file(
                lang_code, lang_file_binary, os_install_dir
            )

        if flatpak_install_exists:
            lang_file_installed = install_lang_file(
                lang_code, lang_file_binary, flatpak_install_dir
            )

    # Inform the user of any errors or completion
    if custom_install_directory and not custom_directory_exists:
        print("Custom installation directory does not exist.")
    elif not flatpak_install_exists and not os_install_exists:
        print(
            "Couldn't find chromium configuration directory (neither OS install nor Flatpak install)"
        )
    elif not lang_file_installed:
        print(
            "Chromium configuration directory was found but the language file could not be installed. Check permissions."
        )
    else:
        print(
            "Please restart chromium and check your language settings at chrome://settings/languages"
        )

    return links_dict


if __name__ == "__main__":
    main()
