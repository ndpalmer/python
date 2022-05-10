import requests
import hashlib
import sys

def api_request(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}')
  return res

def hash_list_check(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0
    
def api_check(password):
  sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  fisrt5_char, tail = sha1_password[:5], sha1_password[5:]
  response = api_request(fisrt5_char)
  return hash_list_check(response, tail)

def main(args):
  for password in args:
    count = api_check(password)
    if count:
      print(f'Password found {count} times.')
    else:
      print(f'No matches found!')
  return 'Done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))