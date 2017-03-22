function login(){
    var password;
    var username;
    var message;
    username=document.getElementById("username").value;
    password=document.getElementById("password").value;
    message=document.getElementById("error-message")
    if (username.length==0){
    message.innerHTML="نام کاربری خود را وارد کنید";
    }
    else if (password.length==0){
       message.innerHTML="کلمه عبور خود را وارد کنید"; 
    }
    
    setTimeout(function(){message.innerHTML=""},"4000");
}



function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}