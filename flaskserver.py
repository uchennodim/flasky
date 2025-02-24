
from flask import Flask #First we imported the Flask class. An instance of this class will be our WSGI application. https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application

app = Flask(__name__) # we generate an instance/object of the Flask class. This instance is our WSGI application. A Web Server Gateway Interface (WSGI) server runs Python code to create a web application https://www.fullstackpython.com/wsgi-servers.html The argument __name__ points to the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
print(__name__) # __main__ -> i.e. this our file, our flask "app" flaskserver.py apu

# @app.route is the flask decorator @app.route() which is used to map a URL to a view function. The view function is a regular Python function that returns a response to an HTTP request. The route decorator specifies as its argment (in this case "/") which Flask ses as the URL to trigger our function, in techspeak, the route() decorator  the route() decorator is used to bind a function to a URL
# @app.route("/") #the url argunment, "/" is the root of our web server -> consider that a single / represents the root directory
@app.route("/test") #updated the url argunment to "/test" so that we can use the single / for the home (index.html) of our new proper universe portfolio webpage project (see DownDown)
def hello_world():
    # return "<p>Hello, World!</p>" #
    return "<p>Hello, U-Billz!</p>" #the function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser whenever we visit the root directory (i.e. "/") since it is the route we deined for our app per the app.route decorator!

#MORE LEARNINGG ON DECORATORS: https://sumit-ghosh.com/posts/demystifying-decorators-python/

#next step is to run our application. we use CLA: flask  or CLA: python -m flask  to which we prepend --app app_name run  -> --app option tells Flask where our application is and should be folloed by the file path (app_name) to our app which for us is flaskserver.py (per relative referencing) -> the run command tells Flask to launch our server. However, as a shortcut, if the file is named app.py or wsgi.py, you don’t have to use --app i.e. CLA: flask run

#CLA: flask --app flaskserver.py run -> works apu with response below:
"""
flaskserver
 * Serving Flask app 'flaskserver.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [29/Jan/2025 16:24:11] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [29/Jan/2025 16:24:11] "GET /favicon.ico HTTP/1.1" 404 -
"""
#this shows that flaskserver was started on port 5000 and that we can access it by going to http://127.0.0.1:5000 where it is running on being that http://127.0.0.1: is our local host, i.e. the address of our machine (which is same or everyone). If another program is already using port 5000, you’ll see OSError: [Errno 98] or OSError: [WinError 10013] when the server tries to start. So when we go to the url http://127.0.0.1:5000  it takes us to webpage with the content "HEllo World" which is what we speciied to be returned by our function by the app.route() decorator.                 

#Debug Mode: The flask run command can do more than just start the development server. By enabling debug mode, the server will automatically reload if code changes, and will show an interactive debugger in the browser if an error occurs during a request. To enable debug mode, use the --debug option so that CLA : flask --app flaskserver.py run --debug -> to run again, we first close the current server by pressing Ctrl+C, then we run the command again. The server will now automatically reload.:
"""
flaskserver
 * Serving Flask app 'flaskserver.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
flaskserver
 * Debugger is active!
 * Debugger PIN: 350-100-969
"""
#Note that the debugger is now active and Flask has generated a debugger PIN. This is a random number that you can use to connect to the debugger in your browser. Also, when wwe change the returned html in our app.route decorator function from "<p>Hello, World!</p>" to "<p>Hello, U-Billz!</p>", it changes it the webpage on refresh, i.e. without having to restart the server like when debug mode was of. Thhe terminal also records the change:
"""
127.0.0.1 - - [29/Jan/2025 23:11:26] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [29/Jan/2025 23:11:27] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [29/Jan/2025 23:11:28] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [29/Jan/2025 23:11:28] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [29/Jan/2025 23:11:32] "GET / HTTP/1.1" 200 -
 * Detected change in 'C:\\Users\\uchen\\PycharmProjects\\modules\\venvwebserver\\flaskserver.py', reloading
 * Restarting with stat
flaskserver
 * Debugger is active!
 * Debugger PIN: 350-100-969
127.0.0.1 - - [29/Jan/2025 23:12:03] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [29/Jan/2025 23:12:11] "GET / HTTP/1.1" 200 -
 * Detected change in 'C:\\Users\\uchen\\PycharmProjects\\modules\\venvwebserver\\flaskserver.py', reloading
 * Restarting with stat
flaskserver
 * Debugger is active!
 * Debugger PIN: 350-100-969
"""

#We can specify other "stuff" (read: pages) to be returned (read: served) by our server for other "endpoints" (read: urls) other than the root "/" by also using the app.route() decorator to speciy them. For example, we can create a 
@app.route("/name") #for the enpoint /name ... to the nction below is served/called when wpoint our browser to the address http://127.0.0.1:5000/name
def my_name():
    return "<p>Braniac Baller Billionasire Benefactor</p>" #wors apu -> 
    
# We get an 404 error (Not Found:The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.) in the browser if we use an enpoint in the browsewr, same "/nawa" i we didnt speciy a unction to return it with the correpsonding @app.route("/nawa") decorator!

# @app.route("/name") #In cases of duplicate endpoints, Flask gives an AssertionError: View function mapping is overwriting an existing endpoint function: my_name 
# def my_name():
#     return "<p>Braniac Baller Billionasire Benefactor</p>" #wont be served as there is a previous endpoint with the same route
#The assertion error once encountered reuses to clear, even after we remove the problematic endpoint, in  this case the duplicate "/name" url. So we have to restart the server to get rid of it -> first do CLA: Cntrl + C to quit the Server and then CLA: flask --app flaskserver.py run --debug to restart it. Then close the previous browser.

#HOW TO CLOSE FLASK  WITHOUT USING CONTROL + C : https://www.google.com/search?q=how+to+quit+Flask+server&sca_esv=b22bf8643ac1f672&rlz=1C1MMCH_enNG1145NG1145&sxsrf=AHTn8zrAljIYZDFpoMr6ddsGuQYc1mwFqw%3A1738258369087&ei=wbebZ7CIBfm3hbIPooyP6QE&ved=0ahUKEwjw7PeE_Z2LAxX5W0EAHSLGIx0Q4dUDCBA&uact=5&oq=how+to+quit+Flask+server&gs_lp=Egxnd3Mtd2l6LXNlcnAiGGhvdyB0byBxdWl0IEZsYXNrIHNlcnZlcjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjILEAAYgAQYhgMYigUyBRAAGO8FMgUQABjvBTIFEAAY7wVIjUBQAFiMO3AAeAGQAQCYAe4BoAGHJ6oBBjAuOC4xNrgBA8gBAPgBAZgCGKACryfCAgoQIxiABBgnGIoFwgIEECMYJ8ICERAuGIAEGJECGNEDGMcBGIoFwgILEAAYgAQYkQIYigXCAgUQABiABMICCxAAGIAEGLEDGIMBwgIIEAAYgAQYsQPCAgQQABgDwgIFEC4YgATCAgoQABiABBhDGIoFwgITEAAYgAQYsQMYQxiDARjJAxiKBcICCxAAGIAEGJIDGIoFwgIOEAAYgAQYsQMYgwEYigXCAggQABiABBiiBJgDAJIHBjAuOC4xNqAH27UB&sclient=gws-wiz-serp#fpstate=ive&vld=cid:1cced245,vid:VFjyW6f1Mek,st:2

@app.route("/name") #No error AssertionError or otherwise -> if there are similar endpoints, the first onee's app.route enpoint function IS CALLED AND RETURNED (because, return) AS LONG AS THE ENPOINT FUNCTIONS ARE DIFFERENTLY NAMED. The AssertionError is only raised by Flask if the endpoint functions are the same (name).
def my_name2():
    return "<p>U_NAUTI</p>" #wont be served as there is a previous endpoint with the same route

# @app.route("/title") #same AssertionError: View function mapping is overwriting an existing endpoint function: my_name -> as long as we have a similar named function, will get AssertionError 
# def my_name():
#     return "<p>U_soFly</p>" #sorry-o!

  #Note that Flask automatically converts the returned string or html to a html webpage with the appropriate headers:
@app.route("/name/forreal") #the endpoint can be sub paths asin /.../.../... as long as its defined, Flask go serve am
def my_name_fr():
    return "Soon And VERY SOON" #works apu -> Even thogh this is a string Flask will convert it to a html doc when serving it. Conirmed with developer tools as: <html><head></head><body>Soon And VERY SOON</body></html> ... shows that indeed our plain string has been converted to html

#Serving Templates: generating html from within Python like wee been doing above is obviosly not too much fun, and flask solves that by providing a render_template() method that can be used to serve html templates. To use this method, we must first import it rom flask:

from flask import render_template
from flask import Flask, render_template #neater way to do multiple imports, should be at top of page tho.

# The templates are html files that have to be stored in a folder called templates in the same directory as (this) our python script (flaskservewr.py in our case). Our endpoint function for which the route to the target html template is deined, will return the render_template() method which itseltakes the name of the template as an argument! If we dont put our html template in the templates older, the render_template() function wont be able to locate and render it or return by the corresponding app.route endpoint function

#Generated a templates folder in or venvwebserver directory and copied oiur test index1.html, style.css and script.js files into it
@app.route("/home") #actually, we cfan mae our html the real home page by sing the root directory "/" as the specified route here
def test_template():
    return render_template("index1.html") #worked, but the css wasnt deployed even tho we kept them in same older o! UPDATE: works apu after serving the css and js iles from the static ffolder -> see below on Serving Static Files

#Serving Static files: these are files that dont (usually) change after we deploy them and include CSS and JS files. To deploy them we have to irst store them in a folder called static which shold be generated in the same directory as our server script, just like we did with the templates folder. Note that the rerence link in our index1.html ile has to be changed to href="../static/style.css" to point to the correct new location of the CSS file ditto href="../static/script.js" or the JS file. 

# We can generate urls for static files using the special "static" enpoint name: url_for('static', filename='style.css')  https://flask.palletsprojects.com/en/stable/api/#flask.url_for 

#Favicons: The conventional way to serve favicons in our html file is to link to it in  the <head> element jsyut like we do with our css but in this case using the rel="icon" attribute: <link rel="icon" href="link_to_favicon_img" /> (note that as BP we should use .ico image iles as the favicon and the ile name should be "favicon" thus our favicon would be favicon.ico placed in the static folder in turn placed in our project folder where (this) our server script is located) With our favicon image in the static folder, rather than hardcoding its url (and assigning it to the href attribute) we can link to it in the html using Flask's url_for() function to generate the url for the favicon image like so: <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}"> ... the double curly brackets is the Jinja templating syntax which Flask incoporates such that anywhere it is in the html doc, Flask evalates the expression within the closed double curly brackets as python code > in this case the Function url_for() is being called with the arguments 'static' and filename='favicon.ico' url_for() is a Flask function used to generate a URL to the given endpoint. In other words, in Python, per the Jinja double curlys, url_for('static', filename='favicon.ico') will evaluate to which is the url of the favicon.ico file in the static folder. https://flask.palletsprojects.com/en/stable/api/#flask.url_for

#Note that the faicon was not originally showing with <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}" even though it was working well with <link rel="shortcut icon" href="../static/favicon.ico"> ...seems it was when I was on other urls like / and /name etc which makes sense as the  favicon is only linked in our index1.html document as represented by /home. So any url endpoint (extension) other than /home will not display the favicon. Thus in web building, each html page must have the favicon linked etc!.

from flask import url_for #need to import the url_for() function from flask

# print(url_for('static', filename='favicon.ico')) #RuntimeError: Working outside of application context -> since this is a Flaask function, we have to be inside a Flask app context such as an app.route() endpoint function like below. Remembet that app.route indicates that .route() is a method of the app object which is the iobject we instantiated rom the Flask class. In otherwords, our app variable is a Flask app object which does all the magic, one of which tricks is to serve data to the browser using an endpoint function decorated by the apps route() method! SUPO!! Futhermore, whever we run this python script as is, either from the UI or CLA python flaskserver.py, it will close our server and if we try to access the app via the the web browser it will return the error 127.0.0.1 refused to connect. Thus, we'd have to get the server back up and running with CLA: flask --app flaskserver.py run --debug

@app.route("/urlfor") #actually, we cfan mae our html the real home page by sing the root directory "/" as the specified route here
# def test_template(): #AssertionError: View function mapping is overwriting an existing endpoint function: test_template
def urlfor():
    print(url_for('static', filename='favicon.ico')) #/static/favicon.ico -> printed in the TErminal
    return url_for('static', filename='favicon.ico') # /static/favicon.ico -> returned in the Webpage UI ... nice!


#Variable Rules: Flask allows us to define routes with variable parts using the <variable_name> syntax. the enclosing <> indicate that string data can be passed in from the browser url as the variable_name that <> encloses. Consequently, variable_name can then be ed into the corresponding endpoint function for use. In other words, the function recieves the <variable_name> as a keyword argument. Say we generate another page (index2.html)

def Testin1():
    @app.route("/<title>") #if the browser's url input is /any_string except /home or /name, then get_title() below is called. This is because both routes for /name and /home already have endpoint functions designed to handle them in this our (flask)server.py script
    def get_title(title = "U-Billz"): #we are deaulting "U-Billz" as the value of the title variable to be passed in from the browser url
        return render_template("index2.html", my_title=title) # any jinja templating braces bearing mytitle in index2.html will be evaluated with title as the value of my_title -> worked apu
# Testin1() #Deactivated this as /<title> endpoint variable is conflicting with our Universe projects' /<pagename> endpoinbt variable DownDown

@app.route("/index2/<title>") #browser url /index2/any_string will trigger the function below
def get_title2(title): # didnt default. Not BP since a user may not input (correct) data in the url syntax 
    return  render_template("index2.html", my_title=title)

#Converters:  you can use a converter to specify the type of the argument with the syntax <converter:variable_name>. the converter types include string (the default, accepts any text without a slash), int (accepts positive integers), float (accepts positive floating point values), path (similar to string but also accepts slashes), and uuid (accepts UUID strings)

# @app.route("/<nickname>/<int: cashflow>/<title>") #ValueError: malformed url rule: '/<nick_name>/<int: cash_flow>/<title>' -> this is because there shouldnt be a space before/after the :
@app.route("/<nickname>/<int:cashflow>/<title>") #per converter, int haS to be a positive integer. If forex it is a string and there is no other route defined for /string/string/string, then the bwroser/flask rewturns an error: Not Found The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
def get_title3(nickname= "U-Billz", cashflow= 10000000000, title="U-Billz"):
    return  render_template("index2.html", my_title=title, nick_name = nickname, cash_flow = cashflow) #INDEX 2 BrianicBallerBillionaireBenefactor is my title! U-Billz is all about the 50000000000 dollar cash flow #BrianicBallerBillionaireBenefactor -> HOWEVER IS NOT EFFECTING THE CSS AZURE BACKGROUND O! WHY NOW?? THOUGN THE FAVICON IS SHOWING SO ITS NOT A LINK ISSUE???

#MIME Types: - A media type (also known as a Multipurpose Internet Mail Extensions or MIME type) indicates the nature and format of a document, file, or assortment of bytes. MIME types are defined and standardized in IETF's RFC 6838. NOTE:  Browsers use the MIME type, not the file extension, to determine how to process a URL, so it's important that web servers send the correct MIME type in the response's Content-Type header. If this is not correctly configured, browsers are likely to misinterpret the contents of files, sites will not work correctly, and downloaded files may be mishandled. 
# Structure of a MIME type: A MIME type most commonly consists of just two parts: a type and a subtype, separated by a slash (/) — with no whitespace between forex image/jpeg for .jpg and .jpeg files. Note that thewre is only one mime type or jpeg and jpg ffiles. 
# To check the mime types of a wbpages files, open developer tools (inspect) go to network, then click headers tab. the mime type o each of the webpages content files will be listed as Content-type. For exzmple the html documment will be text/html while the javascript ile is application/javascript (per new standard though previous standard was text/javascript). Also, APIs generatty send their data as applicationn/json MIME type data. 
#LasLas, all the data that is served is text. Na just d ormat go make am jpeg or json or html ...abi o , lol
# https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types
# Common MIME Types: https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types# 
# https://en.wikipedia.org/wiki/Media_type


#BUILDING A PORTFOLIO: We can generate or html pages for the project (hint: try later with gass or proactiv) ormore easily for learning purposes, we can get sample html/css files online. We will be using a project called universe (we got it from https://mwender.com/mashup-template-com-free-html5-templates/ or http://mashup-template.com/) whose folder (i.e. containing its html, css and js files) is in our main project folder (venvwebserver). However, wew will have to move the projeect/portfolio files to our respective template and static folders in our project. Nte that we will need to chanhge the name of original index.html file since our universe project has an index.html. While we can configure our server to recognise any html file name as the landing page, it is conventional to use index.html, so we changed our plain (read:boring) one to index1.html 
#Other Free Online HTML Template Sources: https://themewagon.com/author/mashuptemplate/  https://www.creative-tim.com/bootstrap-themes/free  https://html5up.net/  

#1. Move all html files to the ./templates folder (using./ to indicate project folder venvwebserver)
#2. Move all css and js files into the Static folder
#3. Move all assets (pictures etc) into an Assets folder and place folder into the static folder. Update the links from the html files to the files whose relative positions have changed, in this case for the links (i.e. hrefs, url and src attributes) i prefixed ../static/ to everything I moved to the static folder (i.e. assets folder, the main.3f6952e4.css and the main.70a66962.js files)
#4. Lets run thew server at CLA and start with serving our new index.html (i.e. for universe):
@app.route("/") #Works apu -> iniitially showing "Hello, U-Billz" from the previous app.route "/" that we defined UpUp. Changed that one's path to /test to avoid conflicts with this one
@app.route("/index.html") # listing both routes together means that the uni_works function will be called for both i.e. our home page, inex.html will be served for both "/" and "/index.html" endpoints ... Neat!
def univ_home():
    return render_template("index.html")

#Oya lets serve the other pages o! -> started inspecting the links/buttons on the home page (i.e. index html above) to see which ones are linked to which pages (other html files). Also on clicking, saw that the url updated thus tellling me which url should be use to route to the respective page which was show upon the page inspection! The href/src/url link endpoint for each of the other pages/html files is the same as the endpoint url in the browser.However, you need to refresh your JS so that you can identify the url that was set in the code for each.  

def Testin2():
    @app.route("/works.html")
    def univ_works():
        return render_template("works.html")

    @app.route("/work.html") #I just dey click any button when I see then serve the corresponding page lol
    def univ_work():
        return render_template("work.html")
    
    @app.route("/about.html") 
    def univ_about():
        return render_template("about.html")

    @app.route("/contact.html") 
    def univ_contact():
        return render_template("contact.html")

    @app.route("/submit_form") #clicked the send button on the /contact.html endpoint page and it yeilded a "/submit_form" in the webpage url address bar. Im guessing its for the thankyou.html page/file. See in this case the enpoint does not nercessarily point to a same named html page to be served. Hence again, need to refresh your JS so that you can identify the url that was set in the code for each.   
    def univ_submit_form():
        return render_template("thankyou.html") #Error: Method Not Allowed The method is not allowed for the requested URL.
# Testin2() #DEactivated to replace with dynamic option below because, DRY

#MAKING THE ABOVE DYNAMIC: we can deploy variable rules to the avove routes, trhis works ll because the route endpoints are similarly named to the html pages/files/temples that we want to return render. 

# @app.route("/<string: page_name>") #Also note that we are specifying that page_name must be a string for the route to be recognised -> ValueError: malformed url rule: '/<string: page_name>' -> betY? 
@app.route("/<page_name>") #the url endpont is passed in as the variable page_name into the (corresponding) endpoint function (univ_page) below -> However wont give the right results since we already have a  enpoint UpUp which is equivalent to this /<page_name> as they have the same syntax/structure. Thus to avoid conflicts, had to go deactivate with Testin1(). 
def univ_page(page_name = ""): #default route to /"" i.e. / which we will point, just like index.html, to the home page etc. 
    # print(page_name)
    return render_template(f"{page_name}") if page_name else render_template("index.html") # works apu! Yaaay!! -> if page_name is empty, return the home page. #Teneray Operator Tinz for the if/else -> Note that the default empty string is a null value and will trigger the else condition 


#BUILDING OUR CONTACT FORM: say we want to make our webpage's submit form function. I had tried before (see Testin2) but didnt work. lets do it the proper way, we will use the endpoint "/submit_form" being thats what the webpage url displays when we click the send button under the contact form (EP: "/contact.html"). To understand how this endpoint "/submit_form" is set in the browser url upon being triggered by the send button (button element attribute type="submit") under the contact.html form, we check the HTML in the contact.html and see that the SEnd button elemtn is in a form element (.reveal_content) as expected (goan revise ur html/css o!). We have to set 2 of the form element attributes as follows action="submit_form"  method="post" -> the action attribute specifies where (i.e. the url) to send the form-data when a form is submitted or better put, the URL that processes the form submission (remember that our send is a button element with type="submit" attribute). The method attribute sets HTTP method to submit the form with. The only allowed methods/values are (case insensitive) post, get and dialog. See more at https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form

from flask import request #For web applications it’s crucial to react to the data a client sends to the server. In Flask this information is provided by the global request object. The request object, used by default in Flask, is a Request subclass and provides all of the attributes Werkzeug defines plus a few Flask specific ones. NOTE: Werkzeug (werkzeug German noun: “tool”. Etymology: werk (“work”), zeug (“stuff”)) is a comprehensive WSGI web application library. It began as a simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility libraries. https://werkzeug.palletsprojects.com/en/stable/ 

# print(request, request.method) #RuntimeError: Working outside of request context. This typically means that you attempted to use functionality that needed an active HTTP request. Consult the documentation on testing for information about how to avoid this problem. .> seems request's .method can only be used during an active (read: ongoing) HTTP request scenario like in our univ_submitform below
# print(request) #same RuntimeError as above, guess request itself also needs an active HTTP request (NPI) scenario

from flask import redirect, abort #To redirect a user to another endpoint, use the redirect() function; to abort a request early with an error code, use the abort() function. 

def testin_submit():
    @app.route('/submit_form', methods=['POST', 'GET']) #set suubmit_form is set as the action attribute in the send buttons parent form element in contact.html. If url route ("/submit_form") isnt same as speciied in the action attribute of the form element, get browser error: Method Not Allowed The method is not allowed for the requested URL. If we check out the developrer tools for the form's page (i.e. /contact.html) under network, we see that when we click thwe send button and go to our /submit_form url, the submit form urls assets include a submit_form document of type text/html with Request URL: http://127.0.0.1:5000/submit_form and Request Method: POST -> CONFAM! As for the methods=['POST', 'GET'] argument, note that by default flask's route decorator only answers to HTTP GET requests. In this case, we also specified the HTTP POST request so that they can also be handled by our associated endpoint function univ_submit_form() -> Note that we can alternatively use the dcorators @app.get('/url') or @app.post('/url') as shortcusts (instead of app.route) to separate views for different methods into different functions for each common HTTP method ...
    def univ_submit_form(): 
            # return "Form Submitted Hoooraayyy!" #displayed in browser -> TestinTestin 
            #to be able to access the data in our html form, the form feild elements that we want to access server side (i.e. have submitted to the server) each need to have a name attribute. It is the name attribute that is used by the browser to gerenerate form data to be sent to the server, in our case this flaskserver.py -> ofcourse the send button dont need noname o! In the developer tools for our submission page (/submit_url triggered by send button) under network and then payload tab, we see that the payload shows the form data with the user input data we typed into the form before submitting! Waweuu!!
            # return render_template('login.html', error=error)
            #Lets generate a thankyou.html page that will be displayed on submitform button click. Rather than build a new html from scratch, and easier (read: lazier) technique is just replace the form element on contact.html with the text content:  Thank you, {{user_name}}! I will get in touch with you, shortly! ...and save the new file as thankyou.html ...not the most creative but anyhow anyhow ... LOOL!
            if request.method == "POST": 
                data_email = request.form["email"] #we can access the different form data fields using theier name attributes (which we assigned in the HTML form element) as "keys" using the dictionary syntax. However a DRYer (read: more concise) way to go about this is to convert all the recieved form data into a dictionary type data structrure (using the .to_dict() method) which we can access the form data values we need
                data = request.form.to_dict() # .to_dict() is actually a Pandas method which is used to convert a DataFrame into a dictionary of series or list-like data type depending on the orient parameter.
                print(data) #{'email': 'uche.nnodim@yahoo.com', 'subject': 'Check Check Again!!', 'message': 'Checking Render Template'} -> however plenty other errors showing that favicon isnt retrieved, solved this by updating the favicon filepath

                #STORING DATA SUBMITTED FROM THE WEB PAGE: When data is submitted from the webpage, like from our /submit_form endpoint, it is by default stored in the browser and thus is lost when the browser is closed. To "persist" the data, we would have to store them in a batabase via our server. Lets make a most simple and basic database which will essentaially be a text file in which our data will be in ccsv format (asin comma seperated values forreal). We will be using Python's FIle I/O open function as below using the database.txt text file we generated in our venwebserver folder as our database ... note that we ould put this in a function above/outside our decorator and call it with passing our data dict into it ... but doing everthing here because, learning. 

                with open("database.txt", mode="a") as database: #The open() function converts our text file into a file OBJECT to allow for "manipulation" by the objects methods. Remember, the append mode="a" adds text at the END of the text content in the file, write mode would have overwritten the contents. append  will also create a new file if it dosent already exist. no need to specify a path as database and this flaskserver.py are in same folder -> actually the file was gebnerated in the working folder, modules and not in the same folder venvwebserver. Python unlike this flask server, relates files from the current working directory, which is the Modules follder. And yes, open() is a python function. Flask on the other hand, relates from the file location!
                    email = data["email"]
                    subject = data["subject"]
                    message = data["message"]

                    file = database.write(f"\n{email},{subject},{message}") # works apu -> asin comma seperated values forreal (but not quite o, ole! the real .csv file dey, no be by to dey disguise .txt lol!!)-> added \n to ensure new entries are on a newline
                    print(file)

                # return "HTTP 200 CODE TINZ! FORM SUBMITTED!!" #HTTP 200 CODE TINZ! FORM SUBMITTED!! -> displayed in browser at /submit_form
                # return redirect("/thankyou.html") #Thank you, ! I will get in touch with you, shortly! -> the redirect function which we get from our imported redirect module redirects THE BROWSER to the specified url endpoint, /thankyou.html in this case. Consequently, the endpoint triggers flash to serve (read: return) the corresponding content or html file according to the app.route decorator that is handling the endpoint. However, we dont have an @app.route(/thankyou.html) but we do have a generic @app.route("/<page_name>") which will handle it and return render_template("/thankyou.html") accoding to its endpoint function univ_page() ... Wawuuu!! Neat!! HENCE THE IMPORTANCE OF THE RIGHT NAMING STRATEGY, BP JUST TO USE THE SAME FILE NAMES AS THE URL ENDPOINTS OR ABI NA VICEVERSA? - ALSO EXPLAINS WHY ENDPOINTS  BE LIKE /bbbb.html RATHER THAN /bbbb i.e. WITHOUT THE .html extension! EXCEPT FOR CASES WHERE THERE ISNT A CORRESPONMDINH HTML FILE LIKE THIS OUR /submit_form WHICH IS ACTING LIKE A BRIDGE BTW /contact.html AND /thankyou.html ... HMMMMMM! WAWUUU!! Note that if we didnt have the @app.route("/<page_name>") decorator, we would get an Error: Not Found The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
                # return redirect("/thankyou.html", user_name=data["email"]) #TypeError: redirect() got an unexpected keyword argument 'user_name' -> here we are tryinmg to pass in the user_name into the web page to display to the user, but redirect() dosent support that parameter the way that render_template does. Note that in the redirect above that worked, the jinja template in the thankyou.html page will return an empty space since no variable from here was passed into it. Need to figure out how to solve this while using redirect() -> for now lets just render_template jejely ojare!
                return render_template("/thankyou.html", user_name=data["email"]) #Thank you, uche.nnodim@yahoo.com! I will get in touch with you, shortly! -> works apu, webpage message includes uche.nnodim@yahoo.com for email 
# Testin_submit()

#CSV Files: Python's csv module implements classes to read and write tabular data in CSV format. However, while the lack of a well-defined standard means that subtle differences (forex varying delimiters and quoting characters) often exist in the data produced and consumed by different applications, the overall format is similar enough that it is possible to write a single module which can efficiently manipulate such data, hiding the details of reading and writing the data from the programmer. The csv module allows programmers to say, “write this data in the format preferred by Excel,” or “read data from this file which was generated by Excel,” without knowing the precise details of the CSV format used by Excel. Programmers can also describe the CSV formats understood by other applications or define their own special-purpose CSV formats. It has reader and writer objects to read and write sequences respectively. Programmers can also read and write data in dictionary form using the DictReader and DictWriter classes. CSV files use the .csv extension https://docs.python.org/3/library/csv.html

#NOTE: Apart from csv, some other well-known data exchange formats are XML, HTML, JSON etc.

import csv #normalnormal
#VERY IMPORTANT TO READ THE BELOW FIRST: 
#https://realpython.com/python-csv/
#https://thepythonguru.com/python-how-to-read-and-write-csv-files/#customizing-the-reader
#https://docs.python.org/3/library/csv.html

#let's generate a new file, database.csv (in our modules folder, because python cwd tinz)
def write_to_csv(data): #using a seperate function rather than embedding the data arrchival process code within our route function
    with open("database.csv", mode="a", newline="") as csv_database: #Pythons csv module works on file objects, hence the need for open(). Also, i for use database but dont wanna conflict...dunno if it really matters, but INFS. Note on newline parameter: If newline='' is not specified, newlines embedded inside quoted fields will not be interpreted correctly, and on platforms that use \r\n linendings on write an extra \r will be added. It should always be safe to specify newline='', since the csv module does its own (universal) newline handling https://docs.python.org/3/library/csv.html#id4 universal newlines is the manner of interpreting text streams in which all of the following are recognized as ending a line: the Unix end-of-line convention '\n', the Windows convention '\r\n', and the old Macintosh convention '\r'. See PEP 278 and PEP 3116, as well as bytes.splitlines() for an additional use https://docs.python.org/3/glossary.html#term-universal-newlines
        email = data["email"] #this is a string value
        subject = data["subject"] #this is a string value
        message = data["message"] #this is a string value
        print(email,subject,data)
        # csv_writer = csv.writer(csv_database, delimiter=",", quoting=csv.QUOTE_MINIMAL) #the quoting raparemtter here means add quotes only when required, for example, when a field contains either the quotechar or the delimiter. This is the default. However, I want all the data to look uniform since if for some reason some users inputs a comma in their name (ikr, diff language settings yeah, but stranger things have happened) and others dont then it means that some lines will have quotes and others wont for the same value "types"
        csv_writer = csv.writer(csv_database, delimiter=",", quoting=csv.QUOTE_NONNUMERIC) #we will put quotes on everything except integers and floats.
        csv_fieldheaders = ["email","subject","message"] #the UD course just manually tyoped the headers into the database.csv file, I decided to programatically insert them instead ... SUPO! but waitO waitO! #notsofast - this means that we will be writing in headers each time we input data on the webpage and thus call this function from our route function below! now I see why UD just wrote in the headers manually, less clumsly than having to write if/elses to check of headers at the top. 
        csv_rowfieldvalues = [email,subject,message]
        # csv_writer.writerow(csv_fieldheaders) #will hard code/write the headers in the csv file gangan, otherwise this line will append the header before each line of users data!
        csv_writer.writerow(csv_rowfieldvalues) #works apu! yaaay!! however, 1 problem, the first row starts right after the manual header we hardwrote, i.e. it didnt start at a new line! the solution is:
        #1. use csv_writer.writerow(csv_fieldheaders) -> the writerow function will generate a newline automatically which is why we dont see the same line problem with the row data we get from the browser as we r using .writerow(csv_rowfieldvalues) -> obviouslywe wont be using this for the header. Note that we can include a lineterminator argument but its redundant as it defaults to '\r\n' and besides  which takes us to solution 2:
        #2. Since we are hardoding the header field, we simply "hard code" the newline by pressing enter (lol) after typing in the header ... and that works apu! easypeasy!!
        # print(csv_writer)


@app.route('/submit_form', methods=['POST', 'GET'])
def univ_submit_form(): 
    if request.method == "POST":
        data = request.form.to_dict() 
        write_to_csv(data)  
        return render_template("/thankyou.html", user_name=data["email"]) #obviously to ensure theres always an email feild, we can implement in the JS/html for the form NOT to submit on absent email by specifying it as a mandatory feild


#DATABASES: Relational Vs. Non-Relational Databases -> Databases which are a collection of data help to organise data in an effiecient way for storage and retrieval. A Database Management System or DBMS is a collection of programs that allow us to manage databases. Relational Databases consist of 2 or more tables with columns and rows. Each row represents an entry which a column sorts a (very) specific type of info like name, address, phone number etc. The relationship between tables and fields is called a "Schema" which must be properly defined before info/data can be added to the database. PostGres, MySQL are examples of relational databases and they all use a management language called SQL (Structured Query Language). NoSQL or non-relational databases (e.g. MongoDB, redis, Hypertable, Apache HBASE) allow you to build a database without first having to define a Schema. NR databases store data as folders holding related info of all types. Forex, in a SQL database, say we wanted to store data for a tweeter type app, we would have several tables for the tweeter users biodata, tweets, followers etc. A particular field like the username could be common to each table and would be called a foreign key (i.e. key equivalaent). So say we wanted to access the tweet of a given user, we could fetch his username (common foriegn key to all tables) from the biodata table then go to the tweets table using the username foriegn key to fetch the user's tweet. The Schema would define the relationship between these different tables becaused, structured. For a No-SQL, all the data for a given user would be selfcontained in a folder (or ducument for MongoDB) such that for any given user you could retrieve any required data. NoSQL databases have their own unique query languages, forex Mongo has the MongoDB QL etc. 

#localhost: our server is hosted on our computer, hence localhost - we are running the browser and our server on the same computer, localhost. Therefore it wont be accessible by anyone except ourserselves, duh. To make it available to the public we have to host it publicly. pythonanywhere by Anaconda is one of the services that can host your website directly from your browser, and it offers a free basic plan with access to a full Python environment already installed, ohyeah?! https://www.pythonanywhere.com/ 
# 1. get a free pythonanywhere account. we are greeted with a dashboard
# 2. we need to upload our project files to pythonanywhere. apu, the fwesh way to do this is to use github
# 3. go to github -> create a new public repo, which Im calling flasky (because, ynot?) -> github.com/uchennodim/flasky repo has been generated -> copy the url under HTTPS so that we can clone it locally
# 4. Ensure we are navigated to our venvwebserver in terminal, since this is where we want to put our clonegithub flasky. Note that even though our venvwebserver was active, we were still working from parents module in the terminal. so did a CLA: cd venvwebserver -> directory changed and venvwebserver still remains activated! Nyoce! HINT: i did a CLA: ls to list directory contents na hwen I realize say na modules get all dis files/folders o! So I realize say I need switch to venvwebserver to place my clone flasky repo.
# 4. CLA: git clone https://github.com/uchennodim/flasky.git -> flasky is now in our venvwebserver ... neat!
# 5. Copy the required server files from our flaskserver to flasky ... gengen! We will copy just the 




#SUMMARY OF HOW THE WHOLE THING WORKS: 
# Click on send btton element -> triggers /submit_form in url in line with action="submit_form" attribute in corresponding contact.html file (but why submit_form not /submit_form ??) -> setting it as Public and adding a README
#  ...




#FILE UPLOADS: You can handle uploaded files with Flask easily. Just make sure not to forget to set the enctype="multipart/form-data" attribute on your HTML form, otherwise the browser will not transmit your files at all.