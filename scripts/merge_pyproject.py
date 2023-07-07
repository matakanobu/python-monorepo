#!/usr/bin/env python

import toml
import argparse

parser = argparse.ArgumentParser(description="Merge root pyproject.toml into project pyproject.toml.")
parser.add_argument("root_pyproject", type=str, help="Path to the root pyproject.toml")
parser.add_argument("project_pyproject", type=str, help="Path to the project pyproject.toml")
parser.add_argument("output_pyproject", type=str, help="Path to the output pyproject.toml")
parser.add_argument("--copy", type=str, nargs="+", default=[], help="Additional sections to copy")

args = parser.parse_args()

with open(args.root_pyproject, "r") as fp:
    root_pyproject = toml.load(fp)

with open(args.project_pyproject, "r") as fp:
    project_pyproject = toml.load(fp)

for section in args.copy:
    keys = section.split(".")
    temp_root = root_pyproject
    temp_project = project_pyproject
    for key in keys[:-1]:
        if key in temp_root:
            temp_root = temp_root[key]
            if key not in temp_project:
                temp_project[key] = {}
            temp_project = temp_project[key]
        else:
            break
    else:
        if keys[-1] in temp_root:
            temp_project[keys[-1]] = temp_root[keys[-1]]

with open(args.output_pyproject, "w") as fp:
    toml.dump(project_pyproject, fp)
