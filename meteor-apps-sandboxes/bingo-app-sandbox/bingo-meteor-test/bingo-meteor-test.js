// Clicks = new Mongo.Collection('clicks');

if (Meteor.isClient) {
  //
  var numbers = new Array();
  for (var i = 1; i <= 75; i++)
    numbers.push(i);

  // counter starts at 0
  Session.setDefault('counter', 0);

  Template.bingo.helpers({
    counter: function () {
      return Session.get('counter');
      // return Clicks.find({}).count();
    }
  });

  Template.bingo.events({
    'click button': function () {
      var randIdx = Math.floor(Math.random() * numbers.length);
      // increment the counter when button is clicked
      // Session.set('counter', Session.get('counter') + 1);
      Session.get('counter', Session.get('counter') + numbers[randIdx]);
      // Clicks.insert({});
      var rs = numbers.splice(randIdx, 1);
    }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
