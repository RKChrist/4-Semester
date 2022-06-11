var { Kafka } = require(['kafkajs'])

var  host = "kafka-server1"

var  kafka = new Kafka({
  brokers: ['kafka-server1:9098']
})

var  topic = 'pdf_topic'
var producer = kafka.producer()

function submitbutton1() 
{
  console.log("here");
  var name=$("#name").val();
  console.log(name);
  var email=$("#email").val();
  console.log(email);
  var phone=$("#phone").val();
  console.log(phone);

  var today = new Date();

  var createdDate = today.getDate() + '-' + (today.getMonth()+1)+'-'+  today.getFullYear();

  var filename = ($("#resume").val()).split(/(\\|\/)/g).pop()
  var blob = document.getElementById("resume").files[0];
  console.log(blob);
//   var newelement = window.URL.createObjectURL(blob);
//   document.getElementById("WebGl").src = newelement;

  var filetype = filename.split(".")[1];
  filename = filename.split(".")[0];
  
  
  
  
   var data = blobToBase64(blob).then(value => {
    
    var data = value;
    return data; });



    var json = "{userid=key, " +
    " filename=" +  filename +", " +
    " createddate=" + createdDate +" ," +
    " data=" + data + ", " +
    " filetype=" +  filetype + ", " +
    " createdby=" + name + ", "



    const produce = async () => {
      try{
        await producer.connect()
      } catch (err) {
        console.log(err)
      }

      let i = 0
    
      // after the produce has connected, we start an interval timer
      setInterval(async () => {
        try {
          console.log("Hello")
          // send a message to the configured topic with
          // the key and value formed from the current value of `i`
          await producer.send({
            topic,
            messages: [
              {
                key: String(i),
                value: data,
              },
            ],
          })
    
          // if the message is written successfully, log it and increment `i`
          console.log("writes: ", i)
          i++
        } catch (err) {
          console.error("could not write message " + err)
        }
      }, 1000)
    
    }
    produce();
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