// Dummy counter

var countDownDate = new Date("Jan 5, 2024 16:37:25").getTime();
var x = setInterval(function() 
{
    var now = new Date().getTime();
    var distance = countDownDate - now;

    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("counter").innerHTML = minutes + "m " + seconds + "s ";

    if (distance < 0) 
    {
        clearInterval(x);
        document.getElementById("demo").innerHTML = "05m 36s";
    }
},
1000);