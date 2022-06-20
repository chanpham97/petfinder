def get_breeds(experience, bark, shed):
  if experience == 0:
    if bark == 0:
      return ["boston terrier", "pug"]
    elif bark == 1:
      if shed == 0:
        return ["cavalier king charles spaniel", "havanese"]
      else: 
        return ["beagle", "corgi"]
    else: 
      if shed == 0:
        return ["dachshund", "schnauzer"]
      else: 
        return ["beagle", "dachshund"]
  else:
    return ["poodle"]