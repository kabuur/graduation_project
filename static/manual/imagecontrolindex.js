

xrayImage = document.getElementById('xrayImage');

imageChecker = document.getElementById("imageChecker")

xrayImage.addEventListener('change', function(event) {
    
    var file = event.target.files[0];
    var reader = new FileReader();
    reader.onload = function(e) {
      var image = new Image();
    
      image.src = e.target.result;
    
  
      image.onload = function() {
        var width = this.width;
        var height = this.height;
        if (width >400 && width <1000 && height >400 && height <1000){
            btn = document.getElementById("btn");
            btn.disabled = false;
            btn.style.display="block";
            imageChecker.textContent = "";
        }
        else{
            btn = document.getElementById("btn");
            btn.disabled = true;
            btn.style.display="none";
            imageChecker.textContent = "image is not eceptable..... ";
        }
  
      };
    };
  
    reader.readAsDataURL(file);
  });