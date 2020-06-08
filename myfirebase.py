import requests
import json
from kivy.app import App


class MyFirebase():
    wak='AIzaSyAoCPYEIWd0S0zF-yp4ZTifnUr7Or4RTIY' # Web_Api_key
    def sign_up(self,email,password):
        app=App.get_running_app()
        print('signup!!')
        signup_url='https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key='+self.wak
        signup_payload={"email":email,"password":password,"returnSecureToken": True}
        signup_request= requests.post(signup_url,data=signup_payload)
        print(signup_request.ok)
        print(signup_request.content.decode())
        sign_up_data=json.loads(signup_request.content.decode())
        if signup_request.ok==True:
            refresh_token=sign_up_data['refreshToken']
            localId=sign_up_data['localId']
            idToken=sign_up_data['idToken']
            # Save refreshtoken
            with open("refresh_token.txt","w") as f:
                f.write(refresh_token)
            #Save localId
            app.local_id=localId
            app.id_token=idToken
            name=str(app.root.ids["signup_screen"].ids["login_name"].text)
            email=str(app.root.ids["signup_screen"].ids['login_email'].text)
            password=str(app.root.ids["signup_screen"].ids['login_password'].text)

            #Create new details in database
            d= {'Name': name,'avatar':'','email': email, 'password': password}
            my_data=json.dumps(d)
            requests.patch("https://ace-app-efc65.firebaseio.com/"+localId+".json?auth="+idToken,data=my_data)
            app.change_screen("login_screen")
        if signup_request.ok == False:
            error_data=json.loads(signup_request.content.decode())
            error_message=error_data["error"]["message"]
            app.root.ids["login_screen"].ids["login_massage"].text= error_message

    def sign_in(self):
        pass
