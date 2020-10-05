window.addEventListener('scroll', function() {
        if (pageYOffset > 250) {
            document.getElementById('arrowUp').style.visibility="visible";
        } else {
            document.getElementById('arrowUp').style.visibility="";
        }
});

arrowUp.onclick = function() {
    window.scrollTo(pageXOffset, 0);
}