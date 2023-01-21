import firebase from "firebase/compat/app";

const firebaseConfig = {
    apiKey: "AIzaSyBU2u8GHqlmDnBLTN2uhXw95qsQpz6KiKA",
    authDomain: "boilermatch-33826.firebaseapp.com",
    databaseURL: "https://boilermatch-33826-default-rtdb.firebaseio.com",
    projectId: "boilermatch-33826",
    storageBucket: "boilermatch-33826.appspot.com",
    messagingSenderId: "469018307651",
    appId: "1:469018307651:web:925533b16b97307aeb78f6"
  };

  // initialize firebase
  initializeApp(firebaseConfig);
  var firestore = firebase.firestore()

  //variable to acccess database collection
  const db = firestore.collection("formData")

  //get submit form data
  let submitButton = document.getElementById('submit')

  // event list
  submitButton.addEventListener("click", (e) => {
    e.preventDefault()

    let name = document.getElementById('name').value
    let puid = document.getElementById('puid').value
    let number = document.getElementById('number').value

    db.doc().set({
      name: name,
      puid: puid,
      number: number,
    }).then( () => {
      console.log("Data saved")
    }).catch((error) => {
      console.log(error)
    })
  })

  /*
  // initialize firebase
  firebase.initializeApp(firebaseConfig);

  // reference your database
  var formDB = firebase.database().ref('matchForm');
  document.getElementById('matchForm').addEventListener('submit', submitForm);

  function submitForm(e) {
    e.preventDefault();

    var name = getInputVal('name');
    var puid = getInputVal('puid');
    var number = getInputVal('number');

    saveForm(name, puid, number);
    document.getElementById('matchForm')
  }

  function getInputVal(id) {
    return document.getElementById(id).value;
  }

  function saveForm(name, puid, email) {
    var newFormRef = formDB.push();
    newFormRef.set({
        name: name,
        puid : puid,
        number : number,
    });
  }*/

  /*const saveForm = (name, puid, number) => {
    var newForm = formDB.push();
    
    newForm.set({
        name : name,
        puid : puid,
        number : number,
    })
  };

  const getElementVal = (id) => {
    return document.getElementById(id).value;
  };*/