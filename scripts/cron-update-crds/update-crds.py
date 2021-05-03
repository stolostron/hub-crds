#!/usr/bin/env python3
# Assumes: Python 3.6+

import yaml
import logging
import os
from git import Repo
from shutil import copyfile


def updateCRDs(repo, operator):
   packageYmlPath = os.path.join("tmp", repo, operator["package-yml"])
   if not os.path.exists(packageYmlPath):
      print("Could not find package.yaml at given path:", operator["package-yml"])
      exit(1)
   
   with open(packageYmlPath, 'r') as f:
      packageYml = yaml.safe_load(f)

   bundlePath = ""
   for channel in packageYml["channels"]:
      if channel["name"] == operator["channel"]:
         version = channel["currentCSV"].split(".", 1)[1][1:]
         bundlePath = os.path.join("tmp", repo, os.path.dirname(operator["package-yml"]), version)
         break

   if bundlePath == "":
      print("Unable to find given channel: " +  operator["channel"] + " in package.yaml: " + operator["package-yml"])
   
   for filename in os.listdir(bundlePath):
      if not filename.endswith(".yaml"): 
         continue
      filepath = os.path.join(bundlePath, filename)
      with open(filepath, 'r') as f:
         resourceFile = yaml.safe_load(f)
      
      if resourceFile["kind"] == "CustomResourceDefinition":
         crdFolder = os.path.join("crds", operator["name"])
         if not os.path.exists(crdFolder):
            os.makedirs(crdFolder)
         copyfile(filepath, os.path.join("crds", operator["name"], filename))



def main():
   community_operatorsYml = "scripts/cron-update-crds/crds.yaml"
   with open(community_operatorsYml, 'r') as f:
      community_operators = yaml.safe_load(f)
   
   for repo in community_operators:
      print("Cloning:", repo["repo_name"])
      repo_path = os.path.join(os.getcwd(), "tmp/" + repo["repo_name"])
      if not os.path.exists(repo_path):
         Repo.clone_from(repo["github_ref"], repo_path)
      for operator in repo["operators"]:
         print("Checking", operator["name"])
         updateCRDs(repo["repo_name"], operator)

if __name__ == "__main__":
   try:
      main()
   except Exception:
      logging.critical("Unhandled exception")
      exit(1)