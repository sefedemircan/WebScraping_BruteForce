function send() {
  var entryCode = document.getElementById("kod").value;
  if (entryCode == "8545") {
    console.log("Login Successful!");
  } else {
    console.log("Error!");
  }

  console.log(entryCode.value);
}
