<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact</title>
</head>
<body>
    <section id="contact">
  <h2>Contact</h2>
  <form action="https://api.web3forms.com/submit" method="POST" class="contact-form">
    <input type="hidden" name="access_key" value="fbbfa945-dce2-45ff-8c69-f3a2e40443cd">
    <label for="name">Name</label>
    <input type="text" id="name" name="name" placeholder="Your name..." required />
    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Your email..." required />
    <label for="message">Message</label>
    <textarea id="message" name="message" rows="4" placeholder="Type your message..." required></textarea>
    <button type="submit" class="contact-btn">Submit Form</button>
  </form>
</section>
</body>
</html>