



function submitbutton1() 
{
  console.log("here");
  var name=$("#name").val();
  console.log(name);
  var email=$("#email").val();
  console.log(email);
  var phone=$("#phone").val();
  console.log(phone);

  var filename = ($("#resume").val()).split(/(\\|\/)/g).pop()
  var blob = document.getElementById("resume").files[0];
  console.log(blob);
//   var newelement = window.URL.createObjectURL(blob);
//   document.getElementById("WebGl").src = newelement;

  var filetype = filename.split(".")[1];
  filename = filename.split(".")[0];
  
  
  
  blobToBase64(blob).then(value => {
    console.log(value);
    var data = value;
    viewer(data);});
  
}
function viewer(data){
    console.log(data);
    new Promise(r => setTimeout(r, 100));
    var arraybuf = base64ToArrayBuffer(data);
    var blob = new Blob([arraybuf], {type: "application/pdf"});
    console.log(blob);
    var newelement = window.URL.createObjectURL(blob);
    document.getElementById("WebGl").src = newelement;
}
function blobToBase64(blob) {
    return new Promise((resolve, _) => {
      const reader = new FileReader();
      reader.onloadend = () => resolve(reader.result);
      reader.readAsDataURL(blob);
    });
  }

//This function takes a base64 string and adds it to a Uint8array, after that is done it should return the array
function base64ToArrayBuffer(base64) {
    var binaryString = atob(base64.split(",")[1]);
    var binaryLen = binaryString.length;
    var bytes = new Uint8Array(binaryLen);
    for (var i = 0; i < binaryLen; i++) {
        var ascii = binaryString.charCodeAt(i);
        bytes[i] = ascii;
    }
    return bytes;
}