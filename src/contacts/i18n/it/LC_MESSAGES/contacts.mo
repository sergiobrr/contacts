��    o      �                                  !     5  E   F     �     �  8   �  "  �  V   	     ]	     j	  
   q	     |	  7   	  l   �	     $
     *
     =
     C
  .   a
     �
  1   �
      �
     �
            
        '     ?     F     M  �   a  D  �     6     B  6   S  =   �     �     �     �     �     �  ,     Y   9  	   �     �     �     �     �  r   �     _     s     �  	   �  .   �     �     �     �  L   �      1    R      Y  X   z  �  �  2   �  �   �  V   :     �     �  ?   �     �  	         
  0        L     e     m  !     r   �  E        Z    l     �     �     �     �     �     �     �  :   �  #   �     #  '  5  #   ]     �     �     �     �     �     �     �     �     �  2  �  O        m     �     �  �  �     8     <     E     L     `  E   q     �     �  8   �  "    V   1      �      �   
   �      �   8   �   l   �      P!     V!     i!     o!  .   �!     �!  1   �!      �!     "     1"     :"  
   H"     S"     k"     r"     y"  �   �"  D  #     b$     n$  6   $  =   �$     �$     �$     %     %      %  ,   8%  Y   e%  	   �%     �%     �%     �%     &  r   &     �&     �&     �&  	   �&  .   �&     �&     �&     �&  L   '      ]'    ~'      �(  X   �(  �  �(  2   �+  �   �+  V   f,     �,     �,  ?   �,     -  	   ,-     6-  2   G-     z-     �-     �-  !   �-  r   �-  E   B.     �.    �.     �/     �/     �/     �/     �/     �/     �/  :   �/  #   -0     Q0  '  c0  #   �1     �1     �1     �1     �1     �1     �1     �1     �1     2  2  2  O   K3     �3     �3     �3    -   Listing  Login  error has Occurred " file under the ), the command went through the
          RootController class to the , manage them, export them. . .
                Each projects gets quickstarted with a . This controller is
        protected globally. Instead of having a @require decorator on each method, we
        have set an allow_only attribute at the class level. All the methods in this
        controller will require the same level of access. You need to be manager to
        access . This one is protected by
        a different set of permissions. You will need to be /controllers /model /templates A  A message with the link for the reset was sent to %(d). A web page viewed by user could be constructed by single or several reusable
                templates under About About Architecture Admin Another protected resource is Architectural basics of a quickstart TG2 site. Authentication Authentication &amp; Authorization in a TG2 site. Authorization and Authentication Code my data model Contacts Copyright ©  Data Model Design my URL structure Email: Error  Export all contacts If you have access to this page, this means you have enabled authentication
        and authorization in the quickstart to create your project. In this page you can see all the WSGI variables your request object has,
             the ones in capital letters are required by the spec, then a sorted by
             component list of variables provided by the Components, and at last
             the "wsgi." namespace with very useful information about your WSGI Server Insert your Invalid Password Learning TurboGears 2.3: Information about TG and WSGI Learning TurboGears 2.3: Quick guide to the Quickstart pages. Login Logout Manage your phone numbers New  Now try to visiting the Only for people with the "manage" permission Only managers are authorized to visit this method. You will need to log-in
        using: Password: Reset password Reuse the web page elements Secure Controller here Send request Sergio Brero made this to check his python knowledge as requested
              from Alessandro Molina, Axant CTO. Simple contacts app Submit reset Submitted... Templates Thank you for your interest in my application. The The " The Master Template The TG2 quickstart command produces this basic TG site. Here's how it works. The WSGI nature of the framework The gearbox command will have created a few specific controllers for you. But
        before you go to play with those controllers you'll need to make sure your
        application has been properly bootstapped. This is dead easy, here is how to do
        this: The keys in the environment are: The last kind of protected resource in this quickstarted app is a full so
        called There's more to the "master.html" template... study it to see how the
        &lt;title&gt; tags and static JS and CSS files are brought into the page.
        Templating with Genshi is a powerful tool and we've only scratched the surface.
        There are also a few little CSS tricks hidden in these pages, like the use of a
        "clearingdiv" to make sure that your footer stays below the sidebars and always
        looks right. That's not TG2 at work, just CSS. You'll need all your skills to
        build a fine web app, but TG2 will make the hard parts easier so that you can
        concentrate more on good design and content rather than struggling with
        mechanics. This simple app was made as a challenge for Axant! Those Python methods are responsible to create the dictionary of variables
          that will be used in your web views (template). To change the comportement of this setup-app command you just need to edit
        the Toggle navigation URL Structure URL. You will
        be challenged with a login/password form. User not found Username: WSGI Environment We don't have a user with %(d) as email address. We hope to see you soon! Welcome Welcome back, %s! Welcome to the Simple Contact App Welcome to the Simple Contacts app, made as a
          challenge for Axant. Standing on the Turbogear's shoulder. When you want a model for storing favorite links or wiki content, the Wrong credentials You can build a dynamic site without any data model at all. There still be a
          default data-model template for you if you didn't enable authentication and
          authorization in quickstart. If you have enabled authorization, the auth
          data-model is ready-made. about about() contacts editor editor_user_only editpass file. folder has
          your URLs. When you called this url ( folder in your site is ready to go. gearbox setup-app inside your application's folder and you'll get a database setup (using the
        preferences you have set in your development.ini file). This database will also
        have been prepopulated with some default logins/passwords so that you can test
        the secured controllers and methods. login: manager
password: managepass manage_permission_only master.html method. or remember me root.py secc secc/some_where secure controller template
        controls the overall design of the page we're looking at. It draws the headers,
        the footer, the notices flash and embeds the content of each page of your web applications.
        Thus the "master.html" template provides the overall architecture for
        each page in this site. template and a bunch of templates for the pages provided by the RootController. to be able to access it. websetup.py with a
        password of Project-Id-Version: contacts 0.1
Report-Msgid-Bugs-To: EMAIL@ADDRESS
POT-Creation-Date: 2019-02-27 01:07+0100
PO-Revision-Date: 2019-02-27 01:09+0100
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: it
Language-Team: it <LL@li.org>
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.6.0
  -   Listing  Login  error has Occurred " file under the ), the command went through the
          RootController class to the , manage them, export them. . .
                Each projects gets quickstarted with a . This controller is
        protected globally. Instead of having a @require decorator on each method, we
        have set an allow_only attribute at the class level. All the methods in this
        controller will require the same level of access. You need to be manager to
        access . This one is protected by
        a different set of permissions. You will need to be /controllers /model /templates A  Abbiamo mandato una email con il link per il reset a %d. A web page viewed by user could be constructed by single or several reusable
                templates under About About Architecture Admin Another protected resource is Architectural basics of a quickstart TG2 site. Authentication Authentication &amp; Authorization in a TG2 site. Authorization and Authentication Code my data model Contacts Copyright ©  Data Model Design my URL structure Email: Error  Export all contacts If you have access to this page, this means you have enabled authentication
        and authorization in the quickstart to create your project. In this page you can see all the WSGI variables your request object has,
             the ones in capital letters are required by the spec, then a sorted by
             component list of variables provided by the Components, and at last
             the "wsgi." namespace with very useful information about your WSGI Server Insert your Invalid Password Learning TurboGears 2.3: Information about TG and WSGI Learning TurboGears 2.3: Quick guide to the Quickstart pages. Login Logout Manage your phone numbers New  Now try to visiting the Only for people with the "manage" permission Only managers are authorized to visit this method. You will need to log-in
        using: Password: Reset password Reuse the web page elements Secure Controller here Send request Sergio Brero made this to check his python knowledge as requested
              from Alessandro Molina, Axant CTO. Simple contacts app Submit reset Submitted... Templates Thank you for your interest in my application. The The " The Master Template The TG2 quickstart command produces this basic TG site. Here's how it works. The WSGI nature of the framework The gearbox command will have created a few specific controllers for you. But
        before you go to play with those controllers you'll need to make sure your
        application has been properly bootstapped. This is dead easy, here is how to do
        this: The keys in the environment are: The last kind of protected resource in this quickstarted app is a full so
        called There's more to the "master.html" template... study it to see how the
        &lt;title&gt; tags and static JS and CSS files are brought into the page.
        Templating with Genshi is a powerful tool and we've only scratched the surface.
        There are also a few little CSS tricks hidden in these pages, like the use of a
        "clearingdiv" to make sure that your footer stays below the sidebars and always
        looks right. That's not TG2 at work, just CSS. You'll need all your skills to
        build a fine web app, but TG2 will make the hard parts easier so that you can
        concentrate more on good design and content rather than struggling with
        mechanics. This simple app was made as a challenge for Axant! Those Python methods are responsible to create the dictionary of variables
          that will be used in your web views (template). To change the comportement of this setup-app command you just need to edit
        the Toggle navigation URL Structure URL. You will
        be challenged with a login/password form. User not found Username: WSGI Environment Non abbiamo un utente con %d come indirizzo email. We hope to see you soon! Welcome Welcome back, %s! Welcome to the Simple Contact App Welcome to the Simple Contacts app, made as a
          challenge for Axant. Standing on the Turbogear's shoulder. When you want a model for storing favorite links or wiki content, the Wrong credentials You can build a dynamic site without any data model at all. There still be a
          default data-model template for you if you didn't enable authentication and
          authorization in quickstart. If you have enabled authorization, the auth
          data-model is ready-made. about about() contacts editor editor_user_only editpass file. folder has
          your URLs. When you called this url ( folder in your site is ready to go. gearbox setup-app inside your application's folder and you'll get a database setup (using the
        preferences you have set in your development.ini file). This database will also
        have been prepopulated with some default logins/passwords so that you can test
        the secured controllers and methods. login: manager
password: managepass manage_permission_only master.html method. or remember me root.py secc secc/some_where secure controller template
        controls the overall design of the page we're looking at. It draws the headers,
        the footer, the notices flash and embeds the content of each page of your web applications.
        Thus the "master.html" template provides the overall architecture for
        each page in this site. template and a bunch of templates for the pages provided by the RootController. to be able to access it. websetup.py with a
        password of 