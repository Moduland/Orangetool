function login(){
    var password;
    var username;
    var message;
    username=document.getElementById("username");
    password=document.getElementById("password");
    message=document.getElementById("error-message")
    if (username.value.length==0){
    message.innerHTML="نام کاربری خود را وارد کنید";
    username.style.backgroundColor="pink";
    }
    else if (password.value.length==0){
       message.innerHTML="کلمه عبور خود را وارد کنید"; 
       password.style.backgroundColor="pink";
    }
    
    setTimeout(function(){message.innerHTML="";password.style.backgroundColor="white";username.style.backgroundColor="white";},"4000");
}



function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}