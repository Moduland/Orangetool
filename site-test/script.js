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
    var menu=document.getElementById("menu");
    if (x.className === "topnav") {
        x.className += " responsive";
        menu.style.height="auto";
        document.getElementById("search").style.display="none";
    } else {
        x.className = "topnav";
        menu.style.height="100px";
        document.getElementById("search").style.display="block";
    }
}


function search_hide(){
    var menu
    menu=document.getElementById("myTopnav");
    menu.style.display="none";
}
function search_view(){
    var menu
    menu=document.getElementById("myTopnav");
    menu.style.display="block";
}