# learning Sessions and Cookies

https://www.geeksforgeeks.org/difference-between-session-and-cookies/

| Step | Action | What Happens? |
|----------|----------|----------|
| 1. Visit / |	Open Home Page | No session → Shows "Hello, Guest!"  |
| 2. Click Login |	Visit /login |	Session is set → Redirects to / |
|3. Visit / again |	After login	| Reads session → Shows "Welcome back, Abishek!" |
|4. Click Logout |	Visit /logout |	Clears session → Redirects to /|



Testing the App 

1. Open the App in Your Browser
Visit: http://127.0.0.1:5000/
You’ll see:

Hello, Guest!
[Login]

2. Click on "Login"
This sets the session and redirects you.
Now you see:

Welcome back, Abishek!
[Logout]

3. Click on "Logout"
This clears the session.
You are redirected to:

Hello, Guest!
[Login]
