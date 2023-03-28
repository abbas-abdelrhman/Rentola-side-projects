import requests

# Set the Splash URL and the script to run
url = 'http://localhost:8050/run'
script = """
function main(splash)
  splash:init_cookies(splash.args.cookies)
  assert(splash:go{
    splash.args.url,
    headers=splash.args.headers,
    http_method=splash.args.http_method,
    body=splash.args.body,
  })
  assert(splash:wait(0.5))

  -- Type the username and password
  username = splash:select('#username')
  username:send_text('user@example.com')
  password = splash:select('#password')
  password:send_text('password')

  -- Click the login button
  login_button = splash:select('button[type=submit]')
  login_button:mouse_click()

  -- Wait for the page to load
  assert(splash:wait(0.5))

  -- Check if we are logged in
  logged_in = splash:select('.logged-in-content')
  if logged_in then
    return {
      html = splash:html(),
      png = splash:png(),
      har = splash:har(),
    }
  else
    return {
      error = 'Login failed'
    }
  end
end
"""

# Set the login URL and the necessary headers and form data
login_url = 'https://example.com/login'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
form_data = {'username': 'user@example.com', 'password': 'password'}

# Make the request to Splash
response = requests.post(url, json={
    'url': login_url,
    'headers': headers,
    'http_method': 'POST',
    'body': form_data,
    'timeout': 30,
    'wait': 0.5,
    'lua_source': script,
})

# Print the response from Splash
print(response.json())
