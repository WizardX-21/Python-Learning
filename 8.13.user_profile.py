def build_profile(first,last,**other_info):
  profile = {}
  profile['first-name'] = first
  profile['last-name'] = last
  for key,value in other_info.items():
    profile[key] = value
  return profile
my_profile = build_profile('hatake','kakashi',location = 'Hidden leaf',field = 'Shinobi')
print(my_profile)  
 