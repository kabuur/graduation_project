// document.getElementById('p_xrayImage').addEventListener('change', function(event) {
//     var file = event.target.files[0];
  
  
//     var reader = new FileReader();
  
//     reader.onload = function(e) {
//       var image = new Image();
  
//       image.src = e.target.result;
  
//       image.onload = function() {
//         var width = this.width;
//         var height = this.height;
//         if (width >400 && width <1000 && height >400 && height <1000){
         
//           console.log('Image width:', width);
//           console.log('Image height:', height);
//           btn = document.getElementById('btn')
//           btn.addEventListener("submit",(event)=>{
//             console.log("size is limit");
            
            
//           })
//         } 
  
//       };
//     };
  
//     reader.readAsDataURL(file);
//   });