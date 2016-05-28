#!/usr/bin/env python
# *-* coding: UTF-8 *-*

from __future__ import print_function 
import argparse
import os
import sys

PURPLE = '\033[95m'
ENDC = '\033[0m'

def insensitive_search(search_key, line, normalized, 
                       replace_with_occurence, replace_key,
                       prefix="", suffix=""):
    occurences = 0
    tmp = []
    start_index = 0
    end_index = normalized.find(search_key, 0)

    while end_index != -1:
        tmp.append(line[start_index:end_index:])
        if replace_with_occurence:
            tmp.append(prefix + line[start_index:start_index + len(search_key) + 1:] 
                       + suffix)
        else:
            tmp.append(prefix + replace_key + suffix)
        start_index = end_index + len(search_key)
        end_index = normalized.find(search_key, start_index)
        occurences += 1

    tmp.append(line[start_index::])
    
    return "".join(tmp), occurences

def replace_grep(filename, search_key, replace_key, 
                 exact_match, case_sensitive):
    
    try:
        file_display_name = os.path.relpath(filename)
        handle = open(filename, "r")
        occurences = 0
        modified_file = []

        for idx, line in enumerate(handle, 1):
            if line[-1] == "\n":
                line = line[:-1:]

            if not case_sensitive:
                normalized = line.lower()
                
                if not exact_match:
                    append_string, matches = insensitive_search(search_key.lower(), line,
                                                                normalized, False, search_key)
                    occurences += matches
                    modified_file.append(append_string)
                else:
                    if normalized == search_key:
                        modified_file.append(replace_key)
                        occurences += 1
                    else:
                        modified_file.append(line)

            else:
                if not exact_match:
                    occurences += line.count(search_key) 
                    modified_file.append(line.replace(search_key, replace_key))
                else:
                    if line == search_key:
                        occurences += 1
                        modified_file.append(replace_key)
                    else:
                        modified_file.append(line)
        handle.close()

        handle = open(filename, "w")

        for line in modified_file:
            handle.write(line + "\n")

        handle.close()

        return occurences
    except IOError:
        return -1

def file_grep(filename, search_key, exact_match, case_sensitive, colored):
    try:
        file_display_name = os.path.relpath(filename)
        handle = open(filename, "r")
        occurences = 0
        occurences_log = []

        for idx, line in enumerate(handle, 1):
            if line[-1] == "\n":
                line = line[:-1:]

            if not case_sensitive:
                if not exact_match:
                    normalized = line.lower()

                    if colored:
                        line, matches = insensitive_search(search_key.lower(), line, 
                                                           normalized, True, None, PURPLE, ENDC)
                    else:
                        matches = normalized.count(search_key.lower())

                    if matches > 0:
                        occurences += matches
                        occurences_log.append(file_display_name + ":" + str(idx) + ":" + line)
                else:
                    if line == search_key:
                        if colored:
                            line = PURPLE + line + ENDC
                        occurences_log.append(file_display_name + ":" + str(idx) + ":" + line)
            else:
                if not exact_match:
                    if colored:
                        matches = line.count(search_key)
                        line = line.replace(search_key, PURPLE + search_key + ENDC)
                    else:
                        matches = line.count()

                    if matches > 0:
                        occurences += matches
                        occurences_log.append(file_display_name + ":" + str(idx) + ":" + line) 
                else:
                    if line == search_key:
                        line = PURPLE + search_key + ENDC
                        occurences += 1
                        occurences_log.append(file_display_name + ":" + str(idx) + ":" + line)

        handle.close()
        return occurences_log, occurences

    except IOError:
        return -1 # it means it's bad

def print_lines(modified_lines):
    for modified_line in modified_lines:
        print(modified_line)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("search_key", help="The key you are searching for")
    parser.add_argument("file_path", help="The file to search for the search key")
    parser.add_argument("-r", "--recursive", help="Do a recursive search",
                        action="store_true")

    parser.add_argument("-i", "--insensitive", help="Search without caring about the case",
                        action="store_true")
    parser.add_argument("-e", "--exact", help="Search for exact matches",
                        action="store_true")
    parser.add_argument("-s", "--substitute", help="Replace occurences") 
    parser.add_argument("-n", "--count", help="Count occurences",
                        action="store_true")
    parser.add_argument("-c", "--colors", help="Colort the search key in red", 
                        action="store_true")
    
    grep = parser.parse_args()
   
    if not os.path.exists(grep.file_path):
        print("The file that you've specified does not exists")
        sys.exit(1)

    if not grep.recursive:
        pretty_path = os.path.filepath(grep.file_path)
        if grep.substitute:
            occurences = replace_grep(grep.file_path, grep.search_key, 
                                      grep.substitute, grep.exact, grep.insensitive)
            if grep.count:
                print("Matches: %d in %s" % (occurences, pretty_path))
                
        else:
            modified_lines, occurences = file_grep(grep.file_path, grep.search_key,
                                                   grep.exact, grep.insensitive,
                                                   grep.colors)
            if grep.count:
                print("Matches: %d in %s" % (occurences, pretty_path))
            else:
                print_lines(modified_lines)
    else:
        for dir_path, dirs, files in os.walk(os.getcwd()):
            for file_name in files:
                pretty_path = os.path.relpath(dir_path + os.sep + file_name)
                if grep.substitute:
                    occurences = replace_grep(dir_path + os.sep + file_name, grep.search_key, 
                                              grep.substitute, grep.exact, grep.insensitive)
                    if grep.count and occurences > 0:
                        print("Matches: %d in %s" % (occurences, pretty_path))
                else:
                    modified_lines, occurences = file_grep(dir_path + os.sep + file_name, 
                                                           grep.search_key, grep.exact,
                                                           grep.insensitive, grep.colors)
                    if grep.count and occurences > 0:
                        print("Matches: %d in %s" % (occurences, pretty_path))
                    else:
                        print_lines(modified_lines)

