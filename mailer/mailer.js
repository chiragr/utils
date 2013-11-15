/*
 * mailer.js
 * 
 * Email utility that uses nodeJS to send customized bulk email.
 * 
 * Steps to execute:
 * 1. Install node.js (http://nodejs.org/)
 * 2. Copy this file to a directory of your choice E.g.: ~/mailer.js
 * 3. Update sections that have comments starting with "Setup"
 * 4. Execute: node mailer.js
 * 
 */
(function(){
    var nodemailer = require("nodemailer");

    // Setup Mail Server
    var smtpServer     = "smtp.gmail.com";
    var smtpPort       = 465;
    var isConnSecure   = true;
    var senderLogin    = "john.doe@gmail.com";
    var senderPassword = "ItsASecret";

    // Setup Sender Name
    var senderName = "John Doe<john.doe@gmail.com>";
    var replyToEmail = "john.doe@yahoo.com";

    // Setup Recipients
    var mailTo =
    {
        "jane.doe@gmail.com" :
        {
            "address" : "Hi ", // You can use Dear here if you like! :)
            "name" : "Jane,",
            "customMessage1" : "Hope you are doing great!",
            "customMessage2" : "I will definitely miss you!"
        }
        // Add more recipeients here.
    };

    // Setup Subject
    var commonMesssageSubject = "Bye ...";

    // Setup Message Body
    var commonMessage1 = "Tomorrow is my last day at Froogle. I had a great time here!";
    var commonMessage2 = "Personal Mail ID: john.doe@gmail.com\nPersonal Web Page: http://johndoe.me\n\nPlease do keep in touch!\n\nThank you!\nJohn";

    // Configure SMTP Server
    var smtpTransport = nodemailer.createTransport("SMTP",
    {
        host: smtpServer,
        secureConnection: isConnSecure,
        port: smtpPort,
        auth:
        {
            user: senderLogin,
            pass: senderPassword
        }
    });

    // Loop thru our recipient list and send individual mails.
    for (var email in mailTo)
    {
        var recipientDetails = mailTo[email];

        // Create message body using the fragments.
        var messageBody = "";

        if (recipientDetails.address && recipientDetails.address.length > 0)
        {
            messageBody = messageBody + recipientDetails.address;
        }

        if (recipientDetails.name && recipientDetails.name.length > 0)
        {
            messageBody = messageBody + recipientDetails.name + "\n\n";
        }

        if (recipientDetails.customMessage1 && recipientDetails.customMessage1.length > 0)
        {
            messageBody = messageBody + recipientDetails.customMessage1 + "\n\n";
        }

        if (commonMessage1 && commonMessage1.length > 0)
        {
            messageBody = messageBody + commonMessage1 + "\n\n";
        }

        if (recipientDetails.customMessage2 && recipientDetails.customMessage2.length > 0)
        {
            messageBody = messageBody + recipientDetails.customMessage2 + "\n\n";
        }

        if (commonMessage2 && commonMessage2.length > 0)
        {
            messageBody = messageBody + commonMessage2;
        }

        if (!replyToEmail)
        {
            replyToEmail = senderName;
        }
        // Email data
        var mailOptions =
        {
            from: senderName,               // Sender address
            replyTo: replyToEmail,          // Reply To address
            to: email,                      // Recipient address
            subject: commonMesssageSubject, // Subject line
            text: messageBody               // Plaintext body
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

    smtpTransport.close(); // Shut down the connection pool
})();

