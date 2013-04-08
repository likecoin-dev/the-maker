from makerUtilities import writeFile
import os

def scaffold(systemDir):
    
    return """<!DOCTYPE html>
<html>
    <head>
     <meta charset="utf-8" />
         <script src=""" + os.path.join(systemDir, "jquery.min.js") + """"></script>
        

        

        <style type="text/css">

        html {

            background: -webkit-gradient(linear, left top, left bottom, from(#000), to(rgb(93,94,120)));
            background-attachment:fixed;
        }

        body {

                font-family: "Helvetica Neue";
                font-size: 14px;
            width:auto;
            /* max-width:694px; */
            color:#fff;
            padding:20px 20px;


        }

        a {

              text-decoration:none;
            color:#000;
            cursor:default;
        }



        p {
            font-weight:lighter;
            color:#fff;
            letter-spacing:0.09em;
            float:left;
            font-size:0.9em;
            line-height:1.45em;
            text-align:justify;
            margin:-6px 0px 24px 10px;

        }


        h5 {
            font-weight:lighter;
            letter-spacing:0.050em;
            margin:-28px 0px 0px 8px;
            line-height:3em;
            font-size:18px;
            
        
        }

        img {
            border:1px solid #333;
                
            width:100%;
            height:100%;
            -webkit-box-reflect: below 0px -webkit-gradient(linear, left top, left bottom, from(transparent), color-stop(50%, transparent), to(rgba(0,0,0,0.1)));
            /* -webkit-transform: perspective( 600px ) rotateY( 20deg );        */    
            margin-bottom:40px;
                }


        .row {
            
            width:100%;
            margin:0px 0px 20px 10px;
            float:left;
            clear:both;
            
        
        }

        .thumbnail {

            width:17%;
            border: 1px solid rgba(0,0,0,0);
            padding:20px 20px 10px 20px;
            margin:0px 20px 0px 0px;
            float:left;
            clear:right;
            -webkit-border-radius:10px;
            -webkit-transition: border-color, 1s;
            

        }

        .thumbnail p {
            
            text-align:center;
            margin:-24px 0px 0px 0px;
            width:100%;
            font-size:14px;
        
        }

        .thumbnail:hover {
        
            border-color: #ccc;
            padding:20px 20px 10px 20px;
            -webkit-border-radius:10px;

        }


        .info {
        
            width:92%;
            float:left;
            clear:both;
            display:none;
            margin:20px 10px 0px 24px;
        
        }

        .info img {

            display:none;        
        }


        a.button {
            
            cursor:default;
            color:#000;
        
        }

        a.button:active {

            color:#000;
            background:  -webkit-gradient(linear, left top, left bottom, from(#eee), to(#bbb));
        
        }


        .template {
        
            float:left;
            clear:both;
            margin-bottom:70px;
        }


        #foo {

            display:none;
        
        }

    </style>


    <script type="text/javascript">
    
        $(document).ready(function(){
              $('.thumbnail').hover(function(){
                      $('.info').hide();
        
                  $($(this).data('info')).show();
     
              });
        }); 
    
    
    </script>


    </head>
    <body>


        <div class="row">
        
            FIRST ROW OF THUMBNAILS HERE
        
        
        </div>


        <div class="row">
            <div class="thumbnail" data-info="#info-modern">
    
        <img src="/Applications/TheMaker.app/Contents/Resources/system/templates/Blue/parts/preview.jpg" />
        <p>Modern</p>
    </div>


        <div class="thumbnail"  data-info="#info-simple">
    
            <img src="/Applications/TheMaker.app/Contents/Resources/system/templates/White/parts/preview.jpg" />
                <p>Simple</p>

        
    </div>

    <div class="thumbnail"  data-info="#info-simple-markdown">
    
        <img src="/Applications/TheMaker.app/Contents/Resources/system/templates/Simple-Markdown/parts/preview.jpg" />
            <p>Simple Markdown</p>

    </div>



    <div class="thumbnail"  data-info="#info-modern">
    
        <img src="/Applications/TheMaker.app/Contents/Resources/system/templates/Simple-Markdown/parts/preview.jpg" />
        
    </div>

        </div>

        

        <div class="info" id="info-modern">
        <h5>Modern</h5>
        <p>This is a modern template but we will not use it anymore... Lorem Ipsum is simply dummy text of the printing and typesetting industry.<br /> Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>
        </div>


        <div class="info" id="info-simple">
        <h5>Simple</h5>
        <p>This is a modern template but we will not use it anymore... Lorem Ipsum is simply dummy text of the printing and typesetting industry.<br /> Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>
        </div>

        <div class="info" id="info-simple-markdown">
        <h5>Simple Markdown</h5>
        <p>    <img src="/Applications/TheMaker.app/Contents/Resources/system/templates/Simple-Markdown/parts/preview.jpg" />
This is a modern template but we will not use it anymore... Lorem Ipsum is simply dummy text of the printing and typesetting industry.<br /> Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>
        


        </div>



    </body>

</html>

"""



def buildView(systemDir, viewPath):
    writeFile(os.path.join(viewPath,"yourTemplates.html"), scaffold(systemDir))
    
    
    
def makeThumbnail(systemDir, templateName):
    
    previewImage = os.path.join(systemDir, "templates", templateName, "parts/preview.jpg")
    thumbnail = """
    
     <div class='thumbnail' data-info='#info-""" + templateName + """'>
                <a href='--""" + templateName + """--'>
        <img src='""" + previewImage + """' />
        <p>""" + templateName + """</p></a>
    </div>
    
    """
    
    
    return thumbnail