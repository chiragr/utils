var nodemailer = require('nodemailer');

// Setup recipients
var mailTo =
{
    "john.doe@gmail.com" :
    {
        "address" : "Hi ", // You can use Dear here if you like! :) A Hi is mandatory. Everything else is optional.
        "name" : "Jonny,", // Name
        "customMessage1" : "Hope you are doing great!",  // Custom message that will appear before commonMessageBody1
        "customMessage2" : "I will definitely miss you!" // custom message that will appear after commonMessageBody1 and before commonMessageBody2
    },
    "jane.doe@gmail.com" :
    {
        "address" : "Dear ",
        "name" : "Jinny,",
        "customMessage1" : "Hope you are doing great!",
        "customMessage2" : "I will definitely miss you while having lunch!"
    }
    // As as many recipients as you like!
};

// Subject
var commonMesssageSubject = "Hey! Bye for now!";

// Message Body. Split into two.
var commonMessageBody1 = "Will not be around for few months.\n\nPing me if you need something.";
var commonMessageBody2 = "Contact me on my cell phone.\n\nThank you!\nChirag";

// Configure SMTP Server
var smtpTransport = nodemailer.createTransport("SMTP",{
            host: 'smtp.gmail.com',    // SMTP server
            secureConnection: true,    // Secure. TTL/SSL required.
            port: 465,                 // Secure port
            auth: {
              user: "me.my@gmail.com", // Sender's username
              pass: "password"         // Sender's password
            }
});

// Loop thru our recipient list and send individual mails.
for (var email in mailTo)
{
    var recipientDetails = mailTo[email];

    // Create message body using the fragments.
    var messageBody = recipientDetails.address;

    if (recipientDetails.name && recipientDetails.name.length > 0)
    {
        messageBody = messageBody + recipientDetails.name + "\n\n";
    }

    if (recipientDetails.customMessage1 && recipientDetails.customMessage1.length > 0)
    {
        messageBody = messageBody + recipientDetails.customMessage1 + "\n\n";
    }

    if (commonMessageBody1 && commonMessageBody1.length > 0)
    {
        messageBody = messageBody + commonMessageBody1;
    }

    if (recipientDetails.customMessage2 && recipientDetails.customMessage2.length > 0)
    {
        messageBody = messageBody + recipientDetails.customMessage2 + "\n\n";
    }

    if (commonMessageBody2 && commonMessageBody2.length > 0)
    {
        messageBody = messageBody + commonMessageBody2;
    }

    // Setup e-mail data
    var mailOptions =
    {
        from: "Chirag <me.my@gmail.com>", // Sender address
        to: email,                        // Recipient address
        subject: commonMesssageSubject,   // Subject line
        text: messageBody                 // Plaintext body
    };

    // Send mail with defined transport object
    smtpTransport.sendMail(mailOptions, function(error, response)
    {
        if(error)
        {
            console.log(error);
        }
        else
        {
            console.log("Message sent: " + response.message);
        }
    });
}

smtpTransport.close(); // Shut down the connection pool, no more messages
