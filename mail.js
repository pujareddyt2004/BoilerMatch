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
  firebase.initializeApp(firebaseConfig);

  // reference your database
  var formDB = firebase.database().ref('matchForm');
  document.getElementById('matchForm').addEventListener('submit', submitForm);

  function submitForm(e) {
    e.preventDefault();

    var name = getElementVal('name');
    var puid = getElementVal('puid');
    var number = getElementVal('number');

    saveForm(name, puid, number);
  }

  const saveForm = (name, puid, number) => {
    var newForm = formDB.push();
    
    newForm.set({
        name : name,
        puid : puid,
        number : number,
    })
  };

  const getElementVal = (id) => {
    return document.getElementById(id).value;
  };