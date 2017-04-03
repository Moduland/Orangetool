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
    var icon=document.getElementById("mobile-icon");
    if (x.className === "topnav") {
        x.className += " responsive";
        menu.style.height="auto";
        document.getElementById("search").style.display="none";
        icon.innerHTML="&#x2716";
    } else {
        x.className = "topnav";
        menu.style.height="100px";
        document.getElementById("search").style.display="block";
        icon.innerHTML="&#9726;"
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

function openNav() {
    var admin_icon=document.getElementById("adicon");
    if (document.getElementById("mySidenav").style.width=="" || document.getElementById("mySidenav").style.width=="0px")
    {
        document.getElementById("mySidenav").style.width = "250px"
        admin_icon.innerHTML="&#x2716;";
    }
    else{
        document.getElementById("mySidenav").style.width = "0"
        admin_icon.innerHTML="&#9776;";
        
    }

}

function search(){
    var input,filter,table,tr,td_list,i;
    input=document.getElementById("myinput");
    filter=input.value.toUpperCase();
    tr=document.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
    td_list = tr[i].getElementsByTagName("td");
        for (j=0;j<td_list.length;j++){
            td=td_list[j];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
          break;
      } else {
        tr[i].style.display = "none";
          
      }
    } 
  }
    }
}

function notif_search(){
    var input,filter,notif,p_list,i;
    input=document.getElementById("myinput");
    filter=input.value.toUpperCase();
    notif=document.getElementById("notif");
    p_list=notif.getElementsByTagName("p");
    for (i=0;i<p_list.length;i++){
        if (p_list[i].innerHTML.toUpperCase().indexOf(filter)>-1){
            p_list[i].style.display="";
        }
        else{
            p_list[i].style.display="none";
        }
    }
    
}


var $TABLE = $('#table');
var $BTN = $('#export-btn');
var $EXPORT = $('#export');

$('.table-add').click(function () {
  var $clone = $TABLE.find('tr.hide').clone(true).removeClass('hide table-line');
  $TABLE.find('table').append($clone);
});

$('.table-remove').click(function () {
  $(this).parents('tr').detach();
});

$('.table-up').click(function () {
  var $row = $(this).parents('tr');
  if ($row.index() === 1) return; // Don't go above the header
  $row.prev().before($row.get(0));
});

$('.table-down').click(function () {
  var $row = $(this).parents('tr');
  $row.next().after($row.get(0));
});

// A few jQuery helpers for exporting only
jQuery.fn.pop = [].pop;
jQuery.fn.shift = [].shift;

$BTN.click(function () {
  var $rows = $TABLE.find('tr:not(:hidden)');
  var headers = [];
  var data = [];
  
  // Get the headers (add special header logic here)
  $($rows.shift()).find('th:not(:empty)').each(function () {
    headers.push($(this).text().toLowerCase());
  });
  
  // Turn all existing rows into a loopable array
  $rows.each(function () {
    var $td = $(this).find('td');
    var h = {};
    
    // Use the headers from earlier to name our hash keys
    headers.forEach(function (header, i) {
      h[header] = $td.eq(i).text();   
    });
    
    data.push(h);
  });
  
  // Output the result
  $EXPORT.text(JSON.stringify(data));
});


