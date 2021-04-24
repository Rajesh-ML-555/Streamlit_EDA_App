import pandas as pd
import streamlit as st

from pandas_profiling import ProfileReport
#Compenents packages

import streamlit.components.v1 as stc
from streamlit_pandas_profiling import st_profile_report

import sweetviz as sv
import sweetviz.sv_html as sv_html

def build_html(self, layout='widescreen', scale=None):
    scale = float(self.use_config_if_none(scale, "html_scale"))
    layout = self.use_config_if_none(layout, "html_layout")
    if layout not in ['widescreen', 'vertical']:
        raise ValueError(f"'layout' parameter must be either 'widescreen' or 'vertical'")
    sv_html.load_layout_globals_from_config()
    self.page_layout = layout
    self.scale = scale
    sv_html.set_summary_positions(self)
    sv_html.generate_html_detail(self)
    if self.associations_html_source:
        self.associations_html_source = sv_html.generate_html_associations(self, "source")
    if self.associations_html_compare:
        self.associations_html_compare = sv_html.generate_html_associations(self, "compare")
    self._page_html = sv_html.generate_html_dataframe_page(self)
        
footer_temp = """
	 <!-- CSS  -->
	  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	  <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	  <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
	 <footer class="page-footer grey darken-4">
	    <div class="container" id="aboutapp">
	      <div class="row">
	        <div class="col l6 s12">
	          <h5 class="white-text">About Streamlit EDA App</h5>
	          <p class="grey-text text-lighten-4">Using Streamlit,Pandas,Pandas Profile and SweetViz.</p>
	        </div>
	      
	   <div class="col l3 s12">
	          <h5 class="white-text">Connect With Me</h5>
	          <ul>
	          <a href="https://www.linkedin.com/in/rajesh-kumar-28ba0713a/" target="_blank" class="white-text">
	            <i class="fab fa-linkedin fa-4x"></i>
	          </a>
	          <a href="https://www.linkedin.com/in/rajesh-kumar-28ba0713a/" target="_blank" class="white-text">
	            <i class="fab fa-youtube-square fa-4x"></i>
	          </a>
	           <a href="https://github.com/Rajesh-ML-555" target="_blank" class="white-text">
	            <i class="fab fa-github-square fa-4x"></i>
	          </a>
	          </ul>
	        </div>
	      </div>
	    </div>
	    <div class="footer-copyright">
	      <div class="container">
	      Made by <a class="white-text text-lighten-3">S Rajesh Kumar</a><br/>
	      <a class="white-text text-lighten-3" href="https://www.instagram.com/s_rajesh_kumar_/">Rajesh Kumar @s_rajesh_kumar</a>
	      </div>
	    </div>
	  </footer>
	"""

@st.cache()
def load_csv_file(data_file_path):
	df = pd.read_csv(data_file_path)
	return df

def main():
    ''' 
    A simple EDA App using Streamlit
    '''
    menu = ["Home","Pandas Profiling", "Sweetviz", "About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Pandas Profiling":
        st.subheader("EDA with Pandas Profiling")
        data_file = st.file_uploader("Upload a csv file", type = ['csv'])
        if data_file is not None:
            df = load_csv_file(data_file)
            st.dataframe(df.head())
            if st.button("Generate Pandas Profiling Report"):
                profile = ProfileReport(df)
                st_profile_report(profile)
    
    elif choice == "Sweetviz":
        st.subheader("EDA with Sweetviz")
        data_file = st.file_uploader("Upload a csv file", type = ['csv'])
        if data_file is not None:
            df = load_csv_file(data_file)
            st.dataframe(df.head())
            if st.button("Generate Sweetviz Report"):
                sv_report = sv.analyze(df)
                build_html(sv_report)
                parsed_html = sv_report._page_html
                stc.html(parsed_html, height = 1500, scrolling = True)


    elif choice == "About":
        st.subheader("About App")
        stc.html(footer_temp, height = 500)
    
    else:
        st.subheader("Home")
        html_temp = """
		<div style="background-color:royalblue;padding:15px;border-radius:10px">
		<h1 style="color:white;text-align:center;">EDA App by S Rajesh Kumar</h1>
		<h2 style="color:white;text-align:center;">App consists of Pandas-Profiling and Sweetviz | Upcoming: DTale</h2>
		</div>
		"""
		# components.html("<p style='color:red;'> Streamlit Components is Awesome</p>")
        stc.html(html_temp)

        stc.html("""
			<style>
			* {box-sizing: border-box}
			body {font-family: Verdana, sans-serif; margin:0}
			.mySlides {display: none}
			img {vertical-align: middle;}
			/* Slideshow container */
			.slideshow-container {
			  max-width: 1000px;
			  position: relative;
			  margin: auto;
			}
			/* Next & previous buttons */
			.prev, .next {
			  cursor: pointer;
			  position: absolute;
			  top: 50%;
			  width: auto;
			  padding: 16px;
			  margin-top: -22px;
			  color: white;
			  font-weight: bold;
			  font-size: 18px;
			  transition: 0.6s ease;
			  border-radius: 0 3px 3px 0;
			  user-select: none;
			}
			/* Position the "next button" to the right */
			.next {
			  right: 0;
			  border-radius: 3px 0 0 3px;
			}
			/* On hover, add a black background color with a little bit see-through */
			.prev:hover, .next:hover {
			  background-color: rgba(0,0,0,0.8);
			}
			/* Caption text */
			.text {
			  color: #f2f2f2;
			  font-size: 15px;
			  padding: 8px 12px;
			  position: absolute;
			  bottom: 8px;
			  width: 100%;
			  text-align: center;
			}
			/* Number text (1/4 etc) */
			.numbertext {
			  color: #f2f2f2;
			  font-size: 12px;
			  padding: 8px 12px;
			  position: absolute;
			  top: 0;
			}
			/* The dots/bullets/indicators */
			.dot {
			  cursor: pointer;
			  height: 15px;
			  width: 15px;
			  margin: 0 2px;
			  background-color: #bbb;
			  border-radius: 50%;
			  display: inline-block;
			  transition: background-color 0.6s ease;
			}
			.active, .dot:hover {
			  background-color: #717171;
			}
			/* Fading animation */
			.fade {
			  -webkit-animation-name: fade;
			  -webkit-animation-duration: 1.5s;
			  animation-name: fade;
			  animation-duration: 1.5s;
			}
			@-webkit-keyframes fade {
			  from {opacity: .4} 
			  to {opacity: 1}
			}
			@keyframes fade {
			  from {opacity: .4} 
			  to {opacity: 1}
			}
			/* On smaller screens, decrease text size */
			@media only screen and (max-width: 300px) {
			  .prev, .next,.text {font-size: 11px}
			}
			</style>
			</head>
			<body>
			<div class="slideshow-container">
			<div class="mySlides fade">
			  <div class="numbertext">1 / 4</div>
			  <img src="https://i.ytimg.com/vi/BoKLMehRahw/maxresdefault.jpg" style="width:100%">
			  <div class="text">Caption Text</div>
			</div>
			<div class="mySlides fade">
			  <div class="numbertext">2 / 4</div>
			  <img src="https://res.cloudinary.com/practicaldev/image/fetch/s--nutW1iT0--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/oyat0fc1lujjztdtx42b.png" style="width:100%">
			  <div class="text">Caption Text</div>
			</div>
			<div class="mySlides fade">
			  <div class="numbertext">3 / 4</div>
			  <img src="https://cdn.journaldev.com/wp-content/uploads/2020/11/Pandas-Profiling-in-Python.png" style="width:100%">
			  <div class="text">Caption Two</div>
			</div>
			<div class="mySlides fade">
			  <div class="numbertext">4 / 4</div>
			  <img src="https://miro.medium.com/max/875/0*ECp-sidL0e_AwG6G.png" style="width:100%">
			  <div class="text">Caption Three</div>
			</div>
			<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
			<a class="next" onclick="plusSlides(1)">&#10095;</a>
			</div>
			<br>
			<div style="text-align:center">
			  <span class="dot" onclick="currentSlide(1)"></span> 
			  <span class="dot" onclick="currentSlide(2)"></span> 
			  <span class="dot" onclick="currentSlide(3)"></span> 
			  <span class="dot" onclick="currentSlide(4)"></span> 
			</div>
			<script>
			var slideIndex = 1;
			showSlides(slideIndex);
			function plusSlides(n) {
			  showSlides(slideIndex += n);
			}
			function currentSlide(n) {
			  showSlides(slideIndex = n);
			}
			function showSlides(n) {
			  var i;
			  var slides = document.getElementsByClassName("mySlides");
			  var dots = document.getElementsByClassName("dot");
			  if (n > slides.length) {slideIndex = 1}    
			  if (n < 1) {slideIndex = slides.length}
			  for (i = 0; i < slides.length; i++) {
			      slides[i].style.display = "none";  
			  }
			  for (i = 0; i < dots.length; i++) {
			      dots[i].className = dots[i].className.replace(" active", "");
			  }
			  slides[slideIndex-1].style.display = "block";  
			  dots[slideIndex-1].className += " active";
			}
			</script>
			""")




if __name__== '__main__':
    main()