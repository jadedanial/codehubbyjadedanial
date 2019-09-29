function removeActivepage(){

	var allmenus = document.getElementById("menu").getElementsByTagName("a");

	for(i = 0, len = allmenus.length; i < len; i++){
    	
    	allmenus[i].classList.remove("activepage");

    }

    var allmenus = document.getElementById("dropdownmenu").getElementsByTagName("a");

    for(i = 0, len = allmenus.length; i < len; i++){
    	
    	allmenus[i].classList.remove("activepage");

    }

}

function scrollView(scrollto){

	var viewelement = document.getElementById(scrollto.id);
    viewelement.scrollIntoView();
   
    removeActivepage();
    
	document.getElementById(scrollto.id+"page").classList.add("activepage");
	document.getElementById(scrollto.id+"pagemenu").classList.add("activepage");

	document.getElementById("menuitems").classList.remove("showmenu");	
	
}

function plusSlides(n, slidename){

	showSlides(slideIndex += n, slidename);

}

function currentSlide(n, slidename){

	showSlides(slideIndex = n, slidename);

}

function showSlides(n, slidename){

	if(slidename == 1){

		var slides = document.getElementsByClassName("projectsslides");

	}else if(slidename == 2){

		var slides = document.getElementsByClassName("codinglogslides");

	}else if(slidename == 3){

		var slides = document.getElementsByClassName("blogslides");

	}

	if(n > slides.length){

		slideIndex = 1;

	}

	if(n < 1){

		slideIndex = slides.length;

	}

	for(i = 0; i < slides.length; i++){

		slides[i].style.display = "none";

	}

	slides[slideIndex-1].style.display = "block";

}

function gotoLog(logcount, logids, logid){

	var index = logids.indexOf(logid);
	
	currentSlide(1, 2);	
	plusSlides(index, 2);

}

function onScroll(){

	var home = document.getElementById("home").offsetHeight;
	var about = document.getElementById("about").offsetHeight;
	var projects = document.getElementById("projects").offsetHeight;
	var codinglog = document.getElementById("codinglog").offsetHeight;
	var blog = document.getElementById("blog").offsetHeight;
	var contact = document.getElementById("contact").offsetHeight;

	if(window.pageYOffset < home * 0.20){

		removeActivepage();

		document.getElementById("homepage").classList.add("activepage");
		document.getElementById("homepagemenu").classList.add("activepage");

		document.getElementsByTagName("title")[0].innerHTML = "Code Hub - Home";

	}else if(window.pageYOffset > home * 0.70 && window.pageYOffset < home + about * 0.20){

		removeActivepage();

		document.getElementById("aboutpage").classList.add("activepage");
		document.getElementById("aboutpagemenu").classList.add("activepage");

		document.getElementsByTagName("title")[0].innerHTML = "Code Hub - About";

	}else if(window.pageYOffset > home + about * 0.70 && window.pageYOffset < home + about + projects * 0.20){

		removeActivepage();

		document.getElementById("projectspage").classList.add("activepage");
		document.getElementById("projectspagemenu").classList.add("activepage");

		document.getElementsByTagName("title")[0].innerHTML = "Code Hub - Project";

	}else if(window.pageYOffset > home + about + projects * 0.70 && window.pageYOffset < home + about + projects + codinglog * 0.20){

		removeActivepage();

		document.getElementById("codinglogpage").classList.add("activepage");
		document.getElementById("codinglogpagemenu").classList.add("activepage");

		document.getElementsByTagName("title")[0].innerHTML = "Code Hub - Coding Log";
	
	}else if(window.pageYOffset > home + about + projects + codinglog * 0.70 && window.pageYOffset < home + about + projects + codinglog + blog * 0.20){

		removeActivepage();

		document.getElementById("blogpage").classList.add("activepage");
		document.getElementById("blogpagemenu").classList.add("activepage");

		document.getElementsByTagName("title")[0].innerHTML = "Code Hub - Post";

	}else if(window.pageYOffset > home + about + projects + codinglog + blog * 0.70 && window.pageYOffset < home + about + projects + codinglog + blog + contact * 0.20){

		removeActivepage();

		document.getElementById("contactpage").classList.add("activepage");
		document.getElementById("contactpagemenu").classList.add("activepage");

		document.getElementsByTagName("title")[0].innerHTML = "Code Hub - Contact";

	}

}

function showMenu(){

	document.getElementById("menuitems").classList.toggle("showmenu");

}